# SAP Activate Dashboard — SAP SuccessFactors Employee Experience by Qualtrics

21-day distribution of SAP Activate activities across 6 phases for a Qualtrics Employee Experience (EmployeeXM) implementation alongside SuccessFactors. Same structure as the SAP SuccessFactors Employee Central Payroll dashboard, with Qualtrics EX content.

**Status:** design template. Every row is `Not Started`; nothing here is a tenant result.  
**Data files:** `SAP-Activate-Dashboard-Qualtrics-EX.csv` (63 rows, Notion-importable) · `EX-AI-CodeX-Prompts.md` (21 prompts)

## Read this first

- The 21 days are a **compressed teaching cadence**, not a delivery duration. The scoping toolkit plans a 16-week delivery; the mapping is below. Re-baseline durations from scope (countries, populations, languages, integrations) and label effort as an estimate.
- **Task IDs.** IDs such as `02.01–02.03` are the SAP Activate for SuccessFactors roadmap groups retained from the source dashboard; the Qualtrics wording is SuccessLabs content mapped onto them. IDs starting `EX-` are SuccessLabs additions for steps the generic roadmap does not cover. `QEX-CAP-DAY-nn` rows are the AI prompt track.
- **Journal cards.** References like `C07` point to the cards in [SF-Qualtrics-Config-Sequence-Journal](../../../01-SF-Qualtrics-Configuration-Sequence-Journal/SF-Qualtrics-Config-Sequence-Journal.md). Those cards are `Designed - not executed` until tenant evidence is added. Policy cases `P1` to `P6` come from the same journal.
- **Wave 1 vs Phase 2** is a hypothesis from the scoping toolkit to confirm with the sponsor, not a decision.

## Quality gates

| Day | Gate | Evidence before sign-off |
|---|---|---|
| 5 | Prepare | Licence and access confirmed, charter approved, security/DPIA review in flight, data-quality baseline, consultation countries identified |
| 7 | Explore | Wave 1 scope and backlog baselined, test strategy with policy cases P1-P6, content freeze plan. No build before this unless an explicit spike |
| 18 | Realize | UAT passed, defects within threshold, rollback tested, named support owner, dress rehearsal done |
| 20 | Deploy | Hypercare running, handover inventory, operations handed over, final customer sign-off |

## Phase summary (roadmap track)

| Phase | Rows | Days |
|---|---|---|
| 1 - Discover | 2 | 1–1 |
| 2 - Prepare | 9 | 2–5 |
| 3 - Explore | 5 | 5–7 |
| 4 - Realize | 21 | 8–18 |
| 5 - Deploy | 3 | 19–20 |
| 6 - Run | 2 | 21–21 |

## Roadmap track by day

| Day | Phase | Task ID | Activity | Type | Priority | Key deliverable |
|---|---|---|---|---|---|---|
| 1 | 1 - Discover | 01.01.01–01.01.04 | 01.01 Define EX Implementation Strategy, Scope & Phasing | Governance | Critical | EX scope statement, Wave 1 vs Phase 2 use-case hypothesis, phasing roadmap, effort estimate (labelled estimate) |
| 1 | 1 - Discover | 01.02.01–01.02.03 | 01.02 Organizational Change Management Overview & Employee-Trust Approach | Change Management | High | OCM approach document, stakeholder briefing, anonymity and trust principles |
| 2 | 2 - Prepare | 02.01–02.03 | 02.01–02.03 Project Kickoff, Licence, Tenant & System Access (Journal C01-C02) | Governance | Critical | Qualtrics EmployeeXM licence, administrator account and tenant URL; SF admin and Upgrade Center access; SFTP details; SAP Cloud ALM tenant |
| 2 | 2 - Prepare | 02.04–02.07 | 02.04–02.07 SF & Qualtrics Environment Strategy and Team Self-Enablement | Enablement | Critical | Environment and test-data decision record; project team enabled on fit-to-standard and the EX configuration sequence |
| 2 | 2 - Prepare | EX-02.S | 02.S Vendor Security, Privacy & DPIA Review Start | Security & IAM | Critical | Qualtrics security pack shared, vendor security and DPIA review started, data-residency question raised |
| 3 | 2 - Prepare | 02.08–02.10 | 02.08–02.10 Project Charter, Governance, Standards & Infrastructure | Governance | Critical | Project charter, governance model, RACI across the 16 stakeholder roles, schedule and budget, team logistics |
| 3 | 2 - Prepare | 02.11–02.13 | 02.11–02.13 Kickoff Workshop, OCM Concept & Change Plan | Change Management | High | Kickoff workshop delivered, OCM roles defined, Change Plan v1 |
| 4 | 2 - Prepare | 02.14–02.17 | 02.14–02.17 Business Config Assessment, Stakeholder & Comms Analysis | Change Management | High | Data as-is questionnaire complete, stakeholder map, communication plan, consultation-country list |
| 4 | 2 - Prepare | 02.18–02.21 | 02.18–02.21 Fit-to-Standard Prep, Employee Data Approach & Enablement Strategy | Data Migration | Critical | F2S workshop schedule, integration and analytics list, employee-data and directory approach, enablement strategy |
| 4 | 2 - Prepare | EX-02.D | 02.D Employee Central Data-Quality Profile | Data Migration | Critical | Profile of manager, email, location and event-reason quality; exception reports |
| 5 | 2 - Prepare | 02.22–02.23 | 02.22–02.23 Enablement Tooling & Prepare Phase Sign-Off | Governance | Critical | Enablement tooling ready, Prepare quality gate passed, customer sign-off |
| 5 | 3 - Explore | 03.01–03.03 | 03.01–03.03 Explore Kickoff, Project Monitoring & Participation Strategy | Project Management | High | Execution monitoring live, communication activities prepared, participation and adoption metrics defined |
| 6 | 3 - Explore | 03.04–03.05 | 03.04–03.05 Fit-to-Standard Workshops by Use Case | Configuration | Critical | Use-case process flows documented, configuration values confirmed, Wave 1 backlog locked |
| 6 | 3 - Explore | 03.06–03.08 | 03.06–03.08 Integration Design, Reporting Planning & Role Design | Integration | High | Integration design confirmed, reporting scope signed off, RBP and Qualtrics role design documented |
| 6 | 3 - Explore | EX-03.A | 03.A Employee Data, Hierarchy & Anonymity Design | Analytics | High | Reporting hierarchy, segmentation attributes, minimum group size and roll-up rules |
| 7 | 3 - Explore | 03.09–03.12 | 03.09–03.12 Learning Needs, Data Load Prep, Test Planning & Explore Sign-Off | Testing | Critical | Enablement curriculum confirmed, load plan, test strategy and plan with policy cases P1-P6, content freeze plan, Explore sign-off |
| 8 | 4 - Realize | 04.01–04.03 | 04.01–04.03 Realize Kickoff, Project Monitoring & Change Impact Analysis | Change Management | Critical | Realize monitoring active, change impact workshops conducted, impacts documented |
| 8 | 4 - Realize | 04.04–04.06 | 04.04–04.06 Qualtrics Projects, Upgrade Center Enablement & Pre-Upgrade Permissions (Journal C04-C06) | Configuration | Critical | Qualtrics projects created, pre-upgrade role-based permissions set, EX enabled in Upgrade Center |
| 9 | 4 - Realize | 04.07–04.09 | 04.07–04.09 Survey Programme Templates: Engagement, Pulse, Onboarding & Exit | Configuration | Critical | Question libraries, scales, anonymity settings and message templates drafted for the four Wave 1 programmes in non-production |
| 9 | 4 - Realize | 04.10–04.12 | 04.10–04.12 Qualtrics Directory Structure, Hierarchy & Copy to Test | Configuration | Critical | Directory fields, hierarchy and segmentation attributes configured, project team users created, configuration copied to test |
| 10 | 4 - Realize | 04.13–04.17 | 04.13–04.17 Integration Center Export, Directory Import Automation & PGP (Journal C07-C09) | Integration | Critical | Employee export scheduled with population filter, directory import automation running, PGP applied to the SFTP export (test) |
| 10 | 4 - Realize | 04.18–04.20 | 04.18–04.20 Role Permissions, OAuth Client & Production Initial Access (Journal C10-C12) | Security & IAM | Critical | Role-based permissions assigned, OAuth client and outbound connection created, production tenant access prepared |
| 11 | 4 - Realize | 04.21.01–04.21.04 | 04.21 Solution Configuration — Iteration 1 (Annual Engagement & Dashboards) | Configuration | Critical | Annual Engagement programme configured: questions, scales, anonymity, languages, hierarchy-based reporting roles |
| 12 | 4 - Realize | 04.21.05–04.21.09 | 04.21 Solution Configuration — Iteration 2 (Pulse, Onboarding, Exit & Triggers) | Configuration | Critical | Pulse, Onboarding and Exit programmes configured; business rule, Qualtrics IDs, email survey integration and Intelligent Services timing set (Journal C13-C16) |
| 13 | 4 - Realize | 04.22–04.24 | 04.22–04.24 Release Cycle Prep, Dashboards (Dev) & Role Configuration | Analytics | High | SF H1/H2 and Qualtrics release preparation, dashboards and role-based reporting in dev, roles configured in development |
| 13 | 4 - Realize | 04.25.01–04.25.03 | 04.25 Data Load — Development (Populate, Execute, Validate) | Data Migration | Critical | Population filter validated, directory loaded in non-production, populations reconciled to Employee Central, exceptions logged |
| 13 | 4 - Realize | EX-04.A | 04.A In-App Survey Integration & Optional SSO (Journal C17-C18) | Integration | High | In-app survey integration configured; SSO configured if in scope |
| 14 | 4 - Realize | 04.26–04.27 | 04.26–04.27 Solution Walkthrough & Dashboards in Test | Testing | High | Walkthrough completed with HR and sample managers, dashboards verified in test |
| 14 | 4 - Realize | 04.28–04.30 | 04.28–04.30 Access Governance (Test) & Integration Setup in Production | Security & IAM | High | Access governance configured in test, production export and directory import automation configured |
| 15 | 4 - Realize | 04.31–04.33 | 04.31–04.33 Production Integration: OAuth, Triggers & Event Timing | Integration | Critical | OAuth, business rule, email survey integration and timing configured in production; in-app survey integration if in scope |
| 15 | 4 - Realize | 04.34–04.35 | 04.34–04.35 Access Governance & Roles in Production | Security & IAM | High | Production roles and permissions set, administrators and reporting roles assigned, project team in production |
| 15 | 4 - Realize | EX-04.B | 04.B Translations, Message Templates & Invitation Deliverability | Configuration | High | Translations and templates loaded, invitation email allow-listing confirmed, reach options for deskless staff agreed |
| 16 | 4 - Realize | 04.36–04.37 | 04.36–04.37 Test Preparation & Directory Load in Test | Testing | Critical | Test cases, scripts and plans including policy oracle P1-P6, directory load in test, final data quality assessment |
| 17 | 4 - Realize | 04.38.01–04.38.03 | 04.38 Test Execution — Integration, UAT, Privacy, Accessibility & Pilot | Testing | Critical | Tests executed, defects re-tested, pilot with a small population, acceptance pack (Journal C19), execution report |
| 18 | 4 - Realize | 04.39–04.41 | 04.39–04.41 Enablement Delivery, Support Model & Cutover Preparation | Enablement | Critical | Manager toolkit and key-user training delivered, support model and runbook, cutover plan documented |
| 18 | 4 - Realize | 04.42–04.43 | 04.42–04.43 Production Reporting & Realize Phase Sign-Off | Analytics | Critical | Dashboards live in production for launch audiences, Realize gate passed, customer sign-off |
| 18 | 4 - Realize | EX-04.C | 04.C Cutover Dress Rehearsal & Rollback Decision Point | Project Management | Critical | Cutover rehearsal completed, go/no-go criteria, tested rollback, named support owner |
| 19 | 5 - Deploy | 05.01–05.02 | 05.01–05.02 Deploy Kickoff, Go/No-Go & Production Cutover | Project Management | Critical | Go/no-go decision, open issues resolved, production sync live, Wave 1 launched per cutover plan |
| 19 | 5 - Deploy | EX-05.A | 05.A Launch Communications & Participation Monitoring | Change Management | High | Sponsor message sent, FAQ and anonymity messaging live, early response-rate report |
| 20 | 5 - Deploy | 05.03–05.05 | 05.03–05.05 Hypercare, Handover & Deploy Phase Sign-Off | Governance | Critical | Hypercare running, handover inventory (Journal C20), operations handed over, Deploy gate and final sign-off |
| 21 | 6 - Run | 06.01–06.03 | 06.01–06.03 Run Phase: Operations, Release Management & Adoption | Governance | High | Operations active, SF and Qualtrics releases managed, participation and adoption metrics tracked, Wave 2 plan |
| 21 | 6 - Run | EX-06.A | 06.A Action Planning, 'You Said, We Did' & Value Tracking | Analytics | High | Action plans tracked, results communicated back, benefit register with baseline and owner |

Notes for each row are in the CSV `Notes` column.

## AI CodeX prompt track

The prompt track runs one day ahead of the roadmap in places (design artifacts are drafted before the matching build step), as in the Employee Central Payroll dashboard. Keep the roadmap track as the system of record for gates.

| Day | Phase | Task ID | Drafts | Type |
|---|---|---|---|---|
| 1 | 1 - Discover | QEX-CAP-DAY-01 | EX business case summary | Enablement |
| 2 | 1 - Discover | QEX-CAP-DAY-02 | EX solution vision document | Enablement |
| 3 | 2 - Prepare | QEX-CAP-DAY-03 | EX project charter | Project Management |
| 4 | 2 - Prepare | QEX-CAP-DAY-04 | EX SAP Activate project plan | Project Management |
| 5 | 2 - Prepare | QEX-CAP-DAY-05 | EX system and access readiness checklist | Security & IAM |
| 6 | 3 - Explore | QEX-CAP-DAY-06 | EX fit-to-standard analysis | Enablement |
| 7 | 3 - Explore | QEX-CAP-DAY-07 | EX survey programme design | Configuration |
| 8 | 3 - Explore | QEX-CAP-DAY-08 | Employee data and hierarchy blueprint | Configuration |
| 9 | 3 - Explore | QEX-CAP-DAY-09 | EX integration design | Integration |
| 10 | 3 - Explore | QEX-CAP-DAY-10 | Anonymity, privacy and DPIA pack | Security & IAM |
| 11 | 3 - Explore | QEX-CAP-DAY-11 | EX role and permission matrix | Security & IAM |
| 12 | 4 - Realize | QEX-CAP-DAY-12 | EX configuration log | Configuration |
| 13 | 4 - Realize | QEX-CAP-DAY-13 | EX configuration workbook | Configuration |
| 14 | 4 - Realize | QEX-CAP-DAY-14 | Survey trigger and business rule document | Configuration |
| 15 | 4 - Realize | QEX-CAP-DAY-15 | EX directory load and data quality strategy | Data Migration |
| 16 | 4 - Realize | QEX-CAP-DAY-16 | EX test strategy | Testing |
| 17 | 4 - Realize | QEX-CAP-DAY-17 | EX test script pack | Testing |
| 18 | 5 - Deploy | QEX-CAP-DAY-18 | EX cutover plan | Project Management |
| 19 | 5 - Deploy | QEX-CAP-DAY-19 | EX OCM and training plan | Change Management |
| 20 | 5 - Deploy | QEX-CAP-DAY-20 | EX go-live readiness checklist | Governance |
| 21 | 6 - Run | QEX-CAP-DAY-21 | EX run-phase support and value plan | Governance |

## Mapping to the 16-week scoping plan

| Scoping plan phase | Weeks | Dashboard days |
|---|---|---|
| Mobilise & discover | 1–2 | 1–5 |
| Design | 3–5 | 5–7 |
| Build & integrate | 5–10 | 8–15 |
| Test & pilot | 10–13 | 16–17 |
| Go-live preparation | 12–14 | 18 |
| Go-live | 14–15 | 19 |
| Hypercare & handover | 15–16 | 20–21 |

## Assumptions and open points

- Sector lens (Energy, from the bootcamp folder) is an assumption to confirm: field and shift workforce reach (deskless access), and avoiding survey windows during critical operating periods, are plausible considerations but are not from client data.
- Candidate Experience depends on SuccessFactors Recruiting go-live; 360 depends on the Qualtrics versus PMGM multi-rater decision.
- Added versus the Employee Central Payroll sample: vendor security/DPIA start (EX-02.S), cutover dress rehearsal and rollback decision point (EX-04.C), launch communications (EX-05.A), action planning and value tracking (EX-06.A).
- No owners, RACI names or effort estimates are assigned yet; add them per engagement.
