# HR08 — Workforce Time & Operations: The Origin Story

SuccessLabs Academy · GICS03 Industrials · OmniWorks Industrial Systems Ltd. · IIL — Industry Immersion Lab · Level 0 → Pre-Foundation · Sprint · 120 minutes · Edition 2026-10-31

Mission: Architecting Experiences for a Better World.

## 1. Your one promise

Design one shutdown shift-time decision that preserves accurate pay inputs, worker rest and an auditable correction path.

Produce one Shutdown Time Decision Build Card. Use synthetic records and a paper prototype. Beginners explain the decision in plain language; experienced learners challenge the same decision's assumptions. Configuration and implementation research remain in the supporting case outside this sprint.

## 2. Read the enterprise and sources accurately

OmniWorks is fictional: 74,000 employees, 36 countries, 61 manufacturing/engineering/assembly facilities and 320 service depots. The 61 is a mixed-facility count, not a confirmed plant-only count. Engineering, maintenance, production and field service shape the workforce problem. Case targets and victory criteria are aspirations, not achieved results. This edition adds a bounded synthetic episode; it does not assert a deployment.

Source-scoped lead: Vikram Desai, Global Workforce Time Product Director. The source describes repeated excessive maintenance hours during a shutdown and requests to override controls. Monika Bauer, Maintenance Supervisor; Idris Bello, Maintenance Technician Persona; Claire Dubois, Labor Relations and Privacy Counsel; and Akira Mori, Payroll Integration Lead retain their case roles. No country working-time limit or collective-agreement interpretation is invented.

Existing enterprise anchors: OW-M17 — risk/security; OW-M18 — workforce/adoption; OW-M19 — delivery readiness. The workforce blueprint also inherits OW-M03, OW-M09 and OW-M11. Keep those IDs unchanged. New IDs prefixed OW-TOS-HR08 are educational additions, not previously approved client requirements.

## 3. Origins: five closed historical teaching windows

These windows group teaching ideas, not universal invention dates or OmniWorks corporate biography. Adoption overlaps; older practices can coexist through the present. Each generation changes the medium without automatically resolving ownership, evidence or authority.

1970–1984 — Timebooks and foreman approvals record hours for wages; missed entries and invisible overtime undermine trust.

1985–1994 — Clock terminals and shift rosters improve attendance capture; presence does not prove payable classification or safe assignment.

1995–2004 — Time evaluation and payroll interfaces automate premiums; the wrong rule or date can spread errors.

2005–2014 — Electronic absence and mobile/project entry support varied work; travel, customer-site time and cross-midnight shifts complicate meaning.

2015–2025 — Cloud time and fatigue alerts improve exception visibility; an alert requires verified inputs and accountable action, not hidden tracking or silent overrides.

Recall prompt: reconstruct the five responses as problem → process/application response → unfinished problem. Which old failure could survive in the newest system?

## 4. One persona-led dilemma

### Scene 1

Vikram reviews the shutdown roster with Monika. Production needs maintenance completed, but Idris asks whether his hours and rest are accurately represented.

### Scene 2

Reveal: a cross-midnight clock-out is missing in the synthetic record. Assuming zero work would understate pay; assuming an unlimited shift would distort fatigue. Vikram retains the raw record and asks for worker/supervisor verification.

### Scene 3

Claire challenges the request to override the rest warning. Akira needs approved time before payroll cutoff. The team separates capture, payable classification, scheduling permission and the safety response.

### Scene 4

Vikram revises the card: document a correction, retain evidence and approval, seek a rested qualified replacement or reschedule affected work through authorized operations. No payroll adjustment is silently made to hide a roster problem.

Decision pause: Extend the same worker, use a verified qualified replacement, or reschedule work. What confirmed rule, capacity and employee evidence would change the choice?

## 5. Responsibilities, ownership and human authority

Time capture (device/time service owner): original clock events with timezone and device/source reference; no inferred location tracking beyond approved purpose.

Time/absence service (time policy owner): validated records, schedules, absence, rule versions, approvals and corrections; SAP Time Tracking/Time Off are examples.

Scheduling/operations (operations owner): planned staffing and work assignments; site safety/authorized operations applies confirmed rest/safety constraints.

Payroll (payroll owner): accepted approved time inputs and calculated pay; source correction and payroll acceptance remain distinct.

Idris can challenge records; authorized supervisor/time approver confirms corrections. Claire advises on applicable rules/privacy; authorized operations decides safe work arrangements.

Design boundary: Do not erase worked time, invent a statutory threshold, or let an alert/manager override silently authorize unsafe work. Proposed responsibilities are learning architecture, not proof that the fictional enterprise already operates this design. Select technology only after the business rule and accountable owner are clear. SAP examples illustrate capabilities, not mandatory product choices.

## 6. Exactly 120 minutes

0–10: Read the promise and dilemma; state the worker and business outcome in two sentences.

10–30: Reconstruct the five historical windows; explain what each process improvement left unresolved.

30–50: Play the scenes and reveal the evidence in order; record your first choice and revised reasoning.

50–65: Draw the responsibility/ownership map; name the human decision right and exception route.

65–95: Complete the one build card; compare two options and explore the three future scenarios. Scan only the resource relevant to your uncertainty.

95–115: Perform the three tabletop tests below; record observed paper results and revise the same card.

115–120: Explain your decision in 60 seconds, reflect, and carry the card into Pre-Foundation. Total: 120 minutes.

## 7. One build card: Shutdown Time Decision Build Card

Synthetic experiment: SYN-SHIFT801 spans 31 October 22:00 to 1 November 06:00 in a declared synthetic site timezone, but its clock-out is absent. Payroll already accepted V1; a proposed V2 correction arrives later. The roster contains a rest warning whose applicable rule must be discovered.

Fill these nine fields on one page: purpose and affected person; current/proposed state and source evidence; identity/object definitions; business date/time and version; application/data owners; human approval and appeal route; chosen option versus alternative with trade-off; exception/fallback and automation boundary; three test observations and revision.

Minimum design reasoning: Separate date/timezone, raw event, evaluated duration, payable classification and authorization. Preserve versioned corrections and acknowledge payroll acceptance; use the approved country correction route after cutoff.

Do not invent country rules, safety thresholds, collective-agreement terms, live data or missing approvals. Record unknowns with an owner and discovery question. Support an accessible human route for the worker. Consider fatigue, learning opportunity, avoidable travel/rework or resource use where the dilemma provides evidence; do not infer environmental savings.

## 8. Exactly three tabletop tests

### OW-TOS-HR08-T01 — Cross-midnight gap

Reveal/input: Clock-in exists but clock-out is missing.

Expected design response: Keep duration unknown until verified, retain original events and reason/approver, and do not equate missing event with no work.

### OW-TOS-HR08-T02 — Rest override

Reveal/input: Monika requests extended duty and a replacement has no verified task qualification.

Expected design response: Escalate to authorized operations/safety, hold the unsafe/unsupported assignment and evaluate qualified cover or rescheduling.

### OW-TOS-HR08-T03 — Post-cutoff correction

Reveal/input: V2 is approved after payroll accepted V1; resend could duplicate hours.

Expected design response: Identify prior accepted version, transmit/reconcile the controlled correction under the approved route and keep pay-impact status visible.

For each test, record input → expected response → actual observed paper response → evidence note → pass/revise. Expected responses are proposed acceptance criteria, not executed results. Publication executes none of these tabletop tests. A bypass of the protected decision requires redesign, even if the card is complete.

## 9. Traceability and honest measures

OW-TOS-HR08-REQ01 — Preserve raw events and explain approved, versioned time evaluation/corrections. Source connection: supporting HR case mandate and OW-M18. Assessed by T01; card must identify the authoritative fact and owner.

OW-TOS-HR08-REQ02 — Separate pay accuracy from scheduling/rest authority and reconcile downstream corrections. Source connection: HR case governance/scenario injection and OW-M17/OW-M19. Assessed by T02–T03; card records exception, authority and recovery condition.

OW-TOS-HR08-ADR01 — Prefer common time semantics with workforce-pattern variants over one rigid clocking process; compare administrative effort against plant/field fit and privacy. Compare the stated alternative and trade-off; this is a proposed educational decision that learners may reject with evidence.

OW-TOS-HR08-EXP01 — this synthetic card and T01–T03 extend OW-M19's traceable-pilot discipline. They do not complete the wider case's tests or rollout.

OW-TOS-HR08-M01 — completed mandatory card fields / 9 × 100; learning completeness only. OW-TOS-HR08-M02 — Record whether original/corrected versions, date semantics and rest decision remain explicit; no actual hours compliance or payroll outcome is claimed. No baseline, target attainment or operating benefit is inferred from an empty result.

OW-TOS-HR08-EV01 — initially unfilled evidence slot for observed tabletop results, revisions and reviewer questions. Existing case success metrics remain separate planned outcomes.

## 10. AI-driven exploration: scenarios, not predictions

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. All require approved purpose, evidence, worker participation, accountable ownership and proportionate controls.

2026–2030 — Assist: Assistance could identify missing clock events and explain correction steps without inventing hours.

2031–2040 — Connect: Connected scheduling, time and qualification evidence could identify coverage options under approved rules.

2041–2050 — Adapt: Adaptive rosters could propose resilient shutdown arrangements, retaining worker participation, review and accountable safety authority.

Competing future: Simpler rosters with stronger staffing buffers may reduce fatigue more effectively than increasingly detailed monitoring.

Disconfirmation question: Would the proposed alert/rostering model increase intrusive tracking or leave repeated rest risks unresolved? Record the evidence that would make you stop or change the hypothesis.

## 11. Reflection and Pre-Foundation handoff

Why can accurate pay and safe scheduling require different decisions? Which missing event changed your assumption? How does Idris correct his record?

Pre-Foundation: Define schedule, raw time event, evaluated time, absence, premium, correction and payroll acceptance; establish timezone and rule ownership first. Carry forward the same card, unresolved questions and proposed acceptance criteria. Deeper implementation, vendor comparisons and the wider capstone stay outside this Origin Story.

## 12. Official resources: choose with a question

NIST AI Risk Management Framework — Which harm, evidence gap or oversight boundary would prevent your proposed assistance from expanding? https://www.nist.gov/itl/ai-risk-management-framework

ISO/IEC 27001 overview — What information risk, accountable owner and review evidence must your design make visible? https://www.iso.org/standard/27001

W3C WCAG 2.2 — Could a worker use the digital journey with keyboard/assistive technology or a shared device, and what needs user testing? https://www.w3.org/TR/WCAG22/

Educational alignment: TOGAF — business-led options and decisions; BIZBOK — capability/value-stream relationships; BABOK — elicitation, requirements and acceptance; DAMA-DMBOK — data ownership, quality and lineage; COBIT — accountability and control evidence; ISO/IEC 27001 principles — information-risk management; ISO 9001/ISO 45001 principles where relevant — quality and worker participation/safety. No certification, conformity or compliance is claimed.

Classification axes remain separate: HR theme = HR08 Workforce Time & Operations; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry, applied as distinct views; enterprise transformation stream = Workforce. These are related axes, not interchangeable stream lists.

## Source and companion record

Supporting HR source: https://app.notion.com/p/7ca6ee9db393464ab321a7103c35fd6e

Enterprise hub: https://app.notion.com/p/d1579523dadb48fea5a6319f072ef755

Workforce blueprint: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/derived-streams/01-workforce.md ; source blob 22f877c403a461b6321cdd484ca9c7d06faf0a8b

Readiness/risk/workforce anchors: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/master/theme-e-execution.md ; source blob 454199f06f9496bd8ca31a190475fbec814e2873

Persona register: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md ; source blob 16313187f92ef25bce6c4a83bba36d5b74399de7

Open source issues OW-Q01–OW-Q06: https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/references/source-and-assumptions.md ; source blob 98fa0891714fbf52d5813e6eb517f936e4bc681e. Do not combine alternate enterprise footprints, asset populations or unvalidated financial benefits. Source-scoped persona designation differences remain unresolved; no merger is implied.

References reviewed 31 October 2026 IST: Materials HR01–HR12 index and Energy HR01. Energy supplies the one-card learning pattern; this edition uses the requested closed history and separate AI scenario windows.

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR08-AWT8-Architecting-Workforce-Time-Operations/03-HR08-IND-industrials/0-The-Origin-Story/sprint/industrials-hr08-origin-evolution-sprint.md

Native Google Doc: https://docs.google.com/document/d/10BDy6YwOC5pyA9OA7weLwoqJt04Y4dEW-9YJTXM9LoA/edit?usp=drivesdk

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/industrials-origin-stories.md

Matching content is explicitly published and read back; no automatic synchronization, public student access or successful copying is established. End of HR08 Origin Story edition.
