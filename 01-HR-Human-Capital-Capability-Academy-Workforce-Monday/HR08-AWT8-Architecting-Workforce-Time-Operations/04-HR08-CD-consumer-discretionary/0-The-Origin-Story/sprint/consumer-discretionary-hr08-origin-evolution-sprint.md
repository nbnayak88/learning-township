# HR08 — Workforce Time & Operations: The Origin Story

SuccessLabs Academy · GICS04 Consumer Discretionary · OmniVibe Consumer Ltd. · IIL — Industry Immersion Lab · Level 0 → Pre-Foundation · Sprint · 120 minutes · Edition 2026-10-31

Mission: Architecting Experiences for a Better World.

## 1. One learner promise

Explain one shift-time exception without confusing a schedule, captured event, approved time or payroll-ready input.

Produce one Shift-Time Decision Build Card using synthetic records and a paper prototype. Beginners explain the decision in plain language; experienced learners challenge its assumptions. Configuration, deeper research and optional vendor comparisons stay in the supporting case outside this sprint.

## 2. Source boundaries

OmniVibe is a fictional consumer group: 72,000 employees across 48 countries; 3,200 owned/franchise stores, 14 e-commerce sites, 26 DCs and 140 micro-fulfillment locations. These are source-stipulated baselines, not verified operations. Franchise inclusion in employee counts and employer authority remain unresolved (OVC-Q04); no site-level rules or benefits are invented. Product names in the case are proposals, not verified deployments or current capability guarantees.

The request also says Industrials/GICS03 and links the Materials index. Existing records identify GICS04 as OmniVibe Consumer Discretionary. This edition follows that explicit publication destination and uses GICS03 as design reference; the inconsistent Industrials wording is recorded rather than imported as enterprise fact.

Existing anchors: OVC-M09–OVC-M12 (capabilities, value streams, operating model, architecture), OVC-M17–OVC-M19 (risk, adoption, pilot readiness), and OVC-SIM-02 and OVC-SIM-05. These are supporting case anchors, not already executed tests. All OVC-TOS-HR08 identifiers below are newly introduced educational IDs. Existing OVC-P persona identities are preserved.

## 3. Origins and process evolution

The five closed windows are educational groupings, not universal invention dates or OmniVibe's corporate biography (the source gives its founding as 1992). Adoption overlaps; older practices can coexist through the present. Ask what problem each response solved and what it left unresolved.

1970–1984 — Rosters and paper time sheets coordinate coverage; planned time can be mistaken for actual work.

1985–1994 — Time clocks and structured shift registers improve capture; missed punches still need human evidence.

1995–2004 — Digital time/payroll rules improve valuation; wrong calendars or intervals can distort results.

2005–2014 — Employee time self-service and approvals improve corrections; schedule, absence and actual events can still disagree.

2015–2025 — Cloud time tools and mobile capture improve visibility; overnight semantics, fair scheduling and downstream correction remain governed decisions.

Recall: reconstruct problem → process/application response → unfinished problem. Which old failure could survive in a modern system?

## 4. One persona-led dilemma

Lead: Oliver Brooks, Store Operations Director (OVC-P06). Counterpart: Nadia Rahman, Global Payroll Director (OVC-P05). These established personas are fictional. The following incident, record IDs and reveals are new synthetic teaching additions.

Scene 1 — Oliver faces a fictional evening promotion spanning store closing and micro-fulfillment work. A synthetic associate's exit event is missing after midnight. Nadia needs approved time; assuming either zero hours or the planned shift would risk pay accuracy.

Scene 2 — Choose the planned schedule as actual time, hold the entire team or investigate the affected record with worker confirmation and authorized correction. Reveal: the clock timestamp is in a different zone from the store roster. A calendar-day total hides the overnight interval.

Scene 3 — Nikhil Das, Store Associate and Workforce Representative (OVC-P16), reports an approved absence that the replacement plan ignored. Oliver revises coverage and time handling separately. Attendance does not establish skill readiness, and a time correction after payroll submission needs a controlled downstream adjustment.

Decision pause: record your first choice before the reveal, then revise it. Name one fact that would make the alternative better.

## 5. Responsibilities and decision rights

Scheduling/Operations owns planned coverage; Time owners govern captured events, approved corrections and valuation inputs; Absence owners govern approved leave; Payroll owns accepted inputs and recalculation. Learning owners provide role-readiness evidence. Oliver's delegated manager approves coverage and time corrections with worker participation; Nadia controls payroll acceptance. SAP Time Tracking illustrates time capture/valuation, not an assumed complete scheduling or optimization solution.

Frame the business rule and accountable owner before selecting technology. Source proposals do not authorize data sharing, sensitive transactions or autonomous decisions. Keep an accessible human exception and worker challenge route.

## 6. The 120-minute learning arc

0–10 — Read the promise and state the worker/business problem.

10–30 — Reconstruct the five historical windows and their unfinished problems.

30–50 — Play the scenes; record an initial choice, reveal evidence and revise.

50–65 — Draw application responsibilities, data ownership and human decision rights.

65–95 — Complete the one build card, compare alternatives and explore the three future scenarios; scan only a resource that answers your question.

95–115 — Perform exactly the three tabletop tests below on the paper design and record observations.

115–120 — Explain the decision in 60 seconds, reflect and hand off to Pre-Foundation. Total: 120 minutes.

## 7. One build card — Shift-Time Decision Build Card

Synthetic experiment (OVC-TOS-HR08-EXP01): SYN-P800 has a planned shift 20:00–02:00 local time, one entry event and no exit event. Device zone differs from roster zone; an absence and a replacement candidate are also shown. No country working-time rule or automatic pay deduction is supplied. Record the questions and authorized correction path.

Fill nine fields on one page: purpose/person affected; current and proposed state with source evidence; object/identity definitions; business date/time and version; application and data owners; human approval and challenge route; chosen option versus alternative and trade-off; exception/fallback and automation boundary; three test observations and your revision.

Unknown country, brand, franchise, device, policy and authority conditions need an owner and discovery question. Use no real personal data. Consider learning access, workload, service continuity and avoidable rework where evidence supports them; do not infer financial or environmental savings.

## 8. Exactly three tabletop tests

### OVC-TOS-HR08-T01 — Cross-midnight missing event

Reveal/input: The exit is absent and device/store zones differ.

Expected design response: Preserve raw event and zone context; seek worker/manager evidence and an approved correction rather than infer zero work or copy planned hours.

### OVC-TOS-HR08-T02 — Absence and service cover

Reveal/input: The roster assigns an absent associate and a replacement with unverified role readiness.

Expected design response: Reconcile absence and feasible qualified cover separately; a roster entry does not prove availability or competence.

### OVC-TOS-HR08-T03 — Correction after submission

Reveal/input: Corrected time arrives after payroll input acceptance.

Expected design response: Version and authorize the correction, notify the payroll owner and reconcile the adjustment route; do not silently mutate the accepted input.

For each, record input → expected response → actual observed paper response → evidence note → pass/revise. These expected responses are proposed acceptance criteria. Publication executes none of the tests; all observation slots start unfilled. A bypass of a protected decision calls for redesign, even if the card is complete.

## 9. Traceability and honest measures

OVC-TOS-HR08-REQ01 — Keep schedule, absence, captured time and approved time semantically distinct. Source connection: HR case focus, OVC-M09–OVC-M12 and OVC-SIM-02 and OVC-SIM-05. Acceptance: T01–T02; identify authoritative evidence, owner and revision.

OVC-TOS-HR08-REQ02 — Protect worker correction rights and controlled payroll handoffs. Source connection: OVC-M17–OVC-M19. Acceptance: T02–T03; identify the protected decision, exception and recovery condition.

OVC-TOS-HR08-ADR01 — Proposed educational choice: Evidence-led exception handling and separately approved coverage rather than using the planned roster as actual time. Learners may reject it with evidence; it is not a client-approved architecture decision.

OVC-TOS-HR08-EXP01 — The single card experiment extends the existing case's bounded-pilot discipline; T01–T03 do not complete the wider case's experiments or implementation tests.

OVC-TOS-HR08-M01 — Mandatory card fields completed / 9 × 100: learning completeness only. OVC-TOS-HR08-M02 — Record whether each proposed acceptance criterion survives its evidence reveal; record observed paper results separately from expectations. Real baselines and targets remain TBD.

OVC-TOS-HR08-EV01 — Initially unfilled evidence slot for the three observations, revised choice and reviewer questions. No achieved operational result, realized saving or executed system test is claimed.

## 10. AI-driven exploration — scenarios, not predictions

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. Each requires approved purpose, evidence, worker participation, proportionate safeguards and accountable human decisions.

2026–2030 — Assist: Explain time exceptions and draft questions without inventing missing punches.

2031–2040 — Connect: Connect schedule, absence, readiness and payroll status through authorized contracts.

2041–2050 — Adapt: Suggest changing coverage patterns with worker participation; humans retain time approval and acceptable-workload decisions.

Competing future: Predictable rosters with simple correction support may deliver fairer work than continual AI schedule changes.

Disconfirmation question: Would the proposed automation improve time accuracy and worker control, or increase unexplained corrections and unstable shifts? State the observation that would make you stop, revise or prefer the competing future.

## 11. Reflection and Pre-Foundation handoff

Which clock does the interval use? Why should coverage readiness and pay correction be decided separately?

Define planned shift, time event, zone, absence, approved time and payroll input; map one overnight correction.

Carry the same card, open questions and proposed acceptance criteria forward. Deeper implementation material and the wider capstone remain outside this Origin Story.

## 12. A few official resources

NIST AI Risk Management Framework — Which evidence gap or oversight boundary limits your proposed assistance? https://www.nist.gov/itl/ai-risk-management-framework

ISO/IEC 27001 overview — Which information risk and accountable owner must the card expose? https://www.iso.org/standard/27001

W3C WCAG 2.2 — Can the worker complete or challenge the journey with assistive technology or a shared device? https://www.w3.org/TR/WCAG22/

Educational alignment: TOGAF — business-led options and architecture decisions; BIZBOK — capability/value-stream relationships; BABOK — elicitation, requirements and acceptance; DAMA-DMBOK — data ownership, quality and lineage; COBIT — accountability and control evidence; relevant ISO/IEC information-risk principles — proportionate safeguards and review. No certification, conformity or compliance is claimed.

Separate classification axes: HR theme = HR08 Workforce Time & Operations; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain, Industry; enterprise transformation stream = Workforce. The twelve HR themes include thirteen source cases because HR02a and HR02b remain separate sources.

## Source and companion record

Supporting HR source and matching sprint location: https://app.notion.com/p/3d0ce6de60898194888ad5a90ac9736c?pvs=204

Enterprise hub: https://app.notion.com/p/5a1022d7db634a10a7c5d00318e0c809?pvs=204

derived-streams/01-workforce.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/derived-streams/01-workforce.md ; reviewed source blob 289c5c3a994a4b6defe2e5b38018e82aca67d99a

personas/persona-cards.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/personas/persona-cards.md ; reviewed source blob 7a60f95f3935b6650eab4650ff235f33a6cf8322

master/theme-c-architecture.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/master/theme-c-architecture.md ; reviewed source blob 6c3198254dfc8364d213dc3a556d2c248ac9eab5

master/theme-e-execution.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/master/theme-e-execution.md ; reviewed source blob 472ec079b9bfd5135b57ac00aec85b996f7f9582

simulations/scenario-scripts.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/simulations/scenario-scripts.md ; reviewed source blob 03f1bb77d5b0e326a7434d56cf9118ae91e5a6d5

references/source-and-assumptions.md: https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/references/source-and-assumptions.md ; reviewed source blob d6d9bcafecd8b62df96c383fec185ac304ad9d9e

Open gaps OVC-Q01–OVC-Q14 remain in the source register: franchise/accountability boundary, customer definition, benefit baselines, source label variants, maturity rubric and product/localization claims are not silently resolved. Source outcome prose is intended architecture, not achieved evidence.

Design reference: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/industrials-origin-stories.md ; supplied Materials reference also reviewed.

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR08-AWT8-Architecting-Workforce-Time-Operations/04-HR08-CD-consumer-discretionary/0-The-Origin-Story/sprint/consumer-discretionary-hr08-origin-evolution-sprint.md

Native Google Doc: https://docs.google.com/document/d/19b-uMlKeTGMFVinraKpvXg9BNXWjmLPEKbU5MtxXCmE/edit?usp=drivesdk

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/consumer-discretionary-origin-stories.md

End of HR08 Origin Story edition. Saved-content verification is recorded separately in the sector index after readback. Automatic synchronization, public student access, successful copying and executed tabletop results are not established.
