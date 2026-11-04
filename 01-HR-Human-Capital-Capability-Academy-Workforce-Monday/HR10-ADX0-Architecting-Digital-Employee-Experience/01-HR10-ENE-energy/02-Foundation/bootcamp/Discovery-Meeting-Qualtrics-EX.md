# Discovery Meeting — SAP Qualtrics Employee Experience for OmniVerse Energy Ltd.

**Project:** OmniVerse Energy — HR10 Digital Employee Experience (Workforce Monday theme)
**Product in scope:** SAP SuccessFactors Employee Experience Management by Qualtrics (EmployeeXM), alongside SuccessFactors Employee Central
**Phase:** 1 - Discover (SAP Activate), Day 1 of the [Activate dashboard](SAP-Activate-Dashboard-Qualtrics-EX.md)
**Status:** Pre-workshop preparation. Nothing here is a tenant result or a confirmed client decision.

## Read this first

- The requirements below are **hypotheses** derived from the OmniVerse Energy case (68,000 workforce, India and USA entities, offshore and refinery shift work, 3,500 contractors) and the 11 EX use cases in the scoping toolkit. The discovery workshop confirms, changes or drops each one.
- Capability evidence comes from public SAP and Qualtrics pages and community posts retrieved on 2026-11-04. Where a source is old or comes from one customer's experience, the row is `U` (Unverified) until Qualtrics or SAP confirms for the client's release and contract.
- Effort values are bands (S/M/L/XL) without day counts. Re-baseline after scope (countries, populations, languages, integrations) is confirmed.

---

## Part 1 — Fit-Gap view: business requirements against Qualtrics EX

Scale: F1 standard · F2 configuration · F3 in-app extensibility · G1 side-by-side extension · G2 third party · G3 custom · P process change · X out of scope · U unverified.

| REQ | Business requirement (hypothesis) | Process step / data object | Qualtrics + SuccessFactors capability | Source | Code | Resolution path | Effort | Risk |
|---|---|---|---|---|---|---|---|---|
| REQ-01 | Annual engagement survey across all legal entities with driver analysis | Engagement programme / survey, results | Employee Engagement solution with key-driver analysis and best-practice libraries | SAP Qualtrics solution announcement; SAP partner page (best-practice libraries) | F2 | Configure from standard template; localise questions | M | Low |
| REQ-02 | Pulse surveys on a frequent cadence to targeted groups (site, crew, function) | Pulse programme / sampling rules | Employee Pulse add-on to Engagement | SAP onboarding resource page | F2 | Configure; agree cadence and survey-fatigue rules | S | Low |
| REQ-03 | Onboarding feedback at set milestones (Day 1, 30, 90), including offshore crew cycles | Lifecycle trigger from Employee Central hire event | Lifecycle surveys triggered at milestones via employee data feed | SAP Qualtrics solution announcement; Qualtrics lifecycle page | F2 | Configure triggers; offshore rotation dates need a custom date attribute | M | Medium |
| REQ-04 | Exit survey on separation, with reason-code routing and sensitive handling | Lifecycle trigger from termination event / personal contact data | Exit surveys triggered from key dates in the employee export | 2019 SAP roadmap deck (dated); Qualtrics lifecycle page | U | Confirm current release; decide personal-email policy for leavers | M | High |
| REQ-05 | Sync of employee master data and org hierarchy from Employee Central | Integration / EX Directory | Scheduled SFTP export from Integration Center plus directory import automation; prepackaged sync extensions listed by SAP | Qualtrics directory automation doc; SAP community; SAP partner page | F2 | Integration Center export, directory automation, PGP; define population filter | M | Medium |
| REQ-06 | Event-driven survey trigger from Employee Central transactions (transfer, promotion) | Business rule / Intelligent Services | Intelligent Services events to Qualtrics, per 2019 roadmap; SAP page cites launch after select transactions | 2019 SAP roadmap deck; SAP partner page | U | Confirm event list and timing for the client's release | M | Medium |
| REQ-07 | Anonymity thresholds so small crews and refinery teams cannot be identified | Reporting roles / minimum group size | Hierarchy-based reporting with role design; exact threshold options not confirmed from sources found | Activate dashboard rows 03.A and 04.21 (design intent) | U | Confirm threshold settings; test against real hierarchy | M | High |
| REQ-08 | Manager dashboards and action planning with "you said, we did" follow-through | Dashboards by audience / action plans | Dashboards and AI-assisted analysis; action-plan integration with SuccessFactors Goals was "on the radar" in the 2019 roadmap | SAP partner page; 2019 SAP roadmap deck | U | Confirm action-plan capability; fallback is process change plus dashboards | M | Medium |
| REQ-09 | Summarise open-text comments across languages without exposing identity | Text analytics | AI summaries of open-text feedback with topics, themes and sentiment, protecting anonymity | SAP partner page (Qualtrics EX) | F2 | Enable per privacy policy; confirm language coverage and data-residency | S | Medium |
| REQ-10 | Reach deskless and offshore staff with no corporate email | Distribution channel | Email invitations documented; mobile, QR or SMS channels not confirmed from sources found | Activate dashboard row 04.B | U | Confirm channels; options may include kiosks, QR at sites, supervisor-led sessions | M | High |
| REQ-11 | Single sign-on for HR users and report viewers | Identity / SSO | SSO with SuccessFactors; SAP Cloud Identity Services recommended in the dashboard | SAP community blog (SSO username append); Activate dashboard row 04.A | F2 | Configure; align with Azure AD identity model | M | Medium |
| REQ-12 | Contractor workforce (3,500) included in selected surveys | Directory population / worker type | Depends on whether contingent workers sit in Employee Central | Case context only | U | Decide population; may need a separate data source (G1) | M | Medium |
| REQ-13 | Works-council or union consultation in applicable countries before launch | Change / consultation plan | Not a product capability | Activate dashboard row 02.14 | P | Process change; launch in unaffected countries first | S | High |
| REQ-14 | GDPR-style deletion and retention of employee data in the Qualtrics directory | Data governance / deletion | One implementer reported a custom iFlow was needed for deletion requirements | Qualtrics community thread (single customer) | U | Confirm native deletion options; fallback custom integration (G1) | M | High |
| REQ-15 | Candidate experience survey | Recruiting integration | Best-practice library includes candidate experience; Recruiting integration depends on Recruiting being live | SAP partner page; Activate dashboard Wave 2 note | X | Defer to Phase 2 until Recruiting is live | — | Low |
| REQ-16 | 360-degree feedback for leaders | Performance and Goals overlap | Qualtrics 360 Feedback exists; overlap with SuccessFactors PMGM multi-rater | SAP EX management page | P | Decision record: Qualtrics 360 or PMGM multi-rater | M | Medium |
| REQ-17 | Combine survey results with operational data (attrition, safety, absence) | People analytics / HR09 link | Qualtrics combines survey data with SAP operational data per SAP; client-side join is not confirmed | SAP EX management page | U | Confirm approach with HR09 Workforce Intelligence; may be G1 on BTP | L | Medium |

### Initial counts (17 requirements)

| Code | Count |
|---|---|
| F1 | 0 |
| F2 | 6 (REQ-01, 02, 03, 05, 09, 11) |
| F3 | 0 |
| G1/G2/G3 | 0 confirmed (REQ-12, 14, 17 are likely G1 candidates) |
| P | 2 (REQ-13, 16) |
| X | 1 (REQ-15) |
| U | 8 (REQ-04, 06, 07, 08, 10, 12, 14, 17) |
| **Total** | **17** (6 + 2 + 1 + 8) |

Reading: 6 of 17 look like standard configuration. 8 are unverified and most sit on the highest-risk topics (anonymity, deskless reach, leaver data, deletion). The discovery workshop should spend most of its time on those.

### Top gaps and risks to resolve in discovery

1. Reaching offshore, refinery and retail staff without corporate email (REQ-10).
2. Anonymity in small crews and rotations (REQ-07).
3. Leaver contact data and exit handling (REQ-04).
4. Data deletion and residency (REQ-14) and vendor DPIA timing.
5. Event-driven triggers: what is native for the client's release (REQ-06).

### Sources

- [SAP SuccessFactors Employee Experience, Qualtrics partner page (SAP)](https://www.sap.com/latvia/products/hcm/partners/qualtrics-llc-qualtrics-employee-experience.html)
- [SAP Introduces Three SAP Qualtrics Solutions (MarketScreener copy of SAP release)](https://www.marketscreener.com/SAP-436555/news/SAP-Introduces-Three-SAP-Qualtrics-Solutions-to-Unlock-New-Chapter-of-Employee-Experience-Manageme-28552914/)
- [Employee directory import automations (Qualtrics support)](https://www.qualtrics.com/support/employee-experience/directories/employee-directory-import-automations/)
- [SuccessFactors to Qualtrics roadmap, Dec 2019 (SAP user group deck, dated)](https://assets.dm.ux.sap.com/webinars/sap-user-groups-k4u/pdfs/191212_qualtrics_successfactors_roadmap.pdf)
- [SF to Qualtrics pulse integration thread (Qualtrics community)](https://community.qualtrics.com/integrations-11/how-to-integration-qualtrics-ex-with-successfactors-to-distribute-pulse-surveys-25140)
- [Qualtrics 360 and SuccessFactors user integration (SAP Community)](https://community.sap.com/t5/human-capital-management-blog-posts-by-members/beginner-s-guide-for-qualtrics-survey-and-sap-successfactors-user/ba-p/13516098)
- [SAP employee experience management overview (SAP, archived)](https://webarchive.library.unt.edu/web/20201219013614/https://www.sap.com/products/human-resources-hcm/employee-experience-management.html)

---

## Part 2 — Discovery workshop questions

Priority tags: **[M]** must ask in the session · **[F]** can follow up by questionnaire. Ask the [M] questions first.

### A. Business case and sponsorship

1. **[M]** What business problem should employee listening solve first: attrition, safety culture, productivity, transformation readiness, or something else?
2. **[M]** Who is the executive sponsor, and what decisions will they take from the results?
3. **[M]** Which outcomes would make the programme a success after 12 months (participation, action completion, retention, safety indicators)?
4. **[F]** What listening exists today (engagement survey, exit interviews, suggestion boxes), who runs it and on which tool?
5. **[F]** What has been tried before, and what did employees see happen as a result?
6. **[M]** What budget range and licence model has been discussed with SAP or Qualtrics?

### B. Scope, use cases and phasing

7. **[M]** Which of the 11 EX use cases are wanted in Wave 1? Test the hypothesis: annual engagement, pulse, onboarding, exit.
8. **[M]** Is Candidate Experience wanted, and is SuccessFactors Recruiting live or planned?
9. **[M]** Is 360 feedback needed in Qualtrics, or does Performance and Goals multi-rater cover it?
10. **[F]** Any use cases not on the list (safety climate, contractor induction feedback, shutdown or turnaround feedback, post-incident pulse)?
11. **[M]** Which legal entities and countries are in Wave 1 (India, USA, others)?
12. **[M]** What is the target go-live date and what is driving it (annual survey calendar, merger, regulation)?
13. **[F]** What is out of scope for now and who agreed that?

### C. Workforce profile and populations

14. **[M]** How many employees per segment (upstream, refining, retail, power, renewable, corporate) should be surveyed?
15. **[M]** Are the 3,500 contractors in scope, and where are they recorded (Employee Central, vendor system, procurement)?
16. **[M]** What share of the workforce has no corporate email or device at work?
17. **[M]** What languages are needed, and for which populations?
18. **[F]** How do crews rotate (14/28 patterns)? Should surveys avoid off-rotation periods?
19. **[F]** Are there seasonal or high-volume hiring groups (500+ retail hires per month) that need separate onboarding handling?
20. **[F]** Which groups are considered survey-fatigued or sensitive (night shift, offshore, new hires on probation)?

### D. Reaching employees

21. **[M]** How should offshore, refinery-floor and retail-station staff receive and complete surveys (personal phone, kiosk, QR code, supervisor-led session, paper)?
22. **[M]** Is it acceptable to use personal mobile numbers or personal emails, and under what policy?
23. **[M]** Is there a site-level communications channel (intranet, display screens, toolbox talks) we can use for launch messages?
24. **[F]** What is the typical time employees can spend on a survey during a shift?
25. **[F]** Are invitation emails filtered or blocked by IT security, and who can allow-list them?

### E. Employee Central data and integration

26. **[M]** Is Employee Central live, in which release, and what is the state of data quality for manager, email, location, event reason and org structure?
27. **[M]** Which attributes are needed for segmentation (legal entity, business unit, site, job family, shift pattern, tenure, grade)? Any that do not exist in Employee Central today?
28. **[M]** How current must the survey population be (daily, weekly, near real time)? What does the business gain from faster refresh?
29. **[M]** Which Employee Central events should trigger surveys (hire, transfer, promotion, leave, termination)? Are event reasons consistent enough to use?
30. **[F]** Which SFTP host, encryption standard (PGP) and file-handling rules does IT security require?
31. **[F]** Who owns the integration after go-live, and who monitors failed loads?
32. **[F]** Are there other HR systems holding employee data (payroll, time, learning) that should feed Qualtrics?
33. **[M]** Does the client already use other Qualtrics products (customer, product, brand) so that directory and tenant separation must be planned?
34. **[F]** Which environments exist (sandbox, test, production) and can a separate Qualtrics test setup be funded?

### F. Anonymity, privacy and legal

35. **[M]** What minimum group size is acceptable before results are shown, and does it differ by country or union agreement?
36. **[M]** Which countries need works-council, union or employee representative consultation before launch, and how long does it usually take?
37. **[M]** Which data protection laws apply (India DPDP Act, US state laws, GDPR for any EU staff)? Who is the Data Protection Officer?
38. **[M]** Where must survey data be hosted, and are there data-residency or cross-border transfer limits?
39. **[M]** How long may survey responses and directory records be kept, and how should deletion requests be handled?
40. **[M]** Is a vendor security review and a DPIA or equivalent assessment required, and how long does the client's process take?
41. **[F]** Is AI-based text analysis of comments allowed, and are there restrictions on sending comments to AI services?
42. **[F]** What is the policy for collecting personal contact data from leavers?
43. **[F]** Are there safety-sensitive topics (incident reporting, whistleblowing) where survey comments must be routed to a formal channel instead?

### G. Survey design and content

44. **[M]** Is there an existing engagement framework or question bank that must be kept for trend comparison?
45. **[F]** What cadence is wanted for pulse surveys and who decides sampling?
46. **[F]** Which onboarding milestones matter (Day 1, 30, 90, 180), and for offshore crews, which points in the rotation?
47. **[F]** What should the exit survey capture, and who sees the results (HR only, line manager, leadership)?
48. **[F]** What tone, branding and sponsor messages should accompany invitations?
49. **[F]** Are there accessibility needs (screen readers, low-literacy formats, translation review by site)?

### H. Reporting, action and follow-through

50. **[M]** Who should see which results (executives, HR business partners, line managers, site leaders)? Are there hierarchy rules?
51. **[M]** What must a manager be able to do with results (see scores, read comments, create an action plan, assign tasks)?
52. **[M]** How will the organisation prove "you said, we did", and who owns action tracking?
53. **[F]** Which dashboards must exist on day one?
54. **[F]** Which operational data should sit beside survey results (attrition, safety incidents, absence, overtime)? Where does it live today?
55. **[F]** Does reporting need to feed the People Analytics work (HR09), and who owns that integration?

### I. Identity, access and security

56. **[M]** Which identity provider is used (Azure AD, SAP Cloud Identity Services), and is single sign-on required for HR users and managers?
57. **[M]** Who will be Qualtrics brand administrator, survey owner and report viewer? Does this match Employee Central roles?
58. **[F]** What segregation of duties is required between survey owners, report viewers and technical administrators?
59. **[F]** Are there restrictions on external SaaS tools or IP ranges?

### J. Change management and adoption

60. **[M]** How do employees view surveys today (trust, past experiences)? What would make them believe results are anonymous?
61. **[M]** Which leaders will visibly sponsor the launch at site level?
62. **[F]** What training do managers, HR business partners and administrators need?
63. **[F]** Which communication channels work best for frontline and offshore staff?
64. **[F]** What participation rate is realistic for each segment, and how will it be monitored during launch?

### K. Governance, delivery and support

65. **[M]** Who sits on the project team and steering committee, and who is the day-to-day decision maker?
66. **[M]** Which other HR workstreams (Employee Central, Recruiting, Onboarding, Learning, Work Zone) share dates or dependencies with this one?
67. **[F]** Who will support the solution after go-live (internal team or partner), and what service levels are expected?
68. **[F]** How will SuccessFactors half-yearly releases and Qualtrics releases be managed?
69. **[F]** What success metrics and benefits register will Finance validate?
70. **[M]** What are the top three risks the client sees today?

### L. Close of session

71. **[M]** What decisions can be taken in the room, and which need escalation?
72. **[M]** Which documents or data should be shared before the Fit-to-Standard workshops (org chart, Employee Central extract profile, security policies, prior survey results)?
73. **[M]** Who owns each open action and by when?

---

## Part 3 — Suggested session plan

| Block | Topic | Questions |
|---|---|---|
| 1 | Business case, sponsorship and success measures | A (1–6) |
| 2 | Scope, use cases and phasing | B (7–13) |
| 3 | Workforce, reach and languages | C and D (14–25) |
| 4 | Employee Central data and integration | E (26–34) |
| 5 | Anonymity, privacy and legal | F (35–43) |
| 6 | Reporting, action, identity and change | H, I, J (50–64, 56–59) |
| 7 | Governance and close | K and L (65–73) |

## Open items after this document

- Confirm the real client requirement list. The REQ rows above come from the case context and the scoping toolkit, not from client sign-off.
- Verify every `U` row with SAP or Qualtrics for the client's release and contract.
- Convert confirmed answers into the REQ catalogue and Fit-Gap workbook for the Fit-to-Standard workshops (Activate days 6 to 7).
