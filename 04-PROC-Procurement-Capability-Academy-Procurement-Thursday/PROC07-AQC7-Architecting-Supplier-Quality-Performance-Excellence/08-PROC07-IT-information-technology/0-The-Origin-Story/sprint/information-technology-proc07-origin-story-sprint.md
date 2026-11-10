# The on-time delivery contained a part nobody could release
## PROC07 — Architecting Supplier Quality and Performance Excellence

**SuccessLabs Academy · OmniTech Solutions Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-PROC07-IT-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one supplier-quality decision that keeps receipt, conformity and corrective-action closure separate.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

A hardware supplier delivers a hardware component for a delivery centre on time, and the scorecard shows a strong result.

**Procurement lead:** Ingrid Sørensen — Procurement and Partner Ecosystem Lead (OTS-P16).  
**Counterpart:** Mei Lin — Data Governance and Knowledge Lead (OTS-P09).  
**Data or business owner:** Daniel Weber — Director Enterprise Architecture (OTS-P12).

Ingrid Sørensen asks what must be true before the team decides. Mei Lin asks which evidence and owner support the decision. Daniel Weber asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic record, delivery was on time but the batch identity is missing and a critical defect blocks release.

**Pause:** What must be true for this decision to stand? Which evidence is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniTech Solutions Ltd. is an aspirational case study (USD 39B technology provider; 98,000 employees; 41 countries; 11,500 clients). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniTech Solutions Ltd. history.

- **1970s–1980s:** Quality is checked at the dock.
- **1980s–1990s:** Supplier scorecards formalize delivery and quality.
- **2000s–2010s:** Quality systems link defects to suppliers; averages hide critical issues.
- **2020s–2026:** Assisted inspection helps triage; release and closure still need owners.

**Mindset shift:** start with what was needed, what evidence exists and who owns the decision, then choose the automation. Automating a weak control can repeat the same mistake faster.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to propose routine work and flag unusual items; retain the evidence gate, a named approver and a way to reverse.

**2040 question:** if buyers and suppliers exchange evidence directly, can it travel with the transaction without losing verification or fairness?

**2050 scene:** Imagine sourcing and supply decisions that explain themselves on request. Providers may show evidence sooner, but a person must own award, commitment and exceptions.

**Competing future:** A simpler, rules-based process with trained buyers may beat an adaptive service on reliability, fairness and cost.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OTS-PROC07-OS-CAP01:** supplier-quality decision. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OTS-PROC07-OS-VS01:** Receive → inspect → release or hold → correct → verify closure → score.

**Objects to distinguish:** receipt, conformity, batch identity, defect and corrective action.

**Proposed responsibility:** Quality owns release; procurement owns supplier follow-up; the supplier owns correction. PROC07 owns the quality decision flow, not the inspection lab.

**Protected boundary:** On-time receipt is not conformity, and a completed action is not verified closure.

Procurement applications are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole process. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OTS-PROC07-OS-SYN001**. Synthetic delivery IT-DL300, batch IT-BT300 identity missing, defect IT-DF300 open. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare scoring on delivery with separating receipt, conformity and closure.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OTS-PROC07-OS-REQ01:** link one supplier-quality experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OTS-PROC07-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — A critical defect exists despite a high overall score

**Expected:** Show the defect separately; do not average it away.

### T02 — The supplier marks a corrective action complete

**Expected:** Verify closure with evidence before accepting it.

### T03 — The batch identity is missing

**Expected:** Quarantine until the batch can be traced.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OTS-PROC07-OS-T01/T02/T03, supporting OTS-PROC07-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OTS-PROC07-OS-KPI01:** Share of deliveries with traced batch, conformity result and verified corrective closure; define window and exclusions. Assign Ingrid Sørensen as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

- [OmniTech Solutions Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/08-information-technology/omnitech-solutions-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/08-information-technology/omnitech-solutions-ltd/personas/persona-cards.md): existing names, designations and OTS-P identifiers.
- **New material:** OTS-PROC07-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OTS-PROC07-OS-CAP01 → OTS-PROC07-OS-VS01 → OTS-PROC07-OS-REQ01 → OTS-PROC07-OS-ADR01 → OTS-PROC07-OS-EXP01 (this tabletop experiment) → OTS-PROC07-OS-T01/T02/T03 → OTS-PROC07-OS-KPI01. OTS-PROC07-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
