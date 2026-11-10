# The service survey is green; the same fault keeps returning
## CRM06 — Architecting Exceptional Customer Experiences

**SuccessLabs Academy · OmniWorks Industrial Systems Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-CRM06-IND-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one customer-feedback experiment that turns a real friction point into a verified improvement decision.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

Field service closes tickets quickly and surveys are positive, yet a transport customer's reliability lead sees the same fault on the same component. A proposal would reward technicians for closure speed.

**Lead:** Isabel Torres — Chief Customer & Service Officer (OW-P09).  
**Counterpart:** Hannah Fischer — Director, Enterprise Architecture (OW-P11).  
**Customer voice:** Elena Brooks — VP Asset Reliability, Transport Customer (OW-P13).

Isabel Torres asks what must be true before the team decides. Hannah Fischer asks which evidence and owner support the decision. Elena Brooks asks for the outcome that matters to the people affected.

**Evidence reveal:** The synthetic ticket closed with a workaround while the root-cause part order stayed open, and the survey asked only about technician courtesy. Resolution, not speed or courtesy, becomes the measure under test.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniWorks Industrial Systems Ltd. is an aspirational case study (USD 48B revenue; 74,000 employees; 36 countries; 61 plants and facilities; 320 service depots; 7,200 suppliers). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniWorks Industrial Systems Ltd. history.

- **1970s–1980s:** Relationship managers learn from conversations; difficult experiences may stay invisible.
- **1980s–1990s:** Surveys and loyalty programs quantify response; selection bias and incentives can distort conclusions.
- **2000s–2010s:** Journey mapping and experience platforms join feedback to touchpoints; correlation is not proven cause.
- **2020s–2026:** Closed-loop feedback and assisted analysis identify patterns; customers still need an accountable response.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and a human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine customers choosing which experience signals to share. Providers may spot friction sooner, but must demonstrate an actual improvement rather than infer emotion as fact.

**Competing future:** If customers stop answering surveys, combine accessible interviews and task observations with carefully scoped service data.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OW-CRM06-OS-CAP01:** closed-loop experience improvement. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OW-CRM06-OS-VS01:** Listen → define friction → propose change → experiment → observe customer effort → decide.

**Objects to distinguish:** journey stage, feedback, respondent population, friction hypothesis, intervention and follow-up.

**Proposed responsibility:** Experience management owns feedback and the improvement backlog; service owns case resolution; analytics owns measure definitions. CRM06 owns the improvement loop, not the channel build.

**Protected boundary:** Higher survey scores or reward redemption alone do not demonstrate a better journey or caused retention.

Customer-experience and service applications are optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OW-CRM06-OS-SYN001**. Synthetic customer IND-C300, asset IND-A300, ticket IND-T300 closed with workaround, part order still open. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare a blanket incentive with fixing the handoff and measuring customer effort.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OW-CRM06-OS-REQ01:** link one customer-feedback experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OW-CRM06-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — The survey asks about courtesy, not repeat faults

**Expected:** Add a repeat-fault question and link feedback to the asset history.

### T02 — Faster closure raises scores while repeat faults persist

**Expected:** Report speed and resolution separately; do not reward closure alone.

### T03 — Feedback hints at a safety-critical fault

**Expected:** Escalate to the asset-safety owner by the agreed route and limit who can read the comment.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OW-CRM06-OS-T01/T02/T03, supporting OW-CRM06-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OW-CRM06-OS-KPI01:** Repeat-contact rate for the chosen journey, with a defined issue window and comparison population; collect effort feedback. Assign Isabel Torres as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

**Acceptance:** the card identifies source and owner, preserves the protected boundary, handles all three tests after documented revisions and explains the decision in 60 seconds. Missing evidence remains visible. Record what is still unverified.

## 7. Use your 120 minutes

- **0–20:** read the origin timeline; explain what changed and what did not.
- **20–45:** role-play the story; ask the lead, counterpart and voice one useful question each.
- **45–65:** draw responsibilities and consult one resource selectively.
- **65–100:** complete the single Decision Card and compare the alternative.
- **100–115:** run the three tests; revise from observed paper behavior.
- **115–120:** explain the decision in 60 seconds and choose the next experiment.

All reading fits within these blocks. Do not complete an entire product course during the sprint.

## 8. Read with a question

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): which evidence, owner and monitoring would bound an assisted decision here?
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework): who owns permitted information use for this card?
- [W3C WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/): can everyone affected perceive, operate and understand the journey?

Official reference pages checked 10 November 2026; access and versions can vary. The historical periods and future stories are educational synthesis, not claims established by these pages.

## 9. Reflect and continue

What became easier for the customer? Who might still be excluded? What evidence would make you reject your design?

**Next Pre-Foundation experiment:** write one falsifiable friction hypothesis and a follow-up observation plan.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniWorks Industrial Systems Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md): existing names, designations and OW-P identifiers.
- **New material:** OW-CRM06-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OW-CRM06-OS-CAP01 → OW-CRM06-OS-VS01 → OW-CRM06-OS-REQ01 → OW-CRM06-OS-ADR01 → OW-CRM06-OS-EXP01 (this tabletop experiment) → OW-CRM06-OS-T01/T02/T03 → OW-CRM06-OS-KPI01. OW-CRM06-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
