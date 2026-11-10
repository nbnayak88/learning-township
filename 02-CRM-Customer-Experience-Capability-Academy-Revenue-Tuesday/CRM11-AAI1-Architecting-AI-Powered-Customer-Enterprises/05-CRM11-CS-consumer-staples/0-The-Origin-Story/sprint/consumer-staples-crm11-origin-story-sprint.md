# The assistant gave a confident answer to the wrong question
## CRM11 — Architecting AI-Powered Customer Enterprises

**SuccessLabs Academy · OmniDaily Consumer Goods Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-CRM11-CS-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one assistant answer path that grounds claims in approved evidence and escalates what it cannot answer.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

An assistant answers a household customer's question about a weekly grocery order fluently, but cites a superseded policy and does not check the customer's contract scope.

**Lead:** Diego Costa — Head of Planning Analytics and AI (ODG-P14).  
**Counterpart:** Omar Haddad — CISO and Privacy Lead (ODG-P12).  
**Customer voice:** Asha Patel — Consumer and Household Representative (ODG-P16).

Diego Costa asks what must be true before the team decides. Omar Haddad asks which evidence and owner support the decision. Asha Patel asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic case, the retrieved policy was superseded and the question concerned a contract outside the assistant's authorized scope.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniDaily Consumer Goods Ltd. is an aspirational case study (USD 51B staples group; 84,000 employees; 57 countries; 420M households served). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniDaily Consumer Goods Ltd. history.

- **1970s–1980s:** Answers depend on the person who happens to answer.
- **1980s–1990s:** Scripts and knowledge bases standardize replies; they age quickly.
- **2000s–2010s:** Search and chatbots deflect simple questions; context is limited.
- **2020s–2026:** Generative assistants draft fluent answers; grounding, scope and escalation decide whether they can be trusted.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and a human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine customers deciding which signals to share. Providers may respond sooner, but must demonstrate a real outcome rather than infer intent as fact.

**Competing future:** A simpler, rules-based service with trained people may beat an adaptive one on reliability, privacy and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — ODG-CRM11-OS-CAP01:** responsible customer assistance. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — ODG-CRM11-OS-VS01:** Verify scope → retrieve approved evidence → draft → check risk → answer or escalate → record.

**Objects to distinguish:** question, scope, approved evidence, draft answer, risk check and escalation.

**Proposed responsibility:** The service owner owns the answer; knowledge owns approved sources; security owns authority and prompts; the contract owner owns scope. CRM11 owns the assistance flow, not the model build.

**Protected boundary:** An assistant cannot invent commitments or issue operational commands, and a fluent answer is not evidence.

Customer-experience and service applications are optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **ODG-CRM11-OS-SYN001**. Synthetic question ODG-Q300, policy ODG-POL300 (superseded), contract ODG-CTR300. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare releasing the drafted answer with requiring approved evidence and scope.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — ODG-CRM11-OS-REQ01:** link one responsible-assistance experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — ODG-CRM11-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — The policy is stale or contradictory

**Expected:** Do not answer from the stale source; escalate with the conflict stated.

### T02 — Retrieved text asks the assistant to bypass controls

**Expected:** Ignore the instruction, keep the original controls and log the attempt.

### T03 — A contract change is outside the assistant's scope

**Expected:** Escalate to the accountable owner instead of answering outside scope.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests ODG-CRM11-OS-T01/T02/T03, supporting ODG-CRM11-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — ODG-CRM11-OS-KPI01:** Share of assistant answers supported by approved evidence and within scope; define the window and exclusions. Assign Diego Costa as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

- [OmniDaily Consumer Goods Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md): existing names, designations and ODG-P identifiers.
- **New material:** ODG-CRM11-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → ODG-CRM11-OS-CAP01 → ODG-CRM11-OS-VS01 → ODG-CRM11-OS-REQ01 → ODG-CRM11-OS-ADR01 → ODG-CRM11-OS-EXP01 (this tabletop experiment) → ODG-CRM11-OS-T01/T02/T03 → ODG-CRM11-OS-KPI01. ODG-CRM11-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
