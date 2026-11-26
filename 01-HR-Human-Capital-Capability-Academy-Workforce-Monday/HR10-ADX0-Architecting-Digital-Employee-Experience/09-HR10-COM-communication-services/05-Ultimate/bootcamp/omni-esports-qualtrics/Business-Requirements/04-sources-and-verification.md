# Sources and Verification

How strong each claim in this folder is, and what was **not** checked. Read this before quoting anything to the client.

Back to [`README.md`](README.md) · Solutions: [`02-what-why-how.md`](02-what-why-how.md)

**Method.** The analysis was drafted from vendor documentation, SAP knowledge-base articles and practitioner posts, then a final check re-read the sources behind the claims that drive the verdicts. Nothing was built or tested in a Qualtrics or SuccessFactors tenant.

| Status | Meaning |
|---|---|
| **Verified** | Re-read in the final check on an official Qualtrics, SAP or SmartRecruiters page |
| **Community** | Reported by practitioners or Qualtrics staff on community forums. Useful, not official |
| **Not re-verified** | Stated in the first pass and not re-read in the final check. Treat as a lead |
| **Inference** | Our reasoning from the above. Validate before relying on it |

---

## 1. Corrections made in the final check

These changed the content of the other files.

| Where | What changed | Why |
|---|---|---|
| BR-11 | "Select up to 3" is now **✅ Standard**, using the **Answers Range** validation. The first draft said there was no maximum-selections setting. | The Qualtrics multiple-choice page lists Answers Range: "Specify a minimum and maximum number of responses the respondent can provide." |
| BR-03 | The statements about a **hybrid link**, about administrators being able to identify respondents in a confidential survey, and about the names of the sensitivity levels are now marked unverified. | The confidentiality overview page does not contain them. |
| BR-16 | Added: Ad Hoc projects have **no organisational hierarchy**. | Confirmed on the project comparison page. |
| BR-17 | Added the dashboard **Reverse Scale** setting. | Confirmed on the Scales (EX) page. |
| BR-20 | The "not applicable" advice is now limited to the case where selected-candidate questions are reused for all candidates. | The candidate-feedback questions are generic, so they do not need it. |
| BR-21 | Softened the statement about callback authentication. | SmartRecruiters documents custom authentication headers for webhooks. How a Qualtrics JSON-event URL is secured was not verified. |
| BR-22 | Candidates are held as **XM Directory contacts** in a mailing list. | The Candidate Experience Program page describes it this way, not as a separate candidate directory. |
| Counts | Verdict totals are now 8 Standard, 14 Standard + config, 3 Workaround. | BR-11 moved. |

---

## 2. Claim-by-claim status

| # | Claim | Used in | Status | Source |
|---|---|---|---|---|
| 1 | EX project types and their differences: org hierarchy available for Engagement and Pulse, **not** for Lifecycle or Ad Hoc; scheduled participant automation for Lifecycle and Pulse, manual import for Engagement and Ad Hoc; up to 15 dashboards per Engagement, Lifecycle or Ad Hoc project; Workflows tab in all | BR-02, 08, 14, 16, 24 | Verified | Creating a Project (EX) |
| 2 | Default confidentiality threshold is **5** for data points and comments. Basic and enhanced confidentiality. Available in Engagement, Lifecycle, Pulse and Ad Hoc. Included in all EX licences. Enhanced groups sub-groups that fall below the threshold | BR-03 | Verified | Confidentiality Overview (EX) |
| 3 | Hybrid link; administrators can identify respondents in a confidential survey; names of sensitivity levels | BR-03 | **Not re-verified** | First pass |
| 4 | Multiple-answer **Answers Range** validation (min and max) | BR-11 | Verified | Qualtrics multiple-choice page |
| 5 | **Carry Forward Choices** can carry forward "Selected Choices" | BR-11 | Verified | Carry Forward Choices page |
| 6 | Participant import automation: date operators (on, on or after, before, between, in the past or next), up to 20 conditions, maximum date range 200 days, run on chosen weekdays and time; participant automation only for Lifecycle and Pulse | BR-08, 09 | Verified | Participant Import Automation |
| 7 | SuccessFactors Integration Center scenario "Qualtrics Integration Definition - EC User Export to SFTP". Re-upgrading it **removes custom fields** | BR-07 | Verified | SAP KBA 3691728 |
| 8 | Integration steps and prerequisites (Upgrade Center, SFTP, brand administrator) | BR-07 | Community | SAP community blog posts |
| 9 | Terminations entered **before** the integration went live are not picked up by the event trigger; one customer sends the exit survey 21 days before the termination date | BR-09 | Community | Qualtrics Experience Community (answer by a Qualtrics employee) |
| 10 | Onboarding survey started from a start-date window via automated participant import. Where the timing rule lives (SuccessFactors or Qualtrics) is disputed in forum posts | BR-08 | Community | Qualtrics Experience Community |
| 11 | Multi-language surveys, translation import and export as XML, Unicode text (Excel), CSV or TSV, custom languages. **Bahasa Indonesia** and **Tagalog** are listed; **Filipino** is not | BR-18 | Verified | Translate Survey; Languages in Qualtrics |
| 12 | Language set by a `Q_Language` link parameter; automatic language by participant data in lifecycle invitations | BR-19 | **Not re-verified** | First pass |
| 13 | Dashboard **Reverse Scale** setting for reverse-coded questions | BR-17 | Verified | Scales (EX) |
| 14 | Recode values and dashboard scoring are different things, so test end to end | BR-17 | Community | Qualtrics Experience Community |
| 15 | Comment Summaries widget needs Text iQ set up, a permission enabled by a brand administrator, and the newer pricing and packaging plan | BR-04, 05 | Verified | Comment Summaries Widget (EX) |
| 16 | **Employee Journey Analytics** joins data from several EX projects: maximum 10 sources, left outer joins only, guided journeys for onboarding to engagement and for attrition. Forum users report row-limit errors when joining several large surveys | BR-15 | Verified; last point Community | Employee Journey Analytics pages; community thread |
| 17 | **Candidate Experience Program**: 4 to 5 pre-built surveys, candidate stage and status from the applicant tracking system, XM Directory mailing list, Workflows triggered by an Experience ID Change event, contact frequency rules. Named integrations are SuccessFactors Recruiting and a JSON event for Greenhouse or Workday | BR-21, 22 | Verified | Candidate Experience Program |
| 18 | A **JSON event** lets external software start a Qualtrics workflow by HTTP request | BR-21 | Verified | JSON Event page |
| 19 | JSON event needs an API token and "advanced programming knowledge" | BR-21 | **Not re-verified** | First pass |
| 20 | SmartRecruiters offers webhooks (for example `application.created`, `application.status.updated`), custom authentication headers for callbacks, and an API using API key or OAuth 2.0 | BR-21 | Verified (developer documentation; event names from a third-party list) | SmartRecruiters developer documentation |
| 21 | **No native Qualtrics connector to SmartRecruiters** was found in the documentation searched. SmartRecruiters has marketplace partners for candidate surveys | BR-21, 23 | Inference (a negative finding) | Searches in both passes; partner pages |
| 22 | SAP completed its acquisition of SmartRecruiters in September 2025. SmartRecruiters stays available as a standalone product and is described as interoperable with SuccessFactors | BR-21 | Verified | SAP news release |
| 23 | SAP and Qualtrics announced in January 2025 that SuccessFactors customers can contract Qualtrics XM for Employee Experience under an SAP Endorsed Apps agreement | README | Verified | Qualtrics news article |
| 24 | A native **per-item comment toggle** does not exist in standard Qualtrics | BR-04 | Inference (a negative finding). Not exhaustively checked | Matrix and engagement documentation reviewed; no such setting found |
| 25 | Action planning is part of the Qualtrics engagement offer | BR-02 | Verified as a product claim. Licence packaging not checked | Qualtrics product page |
| 26 | Qualtrics describes engagement as a composite score of three core measures, one being a recommend statement | S01-9 | Verified | Qualtrics engagement guide |
| 27 | Qualtrics opened a Singapore data centre in 2021 as the default for Southeast Asia. Other regions listed by a third-party marketplace entry: Canada, United States, Australia, Germany | BR-25 | Verified (Singapore); the other list is dated third-party information | Qualtrics news; marketplace listing |
| 28 | Matrix tables hold up to 100 statements; the Qualtrics build guide recommends matrix tables for the bulk of the survey, multiple choice for demographics and text entry for qualitative feedback | BR-01, 05 | **Not re-verified** | First pass |
| 29 | Matrix Text Entry and JavaScript as the route to per-item comments | BR-04 | Community, **not re-verified** | First pass |
| 30 | Statements about local privacy law | BR-06, 22, 25 | **Not researched** | None. Design cautions only, not legal advice |

---

## 3. What was not checked

- **Licences and entitlements.** Which EX modules the client has (Engagement, Lifecycle, Pulse, Journey Analytics, Candidate Experience, AI summaries) and under which pricing plan.
- **The client's tenant.** Data centre, brand settings, existing integrations, and what is switched on.
- **SuccessFactors set-up.** Which fields, events and permissions exist in the client's Employee Central.
- **Local law** in every country where staff or candidates sit.
- **Behaviour in practice.** Every workaround and every date or language trigger should be tested in a sandbox.
- **Sources blocked during the check.** Some Qualtrics support pages could not be fetched. Claims that depend on them are marked **Not re-verified**.

---

## 4. Sources

Qualtrics
- [Creating a Project (EX)](https://www.qualtrics.com/support/employee-experience/projects/creating-a-project-ex/)
- [Confidentiality Overview (EX)](https://www.qualtrics.com/support/confidentiality-overview-ex/)
- [Multiple choice question type](https://www.qualtrics.com/support/survey-platform/survey-module/editing-questions/question-types-guide/standard-content/multiple-choice/)
- [Carry Forward Choices](https://www.qualtrics.com/support/survey-platform/survey-module/question-options/carry-forward-choices/)
- [Participant Import Automation](https://www.qualtrics.com/support/employee-experience/creating-ee-project/participants-tab/participants-ee/participant-import-automation-el/)
- [Getting Started with Employee Lifecycle](https://www.qualtrics.com/support/employee-experience/getting-started-employee-experience/getting-started-employee-lifecycle/getting-started-with-employee-lifecycle/)
- [Translate Survey](https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/translate-survey/)
- [Languages in Qualtrics](https://www.qualtrics.com/support/survey-platform/getting-started/languages-in-qualtrics/)
- [Scales (EX)](https://qualtrics.com/support/employee-experience/creating-ee-project/dashboards-tab/dashboard-management/dashboard-settings/scales-ee)
- [Comment Summaries Widget (EX)](https://www.qualtrics.com/support/employee-experience/creating-ee-project/dashboards-tab/widgets-ee/analysis-widgets-ee/comment-summaries-widget-ex/)
- [Employee Journey Analytics Overview](https://qualtrics.com/support/employee-experience/employee-journey-analytics/employee-journey-analytics-overview/)
- [Creating A Data Model (EX)](https://www.qualtrics.com/support/employee-experience/employee-journey-analytics/creating-a-data-model/)
- [Onboarding Journey](https://www.qualtrics.com/support/employee-experience/employee-journey-analytics/onboarding-journey/)
- [Candidate Experience Program](https://www.qualtrics.com/support/employee-experience/creating-ee-project/common-use-cases-ee/candidate-experience-program/)
- [JSON Event](https://www.qualtrics.com/support/survey-platform/actions-module/json-events/)
- [Workflows Basic Overview](https://www.qualtrics.com/support/survey-platform/actions-module/setting-up-actions/)
- [Qualtrics and SAP announce new partnership (January 2025)](https://www.qualtrics.com/articles/news/qualtrics-and-sap-announce-new-partnership-to-help-organizations-deliver-great-employee-experiences/)
- [Qualtrics announces Singapore data centre](https://qualtrics.com/news/qualtrics-announces-singapore-data-centre-in-support-of-businesses-and-governments-across-southeast-asia)
- [What is employee engagement (composite score)](https://www.qualtrics.com/au/experience-management/employee/start-employee-engagement-program)

SAP
- [SAP KBA 3691728: upgrade option on the Qualtrics export scenario](https://userapps.support.sap.com/sap/support/knowledge/en/3691728)
- [SAP support: Employee Experience Management by Qualtrics onboarding resources](https://support.sap.com/en/product/onboarding-resource-center/qualtrics.html)
- [SAP completes SmartRecruiters acquisition](https://news.sap.com/2025/09/sap-completes-smartrecruiters-acquisition/)
- [SAP user groups: Qualtrics and SuccessFactors integration roadmap (archived, 2019)](https://assets.dm.ux.sap.com/webinars/sap-user-groups-k4u/pdfs/191212_qualtrics_successfactors_roadmap.pdf)

SmartRecruiters
- [Webhooks security](https://developers.smartrecruiters.com/docs/webhooks-security)
- [Receiving webhook notifications](https://developers.smartrecruiters.com/docs/receiving-webhook-notifications)
- [SmartRecruiters Marketplace: Survale](https://marketplace.smartrecruiters.com/partners/survale)

Community and practitioner posts (not official)
- [Lifecycle offboarding survey integrated with SuccessFactors](https://community.qualtrics.com/questions/21425)
- [Lifecycle onboarding survey not triggered using EC SF](https://community.qualtrics.com/questions/21265)
- [Beginner's guide: Qualtrics and SuccessFactors user integration](https://community.sap.com/t5/human-capital-management-blog-posts-by-members/beginner-s-guide-for-qualtrics-survey-and-sap-successfactors-user/ba-p/13516098)
- [Employee Journey Analytics with several surveys](https://community.qualtrics.com/questions/16171)

Product names, packaging and limits change often. Check current documentation, and confirm with SAP and Qualtrics, before quoting.
