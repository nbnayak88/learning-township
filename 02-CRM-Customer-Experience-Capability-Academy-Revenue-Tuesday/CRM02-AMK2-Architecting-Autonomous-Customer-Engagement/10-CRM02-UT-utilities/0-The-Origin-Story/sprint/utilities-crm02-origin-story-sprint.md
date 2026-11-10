# The energy-saving offer reached a customer who asked to stop
## CRM02 — Architecting Autonomous Customer Engagement

**SuccessLabs Academy · OmniGrid Utilities Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-CRM02-UT-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one engagement decision that keeps purpose, permission and message type distinct.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

An energy-saving offer reaches a customer who opted out, while outage notices must still be sent.

**Lead:** Maya Patel — Chief Customer and Flexibility Officer (OGU-P03).  
**Counterpart:** Mei Lin — Asset and Grid Data Lead (OGU-P09).  
**Customer voice:** Amelia Jones — Customer and Community Representative (OGU-P15).

Maya Patel asks what must be true before the team decides. Mei Lin asks which evidence and owner support the decision. Amelia Jones asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic case, the opt-out was recorded for marketing and also blocked an outage message.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniGrid Utilities Ltd. is an aspirational case study (USD 31B utility; 38,000 staff; 17 countries; 21M electricity, gas and water accounts). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniGrid Utilities Ltd. history.

- **1970s–1980s:** Mailings go to lists built by hand; people rarely control what they receive.
- **1980s–1990s:** Direct marketing and call centres scale outreach; opt-out handling is manual.
- **2000s–2010s:** Email and campaign tools automate sends; consent and preference records fragment across systems.
- **2020s–2026:** Assisted segmentation and content drafting speed campaigns; permission and purpose still need an accountable check.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and a human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine customers deciding which signals to share. Providers may respond sooner, but must demonstrate a real outcome rather than infer intent as fact.

**Competing future:** A simpler, rules-based service with trained people may beat an adaptive one on reliability, privacy and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OGU-CRM02-OS-CAP01:** purpose-aware customer engagement. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OGU-CRM02-OS-VS01:** Define purpose → select audience → check permission and preference → approve content → send → observe response.

**Objects to distinguish:** audience, purpose, permission, preference, message and response.

**Proposed responsibility:** Marketing owns purpose and content; the privacy owner owns permission rules; service owns essential notices; data owns segments. CRM02 owns the engagement flow, not the messaging tool build.

**Protected boundary:** Marketing opt-out does not cancel an essential service or safety message, and a stale segment is not current permission.

Customer-experience and service applications are optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OGU-CRM02-OS-SYN001**. Synthetic customer UT-C300, offer UT-OF300, outage notice UT-ON300. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare sending to the prepared audience with re-checking permission at send time.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OGU-CRM02-OS-REQ01:** link one purpose-aware engagement experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OGU-CRM02-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — Opt-out arrives after audience selection

**Expected:** Re-check permission at send time; remove the contact and record the reason.

### T02 — A marketing opt-out meets an outage notice

**Expected:** Send only the essential service message under its own purpose and permission.

### T03 — The segment feed is unavailable

**Expected:** Pause the send, state the gap and use a conservative fallback audience.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OGU-CRM02-OS-T01/T02/T03, supporting OGU-CRM02-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OGU-CRM02-OS-KPI01:** Share of sends with permission re-checked at send time, with a defined window and exclusions. Assign Maya Patel as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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
- **New material:** OGU-CRM02-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OGU-CRM02-OS-CAP01 → OGU-CRM02-OS-VS01 → OGU-CRM02-OS-REQ01 → OGU-CRM02-OS-ADR01 → OGU-CRM02-OS-EXP01 (this tabletop experiment) → OGU-CRM02-OS-T01/T02/T03 → OGU-CRM02-OS-KPI01. OGU-CRM02-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
