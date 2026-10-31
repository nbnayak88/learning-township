# HR07 — Autonomous Payroll Enterprises: The Origin Story

SuccessLabs Academy · GICS03 Industrials · OmniWorks Industrial Systems Ltd. · IIL — Industry Immersion Lab · Level 0 → Pre-Foundation · Sprint · 120 minutes · Edition 2026-10-31

Mission: Architecting Experiences for a Better World.

## 1. Your one promise

Design one payroll exception decision that protects timely, explainable pay and prevents an uncertain payment from becoming a duplicate.

Produce one Payroll Control Build Card. Use synthetic records and a paper prototype. Beginners explain the decision in plain language; experienced learners challenge the same decision's assumptions. Configuration and implementation research remain in the supporting case outside this sprint.

## 2. Read the enterprise and sources accurately

OmniWorks is fictional: 74,000 employees, 36 countries, 61 manufacturing/engineering/assembly facilities and 320 service depots. The 61 is a mixed-facility count, not a confirmed plant-only count. Engineering, maintenance, production and field service shape the workforce problem. Case targets and victory criteria are aspirations, not achieved results. This edition adds a bounded synthetic episode; it does not assert a deployment.

Source-scoped lead: Meera Iyer, Global Payroll Transformation Executive. The source's retroactive time-rule change causes unexpected deductions across two plants three days before pay date. Hans Keller, Germany Payroll Lead; Luciana Silva, Plant Employee Persona; Robert Chen, Group Financial Controller; and Ngozi Adeyemi, Payroll Technology and Security Lead retain their case roles. Local statutory and agreement rules require confirmation; the lesson supplies no legal determination.

Existing enterprise anchors: OW-M17 — risk/security; OW-M18 — workforce/adoption; OW-M19 — delivery readiness. The workforce blueprint also inherits OW-M03, OW-M09 and OW-M11. Keep those IDs unchanged. New IDs prefixed OW-TOS-HR07 are educational additions, not previously approved client requirements.

## 3. Origins: five closed historical teaching windows

These windows group teaching ideas, not universal invention dates or OmniWorks corporate biography. Adoption overlaps; older practices can coexist through the present. Each generation changes the medium without automatically resolving ownership, evidence or authority.

1970–1984 — Wage books and manual pay packets create a promise of accurate payment; missing attendance or arithmetic can break it.

1985–1994 — Batch payroll and bank files reduce repetitive calculation; cutoff dates and rejected outputs still need control.

1995–2004 — Integrated payroll engines connect master data and time; automation magnifies incorrect rules or duplicate inputs.

2005–2014 — Shared services and parallel-run controls standardize operations; one global design cannot erase local pay obligations.

2015–2025 — Cloud payroll and exception monitoring improve visibility; successful calculation does not establish settled payment or reconciled accounting.

Recall prompt: reconstruct the five responses as problem → process/application response → unfinished problem. Which old failure could survive in the newest system?

## 4. One persona-led dilemma

### Scene 1

Luciana asks Meera why her expected pay changed. Meera begins with employee impact and the authoritative rule—not a faster payroll run.

### Scene 2

Hans reveals the retroactive time-rule change. Meera asks for approved rule version, validity, population and before/after results. Without that evidence, a plausible deduction is still unexplained.

### Scene 3

Ngozi reports a payment file was transmitted, but the acknowledgement is missing. The team cannot infer failure from silence and resend blindly. Robert also needs calculation, payment liability and Finance posting to reconcile.

### Scene 4

Meera revises the exception card: contain the disputed change, confirm obligations and correction options with country owners, protect unaffected processing and communicate honestly. Pay release and emergency arrangements remain authorized decisions.

Decision pause: Recalculate immediately, contain the disputed change while reconciling, or use a country-approved correction route. Which evidence and pay-date impact determine the choice?

## 5. Responsibilities, ownership and human authority

HR core (HR owner): approved employment/compensation inputs; time service (time owner): approved time and premium inputs.

Payroll engine (country payroll owner): versioned calculation, retroactivity and pay results; SAP Employee Central Payroll is an example.

Control service (payroll control owner): population, variance, reconciliation and approval evidence; it cannot establish bank settlement.

Payment/bank service (treasury/payment owner): accepted, rejected, unknown and settled statuses. Finance (controller): liabilities and accounting postings.

Meera and delegated country payroll/treasury approvers decide release under segregation of duties; Luciana receives explanation and a human correction route.

Design boundary: Automation may highlight exceptions but cannot decide unknown payment state, statutory interpretation or material pay release without accountable authorization. Proposed responsibilities are learning architecture, not proof that the fictional enterprise already operates this design. Select technology only after the business rule and accountable owner are clear. SAP examples illustrate capabilities, not mandatory product choices.

## 6. Exactly 120 minutes

0–10: Read the promise and dilemma; state the worker and business outcome in two sentences.

10–30: Reconstruct the five historical windows; explain what each process improvement left unresolved.

30–50: Play the scenes and reveal the evidence in order; record your first choice and revised reasoning.

50–65: Draw the responsibility/ownership map; name the human decision right and exception route.

65–95: Complete the one build card; compare two options and explore the three future scenarios. Scan only the resource relevant to your uncertainty.

95–115: Perform the three tabletop tests below; record observed paper results and revise the same card.

115–120: Explain your decision in 60 seconds, reflect, and carry the card into Pre-Foundation. Total: 120 minutes.

## 7. One build card: Payroll Control Build Card

Synthetic experiment: SYN-PAY701 has approved time version V1 and disputed retro version V2. Synthetic gross result changes from 1,000 to 900 units. SYN-FILE701 has unknown payment status. These are teaching values, not actual pay calculations.

Fill these nine fields on one page: purpose and affected person; current/proposed state and source evidence; identity/object definitions; business date/time and version; application/data owners; human approval and appeal route; chosen option versus alternative with trade-off; exception/fallback and automation boundary; three test observations and revision.

Minimum design reasoning: Trace source version → calculation → approval → payment → posting separately. Reconcile disputed deductions and country obligations before release. Do not treat a technical timeout as permission to pay twice.

Do not invent country rules, safety thresholds, collective-agreement terms, live data or missing approvals. Record unknowns with an owner and discovery question. Support an accessible human route for the worker. Consider fatigue, learning opportunity, avoidable travel/rework or resource use where the dilemma provides evidence; do not infer environmental savings.

## 8. Exactly three tabletop tests

### OW-TOS-HR07-T01 — Retro-rule reveal

Reveal/input: V2 reduces synthetic gross by 100 units without confirmed approval evidence.

Expected design response: Contain the affected rule/input, compare V1/V2 and population, assign country review and explain the unresolved result.

### OW-TOS-HR07-T02 — Unknown payment

Reveal/input: SYN-FILE701 was sent but no acknowledgement was received.

Expected design response: Investigate with treasury/bank owner before resending; preserve file identity, duplicate prevention and authorized fallback.

### OW-TOS-HR07-T03 — Finance mismatch

Reveal/input: Payroll results and approved payment totals match, but Finance posting differs.

Expected design response: Keep posting exception open, reconcile liabilities and account mapping with Robert; do not label the entire cycle fully complete.

For each test, record input → expected response → actual observed paper response → evidence note → pass/revise. Expected responses are proposed acceptance criteria, not executed results. Publication executes none of these tabletop tests. A bypass of the protected decision requires redesign, even if the card is complete.

## 9. Traceability and honest measures

OW-TOS-HR07-REQ01 — Explain payroll differences through approved source and calculation versions. Source connection: supporting HR case mandate and OW-M18. Assessed by T01; card must identify the authoritative fact and owner.

OW-TOS-HR07-REQ02 — Keep payment uncertainty and accounting exceptions visible with controlled retry and segregated approval. Source connection: HR case governance/scenario injection and OW-M17/OW-M19. Assessed by T02–T03; card records exception, authority and recovery condition.

OW-TOS-HR07-ADR01 — Prefer a governed hybrid payroll control model with country validation over forcing one universal rule; compare added coordination with local accuracy/continuity. Compare the stated alternative and trade-off; this is a proposed educational decision that learners may reject with evidence.

OW-TOS-HR07-EXP01 — this synthetic card and T01–T03 extend OW-M19's traceable-pilot discipline. They do not complete the wider case's tests or rollout.

OW-TOS-HR07-M01 — completed mandatory card fields / 9 × 100; learning completeness only. OW-TOS-HR07-M02 — Record whether synthetic versions, population totals and per-stage statuses reconcile; no real payroll run or payment success is claimed. No baseline, target attainment or operating benefit is inferred from an empty result.

OW-TOS-HR07-EV01 — initially unfilled evidence slot for observed tabletop results, revisions and reviewer questions. Existing case success metrics remain separate planned outcomes.

## 10. AI-driven exploration: scenarios, not predictions

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. All require approved purpose, evidence, worker participation, accountable ownership and proportionate controls.

2026–2030 — Assist: Assistance could summarize variances and draft employee explanations from verified records.

2031–2040 — Connect: Connected payroll controls could reconcile time, calculation, payment and posting without merging their authorities.

2041–2050 — Adapt: Adaptive exception triage could route novel patterns to country experts while release, fairness and accountability stay human-governed.

Competing future: Stable country payrolls with stronger shared controls may outperform aggressive platform consolidation.

Disconfirmation question: Would consolidation increase unresolved variances or correction delays compared with the controlled country model? Record the evidence that would make you stop or change the hypothesis.

## 11. Reflection and Pre-Foundation handoff

What evidence separates calculated pay from money received? Why is an unknown bank response dangerous? What should Luciana be told now?

Pre-Foundation: Define payroll inputs, cutoff, retroactivity, reconciliation, payment states and posting; map one country-neutral control flow before localization. Carry forward the same card, unresolved questions and proposed acceptance criteria. Deeper implementation, vendor comparisons and the wider capstone stay outside this Origin Story.

## 12. Official resources: choose with a question

NIST AI Risk Management Framework — Which harm, evidence gap or oversight boundary would prevent your proposed assistance from expanding? https://www.nist.gov/itl/ai-risk-management-framework

ISO/IEC 27001 overview — What information risk, accountable owner and review evidence must your design make visible? https://www.iso.org/standard/27001

W3C WCAG 2.2 — Could a worker use the digital journey with keyboard/assistive technology or a shared device, and what needs user testing? https://www.w3.org/TR/WCAG22/

Educational alignment: TOGAF — business-led options and decisions; BIZBOK — capability/value-stream relationships; BABOK — elicitation, requirements and acceptance; DAMA-DMBOK — data ownership, quality and lineage; COBIT — accountability and control evidence; ISO/IEC 27001 principles — information-risk management; ISO 9001/ISO 45001 principles where relevant — quality and worker participation/safety. No certification, conformity or compliance is claimed.

Classification axes remain separate: HR theme = HR07 Autonomous Payroll Enterprises; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry, applied as distinct views; enterprise transformation stream = Workforce. These are related axes, not interchangeable stream lists.

## Source and companion record

Supporting HR source: https://app.notion.com/p/2a5d9ca53ccc45798115a4c12137c2c2

Enterprise hub: https://app.notion.com/p/d1579523dadb48fea5a6319f072ef755

Workforce blueprint: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/derived-streams/01-workforce.md ; source blob 22f877c403a461b6321cdd484ca9c7d06faf0a8b

Readiness/risk/workforce anchors: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/master/theme-e-execution.md ; source blob 454199f06f9496bd8ca31a190475fbec814e2873

Persona register: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md ; source blob 16313187f92ef25bce6c4a83bba36d5b74399de7

Open source issues OW-Q01–OW-Q06: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/references/source-and-assumptions.md ; source blob 98fa0891714fbf52d5813e6eb517f936e4bc681e. Do not combine alternate enterprise footprints, asset populations or unvalidated financial benefits. Source-scoped persona designation differences remain unresolved; no merger is implied.

References reviewed 31 October 2026 IST: Materials HR01–HR12 index and Energy HR01. Energy supplies the one-card learning pattern; this edition uses the requested closed history and separate AI scenario windows.

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR07-APE7-Architecting-Autonomous-Payroll-Enterprises/03-HR07-IND-industrials/0-The-Origin-Story/sprint/industrials-hr07-origin-evolution-sprint.md

Native Google Doc: https://docs.google.com/document/d/1e-fuEeJlgYqmuc5_ZTFwVM2hqmgH6VYi-XcnEPLszq8/edit?usp=drivesdk

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/industrials-origin-stories.md

Matching content is explicitly published and read back; no automatic synchronization, public student access or successful copying is established. End of HR07 Origin Story edition.
