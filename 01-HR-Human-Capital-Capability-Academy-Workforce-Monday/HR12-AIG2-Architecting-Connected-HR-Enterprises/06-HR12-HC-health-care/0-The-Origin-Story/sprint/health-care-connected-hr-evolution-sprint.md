# The event was sent; did the receiving facility change?

SuccessLabs Academy · HR12 — Connected HR Enterprises · GICS06 Health Care · OmniHealth Systems Ltd.
IIL — Industry Immersion Lab · Level 0 — The Origin Story · Format: Sprint · 120 minutes · Edition 2026-10-31
Mission: Architecting Experiences for a Better World.
Planning reference: HUB-ORIGIN-HR12-HC-sprint (not an LMS ID). Community/Citizen Edition. Published lesson content does not establish live enrolment, certification or public companion access.

## 1. One learner promise

In 120 minutes, design one reliable workforce-change handoff that distinguishes source approval, message delivery and confirmed business outcome.

One persona-led story, one Connected Workforce Handoff Build Card, exactly three tabletop tests. Use synthetic data and one card throughout; no tenant is required.

## 2. Read OmniHealth accurately

The fictional enterprise source stipulates 126,000 staff across 19 countries, 86 hospitals, 440 clinics and 670 diagnostic centres. It spans pharmacy, digital health, research and corporate functions. These figures are source stipulations, not independently measured facts. Workforce burden, fragmented information and manual handoffs motivate this lesson.

The source proposes USD620M investment over three years and USD250M annual value; neither is an achieved result or an approved HR budget. OHS-Q01–Q11 retain missing cost, baseline, attribution, privacy and interoperability evidence. OHS-Q12 retains the source's 13-journey versus 14-reference discrepancy. The requested scope is twelve HR themes; Recruiting and Onboarding remain separate source cases within HR02. HR13 remains outside this edition.

Existing persona names, designations and IDs are preserved. The incident, dialogue, synthetic records, proposed controls and all OHS-HR12-prefixed IDs below are newly introduced educational additions, not existing approved enterprise requirements or deployed capabilities. Source “outcomes” describe aspirations. No patient information or real employee data is needed.

## 3. Origins: the problem survives the medium

These closed historical teaching windows are educational groupings, not universal invention dates or OmniHealth's corporate biography. Adoption overlaps; paper and older systems can coexist through the present.

1970–1984 — Paper change notices and telephone calls depend on named recipients; sending a form does not confirm action.

1985–1994 — Batch personnel files distribute changes; late and duplicate records complicate reconciliation.

1995–2004 — Point-to-point interfaces connect HR to payroll and identity; shared identifiers and ownership remain essential.

2005–2014 — APIs and integration platforms improve orchestration; a transport success can still hide a rejected business change.

2015–2025 — Events and assisted monitoring reveal dependencies; retries, ordering and recovery require explicit contracts and accountable owners.

Counterexample: an HTTP success or queue acknowledgement can prove technical receipt without proving correct target access, payroll or roster state.

## 4. One story, one consequential choice

Daniel Weber (OHS-P13), Enterprise Architecture Director, reviews the synthetic facility transfer introduced in HR01 with Sofia Tan (OHS-P05), Chief Digital and Information Officer. Core HR has approved the change, but the receiving scheduling service is unavailable. A delayed older event then arrives after the new assignment event. Dr. Amina Okafor (OHS-P07), Nursing and Care Coordination Director, asks which unit now owns the worker's coordination tasks.

Pause before the reveal. Choose declare success when the event leaves HR, replay every message, or reconcile each target's business state through a versioned contract. State who benefits, who bears the risk and what evidence you need.

Evidence reveal: the worker remains employed by the same legal employer in the exercise. Ending the previous facility assignment is not employment termination. IAM has acknowledged receipt, while the roster has not confirmed its update; clinical readiness remains a separate local decision.

Revised decision: Daniel separates source state, transport receipt, target application outcome and authorized operational readiness. Sofia requires stable identifiers, version/effective-time checks and controlled replay. Amina escalates the unconfirmed roster through its operational owner; no one disables employment or grants clinical authority because of an ambiguous assignment-end event. A learner may defend a different option if the card names its authority, evidence, trade-off and conditions for stopping. Missing evidence remains unknown; an urgent request does not manufacture approval.

## 5. Applications serve accountable people

Proposed responsibilities, subject to local discovery:

- Core HR owns the approved person/employment/assignment change and business effective time; its delegated approver owns source authorization.
- Integration services own transport, contract validation, correlation, retry and technical observability; the integration owner cannot attest to target business correctness.
- Each target owner owns accepted/rejected/pending outcome and reconciliation: payroll for pay inputs, IAM for approved access, scheduling for the roster, Learning for learning context.
- The receiving operational/clinical authority owns readiness and task handoff. Daniel governs architecture exceptions; Sofia sponsors platform priorities; neither overrides local professional authority.

Across these boundaries, HR owns employment facts; designated clinical governance owns clinical privilege decisions; IAM administers approved access. Employment, learning completion, account access and permission for clinical work are distinct states. Share only the data needed for the declared purpose; keep patient records and detailed health information out of general HR learning cards. Omar Haddad (OHS-P10), CISO and Privacy Lead, governs privacy/access assurance; jurisdiction-specific applicability remains unresolved.

SAP examples illustrate responsibilities rather than prescribe a purchase: Integration Suite and SAP BTP as illustrative integration/extension services between SuccessFactors, Finance, payroll, identity and operational applications. No feature availability, license entitlement, configuration, legal compliance or clinical conformance is established here. AI may draft a reminder or summarize permitted evidence; it cannot grant clinical privilege, make a high-impact employment decision or attest to payment or delivery.

## 6. The exact 120-minute sprint

- 0–10 minutes: understand the learner promise and people problem.
- 10–30 minutes: compare the five historical windows and identify the enduring question.
- 30–45 minutes: choose, reveal evidence and revise the story decision.
- 45–60 minutes: map application responsibility, data ownership and human decision rights.
- 60–90 minutes: complete the single build card, comparing one alternative and one local variant.
- 90–110 minutes: discuss the three tabletop tests and record observed paper decisions and revisions.
- 110–120 minutes: explain the design in 60 seconds, reflect and name the Pre-Foundation discovery question.

Selective resource reading fits within these activities. The single card holds all notes; no extra deliverable is required.

## 7. One synthetic build experiment

Synthetic same-employer HC-P100 / HC-E100 transfer CL-A → HP-A, effective 1 November 2026. Event HC-EVT1200 version 2, prior version 1 delayed, duplicate delivery possible; roster unavailable; IAM receipt only. No actual event executed.

Complete one Connected Workforce Handoff Build Card with these six fields:

1. Need and scope: Keep the workforce transfer and coordination ownership visible across systems without converting a sent message into completion. Explain the capability and value-stream step before naming a tool.
2. Facts and time: preserve identifiers, source, effective/as-of time, unknowns and approved policy version. Distinguish a source fact from your assumption.
3. Decision and ownership: Specify event purpose, stable person/employment/assignment identifiers, schema/version, business effective time, producer, permitted fields, target-specific outcome and human authority. Record one alternative, its trade-off and the evidence that could favour it.
4. Handoff and recovery: Quarantine invalid schemas or ambiguous identity; reconcile the authoritative source/target version before replay. Record per-target exception owners, bounded retries, approved fallback, worker notice and the condition for declaring completion. Name the accountable exception role, accessible human route and condition for reconciliation.
5. Local variant and data: choose one facility/language/role variation; justify minimum fields, purpose, owner, retention decision and viewers. Retain a non-digital route.
6. Evidence and learning: record T01–T03 input → expected → observed paper result → revision → reviewer question on this same card. Leave results unfilled until observed.

## 8. Exactly three tabletop tests

### OHS-HR12-T01 — Unavailable target

Input/reveal: HR approves; roster unavailable; IAM only acknowledges receipt.

Expected in the proposed design: Keep per-target business states pending/unconfirmed until their owners verify outcomes; invoke approved operational fallback without expanding authority.

Record: Source approval, transport receipt, target state and named owner. Observed result and pass/revise remain unfilled until learners perform the tabletop.

### OHS-HR12-T02 — Duplicate and out-of-order events

Input/reveal: Version 2 arrives, then duplicate version 2 and old version 1.

Expected in the proposed design: The proposed consumer deduplicates by stable contract key and prevents stale state regression; effective-time policy is explicit rather than arrival order alone.

Record: Expected target views, correlation/version and reconciliation rule. Observed result and pass/revise remain unfilled until learners perform the tabletop.

### OHS-HR12-T03 — Bad schema and replay

Input/reveal: Assignment-end message lacks required context and is mistaken for employment termination.

Expected in the proposed design: Quarantine; do not terminate employment or disable unrelated access. Validate corrected contract and authoritative state before approved replay.

Record: Rejected payload fields, authority boundary, repair owner and replay gate. Observed result and pass/revise remain unfilled until learners perform the tabletop.

Acceptance is a defensible completed card and an explanation of all three decisions after revision. A paper discussion proves neither a working system nor a safe clinical service. Publishing this lesson executes no tests.

## 9. Traceability without invented evidence

Existing enterprise anchors: OHS-M17 — risk/security; OHS-M18 — workforce/adoption; OHS-M19 — readiness/execution; OHS-M20 — measures. The Workforce derived scope also references OHS-M03 and OHS-M11. Theme source page(s), enterprise master and persona cards remain supporting material outside the sprint.

New educational anchors:
- OHS-HR12-REQ01: Make workforce integration outcomes explicit, versioned, independently owned and recoverable without changing employment or clinical authority by inference. Link to the theme source and OHS-M18/M19; assess using T01–T03.
- OHS-HR12-ADR01: Use versioned, minimum-data handoff contracts with target-specific acknowledgements and reconciliation before controlled replay. A proposed decision, open to revision; store alternative, owner and reason on card field 3.
- OHS-HR12-EXP01: this synthetic experiment, linked to REQ01 and ADR01; tests T01–T03 are planned.
- OHS-HR12-ME01: learning completeness = completed card fields / 6 × 100. No observed score exists; completeness alone does not prove correctness.
- OHS-HR12-ME02: Track confirmed target business outcomes / required target handoffs, balanced by stale-state reversions, duplicate effects and unresolved exception age. Proposed observation only; define denominator and balancing measure before a pilot.
- OHS-HR12-EV01: initially unfilled evidence slot for observed paper results, revisions and reviewer questions. No achieved benefit, ROI or system result is claimed.

## 10. AI-driven exploration: three scenarios

Scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps:
- 2026–2030 — Assist: An assistant summarizes failures using permitted correlation evidence.
- 2031–2040 — Connect: Governed contracts connect source changes, target outcomes and accountable exception queues.
- 2041–2050 — Adapt: A bounded coordinator proposes recovery sequences as dependencies change; owners authorize replay and readiness decisions.

Competing future: facilities retain locally governed workflows and modest deterministic tools because evidence quality, cost or worker trust makes broader automation unsuitable.

Falsification question: Would an autonomous recovery coordinator produce more duplicate effects, stale-state regressions or unauthorized access changes than reviewed deterministic recovery? State what observation would make you reduce, redesign or stop assistance. Human accountability does not disappear in any scenario.

## 11. Reflect and continue the story

What changed your first decision? Which record could be accurate yet insufficient? Whose voice or access route is missing?

Pre-Foundation handoff: Discover the actual source/target contracts, identifiers, effective-time semantics, acknowledgement meanings, delegated recovery owners and facility fallback before implementing integration. Carry the same card forward. Beyond this edition, Foundation can map the capability and workflow; Essentials can build a bounded prototype; Advanced can explore exceptions and recovery; Ultimate can conclude with evidenced value, ROI assumptions, troubleshooting and lessons learned. Those later-stage activities and outcomes are not delivered or achieved by this Origin Story.

## 12. A few official resources

- WHO health workforce: https://www.who.int/teams/health-workforce — Which workforce need and equity question should shape the experiment?
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework — What evidence, oversight and stopping condition should bound assistance?
- SAP Employee Central Core Academy: https://learning.sap.com/courses/sap-successfactors-employee-central-core-academy — Use selectively to understand the shared workforce foundation; it does not establish clinical authority or teach all twelve themes.

Educational alignment: TOGAF — problem, options and architecture decision; BIZBOK — capability and value stream; BABOK — stakeholder need and acceptance; DAMA-DMBOK — ownership, quality and lineage; COBIT — accountability, control and assurance; relevant ISO/IEC security and service principles — least privilege, controlled change and recovery evidence. This is conceptual educational alignment, not certification or compliance assessment.

Keep classification axes separate: HR theme = HR12 Connected HR Enterprises; architecture streams = applicable views across Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry, each with its own question; enterprise transformation stream = Workforce. Cross-links do not make the three axes interchangeable.

## Source and edition record

- Enterprise hub: https://app.notion.com/p/48ae8460518643559ed65381fb89b3fe
- Theme source(s): https://app.notion.com/p/3d0ce6de6089819a80b0ce51f81b779a
- Workforce scope: https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/derived-streams/01-workforce.md
- Existing personas: https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/personas/persona-cards.md
- Source/assumptions register: https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/references/source-and-assumptions.md
- GICS02 structural reference: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md
- Standing user approval covers authoring and publication of HR01–HR12. Edition 2026-10-31 IST; future substantive revisions need their own dated record. Companion readback is tracked in the sector index; it is not automatic synchronization.
