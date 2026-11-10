# The facilities invoice matched; the tenant never saw the service
## PROC05 — Architecting Autonomous Procure-to-Pay

**SuccessLabs Academy · OmniSpace Real Estate Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-PROC05-RE-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one purchase-to-payment decision that keeps orders, receipts and payments accountable.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

A facilities service invoice matches the PO, and the property manager confirmed receipt, but the service log is empty.

**Procurement lead:** Amelia Jones — Procurement and Supplier Services Lead (OSP-P15).  
**Counterpart:** David Chen — Group CFO (OSP-P02).  
**Requester or supplier voice:** Maya Patel — Property Operations Director (OSP-P03).

Amelia Jones asks what must be true before the team decides. David Chen asks which evidence and owner support the decision. Maya Patel asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic PO, the service log lacks completion evidence for the sampled site.

**Pause:** What must be true before this invoice is paid? Which evidence is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniSpace Real Estate Ltd. is an aspirational case study (no enterprise numerical profile, budget or quantified benefit is supplied). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniSpace Real Estate Ltd. history.

- **1970s–1980s:** Paper orders and invoices are matched by clerks; control relies on signatures.
- **1980s–1990s:** ERP purchasing and payables modules automate matching; tolerances and master-data errors appear.
- **2000s–2010s:** Supplier portals, e-invoicing and catalogues widen scope; fraud and duplicate risk grow.
- **2020s–2026:** Assisted matching and anomaly checks help; an accountable person still owns exceptions and payment.

**Mindset shift:** start with what was ordered, received and paid, then choose the automation. Automating a weak control can pay the wrong party faster.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to propose matches and flag unusual invoices; retain the evidence gate, an approver and a payment hold.

**2040 question:** if suppliers and buyers exchange events directly, can receipt and invoice evidence travel with the transaction without losing verification?

**2050 scene:** Imagine orders that settle themselves once evidence agrees. Providers may match faster, but a person must own supplier identity and exceptions.

**Competing future:** A simpler manual approval with strong supplier verification may beat an adaptive service on fraud risk and cost.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OSP-PROC05-OS-CAP01:** controlled purchase-to-payment. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OSP-PROC05-OS-VS01:** Request → approve → order → receive → match → pay.

**Objects to distinguish:** requisition, purchase order, goods receipt, invoice, match tolerance and payment block.

**Proposed responsibility:** Procurement owns supplier and order rules; the requester confirms receipt; accounts payable owns matching and payment; finance owns approval limits. PROC05 owns the purchase-to-payment flow, not the supplier portal.

**Protected boundary:** A matched invoice does not show that the right goods were received or that the supplier and bank details are legitimate.

Procurement and payables applications are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole flow. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OSP-PROC05-OS-SYN001**. Synthetic PO RE-PO300, service log RE-LOG300 empty, site RE-ST300. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare paying on document match with requiring measured receipt and verified supplier details.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OSP-PROC05-OS-REQ01:** link one purchase-to-payment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OSP-PROC05-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — A receipt lacks a service log

**Expected:** Require evidence before payment.

### T02 — A vendor's rate changes

**Expected:** Approve the change and update the PO.

### T03 — An invoice refers to a sold property

**Expected:** Block and route to the asset owner.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OSP-PROC05-OS-T01/T02/T03, supporting OSP-PROC05-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OSP-PROC05-OS-KPI01:** Share of invoices paid with complete match evidence, with a defined population and period; track payment blocks by age. Assign Amelia Jones as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

Which payment would you still not release? Who confirmed receipt? What evidence would make you reject your design?

**Next Pre-Foundation experiment:** write one falsifiable payment-risk hypothesis and the check that would test it.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniSpace Real Estate Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/personas/persona-cards.md): existing names, designations and OSP-P identifiers.
- **New material:** OSP-PROC05-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OSP-PROC05-OS-CAP01 → OSP-PROC05-OS-VS01 → OSP-PROC05-OS-REQ01 → OSP-PROC05-OS-ADR01 → OSP-PROC05-OS-EXP01 (this tabletop experiment) → OSP-PROC05-OS-T01/T02/T03 → OSP-PROC05-OS-KPI01. OSP-PROC05-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
