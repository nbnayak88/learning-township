# HR01 — Workforce Foundations: The Origin Story

SuccessLabs Academy · GICS05 Consumer Staples · OmniDaily Consumer Goods Ltd. · IIL — Industry Immersion Lab · Level 0 → Pre-Foundation · Sprint · 120 minutes · Edition 2026-10-31

Mission: Architecting Experiences for a Better World.

## 1. One learner promise

Design one factory-to-distribution transfer that preserves employment history and exposes unfinished pay and access handoffs.

Leave with one Workforce Foundation Decision Card. Use synthetic records and a paper prototype. A beginner explains the decision; an experienced learner challenges its assumptions. Deeper research and implementation stay in the preserved supporting cases, outside this Origin Story.

## 2. Enterprise context and source boundaries

OmniDaily is a fictional consumer-staples enterprise with 84,000 employees across 57 countries, 78 factories/co-packing facilities, 112 distribution centers and 1,900 distributors. These are source stipulations, not observed operating results. Its food, beverage, home-care and personal-care operations connect workforce readiness to everyday essentials. Factory, engineering/maintenance, distribution and field conditions are used only where supported by the enterprise or HR sources. No OmniWorks facility counts, industrial incidents or external seasonal-worker counts are imported.

Source scope: HR01 covers person, employment, job, position, organization, local variation, workflow and access in an integration-ready HR foundation.

Routing record: the request repeatedly names GICS05 but also contains GICS04/Consumer Discretionary and Industrials wording. This edition follows the existing GICS05 Consumer Staples sources; conflicting request labels remain recorded here, not treated as enterprise facts. The supplied Materials URL is GICS02; the actual GICS03 index supplies a learning-pattern reference only.

Existing anchors retained: ODG-M03 (enterprise assets/stakeholders), ODG-M11 (operating model), ODG-M18 (workforce/adoption) and ODG-M19 (delivery readiness), inherited from the Workforce blueprint. ODG-TOS-HR01 identifiers below are newly introduced educational requirements, decisions, experiments, tests and measures; they are not existing approved client records. No detailed HR requirement/ADR/test register was found in the reviewed source pages; this gap is explicit.

## 3. Origins and process evolution

These closed windows are educational groupings, not universal invention dates or OmniDaily corporate biography. Adoption overlaps; older practices can coexist through the present. Reconstruct each as need → response → unresolved problem.

1970–1984 — Personnel ledgers answer who works where; matching names can hide different people.

1985–1994 — Site registers organize jobs and positions; definitions diverge across plants and distribution centers.

1995–2004 — HRIS/ERP connects employment and pay; a wrong identity still travels faster.

2005–2014 — Self-service coordinates transfers; saving a form does not confirm receiving systems.

2015–2025 — Cloud cores support shared definitions and local extensions; historical correctness and authority remain human responsibilities.

## 4. One persona-led story: The transfer that looked complete

Scene 1: Nandita Sen, Group CHRO (ODG-P06), reviews a fictional factory worker's proposed distribution-center move. Elena Petrović, Plant Operations Director (ODG-P09), wants continuity without erasing the sending assignment.

Scene 2: Choose a new person record, overwrite today's job or retain one person with a dated change. Reveal: payroll needs the worker's old assignment for the period before the transfer.

Scene 3: A second reveal shows the receiving access service has not acknowledged the change. Active employment alone says nothing about whether a local restricted task is authorized.

Scene 4: Nandita revises the decision: preserve history, track each receiving outcome and send unresolved readiness to the receiving authority. She keeps legitimate local fields subject to justification.

Decision pause: Would you choose a shared semantic core with governed local extensions or independent local copies? What evidence would make federation preferable? Record a first answer before the reveal, then revise the same card. Name a counterexample that would favor the alternative.

## 5. Responsibilities and human decision rights

Core HR and its HR owner steward person/employment/job facts; SAP Employee Central is an example. Payroll owns approved pay inputs and results. IAM/site security owns access enforcement; operations owns task authorization. Learning owns assessment evidence; MES/EAM owns production/maintenance context. Nandita proposes governance; authorized HR approvers accept the transfer and site authorities decide work readiness.

These are proposed educational responsibilities. Establish the business rule, source of truth and accountable human before choosing technology. SAP examples illustrate a capability and are not verified deployments, licensing claims or product roadmaps. A worker must have an accessible human route to question incorrect data or a decision. HR status, learning completion, work authorization and quality/batch release are distinct decisions.

## 6. Exactly 120 minutes

0–10: Read the promise; frame the workforce and business problem in two sentences.

10–30: Reconstruct the five historical windows and one persistent failure.

30–50: Play the story; reveal evidence in order and revise the initial choice.

50–65: Map application responsibilities, data owners and human authority.

65–95: Complete the single build card; compare alternatives and the future scenarios. Open only a resource that resolves a question.

95–115: Run the three paper tabletop tests; record observations and revise the same card.

115–120: Explain the decision in 60 seconds, reflect and carry the card into Pre-Foundation. Total: 120 minutes.

## 7. One build card: Workforce Foundation Decision Card

Synthetic experiment: SYN-P101 has employment SYN-E101 and a proposed assignment from SYN-FACTORY to SYN-DC effective 1 November 2026. Payroll acknowledgement and receiving qualification are initially unknown.

Fill nine fields on one page: (1) purpose/person affected; (2) current/proposed state and evidence; (3) identifiers and definitions; (4) business time/version; (5) application/data owners; (6) human approval/appeal; (7) chosen option versus alternative and trade-off; (8) exception, fallback and automation boundary; (9) three observed test responses and revision.

Design constraint: Distinguish person, employment, assignment and position. Preserve business validity and entry time; determine which object actually changes before selecting a transaction. Not every entity is technically effective-dated.

All SYN identifiers, episode details and injected evidence are new teaching data. Country rules, collective agreements, qualifications, worker/device populations and local approvals remain unknown unless explicitly sourced. Record each unknown with an owner and discovery question. Do not invent legal rules or calculate unsupported operational benefits.

## 8. Exactly three tabletop tests

### ODG-TOS-HR01-T01 — As-of history

Reveal/input: Compare 31 October and 1 November for SYN-E101.

Expected design response: Show the respective assignment without creating a duplicate person; hold ambiguous employment treatment for HR.

### ODG-TOS-HR01-T02 — Readiness boundary

Reveal/input: A suggestion equates active employment with restricted-task permission.

Expected design response: Hold the task pending receiving authority evidence; do not infer competence or cancel employment.

### ODG-TOS-HR01-T03 — Receiving failure

Reveal/input: Core HR saved but payroll/access completion is unconfirmed.

Expected design response: Expose separate pending outcomes, owners and recovery conditions; do not label the whole transfer complete.

For each test record input → expected response → actual paper response → evidence note → pass/revise. These are proposed acceptance criteria. The evidence slot starts unfilled: publication runs none of the tests and proves no operational result. If a protected human decision can be bypassed, revise the design even if every card field is filled.

## 9. Traceability and measures

ODG-TOS-HR01-REQ01 — Preserve stable person identity and business-valid assignment history. Derived from the supporting HR source mandate and ODG-M18; assessed by T01.

ODG-TOS-HR01-REQ02 — Separate HR approval, work authorization and downstream completion. Derived from the source governance mandate and ODG-M19; assessed by T02–T03.

ODG-TOS-HR01-ADR01 — Prefer a shared semantic core with justified local extensions; compare local copies and their reconciliation cost. This proposed educational decision can be rejected with evidence; record the alternative and consequence.

ODG-TOS-HR01-EXP01 — The one synthetic build card extends ODG-M19's delivery-readiness discipline; T01–T03 do not execute the larger implementation case.

ODG-TOS-HR01-M01 — Mandatory card fields completed / 9 × 100: learning completeness only. ODG-TOS-HR01-M02 — Record whether T02/T03 kept readiness and incomplete handoffs visible. Record actual paper observations rather than assuming success.

ODG-TOS-HR01-EV01 — Unfilled evidence slot for test observations, revisions and reviewer questions. Existing case success measures are intended outcomes; no baseline or target attainment follows from publishing this edition.

## 10. AI-driven exploration: scenarios, not predictions

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. Each needs evidence, approved purpose, accountable ownership and proportionate controls.

2026–2030 — Assist: An assistant could flag missing transfer fields while HR retains approval.

2031–2040 — Connect: Versioned assignment and readiness evidence could be exchanged with receiving owners.

2041–2050 — Adapt: Assignment suggestions could adapt to changing roles while preserving worker challenge and site authority.

Competing future: A controlled federated core with strong local stewardship may outperform centralization where definitions cannot yet be harmonized.

Disconfirmation question: Would the shared core create more unresolved identity errors or legitimate local-process failures than a federated pilot? Name evidence that would stop or change the hypothesis.

## 11. Reflection and Pre-Foundation handoff

Which reveal changed your answer? What does an active record fail to prove? How can the worker challenge an incorrect assignment?

Pre-Foundation: Define person, employment, assignment, position, organization and location; map one legitimate local extension and its owner before configuration. Carry this same card, source questions and acceptance criteria forward. Deeper configuration, vendor comparisons and implementation research remain outside the Origin Story.

## 12. Official resources and architectural lenses

NIST AI RMF: What risk needs oversight? https://www.nist.gov/itl/ai-risk-management-framework

ISO/IEC 27001: Who owns information risk? https://www.iso.org/standard/27001

W3C WCAG 2.2: Who could struggle to use this journey? https://www.w3.org/TR/WCAG22/

Educational alignment only: TOGAF—business-led options and architectural decisions; BIZBOK—capabilities and value streams; BABOK—elicitation, requirements and acceptance; DAMA-DMBOK—data ownership, quality and lineage; COBIT—accountability and control evidence; relevant ISO/IEC information-risk principles. No certification, conformity or compliance is claimed.

Separate classification axes: HR theme = HR01 Workforce Foundations; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry; enterprise transformation stream = Workforce. Related views do not become interchangeable lists.

## Source and companion record

Supporting HR source: https://app.notion.com/p/3d0ce6de6089814789acdcd97750a638

Enterprise hub: https://app.notion.com/p/28a329356ea6481dafbcc579c2463add

Workforce blueprint and existing anchors: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/derived-streams/01-workforce.md

Fictional personas and stable designations: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md

Source gaps ODG-Q01–ODG-Q17: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/references/source-and-assumptions.md

Open enterprise issues remain unresolved: brands/SKUs counting basis; benefit overlap and cash bridge; inconsistent target scopes/horizons; vendor fit and approval evidence. These do not become achieved HR outcomes. Original research is preserved in the hub and source cases.

Learning-pattern reference GICS03: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/industrials-origin-stories.md

Supplied reference GICS02: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR01-AWF1-Architecting-Autonomous-Workforce-Foundations/05-HR01-CS-consumer-staples/0-The-Origin-Story/sprint/consumer-staples-hr01-origin-evolution-sprint.md

Native Google Doc: https://docs.google.com/document/d/1FOJ1YwOWX0IQH_Z1We0N9JY1S44cGDhexfsofjAK0gA/edit?usp=drivesdk

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/consumer-staples-origin-stories.md

Saved-content verification is recorded in the sector index. No automatic synchronization, public student access, successful copying, executed tabletop tests or operational outcomes is asserted. End of HR01 Origin Story edition.
