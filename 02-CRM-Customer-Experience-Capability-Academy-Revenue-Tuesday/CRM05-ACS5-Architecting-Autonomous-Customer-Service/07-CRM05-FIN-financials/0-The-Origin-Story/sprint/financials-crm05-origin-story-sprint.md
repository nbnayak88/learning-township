# The card dispute was closed while the charge remained
## CRM05 — Architecting Autonomous Customer Service

**SuccessLabs Academy · OmniCapital Financial Group Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-CRM05-FIN-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one case decision that separates action taken from outcome verified.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

A card dispute is closed, but the charge is still on the account.

**Lead:** Priya Rao — Chief Customer and Retail Officer (OCF-P03).  
**Counterpart:** Daniel Weber — Director Enterprise Architecture (OCF-P12).  
**Customer voice:** Amelia Brooks — SME Customer Representative (OCF-P15).

Priya Rao asks what must be true before the team decides. Daniel Weber asks which evidence and owner support the decision. Amelia Brooks asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic case, the dispute outcome was recorded but not posted.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniCapital Financial Group Ltd. is an aspirational case study (USD 46B financial group; USD 1.4T AUM; 58M customers; 32 countries). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniCapital Financial Group Ltd. history.

- **1970s–1980s:** Complaints are handled by whoever answers the telephone.
- **1980s–1990s:** Call centres and ticket systems record cases; closure targets reward speed.
- **2000s–2010s:** Knowledge bases and omnichannel tools route work; handoffs lose context.
- **2020s–2026:** Assisted triage and drafted replies speed cases; a person still verifies the outcome.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and a human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine customers deciding which signals to share. Providers may respond sooner, but must demonstrate a real outcome rather than infer intent as fact.

**Competing future:** A simpler, rules-based service with trained people may beat an adaptive one on reliability, privacy and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OCF-CRM05-OS-CAP01:** evidence-based issue resolution. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OCF-CRM05-OS-VS01:** Receive → classify → assign → investigate → confirm action → communicate → verify.

**Objects to distinguish:** case, owner, evidence, action, customer response and verification.

**Proposed responsibility:** Service owns the case; the receiving team owns acknowledgment; knowledge owns articles; operations owns the underlying fix. CRM05 owns the resolution flow, not the case-tool build.

**Protected boundary:** Closing a ticket does not show the customer's issue is resolved.

Customer-experience and service applications are optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OCF-CRM05-OS-SYN001**. Synthetic case FIN-CS300, dispute FIN-D300, posting pending. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare closing on action taken with closing only after the customer confirms.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OCF-CRM05-OS-REQ01:** link one verified-resolution experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OCF-CRM05-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — A transferred case has no receiving acknowledgment

**Expected:** Hold the case with the sender until the receiver acknowledges.

### T02 — A knowledge article conflicts with current policy

**Expected:** Prefer the confirmed status; flag the article for the content owner.

### T03 — The customer reports the charge remains

**Expected:** Reopen the case and verify the outcome with the customer.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OCF-CRM05-OS-T01/T02/T03, supporting OCF-CRM05-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OCF-CRM05-OS-KPI01:** Share of closed cases with verified resolution; define the window and exclusions. Assign Priya Rao as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

- [OmniCapital Financial Group Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/personas/persona-cards.md): existing names, designations and OCF-P identifiers.
- **New material:** OCF-CRM05-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OCF-CRM05-OS-CAP01 → OCF-CRM05-OS-VS01 → OCF-CRM05-OS-REQ01 → OCF-CRM05-OS-ADR01 → OCF-CRM05-OS-EXP01 (this tabletop experiment) → OCF-CRM05-OS-T01/T02/T03 → OCF-CRM05-OS-KPI01. OCF-CRM05-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
