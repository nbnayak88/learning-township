# HR10 — Digital Employee Experience: The Origin Story

SuccessLabs Academy · GICS05 Consumer Staples · OmniDaily Consumer Goods Ltd. · IIL — Industry Immersion Lab · Level 0 → Pre-Foundation · Sprint · 120 minutes · Edition 2026-10-31

Mission: Architecting Experiences for a Better World.

## 1. One learner promise

Design one frontline HR help journey that makes submission, ownership and human resolution visible on a shared device.

Leave with one Employee Help Journey Decision Card. Use synthetic records and a paper prototype. A beginner explains the decision; an experienced learner challenges its assumptions. Deeper research and implementation stay in the preserved supporting cases, outside this Origin Story.

## 2. Enterprise context and source boundaries

OmniDaily is a fictional consumer-staples enterprise with 84,000 employees across 57 countries, 78 factories/co-packing facilities, 112 distribution centers and 1,900 distributors. These are source stipulations, not observed operating results. Its food, beverage, home-care and personal-care operations connect workforce readiness to everyday essentials. Factory, engineering/maintenance, distribution and field conditions are used only where supported by the enterprise or HR sources. No OmniWorks facility counts, industrial incidents or external seasonal-worker counts are imported.

Source scope: HR10 covers persona-based frontline/corporate experiences, HR entry points, content, tasks, notifications and integration; the source exercise focuses on a factory supervisor.

Routing record: the request repeatedly names GICS05 but also contains GICS04/Consumer Discretionary and Industrials wording. This edition follows the existing GICS05 Consumer Staples sources; conflicting request labels remain recorded here, not treated as enterprise facts. The supplied Materials URL is GICS02; the actual GICS03 index supplies a learning-pattern reference only.

Existing anchors retained: ODG-M03 (enterprise assets/stakeholders), ODG-M11 (operating model), ODG-M18 (workforce/adoption) and ODG-M19 (delivery readiness), inherited from the Workforce blueprint. ODG-TOS-HR10 identifiers below are newly introduced educational requirements, decisions, experiments, tests and measures; they are not existing approved client records. No detailed HR requirement/ADR/test register was found in the reviewed source pages; this gap is explicit.

## 3. Origins and process evolution

These closed windows are educational groupings, not universal invention dates or OmniDaily corporate biography. Adoption overlaps; older practices can coexist through the present. Reconstruct each as need → response → unresolved problem.

1970–1984 — Personnel counters and noticeboards offer local help; privacy and availability depend on place/time.

1985–1994 — Help desks and structured forms improve routing; workers repeat information between teams.

1995–2004 — Intranets/portals centralize information; finding a page does not resolve the underlying task.

2005–2014 — Self-service and mobile journeys reduce steps; shared devices and failed submissions expose new gaps.

2015–2025 — Personalized workplaces connect tasks; content freshness, accessibility, privacy and accountable resolution remain essential.

## 4. One persona-led story: The green tick on a shared kiosk

Scene 1: Nandita Sen, Group CHRO (ODG-P06), follows a synthetic factory supervisor seeking a time correction. Elena Petrović, Plant Operations Director (ODG-P09), asks why the worker still needs help after seeing a green tick.

Scene 2: Choose a large dashboard or one guided task with visible status. Reveal: the tick confirmed a local submission, but the receiving HR/time service has not acknowledged a case.

Scene 3: A shared-kiosk session exposes another worker's information. A suggested help article is stale; operational quality/safety concerns need their designated channel rather than a generic HR queue.

Scene 4: Nandita revises the journey to show receiving acknowledgement, owner and escalation. The worker can use a private human route, and task completion is determined by the responsible service rather than the portal's appearance.

Decision pause: Would one task-led route or a feature-rich landing page reduce effort? Which user evidence could justify more navigation? Record a first answer before the reveal, then revise the same card. Name a counterexample that would favor the alternative.

## 5. Responsibilities and human decision rights

Experience/portal owners steward navigation, content provenance and task presentation; HR/time/payroll services own their case and transaction states. Content owners approve guidance and freshness. IAM/security owns sessions and least privilege; HR service staff own confidential handoff. Operations/quality retains its own incident authority. SAP Work Zone is illustrative; the portal is not the system of record for every process.

These are proposed educational responsibilities. Establish the business rule, source of truth and accountable human before choosing technology. SAP examples illustrate a capability and are not verified deployments, licensing claims or product roadmaps. A worker must have an accessible human route to question incorrect data or a decision. HR status, learning completion, work authorization and quality/batch release are distinct decisions.

## 6. Exactly 120 minutes

0–10: Read the promise; frame the workforce and business problem in two sentences.

10–30: Reconstruct the five historical windows and one persistent failure.

30–50: Play the story; reveal evidence in order and revise the initial choice.

50–65: Map application responsibilities, data owners and human authority.

65–95: Complete the single build card; compare alternatives and the future scenarios. Open only a resource that resolves a question.

95–115: Run the three paper tabletop tests; record observations and revise the same card.

115–120: Explain the decision in 60 seconds, reflect and carry the card into Pre-Foundation. Total: 120 minutes.

## 7. One build card: Employee Help Journey Decision Card

Synthetic experiment: Prototype SYN-HELP1010 for one time-correction request on a shared kiosk. Include submitted, acknowledged, assigned and resolved as distinct synthetic states; use no real employee data.

Fill nine fields on one page: (1) purpose/person affected; (2) current/proposed state and evidence; (3) identifiers and definitions; (4) business time/version; (5) application/data owners; (6) human approval/appeal; (7) chosen option versus alternative and trade-off; (8) exception, fallback and automation boundary; (9) three observed test responses and revision.

Design constraint: Separate UI confirmation from receiving-service acknowledgement and resolution. Make status, ownership and human escalation understandable; private employee information must not remain visible to the next user.

All SYN identifiers, episode details and injected evidence are new teaching data. Country rules, collective agreements, qualifications, worker/device populations and local approvals remain unknown unless explicitly sourced. Record each unknown with an owner and discovery question. Do not invent legal rules or calculate unsupported operational benefits.

## 8. Exactly three tabletop tests

### ODG-TOS-HR10-T01 — Submission uncertainty

Reveal/input: The interface shows success but no receiving acknowledgement exists.

Expected design response: Show pending/unknown with a correlation and recovery owner; avoid duplicate requests or claiming resolution.

### ODG-TOS-HR10-T02 — Shared-device exposure

Reveal/input: The next kiosk user can see the previous request.

Expected design response: Require an appropriate session/privacy design and a private assisted route; do not treat a cosmetic hidden field as access control.

### ODG-TOS-HR10-T03 — Wrong/stale guidance

Reveal/input: An outdated article routes a quality concern to HR.

Expected design response: Expose provenance/freshness, route to the designated authority and preserve confidential human escalation.

For each test record input → expected response → actual paper response → evidence note → pass/revise. These are proposed acceptance criteria. The evidence slot starts unfilled: publication runs none of the tests and proves no operational result. If a protected human decision can be bypassed, revise the design even if every card field is filled.

## 9. Traceability and measures

ODG-TOS-HR10-REQ01 — Trace one employee task from understandable entry to accountable receiving status. Derived from the supporting HR source mandate and ODG-M18; assessed by T01.

ODG-TOS-HR10-REQ02 — Protect shared-device privacy and correct human escalation when guidance or routing fails. Derived from the source governance mandate and ODG-M19; assessed by T02–T03.

ODG-TOS-HR10-ADR01 — Prefer a task-led journey with visible ownership over a broad personalized dashboard; compare discoverability, effort and privacy exposure. This proposed educational decision can be rejected with evidence; record the alternative and consequence.

ODG-TOS-HR10-EXP01 — The one synthetic build card extends ODG-M19's delivery-readiness discipline; T01–T03 do not execute the larger implementation case.

ODG-TOS-HR10-M01 — Mandatory card fields completed / 9 × 100: learning completeness only. ODG-TOS-HR10-M02 — Record whether T02/T03 retain privacy and the correct accountable escalation. Record actual paper observations rather than assuming success.

ODG-TOS-HR10-EV01 — Unfilled evidence slot for test observations, revisions and reviewer questions. Existing case success measures are intended outcomes; no baseline or target attainment follows from publishing this edition.

## 10. AI-driven exploration: scenarios, not predictions

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. Each needs evidence, approved purpose, accountable ownership and proportionate controls.

2026–2030 — Assist: Assistance could find scoped guidance and explain status with sources.

2031–2040 — Connect: Workplace and case services could share per-task acknowledgements without merging ownership.

2041–2050 — Adapt: Journeys could adapt to needs with worker control, accessible alternatives and private human support.

Competing future: A dependable small portal plus trusted local service staff may serve frontline workers better than a highly personalized digital workplace.

Disconfirmation question: Would the proposed journey increase duplicate requests, privacy exposure or unresolved effort compared with the existing human route? Name evidence that would stop or change the hypothesis.

## 11. Reflection and Pre-Foundation handoff

What did the green tick actually prove? Who owns resolution? How can a worker ask privately for help?

Pre-Foundation: Define persona, entry point, request, acknowledgement, owner, resolution and content provenance; map the one task before selecting portal features. Carry this same card, source questions and acceptance criteria forward. Deeper configuration, vendor comparisons and implementation research remain outside the Origin Story.

## 12. Official resources and architectural lenses

NIST AI RMF: What risk needs oversight? https://www.nist.gov/itl/ai-risk-management-framework

ISO/IEC 27001: Who owns information risk? https://www.iso.org/standard/27001

W3C WCAG 2.2: Who could struggle to use this journey? https://www.w3.org/TR/WCAG22/

Educational alignment only: TOGAF—business-led options and architectural decisions; BIZBOK—capabilities and value streams; BABOK—elicitation, requirements and acceptance; DAMA-DMBOK—data ownership, quality and lineage; COBIT—accountability and control evidence; relevant ISO/IEC information-risk principles. No certification, conformity or compliance is claimed.

Separate classification axes: HR theme = HR10 Digital Employee Experience; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry; enterprise transformation stream = Workforce. Related views do not become interchangeable lists.

## Source and companion record

Supporting HR source: https://app.notion.com/p/3d0ce6de60898140b833ceffb836b430

Enterprise hub: https://app.notion.com/p/28a329356ea6481dafbcc579c2463add

Workforce blueprint and existing anchors: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/derived-streams/01-workforce.md

Fictional personas and stable designations: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md

Source gaps ODG-Q01–ODG-Q17: https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/references/source-and-assumptions.md

Open enterprise issues remain unresolved: brands/SKUs counting basis; benefit overlap and cash bridge; inconsistent target scopes/horizons; vendor fit and approval evidence. These do not become achieved HR outcomes. Original research is preserved in the hub and source cases.

Learning-pattern reference GICS03: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/industrials-origin-stories.md

Supplied reference GICS02: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR10-ADX0-Architecting-Digital-Employee-Experience/05-HR10-CS-consumer-staples/0-The-Origin-Story/sprint/consumer-staples-hr10-origin-evolution-sprint.md

Native Google Doc: https://docs.google.com/document/d/1i-zxEIl4WCGU93SnFonFPXywO648-lLq8HjvXxYnh6E/edit?usp=drivesdk

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/consumer-staples-origin-stories.md

Saved-content verification is recorded in the sector index. No automatic synchronization, public student access, successful copying, executed tabletop tests or operational outcomes is asserted. End of HR10 Origin Story edition.
