# Workbook Review and Open Decisions

What the review of the client's requirements workbook turned up, survey by survey, and the ten decisions the client needs to make before build. All counts were computed from the workbook, not counted by eye. The company name is written as `[Company]`.

Back to [`README.md`](README.md) · Requirements: [`01-requirements-register.md`](01-requirements-register.md) · Solutions: [`02-what-why-how.md`](02-what-why-how.md)

**Severity:** **High** blocks or changes the design · **Medium** will cause rework or confusion if left · **Low** tidy-up.

---

## Part A. Findings by survey

### S01 Engagement survey (70 items)

| # | Finding | Why it matters | Suggested fix | Severity |
|---|---|---|---|---|
| S01-1 | Items 42, 43 and 44 (safe to dissent, adapting to change, equal opportunities) have **no reporting factor**. | They will be missing from every factor score and from the factor dashboard pages. | Assign each to a factor, or report them as stand-alone items. | Medium |
| S01-2 | The factor **"Social Connection"** holds item 40 (DEI commitment) and item 41 (positive impact on our community). | The name does not describe the content, so managers will misread the score. Item 44 (equal opportunities) is a DEI item with no factor. | Rename the factor, or create an inclusion factor from items 40, 42 and 44. (Our suggestion, to discuss.) | Medium |
| S01-3 | Four factors have only one or two items: Innovation 2, Service and Quality Focus 2, Social Connection 2, Action 1. | Two-item scores swing widely, and with a confidentiality threshold they are often hidden for small teams. | Report these as items, not factors, or merge them into larger factors. | Low |
| S01-4 | Several items ask two or three things at once: item 7 (funding, people and effort), 24 (people, time and budget), 31 (job description and R&R), 45 (feedback and recognition), 47 (rewarded and recognised). | A low score cannot be traced to one cause, which makes action planning harder. | Split or reword. If trend lines from 2025 matter, keep the wording and note the limit. | Medium |
| S01-5 | The job-level answer list reads as nine items separated by semicolons (`L1 ; C-Suite; L2 ; Head of BU; ...`). It looks like five options, each pairing a level code with a title. | The option list could be built wrongly, and respondents may not know their own level code. Item 9 also uses "L1s & L2s" and item 31 uses "R&R". | Confirm the five options and write them as one label each, for example "L1 (C-Suite)". Replace jargon. | Low |
| S01-6 | The engagement survey is **English only**, while the new-hire survey is translated into Bahasa Indonesia and Tagalog. | Staff in those countries answer the long survey in a second language, and response quality may differ from the shorter survey. | Decide D9 before translation work starts. | High |
| S01-7 | The 11 voluntary diversity questions cover several categories that many jurisdictions treat as sensitive personal data, and several options are US-specific (military or veteran status, associate degree, first-generation college graduate, Two-Spirit, Hispanic/Latinx). The workbook does not say which countries are in scope. | Privacy and legal exposure, and answer options that do not fit local contexts. | Privacy review per country before translation and build (D5). | High |
| S01-8 | "Optional comment on every item" means up to **54 extra text fields**. | Large design, build and analysis load. Qualtrics has no native per-item comment toggle in the documentation reviewed (BR-04). | Decide D2. | Medium |
| S01-9 | Items 1 to 5 include the "recommend" statement. Qualtrics describes its own engagement score as a composite of three core measures, one of which is a recommend statement. | The dashboard needs a defined engagement index: which items, and favourable percentage or mean. | Agree the index definition before the dashboard is built (see BR-02). | Medium |

### S02 New hire 30-day check-in (33 items)

| # | Finding | Why it matters | Suggested fix | Severity |
|---|---|---|---|---|
| S02-1 | Items **11 and 28 are word-for-word identical** ("I have had a chance to establish good working relationships with people who are key to my role"). They differ only by a trailing full stop and sit in two sections (Induction and Relationships and Collaboration). | The same result is counted twice and respondents see a repeat. | Keep one. | Low |
| S02-2 | Item 32 is worded as a yes/no question ("Do you feel you are receiving sufficient feedback and support from your immediate manager?") but is typed as open text. | It cannot be scored or trended. | Make it a rating plus an optional comment. | Medium |
| S02-3 | The inventory says "30 days after start date (SF hire date)". In SuccessFactors these can be different fields. | The wrong field sends surveys early, late or twice for rehires. | Name the exact field (D10). | Medium |
| S02-4 | Translations cover **question text only**. Scale labels, instructions, privacy notice and the invitation and reminder emails are not provided. The workbook calls the language "Filipino (Tagalog)"; Qualtrics lists "Tagalog". | Respondents would see mixed languages. | Translate and review the rest. Use the Tagalog entry. | Medium |
| S02-5 | Items 22 to 26 equal engagement items 1 to 5, and item 17 equals engagement item 28. | Good: like-for-like comparison is possible. | Freeze this wording across both surveys. | Info |

### S03 Exit survey (23 questions)

| # | Finding | Why it matters | Suggested fix | Severity |
|---|---|---|---|---|
| S03-1 | The **regretted-leaver flag** is used for reporting and for prioritising follow-up, but it is not assumed to exist in a standard Employee Central set-up. | Without it, one of the main report cuts is empty. | Create the field and agree who sets it, and when (D4). | High |
| S03-2 | The trigger is described as "when a termination is entered". Terminations are often entered ahead of the last day, or after it. | The survey could arrive while the leaver still works, or after work email is gone. | Agree timing relative to the termination date (D8). | Medium |
| S03-3 | The inventory says "4 single select". The question tab has **7 single-select** (Q2, Q3, Q4, Q6, Q17, Q18, Q19), plus 1 multi-select (Q1), 1 yes/no (Q23), 10 ratings and 4 open text (Q5 conditional, Q20 to Q22 optional) = 23. | The two tabs disagree. | Correct the inventory row. | Low |
| S03-4 | The exit ratings are described as matching engagement items, but only one is word-for-word identical (see Part B). | Trend comparison would mix wording effects with real change. | Decide D7. | Medium |
| S03-5 | Question 23 (follow-up conversation) means the leaver is identified to the People team, while the rest of the survey may be read as confidential. | Respondents may not realise they are identified. | State it in the question wording. | Medium |
| S03-6 | Question 6 is noted as "Recommended by Gallup". That attribution was not checked. | An unverified claim in a client document. | Verify or remove the attribution. | Low |

### S04 Remote employee survey (8 items, example set)

| # | Finding | Why it matters | Suggested fix | Severity |
|---|---|---|---|---|
| S04-1 | The group is "filtered from SF data", but a remote or work-arrangement attribute is not assumed to exist. | No attribute means no reliable filter. | Confirm the field, or create one, and add it to the export (BR-16). | Medium |
| S04-2 | Item 6 is negatively worded. | Agreement is unfavourable, so it must be reverse-scaled or the score will read backwards. | Apply the reverse-scale setting and test (BR-17). | Low |
| S04-3 | It is an "example", so the real use is open-ended. | Without rules, ad hoc surveys cause survey fatigue. | Agree who can launch ad hoc surveys and how often one group may be surveyed. | Low |

### S05 to S07 Recruitment surveys (6, 10 and 7 questions)

| # | Finding | Why it matters | Suggested fix | Severity |
|---|---|---|---|---|
| REC-1 | The platform is "SmartRecruiters (to confirm)". The workbook's own overview says these surveys are expected to run in SmartRecruiters. | Qualtrics may not be the platform at all. | Decide D3 first. | High |
| REC-2 | In the selected-candidate survey, questions 5 and 8 are worded "Did you feel...?" but answered on an agreement scale. | The question and answer do not fit. | Reword as statements, for example "The recruitment process was inclusive and respectful." | Medium |
| REC-3 | Questions use four different 5-point scale styles (ease, satisfaction, "how well represented", agreement). | Averages and favourable percentages are not comparable across questions. | Harmonise labels, or map each to a common favourable scale. | Low |
| REC-4 | The candidate survey goes to all outcomes, including rejected candidates. | Consent, opt-out and retention for external people. | Privacy review (BR-22). | Medium |
| REC-5 | There is no single overall "would you recommend" or "would you apply again" measure for candidates. | Harder to trend one headline number. | Consider adding one. (Our suggestion, not in the workbook.) | Low |
| REC-6 | The "how did you hear" question repeats a source-of-hire field the applicant tracking system already holds. | Asking people what the system already knows adds length. | Keep it only if the self-reported answer adds value. | Low |

---

## Part B. Comparability: which items really match

The workbook says exit ratings "match engagement survey wording so results can be compared". Checked item by item:

### Exit survey against engagement survey

| Exit item | Engagement item | Relationship |
|---|---|---|
| 7 | 13 | Reworded (past tense) |
| 8 | 14 | Reworded (the manager is no longer named) |
| 9 | 23 | **Loose** ("tools and resources" versus "information I need") |
| 10 | 45 | **Loose** ("valued and recognised" versus "constructive feedback and recognition") |
| 11 | 51 | Reworded (past tense) |
| 12 | 32 | Reworded (shortened) |
| 13 | 44 | Reworded (past tense, word order) |
| 14 | 34 | Reworded (past tense) |
| 15 | 31 | **Loose** ("role matched what was described" versus "happy with my current role") |
| 16 | 1 | **Identical** |

### New-hire survey against engagement survey

| New-hire item | Engagement item | Relationship |
|---|---|---|
| 22 | 1 | Identical |
| 23 | 2 | Identical |
| 24 | 3 | Identical |
| 25 | 4 | Identical |
| 26 | 5 | Identical |
| 17 | 28 | Identical |

**Reading it:** new-hire to engagement comparison is clean. Exit to engagement is directional for nine of ten items. If like-for-like trends matter, align wording on at least items 9, 10 and 15 (decision D7).

---

## Part C. Ten decisions for the client

| ID | Decision | Options | Our recommendation (judgement) | Linked requirement |
|---|---|---|---|---|
| D1 | Confidentiality model for the engagement survey | Confidential with thresholds; fully anonymous; hybrid | Confidential, with enhanced confidentiality turned on and a higher threshold for diversity cuts | BR-03 |
| D2 | Per-item comments | Keep on all 54 items (custom code); one comment per factor; comment only when an item is rated low | One comment box per factor, or conditional on a low rating | BR-04 |
| D3 | Platform for the recruitment surveys | Qualtrics with webhook and middleware; Qualtrics with a scheduled file; Qualtrics Candidate Experience Program; stay in SmartRecruiters or a partner tool | Decide before any build. If one dashboard for everything is the goal, start with the scheduled file as the lowest-effort route | BR-21, BR-23 |
| D4 | Regretted-leaver flag | Who sets it, when, and in which SuccessFactors field | Set by the manager or HR business partner at the time the termination is entered, so it exists before the survey goes out | BR-10 |
| D5 | Sensitive demographics | Which of the 11 to keep, how to localise options, at what level to report | Keep fewer, localise per country, report at company or division level | BR-06, BR-25 |
| D6 | Exit survey scope | Voluntary leavers only, or involuntary and other leave types too | Voluntary only at first, then review | BR-09 |
| D7 | What "comparable" means | Directional themes; like-for-like items | Align wording on items 9, 10 and 15 if like-for-like is wanted | BR-15 |
| D8 | Exit survey timing and channel | Before the last day; after the last day (needs a personal email); both | Before the last day, with a reminder, unless local law or practice says otherwise | BR-09 |
| D9 | Language of the engagement survey | English only; add Bahasa Indonesia and Tagalog | Add the languages if the new-hire survey is already translated | BR-18, BR-19 |
| D10 | Who the lifecycle surveys cover | Which start-date field; contractors, rehires and internal transfers in or out | Use one named date field, exclude contractors, define a rule for rehires | BR-08 |

Each decision should be recorded with an owner and a date. Most are needed **before design freeze**, not before go-live.
