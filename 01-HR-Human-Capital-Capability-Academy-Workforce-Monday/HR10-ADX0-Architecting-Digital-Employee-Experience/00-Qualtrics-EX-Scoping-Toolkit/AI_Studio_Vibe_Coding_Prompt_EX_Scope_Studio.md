# EX Scope Studio: Google AI Studio vibe-coding prompt pack

Turns the Qualtrics Employee Experience scoping questionnaire (200 questions, 11 use cases, SF module readiness, data inventory, 16-week plan, risks) into a working web app, built in Google AI Studio's **Build** mode.

Companion data file: `ex-scoping-data.json` (load it inside the app after the first build).

---

## How to run it

1. Open Google AI Studio, choose **Build**, paste **Prompt 1** into the input box and run it.
2. When the app opens, click **Import scoping data** and pick `ex-scoping-data.json` from your computer. The browser reads it directly, so you do not need to attach anything in AI Studio. (Google's Build mode documentation describes text prompts and GitHub import, not file attachments, which is why the data lives outside the prompt.)
3. Run the **acceptance checks** at the bottom. Fix anything that fails before moving on.
4. Paste **Prompt 2** (Gemini Scope Advisor). Test. Then Prompt 3 (optional, multi-user), Prompt 4 (exports), Prompt 5 (QA and polish).
5. Refine with the chat panel, annotation mode (point at a screen area and describe the change), or the Code tab. When happy, sync to GitHub, download a ZIP, or deploy to Cloud Run.

**Working rules:** one prompt at a time, test before the next, and when the agent breaks something say "Revert your last change to X and keep Y" rather than re-describing the whole app.

**Privacy:** neither the prompts nor the data file contain client data. Do not type real employee names or personal data into answers if you use the Advisor.

---

## Prompt 1: Master build prompt (paste first)

~~~~text
You are building "EX Scope Studio", a web app that consultants and client teams use to run a scoping questionnaire for a Qualtrics Employee Experience (EX) implementation alongside SAP SuccessFactors.

CONTEXT
The client already runs SAP SuccessFactors Employee Central and Performance & Goals (PMGM). Other SuccessFactors modules go live later. Qualtrics EX go-live is targeted in 3 to 4 months. The app replaces an Excel, Word and PowerPoint pack. It must let people answer about 200 questions, decide which use cases go live first, track readiness, and see a 16-week plan and a risk register.

USERS AND MODES
- Consultant mode: full access to every screen and field.
- Client respondent mode: the user picks their role (an "owner" value) and sees only the questions routed to that owner, with a toggle "Show all questions". They can edit response, status, respondent and follow-up only. They cannot change scope decisions, plan, risks, modules or data inventory. This mode is a UI convenience, not security. Say so in a tooltip.

DATA (do not hardcode the 200 questions)
The app loads a JSON file the user imports with an "Import scoping data" button (file picker, drag and drop, or paste JSON). Until data is imported, show an empty state with that button and a "Load demo data" button. Write a built-in demo dataset of 12 questions across 4 sections in the same style for the demo button.
Top-level keys:
- meta {title, context, projectStart "YYYY-MM-DD"}
- sections [{code, name, description}]
- questions [{id, section, sectionName, useCases[], priority "P1|P2|P3", owner, neededBy "Week 2|Week 4|Week 8|Post go-live", responseType, question, why, kickoff boolean, keyLabel}]
- useCases [{name, covers, sfTrigger, dependsOn, fit, fitReason}]
- sfModules [{module, status, exRelevance, touchpoint, dataTrigger, confirmQuestion}]
- dataFields [{attribute, ecArea, purpose, sensitivity "Low|Medium|High", neededFor}]
- plan [{phase, startWeek, endWeek, activities}]
- risks [{risk, likelihood 1-5, impact 1-5, mitigation, owner}]
- stakeholders [{role, why, involvement}]
- owners [string]
- tagToUseCase {tagCode: use case name or null}
Example question:
{"id":"CTX-02","section":"CTX","sectionName":"Project Context & Objectives","useCases":["ALL"],"priority":"P1","owner":"Executive Sponsor","neededBy":"Week 2","responseType":"Free text","question":"Who is the executive sponsor, and what decision rights do they hold over scope, budget and the go-live date?","why":"Avoids stalled decisions in a 3-4 month window.","kickoff":true,"keyLabel":"Executive sponsor and decision rights"}
Validate on import, show readable error messages, and never crash when an optional key is missing.

USER STATE (kept separate from the imported data)
- Per question: response (text), status ("Not started" | "In progress" | "Answered" | "Follow-up needed" | "Not applicable"), respondent, followUp, updatedAt.
- Per use case: scopeDecision ("Wave 1 (go-live)" | "Phase 2" | "Out of scope" | "To discuss"), businessOwner, audience, annualVolume, comments.
- Per SF module: status, plannedGoLive (date), inScope ("Yes" | "No" | "Phase 2" | "To discuss"), notes.
- Per data field: availableInEC ("Yes" | "No" | "Partly" | "Unknown"), quality (1 to 5), approvedToShare ("Yes" | "No" | "Pending legal review"), notes.
- Risks: editable likelihood and impact. Plan: projectStart date. Stakeholders: name, email, availability.
Persist state to localStorage inside try/catch. If storage is blocked, keep state in memory and show a banner "Changes are not saved. Export JSON to keep your work." Provide export and import of the full state as one JSON file.

SCREENS (sidebar navigation, responsive)
1. Dashboard
   - Tiles: total questions, percent Answered or Not applicable, open P1 count, open P1 due Week 2.
   - Per-section progress bars.
   - "Design-ready" badge when every P1 question with neededBy "Week 2" is Answered or Not applicable. "Build-ready" badge when every P1 with neededBy "Week 2" or "Week 4" is Answered or Not applicable. Show how many remain for each.
   - Open questions by owner (bar chart).
   - "Next best questions": the top 10 open P1 questions, ordered by neededBy then kickoff first; click opens the question.
   - Scope summary: number of use cases per scope decision.
2. Use Case Map
   - One card or table row per use case with a fit chip (High: teal, Medium-High: light teal, Medium: amber, Low-Medium: orange), the covers, trigger and dependency text, and the editable fields.
   - A Wave 1 summary strip.
   - Relevance rule: a question is relevant if any of its useCases tags maps through tagToUseCase to a use case that is not "Out of scope", or if any tag maps to null (cross-cutting, such as ALL). A question whose tags all map to use cases marked "Out of scope" is dimmed and excluded from progress by default. Add a toggle "Include out-of-scope questions".
3. Questionnaire
   - Section rail with per-section progress.
   - Filters that combine: text search, section, use case tag, priority, owner, neededBy, status, "Kick-off only", "Relevant only". Show the result count.
   - Question card: ID, a star for kickoff questions, the question text, collapsible "Why we ask", chips for priority, owner, neededBy, response type and use case tags, a response textarea, status select, respondent, follow-up.
   - Auto-save on blur or after a short debounce. Keyboard: j and k move to the next and previous question.
   - Keep 200 cards fast: paginate or virtualise.
4. SF Module Readiness: editable table with date picker, status and in-scope selects. Flag modules without a planned date as "Date needed".
5. Data Inventory: editable table. Highlight High sensitivity rows. Show a counter "High-sensitivity fields not yet approved".
6. Plan and Risks
   - Project start date input (default meta.projectStart). Build a Gantt from plan[] over 16 weeks using real dates. The "Go-live" phase bar is amber, the others teal.
   - An editable holiday band (default 20 Dec to 3 Jan) that shades the weeks it overlaps.
   - Risk register with editable likelihood and impact. Score = likelihood x impact. Rating: High 15 or more, Medium 8 to 14, Low 7 or less. Add a 5x5 heat map with risks placed on it, and sort by score.
7. Stakeholders: editable table (name, email, availability). Where the role name equals a question owner, show that owner's open question count.
8. Export: (a) full state JSON, (b) CSV of questions with answers and status, (c) a Markdown scoping brief (context, scope decisions, open P1 questions, top risks), (d) a print-friendly view using print CSS.

DESIGN
Professional, calm, high contrast. Palette: navy #14213D, teal #1B998B, amber #F2A541, light grey #F4F6F8, ink #1F2937. System or Inter sans-serif. Cards with 12px radius and a subtle shadow. P1 chip in red-orange. Light and dark mode via prefers-color-scheme. WCAG AA contrast, visible focus rings, a label on every input, ARIA roles for navigation and filters, and no meaning carried by colour alone (always pair colour with text or an icon). Respondent mode must work well on a phone.

TECHNICAL CONSTRAINTS
- React front end. Put logic in pure, testable functions: progress, relevance, readiness gates, risk scoring.
- No hardcoded secrets or API keys. No tracking. No external paid services.
- Footer note on every screen: "SAP and Qualtrics product options change often. Validate with SAP and Qualtrics before committing."

OUT OF SCOPE FOR THIS PROMPT
Gemini features, sign-in and databases come in later prompts. Do not add buttons or placeholders that look functional but do nothing.

DEFINITION OF DONE
The app runs with demo data, imports the JSON file, all eight screens work, filters combine correctly, state survives a reload, and exports download. When finished, summarise what you built and list any assumptions you made.
~~~~

---

## Prompt 2: Gemini Scope Advisor

~~~~text
Add a "Scope Advisor" screen powered by Gemini.

ARCHITECTURE
- Call Gemini only from the app's server-side runtime through POST /api/advisor. Use the GEMINI_API_KEY secret that AI Studio provides. Never expose the key to the browser or put it in client code.
- Use the current default Gemini model for new AI Studio apps. Request structured JSON output (JSON mime type with a response schema). Use a 60 second timeout. Show friendly error messages and a Retry button.

INPUT
- The user chooses the scope: all questions with responses, one section, or one use case.
- Build the payload from ONLY: question id, question text, priority, response text, status, use case scope decisions and risk register. If the payload is large, process section by section and merge the results.
- Before sending, show a "What will be sent" preview and require a checkbox: "I confirm the answers contain no personal data about named individuals." Disable Send until it is ticked.

ACTIONS
A) Scoping brief: a one-page summary of what the client told us.
B) Consistency check: contradictions and gaps. Look for cases such as:
   - go-live date fixed, yet works council or union consultation is needed in some countries;
   - a promise of anonymous surveys, yet SuccessFactors attributes are attached to responses;
   - 360 described as development only, yet results used in promotion or pay decisions;
   - exit surveys sent to personal email, yet no policy on holding leavers' contact data;
   - lifecycle surveys planned, yet the trigger module is not live and no interim feed is agreed;
   - Wave 1 scope too large for the stated team capacity or holiday periods.
C) Wave recommendation: for each use case, Wave 1, Phase 2, Out of scope or Needs decision, with reasons and conditions.
D) Follow-up questions and new risks.

SERVER SYSTEM INSTRUCTION
"You are a senior SAP SuccessFactors and Qualtrics Employee Experience implementation architect reviewing a client's scoping answers. Use ONLY the answers provided. Cite question IDs for every claim. If information is missing or unclear, write 'insufficient information' and list the question IDs needed; never guess. Do not state SAP or Qualtrics product capabilities, licensing or integration options as certain; mark them 'validate with SAP/Qualtrics'. Be concise and practical, and focus on risks to a go-live in 3 to 4 months. Never request or repeat personal data about individuals."

RESPONSE SCHEMA
{
  "summary": "string",
  "waveRecommendations": [{"useCase": "string", "recommendation": "Wave 1 | Phase 2 | Out of scope | Needs decision", "reason": "string", "conditions": ["string"], "evidence": ["question ids"]}],
  "contradictions": [{"issue": "string", "questionIds": ["string"], "suggestedResolution": "string", "severity": "High | Medium | Low"}],
  "gaps": [{"questionId": "string", "whyItMatters": "string"}],
  "newRisks": [{"risk": "string", "likelihood": 1-5, "impact": 1-5, "mitigation": "string", "owner": "string", "evidence": ["question ids"]}],
  "followUpQuestions": [{"question": "string", "owner": "string", "why": "string"}],
  "confidence": "High | Medium | Low"
}

UI
- Show results as cards. Question-ID chips jump to that question.
- Every card is labelled "AI-generated, review before use". Nothing is applied automatically.
- Add Accept buttons: accept a wave recommendation (sets the use case scope decision), accept a new risk (adds it to the register, tagged "AI suggested"), accept a follow-up question (appends to that owner's follow-up list).
- Cache the last result per scope with a timestamp, and allow Regenerate.
- If the model returns invalid JSON, retry once, then show a clear error.
~~~~

---

## Prompt 3 (optional): Multi-user persistence and sign-in

~~~~text
Add shared persistence and sign-in using Firebase Firestore and Firebase Authentication (Google sign-in). Keep the localStorage mode as an "Offline demo" fallback.

MODEL
- projects/{projectId}: name, createdBy, meta, importedData version.
- projects/{projectId}/members/{uid}: email, role "consultant" | "client", ownerRole (required for clients, matches a question owner).
- projects/{projectId}/answers/{questionId}: response, status, respondent, followUp, updatedBy, updatedAt. Add a history subcollection that keeps previous versions.
- Scope decisions, module readiness, data inventory, plan, risks and stakeholders are stored per project and writable by consultants only.

SECURITY RULES (enforced in rules, not only in the UI)
- Only project members can read.
- Clients can write answers only for questions whose owner equals their ownerRole.
- Only consultants can write everything else and manage members.
Explain the rules in plain language after you write them.

FEATURES
- Consultants invite members by email and assign role and owner role.
- Show "last edited by" and time on every answer. On conflicting edits use last-write-wins with a visible warning.
- Do not store real employee personal data. The data inventory holds attribute names only.
~~~~

---

## Prompt 4: Exports

~~~~text
Improve the Export screen:
1. Excel export in the browser using SheetJS with seven sheets: Questionnaire (including responses and status), Use Case Map, SF Module Readiness, Data Inventory, Plan, Risks, Stakeholders. Add header styling, column widths, frozen header rows and a status dropdown on the Status column.
2. A richer Markdown brief: context, scope decisions, answered highlights by section, open P1 questions grouped by owner and neededBy, top five risks, and next steps.
3. An executive one-pager print layout (A4 landscape): dashboard tiles, Wave 1 / Phase 2 decisions, readiness badges, top five risks and the ten most important open questions.
4. Exports must respect the "Include out-of-scope questions" toggle.
~~~~

---

## Prompt 5: QA and polish

~~~~text
Act as a QA engineer for this app. Import ex-scoping-data.json and walk through every item in the acceptance checklist below. Fix every failure, then report pass or fail for each item.
Also: add empty, loading and error states to every screen; check keyboard navigation, focus order and colour contrast; confirm 200 questions scroll and filter without lag; add unit tests for the pure functions (progress, relevance, readiness gates, risk scoring) if the environment supports it; and list any known limitations.
~~~~

---

## Acceptance checklist (after importing `ex-scoping-data.json`)

| # | Check | Expected |
|---|---|---|
| 1 | Dashboard totals | 200 questions, 19 sections, 0% complete, 113 open P1, 47 open P1 due Week 2 |
| 2 | Priority filter | P1 = 113, P2 = 78, P3 = 9 |
| 3 | neededBy filter | Week 2 = 50, Week 4 = 82, Week 8 = 53, Post go-live = 15 |
| 4 | Kick-off only | 84 questions |
| 5 | Owner filter "HR / People Leadership" | 49 questions |
| 6 | Section counts | INT 15, LCE 14, 360 14, DAT 13 |
| 7 | Use Case Map | 11 use cases |
| 8 | Relevance rule | Mark "Candidate Experience" Out of scope: only LCE-08 dims. Mark "Exit" Out of scope: LCE-05, LCE-06, LCE-07 dim |
| 9 | Design-ready badge | Mark all 47 Week 2 P1 questions Answered: "Design-ready" appears. "Build-ready" needs the 61 Week 4 P1 questions answered too |
| 10 | Respondent mode | Role "Legal / DPO / Employee Relations" shows 21 questions and no scope, plan or risk edit controls |
| 11 | SF modules | 16 rows; Employee Central and Performance & Goals show "Live" |
| 12 | Data inventory | 30 fields; 6 High sensitivity; counter shows 6 not yet approved |
| 13 | Risks | 14 risks: 4 High, 9 Medium, 1 Low. Changing a likelihood updates score and rating |
| 14 | Plan | Start 2 Nov 2026: week 14 begins 1 Feb 2027; the Go-live bar (weeks 14 to 15) is amber |
| 15 | Persistence | Reload keeps answers; exported state JSON re-imports with no loss |
| 16 | Exports | CSV, Markdown and print view all download or open and contain answers |
| 17 | Advisor (after Prompt 2) | Send is blocked until the confirmation box is ticked; no API key appears in the browser's network requests or source |

---

## Troubleshooting

- **Agent changes things you did not ask for:** restate the boundary, for example "Only change the Dashboard; do not touch other screens."
- **Storage blocked in the preview:** the banner from Prompt 1 should appear. Export JSON to keep work.
- **Advisor returns invalid JSON:** ask the agent to enforce the response schema on the server and add one automatic retry.
- **Shared app shows a 403:** Google's docs suggest disabling privacy extensions such as Privacy Badger, or asking the agent to fix build issues and reshare.
- **Gemini key:** managed in the Secrets panel. Apps you download as a ZIP need `GEMINI_API_KEY` set in the new host environment.
- **Product accuracy:** AI Studio's features change. Check the current Build mode documentation: https://ai.google.dev/gemini-api/docs/aistudio-build-mode
