# Revenue for the managed service is booked; the usage evidence is not
## FI01 — Architecting Autonomous Financial Close

**SuccessLabs Academy · OmniTech Solutions Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-FI01-IT-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one close-control decision that keeps balances, owners and evidence accountable.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

Usage-based billing depends on a consumption feed that arrives late. An estimate is proposed to book the period.

**Finance lead:** David Chen — Group CFO (OTS-P02).  
**Counterpart:** Ravi Patel — FinOps and Service Economics Lead (OTS-P14).  
**Data or business owner:** Daniel Weber — Director Enterprise Architecture (OTS-P12).

David Chen asks what must be true before the team decides. Ravi Patel asks which evidence and owner support the decision. Daniel Weber asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic contract, the usage feed is late and the estimate lacks an agreed method.

**Pause:** What must be true for this balance to be certified? Which evidence is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniTech Solutions Ltd. is an aspirational case study (USD 39B technology provider; 98,000 employees; 41 countries; 11,500 clients). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniTech Solutions Ltd. history.

- **1970s–1980s:** Ledgers and trial balances are prepared by hand; errors surface at the end.
- **1980s–1990s:** Spreadsheets and early ERP modules speed posting; manual reconciliation and version risk remain.
- **2000s–2010s:** Shared services, close calendars and control frameworks formalize ownership and evidence.
- **2020s–2026:** Automated matching and assisted anomaly review help; a named person still certifies the balance.

**Mindset shift:** start with the balance, its owner and its evidence, then choose the automation. Automating an unreconciled process can post the same mistake faster.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to propose routine matches and flag unusual items; retain the evidence gate, a named reviewer and a way to reverse.

**2040 question:** if continuous close becomes common, can each balance carry its evidence and owner at any moment without losing review discipline?

**2050 scene:** Imagine balances that explain themselves on request. Providers may show lineage sooner, but a certifying owner must still own the judgement.

**Competing future:** A slower, rules-based close with strong reconciliation discipline may beat an adaptive service on reliability and audit cost.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OTS-FI01-OS-CAP01:** controlled period-end close. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OTS-FI01-OS-VS01:** Prepare → post → reconcile → review → certify → report.

**Objects to distinguish:** close task, journal, account reconciliation, intercompany balance, review sign-off and close calendar.

**Proposed responsibility:** The controller owns the close calendar and sign-off; account owners own reconciliations; the data owner owns source balances; internal control owns evidence rules. FI01 owns the close flow, not the ledger build.

**Protected boundary:** A completed close task or an automated journal suggestion does not by itself show a balance is correct or approved.

Finance applications are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole close. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OTS-FI01-OS-SYN001**. Synthetic contract IT-CTR300, usage feed late, estimate method undefined. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare a top-side adjustment to meet the date with resolving the reconciling item and recording the cause.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OTS-FI01-OS-REQ01:** link one close-control hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OTS-FI01-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — The usage feed arrives late

**Expected:** Book an estimate only with an approved method and disclosure.

### T02 — The estimate method changes during close

**Expected:** Require approval and record the change.

### T03 — Client-confidential data appears in a close file

**Expected:** Remove it and restrict access.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OTS-FI01-OS-T01/T02/T03, supporting OTS-FI01-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OTS-FI01-OS-KPI01:** Share of reconciling items cleared with evidence before sign-off, with a defined population and period; track late adjustments after close. Assign David Chen as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

Which balance would you still not trust? Who certifies it? What evidence would make you reject your design?

**Next Pre-Foundation experiment:** write one falsifiable close-risk hypothesis and the evidence needed to test it.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniTech Solutions Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/08-information-technology/omnitech-solutions-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/08-information-technology/omnitech-solutions-ltd/personas/persona-cards.md): existing names, designations and OTS-P identifiers.
- **New material:** OTS-FI01-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OTS-FI01-OS-CAP01 → OTS-FI01-OS-VS01 → OTS-FI01-OS-REQ01 → OTS-FI01-OS-ADR01 → OTS-FI01-OS-EXP01 (this tabletop experiment) → OTS-FI01-OS-T01/T02/T03 → OTS-FI01-OS-KPI01. OTS-FI01-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
