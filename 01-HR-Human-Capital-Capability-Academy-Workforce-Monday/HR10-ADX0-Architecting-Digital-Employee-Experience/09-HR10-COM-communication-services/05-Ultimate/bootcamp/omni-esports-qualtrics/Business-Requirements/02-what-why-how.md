# What, Why, How: Solution for Each Requirement

For each of the 25 requirements: **What** the client needs, **Why** the verdict is what it is (the Qualtrics capability or limit behind it), and **How** to deliver it. Register and verdict legend: [`01-requirements-register.md`](01-requirements-register.md).

**Evidence tags** show how strong the support is:
- **Docs**: Qualtrics, SAP or SmartRecruiters official pages.
- **Community**: practitioner posts on the Qualtrics or SAP communities. Useful, not official.
- **Inference**: my reasoning from the above. Validate before relying on it.

The tags come from a first research pass. A final check re-read the sources behind the claims that drive the verdicts; [`04-sources-and-verification.md`](04-sources-and-verification.md) shows what was re-verified, what was corrected, and what was not re-checked.

Sources: [`04-sources-and-verification.md`](04-sources-and-verification.md).

**Contents:** [Engagement (S01)](#engagement-s01) · [SuccessFactors data](#successfactors-data) · [New hire (S02)](#new-hire-30-day-s02) · [Exit (S03)](#exit-survey-s03) · [Ad hoc (S04)](#ad-hoc-s04) · [Languages](#languages) · [Recruitment (S05 to S07)](#recruitment-s05-to-s07) · [Cross-cutting](#cross-cutting)

---

## Engagement (S01)

<a id="br-01"></a>
### BR-01 · Annual engagement survey with 54 rated items

**Verdict:** ✅ Standard · **Effort:** S · **Evidence:** Docs

**What.** One company-wide survey each year: 54 statements rated on a 5-point agreement scale (Strongly disagree to Strongly agree), 3 open-text questions and 13 demographic questions, 70 items in all.

**Why it works in standard.** Qualtrics EX has a dedicated **Engagement** project type for exactly this, with participants, organisational hierarchies, dashboards and action planning. Qualtrics's own build guide recommends matrix tables for "the bulk of the survey", multiple choice for demographics, and text entry for qualitative feedback. A matrix table holds up to 100 statements.

**How.**
1. Create an **Engagement** project from the catalogue.
2. Build the 54 ratings as Likert **matrix tables**, grouped by the workbook's 9 sections (The Culture 12 items, Your Role 10, Growth and Development 9, People and Teams 6, Overall 5, Our Leaders 4, Your Manager 4, Company Confidence 3, Action 1). Keep each matrix to roughly 5 to 12 statements per page.
3. Use **one identical scale** with identical labels on every matrix so favourable percentages are comparable.
4. Add the 3 text-entry questions and the demographic multiple-choice questions (see BR-05, BR-06).
5. Preview on a phone and on a desktop. Reduce scrolling by page, not by dropping items.

**Watch-outs.** Reporting factors are set up as categories for the dashboard (BR-02). Settle them before the build, not after.

---

<a id="br-02"></a>
### BR-02 · Results by factor and by team, then action planning

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs, Inference

**What.** Dashboards that show results for each of 15 reporting factors (for example Leadership, Management, Enablement) and for each team, followed by action planning.

**Why.** Engagement projects support **organisational hierarchies** and **action planning**. Lifecycle projects do not support hierarchies, which matters for S03 (see BR-14). The work is configuration: the hierarchy must be loaded (BR-07) and each item mapped to a factor.

**How.**
1. Load the org hierarchy and employee attributes from SuccessFactors (BR-07).
2. Map the 54 items to the workbook's "Reporting factor" column. **Fix the gaps first:** items 42, 43 and 44 (safe to dissent, adapting to change, equal opportunities) have **no factor assigned**, and the factor "Social Connection" holds the DEI and community-impact items (40, 41), which does not match its name. See [`03-workbook-review-and-decisions.md`](03-workbook-review-and-decisions.md).
3. Create dashboard roles: leaders see their own hierarchy, People team and analysts see wider.
4. Turn on **action planning**; decide who can create and who can view plans.
5. Set confidentiality thresholds (BR-03). Small teams will be hidden by design.

**Watch-outs.** Four factors have only one or two items (Innovation 2, Service and Quality Focus 2, Social Connection 2, Action 1). Scores on two items are unstable and, with thresholds, often hidden. Consider reporting these as items rather than factors.

---

<a id="br-03"></a>
### BR-03 · Confidentiality model "to be agreed"

**Verdict:** 🟡 Standard + config · **Effort:** S · **Evidence:** Docs

**What.** The workbook leaves the confidentiality model open for the engagement survey.

**Why.** Qualtrics supports the realistic options. Dashboards apply an **anonymity threshold** (minimum responses before data shows; the documented default is **5** for both results and comments). **Enhanced Confidentiality** adds field-level protection: each dashboard field can be marked extremely, somewhat or not sensitive, and results below the threshold are merged into the next smallest group. It is included in all EX licences and available in Engagement, Lifecycle, Pulse and Ad Hoc projects. *Not re-verified in the final check:* a hybrid link mixing identified and anonymous responses, whether administrators can identify respondents in a confidential survey, and the exact names of the sensitivity levels. Confirm these in the tenant before writing the respondent notice.

**How.**
1. Decide the model with the People team and the data protection officer:
   - **Confidential:** personal links, answers tied to HR attributes, small groups hidden. Best for team-level reporting.
   - **Anonymous:** one open link, no attributes. Limits reporting to what respondents choose to tell you.
   - **Hybrid:** both, with expected counts entered so response rates calculate.
2. Set the organisation-wide threshold (admin setting) and per-dashboard thresholds.
3. Turn on **Enhanced Confidentiality** and mark the diversity fields **extremely sensitive** (BR-06).
4. Write the respondent notice to match the model exactly, in every survey language.
5. Test with a small team to confirm what a leader can and cannot see.

**Recommendation (our judgement).** Confidential with Enhanced Confidentiality, and a higher threshold for diversity cuts.

---

<a id="br-04"></a>
### BR-04 · Optional comment on every rated item

**Verdict:** 🟠 Workaround · **Effort:** M to L · **Evidence:** Docs, Community, Inference

**What.** The workbook says respondents can add a comment to every item. That is 54 optional comment fields.

**Why it is not standard.** The Qualtrics matrix-table documentation describes no comment box per statement. The nearest options are a **Matrix Text Entry** variation (a grid of text boxes, built as its own question) and text entry on scale points in a **carousel** matrix only. Qualtrics's engagement build guide recommends a few open-text questions and does not address per-item comments. Practitioners achieve per-row comments with **custom JavaScript** over a hidden Matrix Text Entry question. That is supported by the platform's scripting but is custom code to build, test and maintain. Some other engagement tools offer item-level comments as a built-in setting, so the client may be expecting that.

**How (three options, easiest first).**
1. **Reduce (recommended).** One optional comment box per **factor** (15 boxes) or per section (9), as ordinary text-entry questions. Fully standard.
2. **Conditional.** Show a comment box only when an item is rated low (display logic on each item). Standard, but more questions in the editor.
3. **Per-item, custom.** A hidden Matrix Text Entry plus JavaScript that adds a comment icon to each row. Test on mobile and with screen readers, and document the script. All 54 fields must be mapped as text fields in the dashboard.

For every option: each comment field must be mapped in the dashboard, the **comment anonymity threshold** applies, and text analysis topics need configuring. AI Comment Summaries are available only on the newer pricing and packaging plans.

**Decision for the client.** Is "a comment on every item" a hard requirement, or a feature of the tool they used before? See decision D2 in the review document.

---

<a id="br-05"></a>
### BR-05 · Three open-text questions and comment analysis

**Verdict:** ✅ Standard · **Effort:** S · **Evidence:** Docs

**What.** Three questions: what we do well, what we do not do well, and what else we should have asked.

**Why.** Text entry is a standard question type, and Qualtrics recommends it to "collect qualitative feedback". Analysis uses **Text iQ** topics. The AI **Comment Summaries** widget exists for EX dashboards but is limited to the newer plans and needs a permission enabled by a brand administrator.

**How.**
1. Add the 3 text-entry questions after the ratings.
2. Map them as text fields in the dashboard settings.
3. Configure Text iQ topics (the Qualtrics library includes expert-designed EX topics).
4. Confirm the licence before promising AI summaries.
5. Warn readers that comments can identify people; rely on the comment threshold and brief managers on handling.

---

<a id="br-06"></a>
### BR-06 · 13 demographic questions, 11 voluntary

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs, Inference

**What.** Job level, a "fan before you were hired" question, and 11 voluntary diversity questions: gender identity, sexual orientation, race or ethnicity, disability or long-term health condition, neurodivergence, religion or spirituality, education, first-generation graduate, caregiving, socioeconomic background, and military or veteran affiliation. Each offers "Prefer not to say".

**Why.** They are plain multiple-choice questions, which Qualtrics recommends for demographics. Dashboard settings let you rename fields, set field types and mark sensitivity, and Enhanced Confidentiality suppresses small groups. **The risk is not product capability.** Several of these topics are treated as especially sensitive personal data in many places, the workbook implies a workforce in at least Indonesia and the Philippines (translations exist for both), and some options are US-specific (military or veteran status, "associate degree", "first-generation college graduate").

**How.**
1. Build as single-answer multiple choice, each with "Prefer not to say". Keep them **optional** (no forced response).
2. Ask these **only inside the survey**. Do not import them from HR systems.
3. Map each as a dashboard field and mark all 11 **extremely sensitive**.
4. Get data protection officer and legal review **per country** before translation. Localise the education, military and socioeconomic options.
5. Decide the reporting level: consider showing diversity cuts at company or division level only, with a higher threshold than 5.
6. Job level: if the survey is confidential, take it from SuccessFactors rather than asking; ask it only for anonymous respondents.

---

## SuccessFactors data

<a id="br-07"></a>
### BR-07 · Employee attributes and org hierarchy from SuccessFactors

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs, Community

**What.** Every Qualtrics survey in scope needs people data from Employee Central: hire date, termination details, manager, department, location, job level and language.

**Why.** SAP ships an Integration Center scenario, **"Qualtrics Integration Definition - EC User Export to SFTP"**, that exports employee data to an SFTP location, from where Qualtrics imports it into the employee directory. The 2019 integration roadmap describes a scheduled file with employee data and the organisational hierarchy. Prerequisites reported by practitioners: Qualtrics enabled in the Upgrade Center, an SFTP server, a Qualtrics EX licence and a brand administrator. Some implementation partners prefer SFTP file transfer over the "native" route for flexibility.

**How.**
1. In SuccessFactors, activate the Qualtrics export scenario in the Upgrade Center. **Do not re-upgrade it later:** an SAP knowledge-base article warns that re-upgrading removes custom fields you added.
2. Add the fields you need: user ID, email, manager ID (this builds the hierarchy), department, team, location, job level, hire date, termination date, leave type, language, work arrangement, regretted-leaver flag (BR-10).
3. Schedule the export (daily is typical) to the SFTP location.
4. In Qualtrics, map the file to employee directory metadata and **confirm the date format on each date field** (date-based automations need it, BR-08).
5. Build the hierarchy from the manager field and verify it.
6. Validate with about 20 records across countries before turning on any automation.

**Watch-outs.** Integration user permissions (role-based permissions), employees with no email, and personal data minimisation: export only fields a survey needs.

---

## New hire 30-day (S02)

<a id="br-08"></a>
### BR-08 · 30-day check-in sent automatically after hire date

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs, Community

**What.** Each new hire receives a 33-item survey 30 days after their SuccessFactors start date.

**Why.** **Lifecycle** projects exist to automate participant upload and survey distribution. Participant import automation adds people from the directory on a schedule using conditions on metadata, including **date operators** (on, before, between, in the past), up to 20 conditions, and message automation sends the invitation. Practitioners trigger onboarding surveys from a start-date window. SAP's own integration also supports an Intelligent Services timing rule ("send after X days of the event").

**How.**
1. Create a **Lifecycle** project and build the survey (BR-18 for languages).
2. Participants tab: add an automation on the directory's start-date field. Use a **window** (for example, started between 29 and 31 days ago) rather than an exact day, so weekends and late entries are caught.
3. Exclude groups the client does not want surveyed (for example contractors), by metadata.
4. Message automation: invitation on import, plus reminders (for example day 3 and day 7).
5. Create a dashboard and roles. Lifecycle has no hierarchy (BR-14), so grant access by role.
6. Test with dummy future-dated hires before go-live.

**Watch-outs.** A start date entered late in SuccessFactors can fall outside a narrow window. Rehires and internal transfers need an explicit rule.

---

## Exit survey (S03)

<a id="br-09"></a>
### BR-09 · Exit survey triggered by a termination in SuccessFactors

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs, Community

**What.** The exit survey goes out when a termination is entered in SuccessFactors.

**Why.** SuccessFactors **Intelligent Services** can fire on an Employee Termination event and pass the leaver to Qualtrics, either immediately or with a timing offset (one practitioner runs it 21 days before the termination date). Qualtrics Lifecycle then adds the person as a participant and sends the invitation. Practitioner notes: the event model must have the termination event enabled, and **terminations entered before the integration went live are invisible** to the event trigger.

**How.**
1. Configure the termination event and timing in SuccessFactors (Integration Center with Intelligent Services).
2. Create the exit **Lifecycle** project. Set participant automation to pick up the leaver records.
3. **Choose timing deliberately.** If work email is switched off on the last day, send before it, or collect a personal email where the law allows.
4. Set reminders; decide the survey expiry.
5. Reconcile once before go-live: any termination already entered must be loaded by file, not by event.

**Watch-outs.** Back-dated terminations, cancelled terminations, and rehires. Also confirm whether **involuntary** leavers are in scope (decision D6).

---

<a id="br-10"></a>
### BR-10 · Leaver details pre-filled from SuccessFactors

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs, Inference

**What.** Department, manager, location, level, tenure, leave type and a **regretted-leaver flag** are attached to each response, not asked.

**Why.** Directory metadata travels with the participant and can be mapped to dashboard fields. The only real dependency is on SuccessFactors: a regretted-leaver flag is not something to assume exists in a standard Employee Central set-up (our inference), so it must be created and maintained.

**How.**
1. Add the fields to the export (BR-07). Calculate tenure from hire and termination dates.
2. Create the **regretted-leaver** field in SuccessFactors. Decide **who sets it and when**. It must be set **before** the survey is sent, or the response will not carry it.
3. Map all fields in the dashboard settings; mark department and manager as sensitive.
4. Decide a fallback: if the flag is set after sending, either re-import the attribute or update it on the response record.

---

<a id="br-11"></a>
### BR-11 · Select up to 3 reasons, then pick the main one

**Verdict:** ✅ Standard · **Effort:** S · **Evidence:** Docs

**What.** Question 1 lets the leaver pick up to 3 of 14 reasons. Question 2 asks which was most important and shows only the reasons picked.

**Why.** Qualtrics **carry forward** can show only the selected choices from an earlier question, and display logic can use the **selected count**. The multiple-answer question has an **Answers Range** validation that sets a minimum and maximum number of selections, so "up to 3" is a setting, not code.

**How.**
1. Question 1: multiple answer, 14 choices, with "Other" and a text box.
2. Set **Answers Range** to a maximum of 3 (minimum 1 if a reason is required).
3. Question 2: single answer, **carry forward selected choices** from Question 1 (Carry Forward Choices, "Selected Choices"). Show it only when 2 or more reasons were selected. When only 1 was chosen, record it as the main reason automatically (embedded data).
4. Keep the reason list **stable** across years. Reordering or renaming breaks trend lines.

---

<a id="br-12"></a>
### BR-12 · Conditional question and optional open text

**Verdict:** ✅ Standard · **Effort:** S · **Evidence:** Docs

**What.** Question 5 ("What could we have done?") appears only if Question 4 is "Yes, definitely" or "Possibly". Four open-text questions are optional.

**Why.** Display logic and optional (non-forced) text entry are core survey features.

**How.** Add display logic to Q5 on Q4 equal to Yes or Possibly. Leave "force response" off for Q5 and Q20 to Q22. Keep the 19 core questions as the forced or expected set.

---

<a id="br-13"></a>
### BR-13 · Follow-up conversation request routed to the People team

**Verdict:** 🟡 Standard + config · **Effort:** S · **Evidence:** Docs, Inference

**What.** Question 23 asks whether the leaver wants a follow-up conversation. The People team prioritises regretted leavers.

**Why.** The **Workflows** tab is available in all EX project types (Engagement, Lifecycle, Ad Hoc, 360, Pulse). A workflow can fire when a response meets a condition and send an email or task. SAP also describes real-time alerts for at-risk staff in its Employee Lifecycle offer.

**How.**
1. Workflow trigger: response completed in the exit project.
2. Condition: Q23 equals Yes.
3. Task: email to a **shared People-team mailbox** with leaver, contact detail, manager and the regretted flag.
4. Add a sub-condition: regretted equals Yes sends a high-priority message (or goes to a separate recipient).
5. **Word Q23 plainly:** "If you say yes, the People team will see who you are." Without that, the answer and the identity disclosure are not matched.

**Watch-outs.** Lifecycle has **no hierarchy-based data restrictions**, so keep alert recipients and dashboard access to the People team only.

---

<a id="br-14"></a>
### BR-14 · Exit trends by team, tenure and regretted versus non-regretted

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs, Inference

**What.** Trend reporting of reasons, preventability and experience, cut by team, tenure and leaver type.

**Why.** Lifecycle dashboards filter and break out by mapped metadata and apply anonymity thresholds. Two limits matter: Lifecycle projects have **no organisational hierarchy and no hierarchy-based access restrictions**, so "by team" means a team or department **field**, not a manager roll-up. And leaver counts per team are small, so the default threshold of 5 will hide most team-level cuts.

**How.**
1. Map department, team, manager, tenure band, leave type and regretted flag (BR-10). Create the tenure band in SuccessFactors or as a calculated field.
2. Pages: top 3 reasons and main reason (Q1, Q2), preventability (Q4), time spent deciding (Q3), pay gap (Q19), experience ratings (Q7 to Q16).
3. Use period trend widgets (month, quarter).
4. Set expectations: report most cuts at **division or company level**; team-level cuts appear only when numbers allow.
5. Restrict dashboard access to the People team and named analysts.

---

<a id="br-15"></a>
### BR-15 · Exit and new-hire results comparable with engagement

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs, our analysis of the workbook

**What.** Exit ratings are meant to "match engagement survey wording so results can be compared". The new hire survey repeats engagement items too.

**Why.** Comparability depends on wording, which Qualtrics cannot fix. In the workbook, **only exit item 16 is word-for-word identical** to an engagement item. Items 7 to 15 are reworded into the past tense, and three are loose matches (item 9 "tools and resources" versus "information I need"; item 10 "valued and recognised" versus "constructive feedback and recognition"; item 15 "role matched what was described" versus "happy with my current role"). In the new hire survey, items 22 to 26 equal engagement items 1 to 5 and item 17 equals engagement item 28, so those compare directly. For cross-survey analysis Qualtrics offers **Employee Journey Analytics**, which joins data from several EX projects into one dataset (up to 10 sources, left joins) and includes a guided "onboarding's impact on engagement" analysis. Forum users report row-limit errors when joining several large surveys, so test with real volumes.

**How.**
1. Agree what "comparable" means: like-for-like item trends, or directional themes.
2. For like-for-like, **align wording** on the pairs that matter (at minimum items 9, 10, 15).
3. Use the same scale labels in every survey.
4. For individual-level journeys (new hire, then engagement, then exit), build an **Employee Journey Analytics** project. Confirm the licence and implementation support first.
5. Otherwise, place dashboards side by side with identical factor names, and label cross-survey comparisons "directional".

---

## Ad hoc (S04)

<a id="br-16"></a>
### BR-16 · Ad hoc survey to a filtered group

**Verdict:** 🟡 Standard + config · **Effort:** S · **Evidence:** Docs

**What.** Short targeted surveys for one group, with remote employees as the example (8 items).

**Why.** The **Ad Hoc Employee Research** project type is built for impromptu research. Participants are chosen from the employee directory. Participant automation is not available in Ad Hoc projects, so each run is selected manually. The prerequisite is data: SuccessFactors must hold a reliable "remote" attribute.

**How.**
1. Add a work-arrangement field in SuccessFactors and to the export (BR-07).
2. Create the Ad Hoc project, filter participants by that field, send and remind.
3. Save the project as a template for future ad hoc surveys.
4. Use the standard dashboard with the thresholds from BR-03.
5. Note that Ad Hoc projects have **no organisational hierarchy**, so results cannot be rolled up by manager or unit.

---

<a id="br-17"></a>
### BR-17 · Negatively worded item scored correctly

**Verdict:** ✅ Standard · **Effort:** S · **Evidence:** Docs (general), Inference

**What.** Item 6 ("I sometimes feel like I miss out on things because I work remotely") is negatively worded, so agreeing is unfavourable.

**Why.** Qualtrics can **recode** answer values so a higher score always means more favourable. Confirm the exact setting during the build and that the dashboard's favourable percentage reads the right way.

**How.**
1. In the dashboard, use the **Scales** setting and turn on **Reverse Scale** for the item. Recoding survey values and dashboard scoring are separate things, so do not rely on a recode alone.
2. Check a few test responses end to end (survey to dashboard).
3. Label the item clearly in the data dictionary.
4. Consider placing negatively worded items on their own page to avoid straight-lining.

---

## Languages

<a id="br-18"></a>
### BR-18 · New hire survey in English, Bahasa Indonesia and Filipino (Tagalog)

**Verdict:** ✅ Standard · **Effort:** S, plus review M · **Evidence:** Docs

**What.** 33 questions in three languages. The client has supplied translations of the questions.

**Why.** Qualtrics lets one survey carry **multiple languages**, with translation files imported and exported as XML, Unicode text (Excel), CSV or TSV, and custom languages if one is missing. **Bahasa Indonesia** is listed. Filipino appears as **"Tagalog"**; there is no separate "Filipino" entry.

**How.**
1. Build and freeze the English survey first.
2. Export the translation file and place the supplied translations row by row.
3. Import, preview each language, and make both visible to respondents.
4. **Fill the gaps:** the workbook translates **question text only**. Scale labels, instructions, the privacy notice and the invitation and reminder emails are not provided and must be translated and reviewed.
5. Have a native speaker review each language in the live preview.
6. Confirm how the company name is written in each language.

---

<a id="br-19"></a>
### BR-19 · Each new hire gets the survey in their own language

**Verdict:** 🟡 Standard + config · **Effort:** S to M · **Evidence:** Docs (link parameter), not verified for automated lifecycle invites

**What.** Automatic language selection, not a manual choice.

**Why.** A survey link can carry a language parameter (`Q_Language`), so language can be set per link. This research did **not** confirm how Lifecycle message automation passes a participant's language, so treat it as something to test.

**How.**
1. **Start safe:** put a language selector at the top, with a short instruction in all three languages.
2. Export a language field from SuccessFactors (BR-07).
3. Test whether Lifecycle message automation can use that field. If it cannot, create one message automation per language group (filtered by language or country).
4. Translate the invitation and reminder emails per language (BR-18).

---

## Recruitment (S05 to S07)

<a id="br-20"></a>
### BR-20 · Recruitment survey content

**Verdict:** ✅ Standard · **Effort:** S · **Evidence:** Docs

**What.** Three short surveys (6, 10 and 7 questions): single-select scales, yes/no, multi-select with "Other", and open text.

**Why.** All are standard question types. The surveys use different scale styles (ease, satisfaction, "how well represented", agreement), which is fine for a survey but needs scoring decisions for dashboards.

**How.**
1. Build once, reuse: candidate questions 1, 2 and 6 equal selected-candidate questions 1, 2 and 10.
2. Add a **"Not applicable / did not reach this stage"** option, or display logic, for questions about interviews and offers (a candidate rejected at screening cannot answer them).
3. Assign numeric scores (1 to 5) to each scale for averages, and treat them as ordinal.
4. Harmonise "Did you feel...?" questions that use an agreement scale (selected-candidate questions 5 and 8).

---

<a id="br-21"></a>
### BR-21 · Automatic triggers from SmartRecruiters

**Verdict:** 🟠 Workaround · **Effort:** L · **Evidence:** Docs, vendor pages, Inference

**What.** Candidate survey at the end of the process, selected-candidate survey after offer acceptance, hiring-manager survey after the role is filled. The workbook marks the platform "to confirm".

**Why it is not standard.** This research found **no native Qualtrics connector to SmartRecruiters**. Qualtrics's prebuilt recruiting integration is for **SAP SuccessFactors Recruiting**, not SmartRecruiters. SmartRecruiters has its own marketplace partners for candidate surveys (for example Survale and Starred). The building blocks for a custom link do exist: Qualtrics **Workflows** can be started by an external **JSON event** (an HTTP call; needs an API token and "advanced programming knowledge"), and Qualtrics's **Candidate Experience Program** uses workflows to send a survey as a candidate moves stage. SmartRecruiters offers **webhooks** (for example `application.created`, `application.status.updated`) and a REST API.

**How (options).**
- **A. Webhook plus middleware (best if Qualtrics is the platform).** SmartRecruiters webhook, then a small function or integration platform that translates the call, creates or updates the contact in Qualtrics by API, and starts a JSON-event workflow that sends the survey. Carry stage, outcome, job, recruiter and hiring manager as attributes.
- **B. Scheduled file.** Nightly extract from SmartRecruiters to a file, loaded into Qualtrics, with a scheduled workflow that surveys new rows. Simpler; up to a day of delay.
- **C. Qualtrics Candidate Experience Program.** Delivered by Qualtrics or a partner; confirm the licence and the data feed from SmartRecruiters.
- **D. Keep it in SmartRecruiters or a partner tool.** Nothing to build in Qualtrics; results sit outside the EX dashboards.

**Watch-outs.** SmartRecruiters webhooks support custom authentication headers; how a Qualtrics JSON-event URL should be secured was not verified. Middleware is the safe way to bridge the two, and to handle retries, duplicate prevention (a candidate with several applications) and throttling.

---

<a id="br-22"></a>
### BR-22 · Surveys to external candidates of every outcome

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs, Inference

**What.** Candidate feedback goes to all candidates (including rejected), and the selected-candidate survey to those who accept.

**Why.** Candidates are external people, outside the employee data that EX projects use. The Candidate Experience Program holds them as **XM Directory contacts** in a mailing list. The product handles this; the open points are consent and retention.

**How.**
1. Decide the legal basis for contacting rejected candidates and put an opt-out in every invitation.
2. Decide anonymity: if answers must not influence hiring, do not link them to the candidate record.
3. Set a **retention period** for candidate data.
4. Limit frequency: one survey per candidate per application.
5. Review per country (BR-25).

---

<a id="br-23"></a>
### BR-23 · Hiring manager surveyed when a role is filled

**Verdict:** 🟠 Workaround · **Effort:** M · **Evidence:** Docs, Inference

**What.** The 7-question hiring-manager survey goes to the manager after the role is filled.

**Why.** Same trigger gap as BR-21. The audience is internal, so managers can be matched to the employee directory by email.

**How.**
1. Use the same integration as BR-21 with the **job-filled** event.
2. Match manager by email to the directory; one survey **per filled role**, not per candidate (multi-hire requisitions need a rule).
3. Add reminders.
4. Report by recruiter, function and location.

---

## Cross-cutting

<a id="br-24"></a>
### BR-24 · A results dashboard for every Qualtrics survey

**Verdict:** ✅ Standard · **Effort:** M · **Evidence:** Docs

**What.** Leaders and the People team need dashboards for S01 to S04, with segments.

**Why.** Engagement, Lifecycle, Ad Hoc and Pulse projects all have participants tabs and dashboards. Confidentiality and thresholds apply in each.

**How.**
1. One dashboard per project, with a shared core: response rate, favourable percentage by factor.
2. Roles: People team and analysts (wide), leaders (their hierarchy, S01 only), nobody outside the People team for exit (BR-14).
3. Apply thresholds (BR-03).
4. Add the comment and text-analysis pages (BR-05).

---

<a id="br-25"></a>
### BR-25 · Data protection, sensitive data and data residency

**Verdict:** 🟡 Standard + config · **Effort:** M · **Evidence:** Docs (data centres), Inference

**What.** Sensitive items in scope: 11 diversity questions, a pay-change question in the exit survey, a salary-fairness question for hires, and candidate data. The translations imply staff in several countries.

**Why.** Not a Qualtrics feature gap; a governance task. Qualtrics hosts in regional data centres, and it announced a **Singapore** data centre in 2020 as the default for South-East Asia. Other documentation lists Canada, the United States, Australia and Germany. The tenant's data centre must be confirmed. **Local privacy law was not researched** here.

**How.**
1. Run a privacy impact assessment per country before build.
2. Confirm the **tenant data centre** with SAP or Qualtrics, and the data processing terms.
3. Give notices in each survey language; match them to the confidentiality model (BR-03).
4. Set retention and deletion for survey data and candidate data.
5. Minimise: drop or make optional the high-risk items (for example the pay-change percentage), and report diversity at higher levels.
6. Limit access by role; log who can see exports.
