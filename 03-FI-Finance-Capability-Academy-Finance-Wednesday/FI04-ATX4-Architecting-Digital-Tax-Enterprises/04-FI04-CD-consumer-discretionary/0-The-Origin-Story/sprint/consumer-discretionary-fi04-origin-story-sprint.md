# The tax file was sent; nobody knew whether it was accepted
## FI04 — Architecting Digital Tax Enterprises

**SuccessLabs Academy · OmniVibe Consumer Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-FI04-CD-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one traceable tax-document flow that distinguishes determination, submission, acknowledgment and correction.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

A tax document for a store region is submitted and the system shows sent, while the filing owner needs to know whether the authority accepted it.

**Finance lead:** Adrian Tan — Group CFO (OVC-P02).  
**Counterpart:** Priya Shah — Director Enterprise Architecture (OVC-P11).  
**Data or business owner:** Farah Ahmed — CISO and Privacy Lead (OVC-P13).

Adrian Tan asks what must be true before the team decides. Priya Shah asks which evidence and owner support the decision. Farah Ahmed asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic flow, transport succeeded but no acknowledgment from the authority was recorded, so acceptance is unknown.

**Pause:** What must be true for this submission to count as accepted? Which evidence is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniVibe Consumer Ltd. is an aspirational case study (USD 28B consumer group; 72,000 employees; 48 countries). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniVibe Consumer Ltd. history.

- **1970s–1980s:** Returns are prepared and filed on paper.
- **1980s–1990s:** Electronic filing begins; rules differ by country.
- **2000s–2010s:** Digital reporting and clearance models spread; statuses vary.
- **2020s–2026:** Assisted rule lookup helps; the tax owner still owns interpretation and evidence.

**Mindset shift:** start with the balance, its owner and its evidence, then choose the automation. Automating a weak control can repeat the same mistake faster.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to propose routine work and flag unusual items; retain the evidence gate, a named reviewer and a way to reverse.

**2040 question:** if finance processes become more connected, can each balance and decision carry its evidence and owner without losing review discipline?

**2050 scene:** Imagine finance records that explain themselves on request. Providers may show lineage sooner, but an accountable person must still own the judgement.

**Competing future:** A simpler, rules-based process with strong controls may beat an adaptive service on reliability, audit cost and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OVC-FI04-OS-CAP01:** traceable tax-document flow. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OVC-FI04-OS-VS01:** Determine → prepare → submit → receive acknowledgment → correct → retain.

**Objects to distinguish:** tax determination, document, submission, acknowledgment and correction.

**Proposed responsibility:** The tax owner owns rules; finance owns data; integration owns transport; compliance owns retention. FI04 owns the document flow, not the tax policy.

**Protected boundary:** Not every jurisdiction uses clearance or the same statuses; completion criteria come from official guidance and approved design.

Finance applications are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole process. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OVC-FI04-OS-SYN001**. Synthetic document CD-TX300, submission CD-SUB300, acknowledgment missing; jurisdiction rules come from official guidance, not this exercise. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare treating a sent file as filed with waiting for evidenced acceptance.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OVC-FI04-OS-REQ01:** link one tax-traceability experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OVC-FI04-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — Transport succeeds but authority validation rejects

**Expected:** Show the rejection, keep the status unaccepted and route to the owner.

### T02 — Rule version or jurisdiction is unclear

**Expected:** Stop and ask the tax owner; do not guess a rule.

### T03 — A correction request retries

**Expected:** Make it safe to repeat: one correction, one record.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OVC-FI04-OS-T01/T02/T03, supporting OVC-FI04-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OVC-FI04-OS-KPI01:** Share of submissions with evidenced authority acknowledgment; define the window and jurisdictions. Assign Adrian Tan as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

Which result would you still not trust? Who owns it? What evidence would make you reject your design?

**Next Pre-Foundation experiment:** write one falsifiable control hypothesis and the evidence that would test it.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniVibe Consumer Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/personas/persona-cards.md): existing names, designations and OVC-P identifiers.
- **New material:** OVC-FI04-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OVC-FI04-OS-CAP01 → OVC-FI04-OS-VS01 → OVC-FI04-OS-REQ01 → OVC-FI04-OS-ADR01 → OVC-FI04-OS-EXP01 (this tabletop experiment) → OVC-FI04-OS-T01/T02/T03 → OVC-FI04-OS-KPI01. OVC-FI04-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
