# The margin improved because the cost moved somewhere else
## FI07 — Architecting Cost and Profitability Excellence

**SuccessLabs Academy · OmniVibe Consumer Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-FI07-CD-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one explainable cost-to-margin view that reconciles allocation choices without hiding business impact.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

Margin for a store region improves after an allocation change, and a leader proposes to report it as performance.

**Finance lead:** Adrian Tan — Group CFO (OVC-P02).  
**Counterpart:** Mateo Silva — Supply Chain and Responsible Sourcing Lead (OVC-P14).  
**Data or business owner:** Priya Shah — Director Enterprise Architecture (OVC-P11).

Adrian Tan asks what must be true before the team decides. Mateo Silva asks which evidence and owner support the decision. Priya Shah asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic view, a shared cost was reallocated to another unit, so the group total did not change.

**Pause:** What must be true for this to be approved? Which evidence is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniVibe Consumer Ltd. is an aspirational case study (USD 28B consumer group; 72,000 employees; 48 countries). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniVibe Consumer Ltd. history.

- **1970s–1980s:** Costs are allocated by simple ratios.
- **1980s–1990s:** Cost accounting systems formalize allocations; drivers become contested.
- **2000s–2010s:** Activity-based and profitability analysis spread; complexity grows.
- **2020s–2026:** Assisted analysis speeds reporting; disclosure of drivers still needs an owner.

**Mindset shift:** start with the balance, its owner and its evidence, then choose the automation. Automating a weak control can repeat the same mistake faster.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to propose routine work and flag unusual items; retain the evidence gate, a named reviewer and a way to reverse.

**2040 question:** if finance processes become more connected, can each balance and decision carry its evidence and owner without losing review discipline?

**2050 scene:** Imagine finance records that explain themselves on request. Providers may show lineage sooner, but an accountable person must still own the judgement.

**Competing future:** A simpler, rules-based process with strong controls may beat an adaptive service on reliability, audit cost and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OVC-FI07-OS-CAP01:** explainable cost-to-margin view. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OVC-FI07-OS-VS01:** Define pool → choose driver → allocate → reconcile → explain → decide.

**Objects to distinguish:** cost pool, driver, allocation, margin and avoidable cost.

**Proposed responsibility:** Cost accounting owns allocations; business owners own drivers; finance owns reconciliation. FI07 owns the margin view, not the ledger build.

**Protected boundary:** An allocation is not automatically an avoidable cost, a cash saving or proof of causation.

Finance applications are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole process. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OVC-FI07-OS-SYN001**. Synthetic cost pool CD-CP300, driver CD-DRV300, allocation to CD-U300 and CD-U301. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare reporting the improved margin with reconciling allocation to the approved pool.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OVC-FI07-OS-REQ01:** link one margin explanation experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OVC-FI07-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — Allocated total differs from the approved cost pool

**Expected:** Reconcile to the pool before reporting.

### T02 — The driver changes midway without disclosure

**Expected:** Disclose and restate comparable periods.

### T03 — Lower allocated cost is claimed as cash saving

**Expected:** Separate allocation from avoidable cash cost.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OVC-FI07-OS-T01/T02/T03, supporting OVC-FI07-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OVC-FI07-OS-KPI01:** Share of allocations reconciled to the approved pool with disclosed drivers; define window and exclusions. Assign Adrian Tan as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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
- **New material:** OVC-FI07-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OVC-FI07-OS-CAP01 → OVC-FI07-OS-VS01 → OVC-FI07-OS-REQ01 → OVC-FI07-OS-ADR01 → OVC-FI07-OS-EXP01 (this tabletop experiment) → OVC-FI07-OS-T01/T02/T03 → OVC-FI07-OS-KPI01. OVC-FI07-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
