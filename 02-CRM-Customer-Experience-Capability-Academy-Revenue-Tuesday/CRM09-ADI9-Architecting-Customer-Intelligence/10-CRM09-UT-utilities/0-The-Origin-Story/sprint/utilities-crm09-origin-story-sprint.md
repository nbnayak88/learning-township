# Three dashboards agreed only because nobody asked what customer meant
## CRM09 — Architecting Customer Intelligence

**SuccessLabs Academy · OmniGrid Utilities Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-CRM09-UT-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one analytic decision that states what customer means before any number is used.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

Three dashboards report customer counts for a residential customer's market and agree, until a leader asks whether a customer is a contact, an account or a paying party.

**Lead:** Mei Lin — Asset and Grid Data Lead (OGU-P09).  
**Counterpart:** Omar Haddad — CISO and OT Resilience Lead (OGU-P10).  
**Customer voice:** Amelia Jones — Customer and Community Representative (OGU-P15).

Mei Lin asks what must be true before the team decides. Omar Haddad asks which evidence and owner support the decision. Amelia Jones asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic data, one dashboard counts contacts, one accounts and one invoicing parties; the numbers matched only because they were filtered differently.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniGrid Utilities Ltd. is an aspirational case study (USD 31B utility; 38,000 staff; 17 countries; 21M electricity, gas and water accounts). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniGrid Utilities Ltd. history.

- **1970s–1980s:** Customer insight comes from salespeople and surveys.
- **1980s–1990s:** Databases and reports count customers; definitions differ by department.
- **2000s–2010s:** Warehouses and dashboards scale reporting; metric lineage is often unclear.
- **2020s–2026:** Assisted analysis and prediction speed insight; definitions, permission and validation still need owners.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and a human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine customers deciding which signals to share. Providers may respond sooner, but must demonstrate a real outcome rather than infer intent as fact.

**Competing future:** A simpler, rules-based service with trained people may beat an adaptive one on reliability, privacy and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OGU-CRM09-OS-CAP01:** governed customer decision intelligence. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OGU-CRM09-OS-VS01:** Frame question → define population → inspect lineage → calculate → validate sample → decide.

**Objects to distinguish:** question, population, metric definition, lineage, calculation and decision.

**Proposed responsibility:** Analytics owns calculations; data owners own sources; the business owner owns the decision; privacy owns small-group rules. CRM09 owns the intelligence flow, not the warehouse build.

**Protected boundary:** A score or correlation does not show intent, causation or permission to act.

Customer-experience and service applications are optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OGU-CRM09-OS-SYN001**. Synthetic populations UT-POP300 (contacts), UT-POP301 (accounts), UT-POP302 (invoiced parties). Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare publishing the combined dashboard with defining each population first.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OGU-CRM09-OS-REQ01:** link one metric-lineage experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OGU-CRM09-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — Contact and account counts are combined

**Expected:** Separate the populations; label each measure with its definition.

### T02 — An account-code change triggers a churn alert

**Expected:** Hold the alert until the code mapping is validated and the owner confirms.

### T03 — A small cohort could reveal an individual

**Expected:** Suppress small cells and use an approved aggregation threshold.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OGU-CRM09-OS-T01/T02/T03, supporting OGU-CRM09-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OGU-CRM09-OS-KPI01:** Share of customer metrics with documented population, lineage and owner; define the window and exclusions. Assign Mei Lin as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

**Next Pre-Foundation experiment:** write one falsifiable hypothesis for this journey and the observation that would test it.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniGrid Utilities Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/personas/persona-cards.md): existing names, designations and OGU-P identifiers.
- **New material:** OGU-CRM09-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OGU-CRM09-OS-CAP01 → OGU-CRM09-OS-VS01 → OGU-CRM09-OS-REQ01 → OGU-CRM09-OS-ADR01 → OGU-CRM09-OS-EXP01 (this tabletop experiment) → OGU-CRM09-OS-T01/T02/T03 → OGU-CRM09-OS-KPI01. OGU-CRM09-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
