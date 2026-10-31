# HR12 — Connected HR Enterprises: The Origin Story

SuccessLabs Academy · GICS04 Consumer Discretionary · OmniVibe Consumer Ltd. · IIL — Industry Immersion Lab · Level 0 → Pre-Foundation · Sprint · 120 minutes · Edition 2026-10-31

Mission: Architecting Experiences for a Better World.

## 1. One learner promise

Trace one workforce change across applications without confusing event delivery with approved and completed business outcomes.

Produce one Connected Workforce Handoff Build Card using synthetic records and a paper prototype. Beginners explain the decision in plain language; experienced learners challenge its assumptions. Configuration, deeper research and optional vendor comparisons stay in the supporting case outside this sprint.

## 2. Source boundaries

OmniVibe is a fictional consumer group: 72,000 employees across 48 countries; 3,200 owned/franchise stores, 14 e-commerce sites, 26 DCs and 140 micro-fulfillment locations. These are source-stipulated baselines, not verified operations. Franchise inclusion in employee counts and employer authority remain unresolved (OVC-Q04); no site-level rules or benefits are invented. Product names in the case are proposals, not verified deployments or current capability guarantees.

The request also says Industrials/GICS03 and links the Materials index. Existing records identify GICS04 as OmniVibe Consumer Discretionary. This edition follows that explicit publication destination and uses GICS03 as design reference; the inconsistent Industrials wording is recorded rather than imported as enterprise fact.

Existing anchors: OVC-M09–OVC-M12 (capabilities, value streams, operating model, architecture), OVC-M17–OVC-M19 (risk, adoption, pilot readiness), and OVC-SIM-07 and OVC-SIM-05. These are supporting case anchors, not already executed tests. All OVC-TOS-HR12 identifiers below are newly introduced educational IDs. Existing OVC-P persona identities are preserved.

## 3. Origins and process evolution

The five closed windows are educational groupings, not universal invention dates or OmniVibe's corporate biography (the source gives its founding as 1992). Adoption overlaps; older practices can coexist through the present. Ask what problem each response solved and what it left unresolved.

1970–1984 — Paper change notices coordinate departments; receipt and execution can be unclear.

1985–1994 — Batch files standardize exchange; file delivery still does not prove applied records.

1995–2004 — ERP interfaces and middleware reduce rekeying; field semantics and rejection handling remain difficult.

2005–2014 — Services and APIs improve reuse; synchronous success cannot guarantee every business outcome.

2015–2025 — API/event-aware platforms and monitoring improve orchestration; duplicates, ordering, privacy and target reconciliation remain design obligations.

Recall: reconstruct problem → process/application response → unfinished problem. Which old failure could survive in a modern system?

## 4. One persona-led dilemma

Lead: Jonas Lim, Integration and HR Data Lead (OVC-P12). Counterpart: Priya Shah, Director Enterprise Architecture (OVC-P11). These established personas are fictional. The following incident, record IDs and reveals are new synthetic teaching additions.

Scene 1 — Jonas follows a synthetic owned-store reassignment into time, payroll and access services. The integration dashboard is green but the receiving store still cannot confirm the associate's approved access. The business problem is a reliable handoff and recovery, before an API or event choice.

Scene 2 — Choose point-to-point copies, one large synchronous transaction or versioned contracts with per-target business reconciliation. Reveal: an assignment ended at the old store while employment remains active. Treating assignment-end as termination would remove legitimate access and distort pay.

Scene 3 — Farah Ahmed, CISO and Privacy Lead (OVC-P13), reveals that a commerce consumer requested salary data and a franchise target has unclear authority. Jonas revises the contract to minimum necessary fields, explicit purpose and target-specific approval. Priya requires a recovery condition rather than a blanket replay.

Decision pause: record your first choice before the reveal, then revise it. Name one fact that would make the alternative better.

## 5. Responsibilities and decision rights

HR core owns approved person, employment and assignment facts. Time owns accepted time context; Payroll owns pay-impact acceptance; IAM/security owns approved entitlements; each store operator owns authorized local execution. Integration owns transport, contract validation, observable state and recovery coordination, not HR truth or target business approval. Priya governs architecture; Jonas operates contract design; data/security owners approve permitted fields. SAP Integration Suite/BTP is an illustrative platform proposal; select API, event or scheduled batch per evidence.

Frame the business rule and accountable owner before selecting technology. Source proposals do not authorize data sharing, sensitive transactions or autonomous decisions. Keep an accessible human exception and worker challenge route.

## 6. The 120-minute learning arc

0–10 — Read the promise and state the worker/business problem.

10–30 — Reconstruct the five historical windows and their unfinished problems.

30–50 — Play the scenes; record an initial choice, reveal evidence and revise.

50–65 — Draw application responsibilities, data ownership and human decision rights.

65–95 — Complete the one build card, compare alternatives and explore the three future scenarios; scan only a resource that answers your question.

95–115 — Perform exactly the three tabletop tests below on the paper design and record observations.

115–120 — Explain the decision in 60 seconds, reflect and hand off to Pre-Foundation. Total: 120 minutes.

## 7. One build card — Connected Workforce Handoff Build Card

Synthetic experiment (OVC-TOS-HR12-EXP01): Synthetic event SYN-EVT1200 v2 ends assignment SYN-A01 and starts SYN-A02 on 1 November 2026; employment SYN-E1200 remains active. Three consumers show accepted, rejected and unknown states. Model event ID, business key, version, effective time, schema, allowed fields and each target's confirmation/recovery route.

Fill nine fields on one page: purpose/person affected; current and proposed state with source evidence; object/identity definitions; business date/time and version; application and data owners; human approval and challenge route; chosen option versus alternative and trade-off; exception/fallback and automation boundary; three test observations and your revision.

Unknown country, brand, franchise, device, policy and authority conditions need an owner and discovery question. Use no real personal data. Consider learning access, workload, service continuity and avoidable rework where evidence supports them; do not infer financial or environmental savings.

## 8. Exactly three tabletop tests

### OVC-TOS-HR12-T01 — Rejection or unavailable target

Reveal/input: HR approved the change; payroll rejects it and access status is unknown.

Expected design response: Expose per-target business state and owner; reconcile safe fallback and do not mark the entire workforce journey complete from transport success.

### OVC-TOS-HR12-T02 — Duplicate and reordered events

Reveal/input: Version 2 arrives twice, followed by version 1.

Expected design response: Use defined idempotency and ordering/version rules; preserve audit evidence and avoid undoing a later approved state or duplicating a business effect.

### OVC-TOS-HR12-T03 — Bad schema and unsafe replay

Reveal/input: A payload carries an unauthorized salary field and ambiguous assignment-end meaning.

Expected design response: Reject or quarantine with accountable correction, minimize fields and confirm assignment versus employment semantics before authorized replay; do not blindly resend.

For each, record input → expected response → actual observed paper response → evidence note → pass/revise. These expected responses are proposed acceptance criteria. Publication executes none of the tests; all observation slots start unfilled. A bypass of a protected decision calls for redesign, even if the card is complete.

## 9. Traceability and honest measures

OVC-TOS-HR12-REQ01 — Preserve workforce meaning, version and target-specific business evidence. Source connection: HR case focus, OVC-M09–OVC-M12 and OVC-SIM-07 and OVC-SIM-05. Acceptance: T01–T02; identify authoritative evidence, owner and revision.

OVC-TOS-HR12-REQ02 — Control field sharing, duplicate effects and accountable recovery. Source connection: OVC-M17–OVC-M19. Acceptance: T02–T03; identify the protected decision, exception and recovery condition.

OVC-TOS-HR12-ADR01 — Proposed educational choice: Versioned minimum-data contracts with per-target reconciliation rather than unrestricted point-to-point replication; compare API, event and scheduled batch by timeliness and recoverability. Learners may reject it with evidence; it is not a client-approved architecture decision.

OVC-TOS-HR12-EXP01 — The single card experiment extends the existing case's bounded-pilot discipline; T01–T03 do not complete the wider case's experiments or implementation tests.

OVC-TOS-HR12-M01 — Mandatory card fields completed / 9 × 100: learning completeness only. OVC-TOS-HR12-M02 — Record whether each proposed acceptance criterion survives its evidence reveal; record observed paper results separately from expectations. Real baselines and targets remain TBD.

OVC-TOS-HR12-EV01 — Initially unfilled evidence slot for the three observations, revised choice and reviewer questions. No achieved operational result, realized saving or executed system test is claimed.

## 10. AI-driven exploration — scenarios, not predictions

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. Each requires approved purpose, evidence, worker participation, proportionate safeguards and accountable human decisions.

2026–2030 — Assist: Explain contract failures and draft recovery questions.

2031–2040 — Connect: Connect versioned business evidence across authorized HR and store services.

2041–2050 — Adapt: Suggest contract or routing adaptations as partners change; humans approve semantics, sharing and recovery authority.

Competing future: A controlled scheduled batch with clear reconciliation may outperform event-driven complexity when consumers cannot confirm or safely replay changes.

Disconfirmation question: Would event-aware integration reduce unresolved business handoffs without increasing duplicate effects, privacy exposure or recovery effort? State the observation that would make you stop, revise or prefer the competing future.

## 11. Reflection and Pre-Foundation handoff

Which system owns the fact and which owns the effect? What evidence makes replay safe?

Define business event, contract, schema, idempotency, ordering, acknowledgement and business reconciliation; carry one consumer recovery path into Pre-Foundation.

Carry the same card, open questions and proposed acceptance criteria forward. Deeper implementation material and the wider capstone remain outside this Origin Story.

## 12. A few official resources

NIST AI Risk Management Framework — Which evidence gap or oversight boundary limits your proposed assistance? https://www.nist.gov/itl/ai-risk-management-framework

ISO/IEC 27001 overview — Which information risk and accountable owner must the card expose? https://www.iso.org/standard/27001

W3C WCAG 2.2 — Can the worker complete or challenge the journey with assistive technology or a shared device? https://www.w3.org/TR/WCAG22/

Educational alignment: TOGAF — business-led options and architecture decisions; BIZBOK — capability/value-stream relationships; BABOK — elicitation, requirements and acceptance; DAMA-DMBOK — data ownership, quality and lineage; COBIT — accountability and control evidence; relevant ISO/IEC information-risk principles — proportionate safeguards and review. No certification, conformity or compliance is claimed.

Separate classification axes: HR theme = HR12 Connected HR Enterprises; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain, Industry; enterprise transformation stream = Workforce. The twelve HR themes include thirteen source cases because HR02a and HR02b remain separate sources.

## Source and companion record

Supporting HR source and matching sprint location: https://app.notion.com/p/3d0ce6de608981da91b8daecec2b789f?pvs=204

Enterprise hub: https://app.notion.com/p/5a1022d7db634a10a7c5d00318e0c809?pvs=204

derived-streams/01-workforce.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/derived-streams/01-workforce.md ; reviewed source blob 289c5c3a994a4b6defe2e5b38018e82aca67d99a

personas/persona-cards.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/personas/persona-cards.md ; reviewed source blob 7a60f95f3935b6650eab4650ff235f33a6cf8322

master/theme-c-architecture.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/master/theme-c-architecture.md ; reviewed source blob 6c3198254dfc8364d213dc3a556d2c248ac9eab5

master/theme-e-execution.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/master/theme-e-execution.md ; reviewed source blob 472ec079b9bfd5135b57ac00aec85b996f7f9582

simulations/scenario-scripts.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/simulations/scenario-scripts.md ; reviewed source blob 03f1bb77d5b0e326a7434d56cf9118ae91e5a6d5

references/source-and-assumptions.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/references/source-and-assumptions.md ; reviewed source blob d6d9bcafecd8b62df96c383fec185ac304ad9d9e

Open gaps OVC-Q01–OVC-Q14 remain in the source register: franchise/accountability boundary, customer definition, benefit baselines, source label variants, maturity rubric and product/localization claims are not silently resolved. Source outcome prose is intended architecture, not achieved evidence.

Design reference: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/industrials-origin-stories.md ; supplied Materials reference also reviewed.

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR12-AIG2-Architecting-Connected-HR-Enterprises/04-HR12-CD-consumer-discretionary/0-The-Origin-Story/sprint/consumer-discretionary-hr12-origin-evolution-sprint.md

Native Google Doc: https://docs.google.com/document/d/1tpcgzPhe-PvmU9Wmj5tqgXT_cNU9vJ19dHFTE71P4eE/edit?usp=drivesdk

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/consumer-discretionary-origin-stories.md

End of HR12 Origin Story edition. Saved-content verification is recorded separately in the sector index after readback. Automatic synchronization, public student access, successful copying and executed tabletop results are not established.
