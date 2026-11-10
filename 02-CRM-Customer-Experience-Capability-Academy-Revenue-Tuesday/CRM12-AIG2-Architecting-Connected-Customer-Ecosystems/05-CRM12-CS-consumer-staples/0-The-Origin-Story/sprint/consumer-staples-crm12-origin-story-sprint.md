# The message arrived; the customer's service did not change
## CRM12 — Architecting Connected Customer Ecosystems

**SuccessLabs Academy · OmniDaily Consumer Goods Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-CRM12-CS-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one exchange that keeps delivery, validation and business completion distinct.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

A change for a household customer is sent between two systems and the sender shows success, yet the distribution system never applies it and the customer's service is unchanged.

**Lead:** Sofia Alvarez — Chief Digital and Data Officer (ODG-P05).  
**Counterpart:** Priya Nair — Director Enterprise Architecture (ODG-P13).  
**Customer voice:** Asha Patel — Consumer and Household Representative (ODG-P16).

Sofia Alvarez asks what must be true before the team decides. Priya Nair asks which evidence and owner support the decision. Asha Patel asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic case, the message was delivered but the target rejected it as invalid, and no business acknowledgment came back.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniDaily Consumer Goods Ltd. is an aspirational case study (USD 51B staples group; 84,000 employees; 57 countries; 420M households served). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniDaily Consumer Goods Ltd. history.

- **1970s–1980s:** Systems exchange files overnight and errors surface later.
- **1980s–1990s:** Point-to-point interfaces connect applications; failures are silent.
- **2000s–2010s:** APIs and messaging scale connections; delivery is mistaken for completion.
- **2020s–2026:** Event streams and assisted mapping speed integration; acknowledgment, ordering and recovery still need owners.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and a human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine customers deciding which signals to share. Providers may respond sooner, but must demonstrate a real outcome rather than infer intent as fact.

**Competing future:** A simpler, rules-based service with trained people may beat an adaptive one on reliability, privacy and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — ODG-CRM12-OS-CAP01:** governed customer ecosystem exchange. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — ODG-CRM12-OS-VS01:** Authorize change → emit → validate → apply once → acknowledge outcome → reconcile → recover.

**Objects to distinguish:** change, message, validation, application, acknowledgment and reconciliation.

**Proposed responsibility:** The business owner authorizes change; integration owns delivery; each target owns validation and application; operations owns reconciliation. CRM12 owns the exchange flow, not the integration build.

**Protected boundary:** HTTP success, broker delivery and business completion are different outcomes.

Customer-experience and service applications are optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **ODG-CRM12-OS-SYN001**. Synthetic message ODG-MSG300, change ODG-CHG300, target rejection without acknowledgment. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare treating delivery as completion with requiring a business acknowledgment.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — ODG-CRM12-OS-REQ01:** link one ecosystem-exchange experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — ODG-CRM12-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — The target rejects a validly delivered message

**Expected:** Record the rejection, notify the owner and keep the customer's status unchanged.

### T02 — A duplicate or older event arrives

**Expected:** Apply the event once, ignore the older one and record both.

### T03 — Recovery replays an already accepted event

**Expected:** Make replay safe by detecting the prior acceptance.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests ODG-CRM12-OS-T01/T02/T03, supporting ODG-CRM12-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — ODG-CRM12-OS-KPI01:** Share of exchanged changes with a business acknowledgment; define the window and exclusions. Assign Sofia Alvarez as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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
- **New material:** ODG-CRM12-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → ODG-CRM12-OS-CAP01 → ODG-CRM12-OS-VS01 → ODG-CRM12-OS-REQ01 → ODG-CRM12-OS-ADR01 → ODG-CRM12-OS-EXP01 (this tabletop experiment) → ODG-CRM12-OS-T01/T02/T03 → ODG-CRM12-OS-KPI01. ODG-CRM12-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
