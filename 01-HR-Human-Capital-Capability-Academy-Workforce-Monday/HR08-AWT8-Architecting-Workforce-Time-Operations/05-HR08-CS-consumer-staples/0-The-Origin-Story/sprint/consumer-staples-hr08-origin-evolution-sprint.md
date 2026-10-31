# HR08 — Workforce Time & Operations: The Origin Story

SuccessLabs Academy · GICS05 Consumer Staples · OmniDaily Consumer Goods Ltd. · IIL — Industry Immersion Lab · Level 0 → Pre-Foundation · Sprint · 120 minutes · Edition 2026-10-31

Mission: Architecting Experiences for a Better World.

## 1. One learner promise

Design one shift-time correction that preserves actual events, approval and the payroll handoff without inventing missing hours.

Leave with one Shift-Time Decision Card. Use synthetic records and a paper prototype. A beginner explains the decision; an experienced learner challenges its assumptions. Deeper research and implementation stay in the preserved supporting cases, outside this Origin Story.

## 2. Enterprise context and source boundaries

OmniDaily is a fictional consumer-staples enterprise with 84,000 employees across 57 countries, 78 factories/co-packing facilities, 112 distribution centers and 1,900 distributors. These are source stipulations, not observed operating results. Its food, beverage, home-care and personal-care operations connect workforce readiness to everyday essentials. Factory, engineering/maintenance, distribution and field conditions are used only where supported by the enterprise or HR sources. No OmniWorks facility counts, industrial incidents or external seasonal-worker counts are imported.

Source scope: HR08 covers plant, distribution and field time, schedules/calendars, overtime, valuations, exceptions, approvals and payroll-ready integration; its source exercise uses a three-shift factory.

Routing record: the request repeatedly names GICS05 but also contains GICS04/Consumer Discretionary and Industrials wording. This edition follows the existing GICS05 Consumer Staples sources; conflicting request labels remain recorded here, not treated as enterprise facts. The supplied Materials URL is GICS02; the actual GICS03 index supplies a learning-pattern reference only.

Existing anchors retained: ODG-M03 (enterprise assets/stakeholders), ODG-M11 (operating model), ODG-M18 (workforce/adoption) and ODG-M19 (delivery readiness), inherited from the Workforce blueprint. ODG-TOS-HR08 identifiers below are newly introduced educational requirements, decisions, experiments, tests and measures; they are not existing approved client records. No detailed HR requirement/ADR/test register was found in the reviewed source pages; this gap is explicit.

## 3. Origins and process evolution

These closed windows are educational groupings, not universal invention dates or OmniDaily corporate biography. Adoption overlaps; older practices can coexist through the present. Reconstruct each as need → response → unresolved problem.

1970–1984 — Attendance sheets support wage inputs; missing or disputed entries depend on recollection.

1985–1994 — Clocks and roster rules structure shift records; cross-midnight interpretation remains difficult.

1995–2004 — Electronic time/ERP systems calculate totals; a raw event is not an approved payable duration.

2005–2014 — Self-service approvals connect employees and supervisors; late corrections still need payroll controls.

2015–2025 — Cloud/mobile time broadens access; offline events, policy versions and fair exceptions remain unresolved by automation alone.

## 4. One persona-led story: The shift ended, the clock did not

Scene 1: Elena Petrović, Plant Operations Director (ODG-P09), reviews a synthetic overnight factory shift with Nandita Sen, Group CHRO (ODG-P06). The start event exists; the end event is missing.

Scene 2: Choose scheduled hours, zero hours or an evidence-led exception. Reveal: the roster says what was planned, not what the worker actually performed.

Scene 3: A replacement suggestion ignores whether the substitute is ready for the task. Separately, a corrected event arrives after payroll input submission.

Scene 4: Elena requests worker/supervisor evidence and preserves the raw event. Nandita separates time approval, staffing readiness and the downstream correction so one resolution cannot silently imply all three.

Decision pause: Would automatic schedule substitution or an exception with a human route be fairer here? What reliable evidence could permit bounded automation? Record a first answer before the reveal, then revise the same card. Name a counterexample that would favor the alternative.

## 5. Responsibilities and human decision rights

Time services own captured events, valuation and approved time results; schedule owners own planned rosters. Supervisors approve corrections under authorized policy; workers can contest records. Payroll owns accepted time inputs and corrections; operations/quality owns replacement readiness and task authorization. SAP Time Tracking is illustrative; a time approval does not release a production task.

These are proposed educational responsibilities. Establish the business rule, source of truth and accountable human before choosing technology. SAP examples illustrate a capability and are not verified deployments, licensing claims or product roadmaps. A worker must have an accessible human route to question incorrect data or a decision. HR status, learning completion, work authorization and quality/batch release are distinct decisions.

## 6. Exactly 120 minutes

0–10: Read the promise; frame the workforce and business problem in two sentences.

10–30: Reconstruct the five historical windows and one persistent failure.

30–50: Play the story; reveal evidence in order and revise the initial choice.

50–65: Map application responsibilities, data owners and human authority.

65–95: Complete the single build card; compare alternatives and the future scenarios. Open only a resource that resolves a question.

95–115: Run the three paper tabletop tests; record observations and revise the same card.

115–120: Explain the decision in 60 seconds, reflect and carry the card into Pre-Foundation. Total: 120 minutes.

## 7. One build card: Shift-Time Decision Card

Synthetic experiment: SYN-SHIFT808 spans 22:00 to 06:00 local time across two dates. SYN-W808 has a missing end event; time-zone and approved policy are discovery fields, not assumed payroll rules.

Fill nine fields on one page: (1) purpose/person affected; (2) current/proposed state and evidence; (3) identifiers and definitions; (4) business time/version; (5) application/data owners; (6) human approval/appeal; (7) chosen option versus alternative and trade-off; (8) exception, fallback and automation boundary; (9) three observed test responses and revision.

Design constraint: Preserve event time/zone, source, arrival time and version. Planned attendance, actual attendance, payable time and task readiness must remain distinct; no automatic punitive zeroing.

All SYN identifiers, episode details and injected evidence are new teaching data. Country rules, collective agreements, qualifications, worker/device populations and local approvals remain unknown unless explicitly sourced. Record each unknown with an owner and discovery question. Do not invent legal rules or calculate unsupported operational benefits.

## 8. Exactly three tabletop tests

### ODG-TOS-HR08-T01 — Missing cross-midnight event

Reveal/input: Only the start event is present for SYN-SHIFT808.

Expected design response: Open a correction with evidence/owner; do not fabricate the end or use date-only arithmetic.

### ODG-TOS-HR08-T02 — Replacement readiness

Reveal/input: A roster algorithm picks someone with no current task evidence.

Expected design response: Keep coverage unresolved until authorized readiness review; do not infer competence from availability.

### ODG-TOS-HR08-T03 — Late correction

Reveal/input: Corrected time arrives after payroll accepted the previous version.

Expected design response: Version and approve the correction, reconcile the payroll handoff and preserve prior-state traceability.

For each test record input → expected response → actual paper response → evidence note → pass/revise. These are proposed acceptance criteria. The evidence slot starts unfilled: publication runs none of the tests and proves no operational result. If a protected human decision can be bypassed, revise the design even if every card field is filled.

## 9. Traceability and measures

ODG-TOS-HR08-REQ01 — Trace one cross-midnight shift from raw events to approved time evidence. Derived from the supporting HR source mandate and ODG-M18; assessed by T01.

ODG-TOS-HR08-REQ02 — Keep staffing authorization and versioned payroll correction separate. Derived from the source governance mandate and ODG-M19; assessed by T02–T03.

ODG-TOS-HR08-ADR01 — Prefer an evidence-led exception over silent schedule substitution for missing events; compare administrative effort and worker harm. This proposed educational decision can be rejected with evidence; record the alternative and consequence.

ODG-TOS-HR08-EXP01 — The one synthetic build card extends ODG-M19's delivery-readiness discipline; T01–T03 do not execute the larger implementation case.

ODG-TOS-HR08-M01 — Mandatory card fields completed / 9 × 100: learning completeness only. ODG-TOS-HR08-M02 — Record whether T02/T03 preserve readiness and accepted-input version boundaries. Record actual paper observations rather than assuming success.

ODG-TOS-HR08-EV01 — Unfilled evidence slot for test observations, revisions and reviewer questions. Existing case success measures are intended outcomes; no baseline or target attainment follows from publishing this edition.

## 10. AI-driven exploration: scenarios, not predictions

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. Each needs evidence, approved purpose, accountable ownership and proportionate controls.

2026–2030 — Assist: Assistance could explain missing-event exceptions for human review.

2031–2040 — Connect: Schedule, time and payroll services could exchange versioned acknowledgements.

2041–2050 — Adapt: Roster suggestions could adapt within approved fatigue/readiness constraints without deciding worker disputes.

Competing future: Simple reliable clocks and empowered local exception handling may outperform extensive mobile automation where connectivity is weak.

Disconfirmation question: Would the connected design increase unresolved pay disputes or hidden corrections compared with a simpler approved process? Name evidence that would stop or change the hypothesis.

## 11. Reflection and Pre-Foundation handoff

What does a roster fail to prove? Which timestamp changed the result? How can the worker correct a record?

Pre-Foundation: Define event, schedule, time type, valuation, approval and payroll input; map dates/zones and one correction before configuring policies. Carry this same card, source questions and acceptance criteria forward. Deeper configuration, vendor comparisons and implementation research remain outside the Origin Story.

## 12. Official resources and architectural lenses

NIST AI RMF: What risk needs oversight? https://www.nist.gov/itl/ai-risk-management-framework

ISO/IEC 27001: Who owns information risk? https://www.iso.org/standard/27001

W3C WCAG 2.2: Who could struggle to use this journey? https://www.w3.org/TR/WCAG22/

Educational alignment only: TOGAF—business-led options and architectural decisions; BIZBOK—capabilities and value streams; BABOK—elicitation, requirements and acceptance; DAMA-DMBOK—data ownership, quality and lineage; COBIT—accountability and control evidence; relevant ISO/IEC information-risk principles. No certification, conformity or compliance is claimed.

Separate classification axes: HR theme = HR08 Workforce Time & Operations; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry; enterprise transformation stream = Workforce. Related views do not become interchangeable lists.

## Source and companion record

Supporting HR source: https://app.notion.com/p/3d0ce6de608981719dd9d9a3c5bdaf58

Enterprise hub: https://app.notion.com/p/28a329356ea6481dafbcc579c2463add

Workforce blueprint and existing anchors: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/derived-streams/01-workforce.md

Fictional personas and stable designations: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md

Source gaps ODG-Q01–ODG-Q17: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/references/source-and-assumptions.md

Open enterprise issues remain unresolved: brands/SKUs counting basis; benefit overlap and cash bridge; inconsistent target scopes/horizons; vendor fit and approval evidence. These do not become achieved HR outcomes. Original research is preserved in the hub and source cases.

Learning-pattern reference GICS03: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/industrials-origin-stories.md

Supplied reference GICS02: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR08-AWT8-Architecting-Workforce-Time-Operations/05-HR08-CS-consumer-staples/0-The-Origin-Story/sprint/consumer-staples-hr08-origin-evolution-sprint.md

Native Google Doc: https://docs.google.com/document/d/1hpJQ_hNrAt9c5PmApYdWi8dlot1SRmlX_Lf_VrA5Tz0/edit?usp=drivesdk

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/consumer-staples-origin-stories.md

Saved-content verification is recorded in the sector index. No automatic synchronization, public student access, successful copying, executed tabletop tests or operational outcomes is asserted. End of HR08 Origin Story edition.
