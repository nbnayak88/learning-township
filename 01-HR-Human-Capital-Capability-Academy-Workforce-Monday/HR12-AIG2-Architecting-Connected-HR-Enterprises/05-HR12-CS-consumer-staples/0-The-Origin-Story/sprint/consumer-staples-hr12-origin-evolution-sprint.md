# HR12 — Connected HR Enterprises: The Origin Story

SuccessLabs Academy · GICS05 Consumer Staples · OmniDaily Consumer Goods Ltd. · IIL — Industry Immersion Lab · Level 0 → Pre-Foundation · Sprint · 120 minutes · Edition 2026-10-31

Mission: Architecting Experiences for a Better World.

## 1. One learner promise

Design one workforce handoff that proves each receiving outcome and can recover safely from duplicate, late or rejected events.

Leave with one Connected Workforce Handoff Decision Card. Use synthetic records and a paper prototype. A beginner explains the decision; an experienced learner challenges its assumptions. Deeper research and implementation stay in the preserved supporting cases, outside this Origin Story.

## 2. Enterprise context and source boundaries

OmniDaily is a fictional consumer-staples enterprise with 84,000 employees across 57 countries, 78 factories/co-packing facilities, 112 distribution centers and 1,900 distributors. These are source stipulations, not observed operating results. Its food, beverage, home-care and personal-care operations connect workforce readiness to everyday essentials. Factory, engineering/maintenance, distribution and field conditions are used only where supported by the enterprise or HR sources. No OmniWorks facility counts, industrial incidents or external seasonal-worker counts are imported.

Source scope: HR12 connects HR with payroll, finance, identity, manufacturing, workforce management, learning and analytics through governed APIs/events, mappings, monitoring and recovery.

Routing record: the request repeatedly names GICS05 but also contains GICS04/Consumer Discretionary and Industrials wording. This edition follows the existing GICS05 Consumer Staples sources; conflicting request labels remain recorded here, not treated as enterprise facts. The supplied Materials URL is GICS02; the actual GICS03 index supplies a learning-pattern reference only.

Existing anchors retained: ODG-M03 (enterprise assets/stakeholders), ODG-M11 (operating model), ODG-M18 (workforce/adoption) and ODG-M19 (delivery readiness), inherited from the Workforce blueprint. ODG-TOS-HR12 identifiers below are newly introduced educational requirements, decisions, experiments, tests and measures; they are not existing approved client records. No detailed HR requirement/ADR/test register was found in the reviewed source pages; this gap is explicit.

## 3. Origins and process evolution

These closed windows are educational groupings, not universal invention dates or OmniDaily corporate biography. Adoption overlaps; older practices can coexist through the present. Reconstruct each as need → response → unresolved problem.

1970–1984 — Paper notices move workforce changes between offices; receipt and completion are hard to distinguish.

1985–1994 — Batch files reduce rekeying; late or missing files leave teams with different states.

1995–2004 — Point-to-point ERP interfaces automate handoffs; coupling and inconsistent identifiers complicate change.

2005–2014 — Service-oriented/API patterns improve reuse; accepted messages still may fail downstream.

2015–2025 — Cloud APIs/events and integration monitoring broaden connectivity; ordering, idempotency, ownership and recovery remain architectural decisions.

## 4. One persona-led story: The message arrived, the worker did not move

Scene 1: Priya Nair, Director Enterprise Architecture (ODG-P13), follows a synthetic factory-to-distribution assignment change with Nandita Sen, Group CHRO (ODG-P06). The integration console says delivered.

Scene 2: Choose fire-and-forget publication or per-consumer business acknowledgement. Reveal: core HR saved the change, but a receiving system rejected its location mapping.

Scene 3: A duplicate and an older event arrive after the corrected event. Omar Haddad, CISO and Privacy Lead (ODG-P12), asks whether a recovery could accidentally restore old access.

Scene 4: Priya revises the contract: stable worker/employment correlation, event/version meaning, consumer outcome and controlled replay. HR, payroll and security retain their own decisions; a delivered event proves none of them complete.

Decision pause: Would a governed event contract or a simpler scheduled reconciliation fit this handoff? What volume, latency or recovery evidence would change the choice? Record a first answer before the reveal, then revise the same card. Name a counterexample that would favor the alternative.

## 5. Responsibilities and human decision rights

Core HR owns workforce facts and approved business changes; each receiving payroll/finance/learning/operations service owns its accepted state. Integration owners own mapping, delivery, correlation, retry and monitoring, not business authorization. IAM/site security owns access decisions and enforcement; HR owns employment approval. Priya governs contracts/exceptions; authorized owners approve recovery. SAP Integration Suite/BTP are examples, not selected or deployed components.

These are proposed educational responsibilities. Establish the business rule, source of truth and accountable human before choosing technology. SAP examples illustrate a capability and are not verified deployments, licensing claims or product roadmaps. A worker must have an accessible human route to question incorrect data or a decision. HR status, learning completion, work authorization and quality/batch release are distinct decisions.

## 6. Exactly 120 minutes

0–10: Read the promise; frame the workforce and business problem in two sentences.

10–30: Reconstruct the five historical windows and one persistent failure.

30–50: Play the story; reveal evidence in order and revise the initial choice.

50–65: Map application responsibilities, data owners and human authority.

65–95: Complete the single build card; compare alternatives and the future scenarios. Open only a resource that resolves a question.

95–115: Run the three paper tabletop tests; record observations and revise the same card.

115–120: Explain the decision in 60 seconds, reflect and carry the card into Pre-Foundation. Total: 120 minutes.

## 7. One build card: Connected Workforce Handoff Decision Card

Synthetic experiment: Use SYN-E1212, SYN-CHANGE1212 and event versions 1/2 for one factory-to-DC transfer. Model payroll, identity and learning as consumers with separate accepted/rejected/unknown outcomes; no live connection is built.

Fill nine fields on one page: (1) purpose/person affected; (2) current/proposed state and evidence; (3) identifiers and definitions; (4) business time/version; (5) application/data owners; (6) human approval/appeal; (7) chosen option versus alternative and trade-off; (8) exception, fallback and automation boundary; (9) three observed test responses and revision.

Design constraint: Define business effective time separately from event creation/arrival and per-consumer completion. Do not treat assignment end as employment termination. Replay must preserve authorization, schema validity and deduplication.

All SYN identifiers, episode details and injected evidence are new teaching data. Country rules, collective agreements, qualifications, worker/device populations and local approvals remain unknown unless explicitly sourced. Record each unknown with an owner and discovery question. Do not invent legal rules or calculate unsupported operational benefits.

## 8. Exactly three tabletop tests

### ODG-TOS-HR12-T01 — Rejected target

Reveal/input: Delivery succeeds but the receiving location mapping is rejected.

Expected design response: Keep business completion pending, expose consumer reason/owner and correct via approved mapping; do not report full success.

### ODG-TOS-HR12-T02 — Duplicate and late event

Reveal/input: Version 1 arrives twice after version 2.

Expected design response: Deduplicate and apply a documented ordering/version policy; do not restore stale employment or access state.

### ODG-TOS-HR12-T03 — Ambiguous replay

Reveal/input: An operator proposes replay with an incompatible schema and uncertain prior outcome.

Expected design response: Quarantine, reconcile prior outcome and obtain authorized recovery; prevent uncontrolled duplicate side effects.

For each test record input → expected response → actual paper response → evidence note → pass/revise. These are proposed acceptance criteria. The evidence slot starts unfilled: publication runs none of the tests and proves no operational result. If a protected human decision can be bypassed, revise the design even if every card field is filled.

## 9. Traceability and measures

ODG-TOS-HR12-REQ01 — Trace one approved workforce change to explicit per-consumer business outcomes. Derived from the supporting HR source mandate and ODG-M18; assessed by T01.

ODG-TOS-HR12-REQ02 — Preserve identity, version semantics and authorized duplicate/late/replay handling. Derived from the source governance mandate and ODG-M19; assessed by T02–T03.

ODG-TOS-HR12-ADR01 — Prefer governed handoff contracts and reconciliation over fire-and-forget delivery; compare complexity with a simpler scheduled reconciliation option. This proposed educational decision can be rejected with evidence; record the alternative and consequence.

ODG-TOS-HR12-EXP01 — The one synthetic build card extends ODG-M19's delivery-readiness discipline; T01–T03 do not execute the larger implementation case.

ODG-TOS-HR12-M01 — Mandatory card fields completed / 9 × 100: learning completeness only. ODG-TOS-HR12-M02 — Record whether T02/T03 prevent stale/duplicate effects and expose uncertain recovery. Record actual paper observations rather than assuming success.

ODG-TOS-HR12-EV01 — Unfilled evidence slot for test observations, revisions and reviewer questions. Existing case success measures are intended outcomes; no baseline or target attainment follows from publishing this edition.

## 10. AI-driven exploration: scenarios, not predictions

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. Each needs evidence, approved purpose, accountable ownership and proportionate controls.

2026–2030 — Assist: Assistance could explain mapping failures while owners approve corrections.

2031–2040 — Connect: Services could exchange versioned business acknowledgements and recovery evidence.

2041–2050 — Adapt: Routing could adapt within approved contracts with rollback and human control over consequential changes.

Competing future: Scheduled file exchange with rigorous reconciliation may outperform event-heavy integration where latency needs are modest and support capacity is limited.

Disconfirmation question: Would event-based orchestration increase unresolved states, support effort or stale access compared with governed batch reconciliation? Name evidence that would stop or change the hypothesis.

## 11. Reflection and Pre-Foundation handoff

What did delivered actually prove? Which owner can accept the change? What evidence makes replay safe?

Pre-Foundation: Define producer, consumer, contract, correlation, business date/version, acknowledgement and recovery; map one handoff before choosing integration technology. Carry this same card, source questions and acceptance criteria forward. Deeper configuration, vendor comparisons and implementation research remain outside the Origin Story.

## 12. Official resources and architectural lenses

NIST AI RMF: What risk needs oversight? https://www.nist.gov/itl/ai-risk-management-framework

ISO/IEC 27001: Who owns information risk? https://www.iso.org/standard/27001

W3C WCAG 2.2: Who could struggle to use this journey? https://www.w3.org/TR/WCAG22/

Educational alignment only: TOGAF—business-led options and architectural decisions; BIZBOK—capabilities and value streams; BABOK—elicitation, requirements and acceptance; DAMA-DMBOK—data ownership, quality and lineage; COBIT—accountability and control evidence; relevant ISO/IEC information-risk principles. No certification, conformity or compliance is claimed.

Separate classification axes: HR theme = HR12 Connected HR Enterprises; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry; enterprise transformation stream = Workforce. Related views do not become interchangeable lists.

## Source and companion record

Supporting HR source: https://app.notion.com/p/3d0ce6de608981dea3c0d53724530c8c

Enterprise hub: https://app.notion.com/p/28a329356ea6481dafbcc579c2463add

Workforce blueprint and existing anchors: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/derived-streams/01-workforce.md

Fictional personas and stable designations: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md

Source gaps ODG-Q01–ODG-Q17: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/references/source-and-assumptions.md

Open enterprise issues remain unresolved: brands/SKUs counting basis; benefit overlap and cash bridge; inconsistent target scopes/horizons; vendor fit and approval evidence. These do not become achieved HR outcomes. Original research is preserved in the hub and source cases.

Learning-pattern reference GICS03: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/industrials-origin-stories.md

Supplied reference GICS02: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR12-AIG2-Architecting-Connected-HR-Enterprises/05-HR12-CS-consumer-staples/0-The-Origin-Story/sprint/consumer-staples-hr12-origin-evolution-sprint.md

Native Google Doc: https://docs.google.com/document/d/176QJLgXjSxyglZxYUVzkBnrZRIDoFcLxnatlDZYVOjM/edit?usp=drivesdk

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/consumer-staples-origin-stories.md

Saved-content verification is recorded in the sector index. No automatic synchronization, public student access, successful copying, executed tabletop tests or operational outcomes is asserted. End of HR12 Origin Story edition.
