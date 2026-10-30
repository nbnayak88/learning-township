# Qualtrics EX Scoping Toolkit

A ready-to-use scoping questionnaire for implementing **SAP Qualtrics Employee Experience (EX)** alongside **SAP SuccessFactors**, packaged in four formats plus a build kit for turning it into a web app.

**Starting point assumed:** SuccessFactors Employee Central and Performance & Goals (PMGM) are live; the other SuccessFactors modules are upcoming; Qualtrics EX must go live in 3 to 4 months.

**Version:** 1.0, 28 October 2026 (AI Studio kit added 30 October 2026).

---

## What is in this folder

| File | What it is | Best used for |
|---|---|---|
| `Qualtrics_EX_Scoping_Questionnaire.xlsx` | Working tracker with nine tabs: Read Me, Summary, Use Case Map, Questionnaire, SF Module Readiness, Data Inventory, Timeline & Risks, Stakeholders, Sources | Running discovery. Clients answer in the yellow cells; the Summary tab shows progress automatically |
| `Qualtrics_EX_Scoping_Questionnaire.docx` | Landscape Word document with a response column beside every question, plus appendices | Sending to client stakeholders who prefer a document |
| `Qualtrics_EX_Scoping_Questionnaire.pptx` | 20-slide workshop deck: starting point, use-case landscape, Wave 1 vs Phase 2 hypothesis, architecture sketch, themes, ten first decisions, 16-week plan, top risks, next steps. Full question lists are in the speaker notes | Kick-off and discovery workshops |
| `Qualtrics_EX_Scoping_Questionnaire.md` | The complete questionnaire as Markdown | Editing, diffing and version control |
| `AI_Studio_Vibe_Coding_Prompt_EX_Scope_Studio.md` | A five-prompt pack for Google AI Studio's Build mode that generates an interactive app ("EX Scope Studio") from this questionnaire, with a 17-point acceptance checklist | Turning the questionnaire into a web app |
| `ex-scoping-data.json` | All questionnaire data in one JSON file: 200 questions, 11 use cases, 16 SF modules, 30 data fields, plan, 14 risks, 16 stakeholders | Import into the app built from the prompt pack |

The four `Qualtrics_EX_Scoping_Questionnaire.*` files carry the same content. They were generated from one shared question bank, so counts and wording match across formats.

---

## How to use it

1. **Kick-off:** present the `.pptx`. Ask the sponsor to mark every use case Wave 1, Phase 2 or Out of scope.
2. **Issue the questionnaire:** send the `.xlsx` (tracker) or the `.docx` (document). Ask people to answer the 84 kick-off questions (starred) first.
3. **Track:** the Summary tab of the `.xlsx` counts answered and open questions by section, priority and needed-by week.
4. **Decide scope:** use the Use Case Map, then challenge our Wave 1 / Phase 2 hypothesis in a workshop.
5. **Optional app:** follow `AI_Studio_Vibe_Coding_Prompt_EX_Scope_Studio.md` to build an interactive version and import `ex-scoping-data.json` into it.

---

## What the questionnaire covers

200 questions in 19 sections.

| # | Section | Questions |
|---|---|---|
| 1 | Project Context & Objectives | 11 |
| 2 | Use-Case Selection & Prioritisation | 9 |
| 3 | Licensing, Commercials & Contracting | 8 |
| 4 | Employee Engagement Survey | 11 |
| 5 | Pulse & Ad Hoc Listening | 8 |
| 6 | Lifecycle Moments: Onboarding, Exit & Candidate | 14 |
| 7 | 360 / Multi-Rater Feedback | 14 |
| 8 | Manager Effectiveness & Action Planning | 9 |
| 9 | Employee Technology Experience | 7 |
| 10 | Survey Content, Scales & Languages | 10 |
| 11 | SuccessFactors Integration & Architecture | 15 |
| 12 | Employee Data, Hierarchy & Attributes | 13 |
| 13 | Reporting, Dashboards & Analytics (incl. AI) | 11 |
| 14 | Security, Privacy & Compliance | 12 |
| 15 | Roles, Access & Governance | 8 |
| 16 | Communications, Change & Adoption | 10 |
| 17 | Upcoming SuccessFactors Modules & Sequencing | 10 |
| 18 | Delivery, Timeline, Testing & Support | 12 |
| 19 | Success Measures & Operating Model | 8 |

**Priority:** 113 questions are P1 (must answer, otherwise design or build is blocked), 78 are P2 (should answer before build), 9 are P3 (nice to have).

**Needed by:** 50 questions by Week 2, 82 by Week 4, 53 by Week 8, 15 after go-live.

**Each question carries:** an ID, the use case(s) it applies to, a priority, a primary owner (for example HRIS lead, Legal / DPO, People Analytics), a needed-by week, a response type, and a short "why we ask" note.

**Designed around the starting point:** for example, whether Qualtrics 360 or PMGM's multi-rater feedback should be the system of record, and how other SuccessFactors modules going live in the same window affect survey triggers, data and test calendars.

---

## Important caveats

- **Product options change.** SAP and Qualtrics product names, packaging and integration options change often. Treat every product option mentioned as something to validate with SAP and Qualtrics, not as a commitment.
- **Our judgement, not vendor statements.** The use-case "fit for a 3-4 month window" ratings, the Wave 1 / Phase 2 split, the 16-week plan and the risk scores are consulting hypotheses to be challenged in discovery.
- **Placeholders.** `[Client name]` and `[Consultant / firm]` are left blank for you to fill in. The example respondent in the Excel Read Me tab is fictional.
- **No client data.** Nothing in this folder contains real client or employee data. Do not add personal data about named individuals to answers if you use any AI features.
- **Edits are per file.** The files match today; editing one does not update the others. If you want the generator scripts added so all formats can be rebuilt from one source, that can be added.
- **AI Studio kit is untested by its author.** The prompt pack has been checked against the data file (for example the sample question in Prompt 1 matches question CTX-02 exactly), but the app it generates has not been run. Use the acceptance checklist in that file.

---

## Sources

- [Qualtrics Support: Step 1, Getting Ready to Launch Your 360 Project](https://www.qualtrics.com/support/employee-experience/getting-started-employee-experience/360-onboarding/form-building/)
- [Qualtrics and SAP announce new partnership (SAP Endorsed Apps), January 2025](https://www.qualtrics.com/articles/news/qualtrics-and-sap-announce-new-partnership-to-help-organizations-deliver-great-employee-experiences/)
- [SAP Store: Qualtrics XM for Employee Experience](https://www.sap.com/uk/products/hcm/partners/qualtrics-llc-qualtrics-employee-experience.html)
- [SAP User Groups: Qualtrics / SuccessFactors integration roadmap (archived deck)](https://assets.dm.ux.sap.com/webinars/sap-user-groups-k4u/pdfs/191212_qualtrics_successfactors_roadmap.pdf)
- [TechTarget: What capabilities does Qualtrics EmployeeXM offer?](https://www.techtarget.com/enterprise-software/answer/What-capabilities-does-Qualtrics-EmployeeXM-offer)
- [Google: Build apps in AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode)

Licence: see the repository's `LICENSE` and `NOTICE`.
