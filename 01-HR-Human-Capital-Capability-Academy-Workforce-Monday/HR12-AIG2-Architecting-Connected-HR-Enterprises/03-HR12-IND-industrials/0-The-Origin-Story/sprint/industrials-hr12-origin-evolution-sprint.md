# HR12 — Connected HR Enterprises: The Origin Story

SuccessLabs Academy · GICS03 Industrials · OmniWorks Industrial Systems Ltd. · IIL — Industry Immersion Lab · Level 0 → Pre-Foundation · Sprint · 120 minutes · Edition 2026-10-31

Mission: Architecting Experiences for a Better World.

## 1. Your one promise

Design one workforce-event handoff that exposes incomplete access closure and supports controlled recovery without duplicate or stale actions.

Produce one Connected Workforce Handoff Build Card. Use synthetic records and a paper prototype. Beginners explain the decision in plain language; experienced learners challenge the same decision's assumptions. Configuration and implementation research remain in the supporting case outside this sprint.

## 2. Read the enterprise and sources accurately

OmniWorks is fictional: 74,000 employees, 36 countries, 61 manufacturing/engineering/assembly facilities and 320 service depots. The 61 is a mixed-facility count, not a confirmed plant-only count. Engineering, maintenance, production and field service shape the workforce problem. Case targets and victory criteria are aspirations, not achieved results. This edition adds a bounded synthetic episode; it does not assert a deployment.

Source-scoped lead: Sameer Kulkarni, Enterprise HR Integration Architect. The source describes a termination event failing across HR, identity and plant access, with access left open for 18 hours, plus duplicate time records and weak end-to-end ownership. These are fictional case triggers, not measured incidents here. Sameer retains his source designation. Proposed SAP Integration Suite/BTP examples remain technology options.

Existing enterprise anchors: OW-M17 — risk/security; OW-M18 — workforce/adoption; OW-M19 — delivery readiness. The workforce blueprint also inherits OW-M03, OW-M09 and OW-M11. Keep those IDs unchanged. New IDs prefixed OW-TOS-HR12 are educational additions, not previously approved client requirements.

## 3. Origins: five closed historical teaching windows

These windows group teaching ideas, not universal invention dates or OmniWorks corporate biography. Adoption overlaps; older practices can coexist through the present. Each generation changes the medium without automatically resolving ownership, evidence or authority.

1970–1984 — Paper notices and telephone calls transmit workforce changes; receipt and action are difficult to prove.

1985–1994 — Batch files move more records; late delivery and unowned rejects can leave access or pay incorrect.

1995–2004 — Point-to-point interfaces automate handoffs; technical success can conceal inconsistent business meaning.

2005–2014 — APIs and integration platforms improve reuse; retries, schema changes and source/target disagreement still need control.

2015–2025 — Events and observable integration products improve coordination; published events do not prove target action or end-to-end closure.

Recall prompt: reconstruct the five responses as problem → process/application response → unfinished problem. Which old failure could survive in the newest system?

## 4. One persona-led dilemma

### Scene 1

Sameer reads the source termination incident. HR shows inactive employment while digital and plant access remain open. He begins with the consequence and accountable closure owner rather than a new interface.

### Scene 2

An integration dashboard is green because it sent the message. Sameer asks whether IAM and physical-access services confirmed the required action and whether plant security reconciled the result. A successful send is insufficient.

### Scene 3

Reveal: a synthetic delayed earlier 'active' event arrives after termination, followed by a duplicate termination. Replaying everything blindly could reopen access or create repeated actions.

### Scene 4

Sameer revises one handoff contract with business meaning, source authority, correlation, version/order, idempotency and per-consumer outcome. Security owners invoke an approved compensating closure path during outage; recovery must reconcile actual target state before declaring completion.

Decision pause: Add a quick custom interface, create a reusable thin-slice integration product, or retain a controlled manual handoff temporarily. Which risk and readiness evidence determine sequencing?

## 5. Responsibilities, ownership and human authority

HR core (HR data owner): authoritative employment status and business-valid change; it does not own every target entitlement.

Integration product (journey/integration owner): validated contract, routing, correlation, ordering, duplicate control, observability and controlled recovery; SAP Integration Suite is one possible platform.

IAM (identity owner): account/entitlement actions under access policy. Physical-access service (plant security owner): badge/site access actions and actual closure confirmation.

Payroll/time and other consumers (domain owners): their independent lifecycle consequences and reconciliation. A source inactive status is not automatically a zero-pay instruction.

Security/operations authorities own compensating access action and incident escalation; the journey owner tracks end-to-end outcome, while source stewards correct disputed employment facts.

Design boundary: Integration transports approved facts and requests; it cannot invent employment authority, bypass plant security or equate broker acknowledgement with completed access removal. Proposed responsibilities are learning architecture, not proof that the fictional enterprise already operates this design. Select technology only after the business rule and accountable owner are clear. SAP examples illustrate capabilities, not mandatory product choices.

## 6. Exactly 120 minutes

0–10: Read the promise and dilemma; state the worker and business outcome in two sentences.

10–30: Reconstruct the five historical windows; explain what each process improvement left unresolved.

30–50: Play the scenes and reveal the evidence in order; record your first choice and revised reasoning.

50–65: Draw the responsibility/ownership map; name the human decision right and exception route.

65–95: Complete the one build card; compare two options and explore the three future scenarios. Scan only the resource relevant to your uncertainty.

95–115: Perform the three tabletop tests below; record observed paper results and revise the same card.

115–120: Explain your decision in 60 seconds, reflect, and carry the card into Pre-Foundation. Total: 120 minutes.

## 7. One build card: Connected Workforce Handoff Build Card

Synthetic experiment: SYN-EVT1201 terminates synthetic employment SYN-E1201 effective 1 November 2026. IAM acknowledges closure; the plant access target times out. An earlier active-state version arrives late and a duplicate termination follows. IDs, dates and event sequence are new teaching data, not executed integrations.

Fill these nine fields on one page: purpose and affected person; current/proposed state and source evidence; identity/object definitions; business date/time and version; application/data owners; human approval and appeal route; chosen option versus alternative with trade-off; exception/fallback and automation boundary; three test observations and revision.

Minimum design reasoning: Define source/target identifiers, event meaning, business-valid time versus arrival time, schema/version and authorized audience. Use an idempotency scope and state/version rule appropriate to the domain; do not claim 'exactly once' transport or blindly discard corrections. Minimize payload and preserve investigation evidence.

Do not invent country rules, safety thresholds, collective-agreement terms, live data or missing approvals. Record unknowns with an owner and discovery question. Support an accessible human route for the worker. Consider fatigue, learning opportunity, avoidable travel/rework or resource use where the dilemma provides evidence; do not infer environmental savings.

## 8. Exactly three tabletop tests

### OW-TOS-HR12-T01 — Unconfirmed target closure

Reveal/input: Message delivery succeeded but plant access has no confirmed action.

Expected design response: Keep closure incomplete, escalate to the plant/security owner and invoke only an approved compensating route; reconcile target state.

### OW-TOS-HR12-T02 — Duplicate and stale event

Reveal/input: Duplicate termination and older active event arrive after the newer state.

Expected design response: Avoid repeated side effects and stale reopening using agreed identity/version semantics; retain audit and route ambiguous corrections for review.

### OW-TOS-HR12-T03 — Schema/replay ambiguity

Reveal/input: A replay contains an unknown schema and disputed employment identifier.

Expected design response: Quarantine the affected message, avoid side effects, obtain owner-approved mapping/schema correction and reconcile before controlled replay.

For each test, record input → expected response → actual observed paper response → evidence note → pass/revise. Expected responses are proposed acceptance criteria, not executed results. Publication executes none of these tabletop tests. A bypass of the protected decision requires redesign, even if the card is complete.

## 9. Traceability and honest measures

OW-TOS-HR12-REQ01 — Trace an authoritative workforce event to distinct, verified consumer outcomes. Source connection: supporting HR case mandate and OW-M18. Assessed by T01; card must identify the authoritative fact and owner.

OW-TOS-HR12-REQ02 — Make failure, duplicate/stale events and recovery explicit without granting unauthorized actions. Source connection: HR case governance/scenario injection and OW-M17/OW-M19. Assessed by T02–T03; card records exception, authority and recovery condition.

OW-TOS-HR12-ADR01 — Prefer a reusable thin-slice event contract with reconcilable target states over an unobserved point-to-point send; compare initial speed with recovery and reuse cost. Compare the stated alternative and trade-off; this is a proposed educational decision that learners may reject with evidence.

OW-TOS-HR12-EXP01 — this synthetic card and T01–T03 extend OW-M19's traceable-pilot discipline. They do not complete the wider case's tests or rollout.

OW-TOS-HR12-M01 — completed mandatory card fields / 9 × 100; learning completeness only. OW-TOS-HR12-M02 — Record per-consumer confirmed/unconfirmed state and whether T02–T03 prevented stale/ambiguous action; no actual latency, access closure or recovery result is claimed. No baseline, target attainment or operating benefit is inferred from an empty result.

OW-TOS-HR12-EV01 — initially unfilled evidence slot for observed tabletop results, revisions and reviewer questions. Existing case success metrics remain separate planned outcomes.

## 10. AI-driven exploration: scenarios, not predictions

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. All require approved purpose, evidence, worker participation, accountable ownership and proportionate controls.

2026–2030 — Assist: Assistance could summarize integration exceptions and identify the accountable owner.

2031–2040 — Connect: Connected journey products could reconcile workforce, identity, access and pay consequences with source authority preserved.

2041–2050 — Adapt: Adaptive operations could propose recovery plans from approved patterns; privileged action and ambiguous business correction remain controlled.

Competing future: Fewer critical interfaces with rehearsed human closure may be safer than a highly connected ecosystem lacking ownership and recovery capacity.

Disconfirmation question: Would the new event platform still declare success while targets remain inconsistent, or recover more slowly than a controlled manual process? Record the evidence that would make you stop or change the hypothesis.

## 11. Reflection and Pre-Foundation handoff

What does delivery prove—and what does it leave unknown? Who owns actual plant access removal? When could a replay make the situation worse?

Pre-Foundation: Define one event contract, authoritative object, producer/consumer owners, identity/date/version semantics, acknowledgement meaning and recovery/reconciliation path. Carry forward the same card, unresolved questions and proposed acceptance criteria. Deeper implementation, vendor comparisons and the wider capstone stay outside this Origin Story.

## 12. Official resources: choose with a question

NIST AI Risk Management Framework — Which harm, evidence gap or oversight boundary would prevent your proposed assistance from expanding? https://www.nist.gov/itl/ai-risk-management-framework

ISO/IEC 27001 overview — What information risk, accountable owner and review evidence must your design make visible? https://www.iso.org/standard/27001

W3C WCAG 2.2 — Could a worker use the digital journey with keyboard/assistive technology or a shared device, and what needs user testing? https://www.w3.org/TR/WCAG22/

Educational alignment: TOGAF — business-led options and decisions; BIZBOK — capability/value-stream relationships; BABOK — elicitation, requirements and acceptance; DAMA-DMBOK — data ownership, quality and lineage; COBIT — accountability and control evidence; ISO/IEC 27001 principles — information-risk management; ISO 9001/ISO 45001 principles where relevant — quality and worker participation/safety. No certification, conformity or compliance is claimed.

Classification axes remain separate: HR theme = HR12 Connected HR Enterprises; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry, applied as distinct views; enterprise transformation stream = Workforce. These are related axes, not interchangeable stream lists.

## Source and companion record

Supporting HR source: https://app.notion.com/p/d921f5991d264e14af802077d41cd482

Enterprise hub: https://app.notion.com/p/d1579523dadb48fea5a6319f072ef755

Workforce blueprint: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/derived-streams/01-workforce.md ; source blob 22f877c403a461b6321cdd484ca9c7d06faf0a8b

Readiness/risk/workforce anchors: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/master/theme-e-execution.md ; source blob 454199f06f9496bd8ca31a190475fbec814e2873

Persona register: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md ; source blob 16313187f92ef25bce6c4a83bba36d5b74399de7

Open source issues OW-Q01–OW-Q06: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/references/source-and-assumptions.md ; source blob 98fa0891714fbf52d5813e6eb517f936e4bc681e. Do not combine alternate enterprise footprints, asset populations or unvalidated financial benefits. Source-scoped persona designation differences remain unresolved; no merger is implied.

References reviewed 31 October 2026 IST: Materials HR01–HR12 index and Energy HR01. Energy supplies the one-card learning pattern; this edition uses the requested closed history and separate AI scenario windows.

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR12-AIG2-Architecting-Connected-HR-Enterprises/03-HR12-IND-industrials/0-The-Origin-Story/sprint/industrials-hr12-origin-evolution-sprint.md

Native Google Doc: https://docs.google.com/document/d/1myoZV5AAHciV8PAWa1WTlA_GxwK02ODBkP361gjWja8/edit?usp=drivesdk

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/industrials-origin-stories.md

Matching content is explicitly published and read back; no automatic synchronization, public student access or successful copying is established. End of HR12 Origin Story edition.
