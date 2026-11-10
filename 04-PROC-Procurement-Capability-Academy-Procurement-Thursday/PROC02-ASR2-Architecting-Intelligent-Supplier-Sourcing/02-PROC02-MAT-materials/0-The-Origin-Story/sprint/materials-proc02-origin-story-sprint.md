# The winning bid had not passed the technical gate
## PROC02 — Architecting Intelligent Supplier Sourcing

**SuccessLabs Academy · OmniForge Materials Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-PROC02-MAT-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one fair sourcing award recommendation with comparable bids and explicit qualification gates.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

A bulk-chemical supplier submits the lowest bid for a catalyst supply for a plant, and the award recommendation is due.

**Procurement lead:** Grace Mensah — Chief Supply Chain and Procurement Officer (OMF-P09).  
**Counterpart:** Thomas van Dijk — Group CFO (OMF-P02).  
**Data or business owner:** Hassan Al-Farsi — CISO and OT Security Lead (OMF-P12).

Grace Mensah asks what must be true before the team decides. Thomas van Dijk asks which evidence and owner support the decision. Hassan Al-Farsi asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic bid record, the lowest bidder lacks the mandatory technical evidence, and its price excludes installation.

**Pause:** What must be true for this decision to stand? Which evidence is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniForge Materials Ltd. is an aspirational case study (USD 42B materials group; 46,000 employees; 31 countries). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniForge Materials Ltd. history.

- **1970s–1980s:** Bids are opened and compared by hand.
- **1980s–1990s:** Tender processes formalize criteria; scope differences hide in prices.
- **2000s–2010s:** E-sourcing speeds events; criteria change mid-event.
- **2020s–2026:** Assisted evaluation speeds review; gates and fairness still need owners.

**Mindset shift:** start with what was needed, what evidence exists and who owns the decision, then choose the automation. Automating a weak control can repeat the same mistake faster.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to propose routine work and flag unusual items; retain the evidence gate, a named approver and a way to reverse.

**2040 question:** if buyers and suppliers exchange evidence directly, can it travel with the transaction without losing verification or fairness?

**2050 scene:** Imagine sourcing and supply decisions that explain themselves on request. Providers may show evidence sooner, but a person must own award, commitment and exceptions.

**Competing future:** A simpler, rules-based process with trained buyers may beat an adaptive service on reliability, fairness and cost.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OMF-PROC02-OS-CAP01:** fair sourcing award. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OMF-PROC02-OS-VS01:** Define criteria → invite → gate → compare → recommend → award.

**Objects to distinguish:** criteria, bid, qualification gate, normalized price and award recommendation.

**Proposed responsibility:** Sourcing owns the event; technical owners own the gate; finance owns price comparison. PROC02 owns the award recommendation, not the contract.

**Protected boundary:** A lowest price is not a winning bid until it passes the gates on a comparable basis.

Procurement applications are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole process. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OMF-PROC02-OS-SYN001**. Synthetic sourcing event MAT-RFX300, bids MAT-BID300 to MAT-BID302, technical gate evidence missing for one bid. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare ranking by price with gating first and normalizing scope.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OMF-PROC02-OS-REQ01:** link one fair-award experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OMF-PROC02-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — The lowest bidder lacks mandatory evidence

**Expected:** Hold the bid at the gate; do not rank it until evidence is supplied.

### T02 — A criterion changes after bids are visible

**Expected:** Do not change it; reissue to all bidders if it must change.

### T03 — A bid price excludes installation

**Expected:** Normalize to a comparable scope before ranking.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OMF-PROC02-OS-T01/T02/T03, supporting OMF-PROC02-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OMF-PROC02-OS-KPI01:** Share of awards with all gate evidence and comparable scope; define window and exclusions. Assign Grace Mensah as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

- [OmniForge Materials Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md): existing names, designations and OMF-P identifiers.
- **New material:** OMF-PROC02-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OMF-PROC02-OS-CAP01 → OMF-PROC02-OS-VS01 → OMF-PROC02-OS-REQ01 → OMF-PROC02-OS-ADR01 → OMF-PROC02-OS-EXP01 (this tabletop experiment) → OMF-PROC02-OS-T01/T02/T03 → OMF-PROC02-OS-KPI01. OMF-PROC02-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
