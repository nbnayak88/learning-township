# A transfer delivered twice, an access change never confirmed

SuccessLabs Academy · HR12 — Connected HR Enterprises · GICS11 Real Estate · OmniSpace Real Estate Ltd.

IIL — Industry Immersion Lab · Level 0 Origin Story · Sprint · Edition 2026-11-01

Mission: Architecting Experiences for a Better World.

Planning reference: HUB-ORIGIN-HR12-RE-sprint. This preserves the existing planning ID, not an LMS or enrollment ID.

## 1. One learner promise

In 120 minutes, design one recoverable HR handoff that separates event delivery from confirmed business outcome.

One persona-led story · One Decision Build Card · Exactly three tabletop tests. Use synthetic data and paper decisions. No tenant configuration, live workforce data or executed system test is required.

## 2. Read the evidence accurately

HR12 describes disconnected HR, payroll, finance, property and project services, duplicate entry and weak cross-system auditability.

OmniSpace is fictional. Original detailed research remains outside this Origin Story. Existing OSP persona and master IDs are retained. This incident, dialogue, worker records and proposed controls are new educational additions. They do not describe an actual event, configured deployment or achieved result.

Unresolved source conflict: HR02a stipulates 19,000 employees, 24 countries, Dubai/New York HQ, $185B AUM and 1,150 assets. Several other HR pages use 5,000+ employees and seven regions; the enterprise register OSP-Q01 says scale/HQ were not supplied in its earlier parent-only review. Neither profile is promoted to a reconciled enterprise fact. Source financial figures, dates, error rates, roadmaps and benefit claims remain unvalidated fictional assumptions or proposals. No US-HQ/Hyderabad historical variant is silently merged.

## 3. Origins: the question survives the medium

These closed windows are educational groupings, not universal invention dates or OmniSpace corporate biography. Adoption overlaps. Older paper, spreadsheet, ERP and cloud practices can coexist through the present. The point is to ask what each process makes easier and which decision remains unresolved.

| Teaching window | Process evolution lens | Question to carry forward |
|---|---|---|
| 1970–1984 | Paper notifications and rekeying | Who records and owns the fact? |
| 1985–1994 | Scheduled file exchange | Do two records describe the same thing? |
| 1995–2004 | ERP interfaces and shared master-data mappings | Which rule and approval make the change valid? |
| 2005–2014 | APIs and event-based workflow orchestration | Did the receiving service complete the task? |
| 2015–2025 | Cloud observability and assisted integration triage | What evidence and human authority bound assistance? |

Counterexample: digitizing an inaccurate record can spread its error faster. Choose an older practice worth retaining, such as a visible owner or a worker’s right to challenge a record.

## 4. One persona-led story

Sofia Tan (OSP-P05), Chief Digital and Information Officer leads this episode.

Sofia follows a synthetic approved property transfer from HR to payroll, IAM and property services. The event broker reports delivery success twice. Maya Patel still sees the previous property assignment and Omar Haddad cannot confirm access removal. Choose: declare integration complete, replay everything, or reconcile each target by business key and version.

Pause: write your choice and reason before opening the evidence reveal. Identify the person who bears the cost of a wrong answer.

Evidence reveal: The second message is a retry, an older assignment event arrived later, and property services rejected the newest schema. Sofia records an idempotency key, effective assignment version and target-specific status. HR remains authoritative for the approved employment fact. Each target owner confirms its own business result before closure.

Revise the original decision in a different color. Explain what evidence changed it and which uncertainty remains. A reasonable alternative is a controlled manual workflow with fewer integrations. Defend its cost, accessibility and reliability rather than assuming more automation is better.

## 5. Application responsibility, data ownership and human rights

This is a proposed learning architecture, with vendor-independent responsibilities. SAP examples illustrate possible application roles only; no license, configured connector or present product capability is inferred.

| Application responsibility | Accountable owner | Authoritative facts | Human decision right |
|---|---|---|---|
| Core HR | HR data owner | Approved assignment and effective version | HR authorizes correction to source fact |
| Integration service | Integration owner | Contract, idempotency key, retries and dead-letter record | Operator replays only under approved recovery rules |
| Payroll, IAM and property targets | Each target business owner | Accepted version and realized target outcome | Targets reconcile and confirm outcome independently |

An application processes records; an accountable business owner governs them. Share only the minimum data required for a declared purpose. Record who may see, correct, approve and challenge it. Keep sensitive employee and tenant detail outside general worksheets. Automation may check completeness or draft a notice; consequential hiring, pay, promotion, work authorization and access decisions retain designated human approval.

People and adoption: Ingrid’s change discipline asks for an accessible notice, protected practice time, an employee challenge route and role rehearsal. A completed walkthrough is insufficient evidence of independent task success. Consider shared devices, language, field connectivity and shift constraints.

Real Estate connection: dependable workforce handoffs support property service and tenant trust. Workforce changes alone do not prove lower building energy, higher occupancy, improved asset value or investment returns. Those outcomes need separate measurement and attribution.

## 6. The exact 120-minute Origin Story

| Minutes | Work on the same card |
|---|---|
| 0–10 | State the promise, business need and affected people. |
| 10–30 | Explore the historical windows and retain one useful older practice. |
| 30–45 | Choose, reveal evidence and revise the story decision. |
| 45–60 | Assign application responsibilities, data owners and human authority. |
| 60–90 | Build the synthetic decision card; compare an alternative and a justified local variation. |
| 90–110 | Conduct T01–T03 on paper and record observed decisions and revisions. |
| 110–120 | Explain the card in 60 seconds and frame the Pre-Foundation question. |

Selective resource use fits inside these activities. Sprint is the format only at Origin Story; later levels continue the same narrative through deeper learning and implementation work.

## 7. One synthetic experiment: Decision Build Card

Inputs: RE-EVENT1200, assignment version 2 effective 2 November, duplicate v2, delayed v1, property-schema rejection and missing IAM outcome confirmation.

Build task: Write one event contract, data-minimization rule, per-target state map, reconciliation and authorized replay condition.

Use one card with seven fields:

1. Need and history — the affected person, business capability and enduring lesson.
2. Identity and time — relevant keys, population, dates, timezone and source versions.
3. Ownership and authority — application, authoritative fact, accountable owner and human approver.
4. Choice and alternative — initial choice, evidence reveal, revised decision and a credible counterexample.
5. Local variation and safeguards — justified regional/property policy, minimum data and accessible challenge route.
6. Exception and recovery — state, owner, notification, containment, fallback and reconciliation condition.
7. Test evidence and measure — T01–T03 input, expected, observed, evidence note, revision and remaining uncertainty.

## 8. Exactly three tabletop tests

| Test ID and challenge | Input / reveal | Expected decision in this proposed design |
|---|---|---|
| OSP-HR12-T01 — Duplicate and reorder | v2 arrives twice, then older v1. | Apply v2 once, prevent older state overwriting it, retain traceable processing evidence. |
| OSP-HR12-T02 — Rejecting target | Property service rejects the new schema. | Quarantine affected delivery, alert owner and correct/version contract before controlled replay. |
| OSP-HR12-T03 — Unknown outcome | Transport acknowledgment exists but IAM result is missing. | Keep business outcome unconfirmed, reconcile target record and invoke approved recovery. |

Learner records: observed tabletop result, evidence, reviewer question and pass/revise for each test. These fields are initially empty. Publishing expected results does not execute tests or establish a pass. Accept the card only after all fields and three observed results support the promise; any unauthorized consequential action requires redesign.

## 9. Source-to-evidence traceability

Existing enterprise anchors: OSP-M03 (scope), OSP-M10 (process), OSP-M11 (digital thread), OSP-M17 (risk/security), OSP-M18 (workforce/adoption), OSP-M19 (readiness/quality), OSP-M20–22 (value/optimization). The source crosswalk is retained in the source register below.

The following IDs are newly introduced educational design anchors, not pre-existing approved client requirements or achieved evidence:

| Educational ID | Connection and purpose | Evidence / present status |
|---|---|---|
| OSP-HR12-REQ01 | OSP-M10/M18: design one recoverable HR handoff that separates event delivery from confirmed business outcome | Card choice, source facts and T01; planned. |
| OSP-HR12-REQ02 | OSP-M17/M19: preserve human authority, exceptions and recoverability | Card boundaries and T02–T03; planned. |
| OSP-HR12-ADR01 | OSP-M03/M11: bounded authoritative records and explicit handoffs rather than an ungoverned all-in-one status | Record alternatives, trade-off, owner and conditions; proposed. |
| OSP-HR12-EXP01 | OSP-M19: one synthetic Decision Build Card | T01–T03; unexecuted. |
| OSP-HR12-M01 | Learning measure: completeness of seven card fields | Completed fields / 7 × 100 after observation. Unfilled result stays unavailable; completeness alone does not prove correctness. |
| OSP-HR12-M02 | OSP-M20: operational measurement hypothesis — unreconciled targets, duplicate side effects and version-consistency exceptions | Baseline, population, period, owner and attribution need discovery; no target or benefit achieved. |
| OSP-HR12-EV01 | Evidence for EXP01 and T01–T03 | Empty until learners record observations and revisions. |

## 10. AI-driven exploration: three scenarios

Scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps.

| Scenario window | Explore | Retained boundary |
|---|---|---|
| 2026–2030 — Assist | Explain failed handoffs using logs | Check sources, scope and uncertainty before using a suggestion. |
| 2031–2040 — Connect | Connect target acknowledgments and business reconciliation | Verify purpose, consent/access, version and each accountable owner. |
| 2041–2050 — Adapt | Adapt recovery suggestions under contract and replay authority | Keep consequential authority human, with stop, appeal and recovery controls. |

Competing future: a smaller, rules-based service with trained people and fewer connections could outperform an adaptive AI service on reliability, privacy, cost and trust.

Disconfirming question: Would event delivery improve without reducing business errors if targets use incompatible definitions? State what observation would make you abandon or narrow your hypothesis. Select one reversible experiment rather than promising a 2050 deployment.

## 11. Reflection and the six-level story arc

Which reveal changed your choice? Which record could still be wrong? Who can challenge your decision, and how would they do so without a personal device?

Pre-Foundation handoff: define source-of-record boundaries, canonical contracts, state semantics and recovery ownership. Carry the same card forward.

| Level | How this episode progresses | Evidence boundary |
|---|---|---|
| Origin Story | Discover the dilemma and produce this single card in 120 minutes. | Authored exercise; learner observations remain empty. |
| Pre-Foundation | Clarify vocabulary, people, process and source gaps. | Handoff, not a completed course. |
| Foundation | Model capability, value stream, data and authority. | Planned continuation. |
| Essentials | Implement one bounded workflow with traceable acceptance criteria. | Planned continuation. |
| Advanced | Investigate exceptions, integration, security and adoption trade-offs. | Planned continuation. |
| Ultimate | Conclude with measured value, cost/ROI assumptions, troubleshooting and lessons; defend scale/redesign/stop. | Requires actual evidence or explicitly synthetic calculations; no achieved ROI here. |

## 12. Resources and source record

Use a few official resources with a question. Extensive vendor comparisons are optional, outside the sprint.

R1 — NIST AI Risk Management Framework: what evidence, owner and monitoring would bound this assistant? https://www.nist.gov/itl/ai-risk-management-framework

R2 — W3C WCAG overview: can employees perceive, operate and understand the journey? https://www.w3.org/WAI/standards-guidelines/wcag/

R3 — SAP SuccessFactors product documentation, an optional application example: find the relevant module and verify object/permission behavior rather than assuming it. https://help.sap.com/docs/SAP_SUCCESSFACTORS_HCM_SUITE

S01 — Existing HR12 source case: https://app.notion.com/p/3cdce6de608981f88298f23cc51a91e4

S02 — Enterprise hub: https://app.notion.com/p/979c5b1e1e7d4664a1c64f2874007908

S03 — Workforce blueprint: https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/derived-streams/01-workforce.md (blob 2f5d352fb96985df6cb262d245624264c82a7c94).

S04 — Fictional personas: https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/personas/persona-cards.md (blob c7f1c2c9aefc5cffd1e1a86ab70ff951097a7108).

S05 — Source crosswalk and earlier gaps: https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/references/source-and-assumptions.md (blob 989adb98bbe79620882ddbbb4065701df42f7d89). The new child-source conflicts above supplement rather than silently overwrite this register.

S06 — GICS02 pattern: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md

Reviewed 1 November 2026 IST. Preserve original source assertions, personas, stable IDs, regional variations and research. Incorrect cross-theme labels in older source related-links do not redefine the current HR01–HR12 taxonomy.

Educational alignment: TOGAF for options/decisions; BIZBOK for capabilities/value streams; BABOK for needs/requirements/acceptance; DAMA-DMBOK for ownership/quality/lineage; COBIT for accountability/control; relevant ISO/IEC principles for least privilege, controlled change, evidence and accessibility. No certification, compliance or conformance is claimed.

Classification axes stay separate: HR theme = HR12 Connected HR Enterprises; enterprise transformation stream = Workforce; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry. Apply distinct views and responsibility boundaries; these are not twelve copies of the HR themes.

## Companion workspace

GitHub: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR12-AIG2-Architecting-Connected-HR-Enterprises/11-HR12-RE-real-estate/0-The-Origin-Story/sprint/real-estate-connected-hr-evolution-sprint.md

Google Doc: https://docs.google.com/document/d/19Ec1MkNBHwY_6H0SoTmH98vBExYQzWAHuZKZCOteuhc/edit?usp=drivesdk

Google Slides: https://docs.google.com/presentation/d/1n9gTs1EgfxFvaM4RzZ1RcjB7-eYH5GlMVV89uh3gk-0/edit?usp=drivesdk

Google Sheets build card: https://docs.google.com/spreadsheets/d/1g54YF8MWWkDhqRQecq-oF9WnVQxezn1sqiJHQEkqcZs/edit?usp=drivesdk

Notion: https://app.notion.com/p/3cdce6de608981f88298f23cc51a91e4

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/real-estate-origin-stories.md

Matching editions use deliberate publication and saved-content readback. Automatic synchronization, public student access, successful learner copying, executed tests and operational outcomes remain unverified.
