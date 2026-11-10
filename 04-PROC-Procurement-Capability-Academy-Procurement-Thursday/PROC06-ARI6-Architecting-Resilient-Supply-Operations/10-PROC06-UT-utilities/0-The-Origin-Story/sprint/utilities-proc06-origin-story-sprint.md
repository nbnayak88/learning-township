# The shipment arrived after the shutdown window
## PROC06 — Architecting Resilient Supply Operations

**SuccessLabs Academy · OmniGrid Utilities Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-PROC06-UT-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one critical-supply exception decision with a verified recovery option and accountable operational acceptance.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

A shipment of a replacement transformer part for a service territory is shown as on track, yet the required-by time passes before it arrives.

**Procurement lead:** Ingrid Sørensen — Procurement and Partner Assurance Lead (OGU-P16).  
**Counterpart:** Daniel Weber — Director Enterprise Architecture (OGU-P12).  
**Data or business owner:** Mei Lin — Asset and Grid Data Lead (OGU-P09).

Ingrid Sørensen asks what must be true before the team decides. Daniel Weber asks which evidence and owner support the decision. Mei Lin asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic record, the predicted arrival was never confirmed by the supplier, and the alternative part lacks equivalence evidence.

**Pause:** What must be true for this decision to stand? Which evidence is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniGrid Utilities Ltd. is an aspirational case study (USD 31B utility; 38,000 staff; 17 countries; 21M electricity, gas and water accounts). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniGrid Utilities Ltd. history.

- **1970s–1980s:** Shortages are handled by phone.
- **1980s–1990s:** Expediting teams react to late orders.
- **2000s–2010s:** Tracking and alerts improve visibility; predictions are trusted too early.
- **2020s–2026:** Assisted prediction helps planning; confirmed facts and acceptance still need owners.

**Mindset shift:** start with what was needed, what evidence exists and who owns the decision, then choose the automation. Automating a weak control can repeat the same mistake faster.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to propose routine work and flag unusual items; retain the evidence gate, a named approver and a way to reverse.

**2040 question:** if buyers and suppliers exchange evidence directly, can it travel with the transaction without losing verification or fairness?

**2050 scene:** Imagine sourcing and supply decisions that explain themselves on request. Providers may show evidence sooner, but a person must own award, commitment and exceptions.

**Competing future:** A simpler, rules-based process with trained buyers may beat an adaptive service on reliability, fairness and cost.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OGU-PROC06-OS-CAP01:** critical-supply exception decision. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OGU-PROC06-OS-VS01:** Detect exception → confirm facts → assess options → decide → accept → recover.

**Objects to distinguish:** shipment, required-by time, confirmation, alternative part and acceptance.

**Proposed responsibility:** Supply operations owns the exception; engineering owns equivalence; the supplier owns confirmation. PROC06 owns the exception flow, not the logistics build.

**Protected boundary:** A predicted arrival or a similar part is not confirmation or equivalence.

Procurement applications are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole process. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OGU-PROC06-OS-SYN001**. Synthetic shipment UT-SH300, required-by UT-RB300, alternative UT-ALT300 without equivalence evidence. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare acting on the prediction with confirming facts first.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OGU-PROC06-OS-REQ01:** link one supply-exception experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OGU-PROC06-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — A predicted arrival lacks supplier confirmation

**Expected:** Label it a prediction and ask the supplier to confirm.

### T02 — An alternative part lacks equivalence evidence

**Expected:** Do not substitute until a technical owner approves.

### T03 — The tracking feed is unavailable near the required-by time

**Expected:** Use a manual confirmation route and record the gap.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OGU-PROC06-OS-T01/T02/T03, supporting OGU-PROC06-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OGU-PROC06-OS-KPI01:** Share of critical exceptions resolved with confirmed arrival or approved equivalent; define window and exclusions. Assign Ingrid Sørensen as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

Which decision would you still not release? Who owns the evidence? What would make you reject your design?

**Next Pre-Foundation experiment:** write one falsifiable procurement hypothesis and the evidence that would test it.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniGrid Utilities Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/personas/persona-cards.md): existing names, designations and OGU-P identifiers.
- **New material:** OGU-PROC06-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OGU-PROC06-OS-CAP01 → OGU-PROC06-OS-VS01 → OGU-PROC06-OS-REQ01 → OGU-PROC06-OS-ADR01 → OGU-PROC06-OS-EXP01 (this tabletop experiment) → OGU-PROC06-OS-T01/T02/T03 → OGU-PROC06-OS-KPI01. OGU-PROC06-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
