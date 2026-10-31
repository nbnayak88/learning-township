# A payment timeout is not permission to pay again

SuccessLabs Academy · HR07 — Autonomous Payroll Enterprises · GICS06 Health Care · OmniHealth Systems Ltd.
IIL — Industry Immersion Lab · Level 0 — The Origin Story · Format: Sprint · 120 minutes · Edition 2026-10-31
Mission: Architecting Experiences for a Better World.
Planning reference: HUB-ORIGIN-HR07-HC-sprint (not an LMS ID). Community/Citizen Edition. Published lesson content does not establish live enrolment, certification or public companion access.

## 1. One learner promise

In 120 minutes, design one controlled payroll exception decision that protects correct pay without treating an uncertain payment as a failure or success.

One persona-led story, one Payroll Exception Build Card, exactly three tabletop tests. Use synthetic data and one card throughout; no tenant is required.

## 2. Read OmniHealth accurately

The fictional enterprise source stipulates 126,000 staff across 19 countries, 86 hospitals, 440 clinics and 670 diagnostic centres. It spans pharmacy, digital health, research and corporate functions. These figures are source stipulations, not independently measured facts. Workforce burden, fragmented information and manual handoffs motivate this lesson.

The source proposes USD620M investment over three years and USD250M annual value; neither is an achieved result or an approved HR budget. OHS-Q01–Q11 retain missing cost, baseline, attribution, privacy and interoperability evidence. OHS-Q12 retains the source's 13-journey versus 14-reference discrepancy. The requested scope is twelve HR themes; Recruiting and Onboarding remain separate source cases within HR02. HR13 remains outside this edition.

Existing persona names, designations and IDs are preserved. The incident, dialogue, synthetic records, proposed controls and all OHS-HR07-prefixed IDs below are newly introduced educational additions, not existing approved enterprise requirements or deployed capabilities. Source “outcomes” describe aspirations. No patient information or real employee data is needed.

## 3. Origins: the problem survives the medium

These closed historical teaching windows are educational groupings, not universal invention dates or OmniHealth's corporate biography. Adoption overlaps; paper and older systems can coexist through the present.

1970–1984 — Wage books and manual time summaries rely on local checking; a copied number may carry no source.

1985–1994 — Computerized payroll standardizes calculation; wrong approved inputs still produce wrong pay.

1995–2004 — HR/payroll integration links employment changes and earnings; entry, effective and payment dates differ.

2005–2014 — Service centres and payroll controls expose exceptions; reconciliation across bank and accounting stages remains essential.

2015–2025 — Cloud monitoring and assisted triage accelerate investigation; accountable payroll release and settlement evidence remain distinct.

Counterexample: a calculation with no technical error can still use an incorrect on-call allowance or pay the same instruction twice.

## 4. One story, one consequential choice

Michael Chen (OHS-P02), Group CFO, asks Nina Fernandes (OHS-P06), Group CHRO, why a synthetic on-call allowance is missing after a care-team transfer. An approved time correction arrived after payroll input cut-off. A later payment attempt returns a timeout, and the operations desk suggests sending it again immediately. Nina wants the worker paid correctly; Michael wants evidence before a duplicate instruction creates a second problem.

Pause before the reveal. Choose retry immediately, assume payment succeeded, or investigate calculation and settlement states through separate accountable owners. State who benefits, who bears the risk and what evidence you need.

Evidence reveal: the time correction is approved but its payroll treatment is unconfirmed. The bank request has a stable instruction reference and an unknown settlement outcome. No country-specific tax, allowance or retroactivity rules have been supplied.

Revised decision: Nina routes the dated input correction to the delegated payroll owner and keeps the worker informed. Michael requires reconciliation of the existing payment reference before any replacement. Payroll determines the authorized correction process; no invented formula, statutory rule or bank outcome fills the evidence gap. A learner may defend a different option if the card names its authority, evidence, trade-off and conditions for stopping. Missing evidence remains unknown; an urgent request does not manufacture approval.

## 5. Applications serve accountable people

Proposed responsibilities, subject to local discovery:

- Core HR owns employment/assignment facts; Time owns approved time and correction evidence, with effective and approval dates.
- Payroll owns input validation, local rule application, calculation, controlled release and payroll reconciliation; a delegated payroll approver authorizes action.
- Payment services transport approved instructions; Treasury/banking authorities reconcile receipt and settlement using stable references.
- Finance owns payroll accounting and ledger reconciliation. HR service teams communicate permitted status; an assistant may triage but cannot release or attest to pay.

Across these boundaries, HR owns employment facts; designated clinical governance owns clinical privilege decisions; IAM administers approved access. Employment, learning completion, account access and permission for clinical work are distinct states. Share only the data needed for the declared purpose; keep patient records and detailed health information out of general HR learning cards. Omar Haddad (OHS-P10), CISO and Privacy Lead, governs privacy/access assurance; jurisdiction-specific applicability remains unresolved.

SAP examples illustrate responsibilities rather than prescribe a purchase: Employee Central Payroll with Employee Central, Time and Finance; monitoring/control tools assist an accountable payroll operating model. No feature availability, license entitlement, configuration, legal compliance or clinical conformance is established here. AI may draft a reminder or summarize permitted evidence; it cannot grant clinical privilege, make a high-impact employment decision or attest to payment or delivery.

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

Synthetic HC-E700; corrected on-call entry HC-T700 approved after illustrative cut-off; payroll run HC-RUN700; payment HC-PAY700 timed out. Amount and local rule are intentionally unspecified. No real payroll execution.

Complete one Payroll Exception Build Card with these six fields:

1. Need and scope: Resolve the worker's pay concern while preserving evidence across input, calculation, release, payment and accounting. Explain the capability and value-stream step before naming a tool.
2. Facts and time: preserve identifiers, source, effective/as-of time, unknowns and approved policy version. Distinguish a source fact from your assumption.
3. Decision and ownership: Separate effective/entry/approval/cut-off dates; map each stage's owner and status; compare controlled correction with an unsafe blanket rerun. Record one alternative, its trade-off and the evidence that could favour it.
4. Handoff and recovery: Quarantine the affected exception under approved payroll procedures; reconcile HC-PAY700 before retry. Define worker notice, escalation time, payroll fallback authority and accounting reconciliation condition. Name the accountable exception role, accessible human route and condition for reconciliation.
5. Local variant and data: choose one facility/language/role variation; justify minimum fields, purpose, owner, retention decision and viewers. Retain a non-digital route.
6. Evidence and learning: record T01–T03 input → expected → observed paper result → revision → reviewer question on this same card. Leave results unfilled until observed.

## 8. Exactly three tabletop tests

### OHS-HR07-T01 — Late approved input

Input/reveal: On-call correction arrives after input cut-off.

Expected in the proposed design: Do not assume it is included or select a retro rule; payroll checks the applicable approved correction path and authorizes the treatment.

Record: Dates, input acknowledgement, policy gap and accountable decision. Observed result and pass/revise remain unfilled until learners perform the tabletop.

### OHS-HR07-T02 — Unknown settlement

Input/reveal: Payment request times out after submission.

Expected in the proposed design: Keep settlement unknown; query/reconcile the stable instruction before any replacement; avoid duplicate release.

Record: Instruction reference, authoritative status and retry gate. Observed result and pass/revise remain unfilled until learners perform the tabletop.

### OHS-HR07-T03 — Accounting mismatch

Input/reveal: Payroll calculation reconciles, but ledger posting is rejected.

Expected in the proposed design: Pay, payment and posting states remain distinct; Finance owns posting repair without an automatic second payment.

Record: Per-stage totals/status, exception owner and accounting recovery condition. Observed result and pass/revise remain unfilled until learners perform the tabletop.

Acceptance is a defensible completed card and an explanation of all three decisions after revision. A paper discussion proves neither a working system nor a safe clinical service. Publishing this lesson executes no tests.

## 9. Traceability without invented evidence

Existing enterprise anchors: OHS-M17 — risk/security; OHS-M18 — workforce/adoption; OHS-M19 — readiness/execution; OHS-M20 — measures. The Workforce derived scope also references OHS-M03 and OHS-M11. Theme source page(s), enterprise master and persona cards remain supporting material outside the sprint.

New educational anchors:
- OHS-HR07-REQ01: Preserve controlled payroll exception handling across approved inputs, calculation, release, settlement and accounting. Link to the theme source and OHS-M18/M19; assess using T01–T03.
- OHS-HR07-ADR01: Use evidence-gated correction and stable-reference reconciliation instead of inferring success or repeating uncertain payments. A proposed decision, open to revision; store alternative, owner and reason on card field 3.
- OHS-HR07-EXP01: this synthetic experiment, linked to REQ01 and ADR01; tests T01–T03 are planned.
- OHS-HR07-ME01: learning completeness = completed card fields / 6 × 100. No observed score exists; completeness alone does not prove correctness.
- OHS-HR07-ME02: Track unresolved payment-status exceptions / instructions examined, balanced by pay-resolution time and duplicate-instruction incidents. Proposed observation only; define denominator and balancing measure before a pilot.
- OHS-HR07-EV01: initially unfilled evidence slot for observed paper results, revisions and reviewer questions. No achieved benefit, ROI or system result is claimed.

## 10. AI-driven exploration: three scenarios

Scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps:
- 2026–2030 — Assist: An assistant groups payroll exceptions and drafts worker updates.
- 2031–2040 — Connect: Governed evidence connects approved time, calculated pay, Treasury status and accounting.
- 2041–2050 — Adapt: A bounded coordinator suggests recovery sequences under country-specific human controls; release authority remains explicit.

Competing future: facilities retain locally governed workflows and modest deterministic tools because evidence quality, cost or worker trust makes broader automation unsuitable.

Falsification question: Would assisted exception handling increase duplicate instructions or reduce workers' ability to challenge incorrect pay? State what observation would make you reduce, redesign or stop assistance. Human accountability does not disappear in any scenario.

## 11. Reflect and continue the story

What changed your first decision? Which record could be accurate yet insufficient? Whose voice or access route is missing?

Pre-Foundation handoff: Discover the local payroll calendar, earning policy, correction/retro rules, release authority and authoritative settlement evidence before calculating any amount. Carry the same card forward. Beyond this edition, Foundation can map the capability and workflow; Essentials can build a bounded prototype; Advanced can explore exceptions and recovery; Ultimate can conclude with evidenced value, ROI assumptions, troubleshooting and lessons learned. Those later-stage activities and outcomes are not delivered or achieved by this Origin Story.

## 12. A few official resources

- WHO health workforce: https://www.who.int/teams/health-workforce — Which workforce need and equity question should shape the experiment?
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework — What evidence, oversight and stopping condition should bound assistance?
- SAP Employee Central Core Academy: https://learning.sap.com/courses/sap-successfactors-employee-central-core-academy — Use selectively to understand the shared workforce foundation; it does not establish clinical authority or teach all twelve themes.

Educational alignment: TOGAF — problem, options and architecture decision; BIZBOK — capability and value stream; BABOK — stakeholder need and acceptance; DAMA-DMBOK — ownership, quality and lineage; COBIT — accountability, control and assurance; relevant ISO/IEC security and service principles — least privilege, controlled change and recovery evidence. This is conceptual educational alignment, not certification or compliance assessment.

Keep classification axes separate: HR theme = HR07 Autonomous Payroll Enterprises; architecture streams = applicable views across Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry, each with its own question; enterprise transformation stream = Workforce. Cross-links do not make the three axes interchangeable.

## Source and edition record

- Enterprise hub: https://app.notion.com/p/48ae8460518643559ed65381fb89b3fe
- Theme source(s): https://app.notion.com/p/3d0ce6de6089817a9f86d0c1f5196750
- Workforce scope: https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/derived-streams/01-workforce.md
- Existing personas: https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/personas/persona-cards.md
- Source/assumptions register: https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/references/source-and-assumptions.md
- GICS02 structural reference: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md
- Standing user approval covers authoring and publication of HR01–HR12. Edition 2026-10-31 IST; future substantive revisions need their own dated record. Companion readback is tracked in the sector index; it is not automatic synchronization.
