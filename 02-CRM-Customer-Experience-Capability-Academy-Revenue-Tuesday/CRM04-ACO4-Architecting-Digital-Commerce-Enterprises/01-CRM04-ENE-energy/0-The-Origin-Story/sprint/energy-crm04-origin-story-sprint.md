# The checkout was successful; the purchase was still uncertain
## CRM04 — Architecting Digital Commerce Enterprises

**SuccessLabs Academy · OmniVerse Energy Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 31 October 2026**  
**Planning reference:** HUB-ORIGIN-CRM04-ENE-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one transparent energy-service checkout that separates customer intent, payment and accepted order.

**One story · One build card · Three tabletop tests**

## 1. Start with the customer

An industrial buyer orders an illustrative energy-efficiency assessment through a storefront. The page displays a final price before service location and eligibility checks finish; the customer retries after a timeout.

**Lead:** Grace Okafor — Chief Customer and Retail Officer (OVE-P10).  
**Counterpart:** Michael Reed — Group Chief Financial Officer (OVE-P03).  
**Customer voice:** Elena Brooks — VP Energy Procurement (OVE-P15).

Elena asks whether she purchased a service or only requested it. Michael asks whether the second click can create another charge. Grace asks which confirmation the customer can trust.

The team distinguishes cart, eligibility check, payment authorization and accepted order. It provides a recoverable pending state and one reference for the purchase attempt.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniVerse is a fictional integrated energy enterprise with 68,000 employees in 42 countries. These new incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniVerse history.

- **1970s–1980s:** Counter sales and paper catalogs let staff explain terms; buying hours and reach are limited.
- **1980s–1990s:** Electronic catalogs and telephone ordering improve discovery; price and availability remain disconnected.
- **2000s–2010s:** Web commerce and online checkout expand access; cart, payment and order systems can disagree.
- **2020s–2026:** Omnichannel buying and assistance reduce friction; recovery, accessibility and transparent terms still need design.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost: customer, frontline colleague or community?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine a 2050 buying assistant comparing energy-service packages against a customer's budget. It must expose assumptions, eligibility and cancellation terms before seeking authorized purchase approval.

**Competing future:** If customers prefer assisted purchasing or connectivity is poor, retain a human-supported path with the same terms and order reference.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OVE-CRM04-OS-CAP01:** transparent digital purchase orchestration. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OVE-CRM04-OS-VS01:** Discover → check eligibility → show total terms → confirm intent → authorize payment → receive order acknowledgment.

**Objects to distinguish:** catalog item, eligibility, cart, quote/price version, payment authorization and order acknowledgment.

**Proposed responsibility:** Commerce owns catalog presentation and checkout intent; pricing supplies approved prices; payment services own authorization; order management accepts the order. CRM04 ends at a governed purchase handoff.

**Protected boundary:** A browser success page is not proof that payment settled, the order was accepted or the service was delivered.

Use SAP CX and adjacent services as optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. CRM01–CRM12 are curriculum themes; the twelve architecture streams are a separate axis. This sprint focuses application responsibility while referencing data, experience, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OVE-CRM04-OS-SYN001**. Keep everything on one card or screen.

1. **Need:** customer outcome, affected population and one missing fact.
2. **Evidence:** relevant object IDs, source, validity/effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and customer-visible message.
5. **Alternative:** Compare optimistic success messaging with an acknowledged order state and recoverable pending experience.
6. **Exception:** one failure state, escalation owner and safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop/revise/proceed decision.

**Requirement — OVE-CRM04-OS-REQ01:** show accurate total terms and distinguish pending, accepted and failed purchase states with safe retry.

**Decision — OVE-CRM04-OS-ADR01:** record your chosen option and alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — Eligibility fails after cart creation

**Expected:** Explain the restriction before commitment; preserve the customer's ability to change or exit.

### T02 — Timeout followed by repeat click

**Expected:** Reuse the attempt reference and check existing outcome before another charge/order.

### T03 — Payment authorized but order rejected

**Expected:** Show unresolved status, assign reconciliation and apply the approved release/refund process.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OVE-CRM04-OS-T01/T02/T03, supporting OVE-CRM04-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OVE-CRM04-OS-KPI01:** Confirmed checkout completion: accepted orders / valid checkout attempts, excluding retries under a documented rule. Assign the lead as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

**Acceptance:** the card identifies source/owner, preserves the protected boundary, handles all three tests after documented revisions and explains the decision in 60 seconds. Missing evidence remains visible. Record what is still unverified.

## 7. Use your 120 minutes

- **0–20:** read the origin timeline; explain what changed and what did not.
- **20–45:** role-play the story; ask the lead, counterpart and customer one useful question each.
- **45–65:** draw responsibilities and consult one resource selectively.
- **65–100:** complete the single Decision Card and compare the alternative.
- **100–115:** run the three tests; revise from observed paper behavior.
- **115–120:** explain the decision in 60 seconds and choose the next experiment.

All reading fits within these blocks. Do not complete an entire product course during the sprint.

## 8. Read with a question

- [SAP CX learning portfolio](https://learning.sap.com/products/customer-experience): select the resource for commerce and confirmed transaction states. Which responsibility belongs to which application?
- [SAP lead-to-cash integration lesson](https://learning.sap.com/courses/exploring-ai-driven-lead-to-cash-in-sap-customer-experience/integrating-sap-customer-experience-solutions-within-the-lead-to-cash-process_f21f46c5-96bf-4d39-852d-f14814b55db8): inspect the relevant handoff. What does the receiver need to confirm?
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework): optional next-step references. Who owns risk and permitted information use?

Official reference pages checked 31 October 2026; access, product versions and licensed capabilities can vary. The historical periodization and future stories are educational synthesis, not claims established by these product pages.

## 9. Reflect and continue

What became easier for the customer? Who might still be excluded? What evidence would make you reject your current design?

**Next Pre-Foundation experiment:** define one checkout state transition and its timeout recovery.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniVerse executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md): fictional enterprise baseline. Existing targets remain targets.
- [Customer-experience blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/02-customer-experience.md): retail/digital services, outage communication and Customer 360 scope; inherited anchors OVE-M02, OVE-M10, OVE-M12 and OVE-M20.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md): existing names, designations and OVE-P identifiers.
- [CRM academy source](https://app.notion.com/p/b65e0b41255b4fcaa6c4fea15197f44a): twelve curriculum theme definitions.
- **New material:** OVE-CRM04-OS is a new sprint-local namespace. Scenario, requirement, alternative, tests and measure are proposed learning designs, not an already-approved enterprise implementation.

**Trace:** source blueprint → OVE-CRM04-OS-CAP01 → OVE-CRM04-OS-VS01 → OVE-CRM04-OS-REQ01 → OVE-CRM04-OS-ADR01 → OVE-CRM04-OS-EXP01 (this tabletop experiment) → OVE-CRM04-OS-T01/T02/T03 → OVE-CRM04-OS-KPI01. OVE-CRM04-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value distinction; BABOK need-to-acceptance trace; DAMA ownership/quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** GitHub sprint with matching manually published Google Doc and Notion edition. No live implementation, achieved customer outcome or unattended synchronization is claimed.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/02-CRM-Customer-Experience-Capability-Academy-Revenue-Tuesday/CRM04-ACO4-Architecting-Digital-Commerce-Enterprises/01-CRM04-ENE-energy/0-The-Origin-Story/sprint/energy-crm04-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1p_8gH8pDkuovcNn40P1A-FbKJUqQRLdTxWeEACw6-qI/edit?usp=drivesdk) · [Notion edition](https://app.notion.com/p/409ce6de608981c19c2ef2906a492494?pvs=204)
