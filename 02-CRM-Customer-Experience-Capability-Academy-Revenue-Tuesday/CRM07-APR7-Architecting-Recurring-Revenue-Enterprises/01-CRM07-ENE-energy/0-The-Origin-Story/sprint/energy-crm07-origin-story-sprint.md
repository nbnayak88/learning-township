# The subscription ended; the invoices kept arriving
## CRM07 — Architecting Recurring Revenue Enterprises

**SuccessLabs Academy · OmniVerse Energy Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 31 October 2026**  
**Planning reference:** HUB-ORIGIN-CRM07-ENE-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one auditable subscription change that keeps contract, entitlement and billing outcomes consistent.

**One story · One build card · Three tabletop tests**

## 1. Start with the customer

In a proposed energy-monitoring subscription scenario, Elena cancels one site's service midway through a period. The portal says cancelled, the device still reports usage and billing creates another full-period invoice.

**Lead:** Michael Reed — Group Chief Financial Officer (OVE-P03).  
**Counterpart:** Grace Okafor — Chief Customer and Retail Officer (OVE-P10).  
**Customer voice:** Elena Brooks — VP Energy Procurement (OVE-P15).

Elena asks what date the cancellation means. Michael asks which approved rule governs charges. Grace asks whether ending an optional service is being confused with an essential energy-supply decision.

The team versions the change, makes effective dates explicit and separates contract termination, entitlement removal and invoice correction. It asks for policy before calculating any proration.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniVerse is a fictional integrated energy enterprise with 68,000 employees in 42 countries. These new incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniVerse history.

- **1970s–1980s:** Periodic supply/service contracts and paper invoices support repeat business; changes require manual reconciliation.
- **1980s–1990s:** Contract and billing databases automate recurring charges; effective dates can disagree.
- **2000s–2010s:** Subscription and usage-based services link entitlement to consumption; metering evidence and adjustments matter.
- **2020s–2026:** Assisted revenue operations can propose changes; approved policy and financial reconciliation remain necessary.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost: customer, frontline colleague or community?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine a 2050 customer buying a flexible bundle of monitoring and energy services. A broker may suggest changes, but each component needs clear terms, effective time and an accountable billing decision.

**Competing future:** If usage data arrives late or markets change sharply, preserve controlled adjustment and dispute routes rather than assuming perfect real-time data.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OVE-CRM07-OS-CAP01:** subscription lifecycle and billing consistency. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OVE-CRM07-OS-VS01:** Agree terms → activate → measure usage → request change → approve effective date → reconcile bill and entitlement.

**Objects to distinguish:** contract version, subscription, entitlement, usage period, effective date and invoice adjustment.

**Proposed responsibility:** Contract/subscription services own agreed terms; entitlement services own optional-service access; metering owns usage evidence; billing owns invoice calculation; Finance owns financial controls.

**Protected boundary:** This learning scenario adds an optional service; it does not authorize disconnection of essential supply or prescribe regulatory/proration rules.

Use SAP CX and adjacent services as optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. CRM01–CRM12 are curriculum themes; the twelve architecture streams are a separate axis. This sprint focuses application responsibility while referencing data, experience, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OVE-CRM07-OS-SYN001**. Keep everything on one card or screen.

1. **Need:** customer outcome, affected population and one missing fact.
2. **Evidence:** relevant object IDs, source, validity/effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and customer-visible message.
5. **Alternative:** Compare immediate status overwrite with a versioned lifecycle change and reconciliation.
6. **Exception:** one failure state, escalation owner and safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop/revise/proceed decision.

**Requirement — OVE-CRM07-OS-REQ01:** retain approved effective dates and trace the resulting entitlement and billing changes to their confirmed outcomes.

**Decision — OVE-CRM07-OS-ADR01:** record your chosen option and alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — Mid-period cancellation has no approved proration rule

**Expected:** Hold unsupported calculation, seek policy and communicate the pending amount/date decision.

### T02 — Late usage arrives after cancellation

**Expected:** Allocate to the correct period under approved rules; create a traceable adjustment if required.

### T03 — Cancellation message retries

**Expected:** Prevent duplicate financial or entitlement effects and reconcile the receiving states.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OVE-CRM07-OS-T01/T02/T03, supporting OVE-CRM07-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OVE-CRM07-OS-KPI01:** Change reconciliation completeness: approved changes with confirmed contract, entitlement and billing outcomes / changes due. Assign the lead as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

- [SAP CX learning portfolio](https://learning.sap.com/products/customer-experience): select the resource for recurring revenue and lead-to-cash responsibility. Which responsibility belongs to which application?
- [SAP lead-to-cash integration lesson](https://learning.sap.com/courses/exploring-ai-driven-lead-to-cash-in-sap-customer-experience/integrating-sap-customer-experience-solutions-within-the-lead-to-cash-process_f21f46c5-96bf-4d39-852d-f14814b55db8): inspect the relevant handoff. What does the receiver need to confirm?
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework): optional next-step references. Who owns risk and permitted information use?

Official reference pages checked 31 October 2026; access, product versions and licensed capabilities can vary. The historical periodization and future stories are educational synthesis, not claims established by these product pages.

## 9. Reflect and continue

What became easier for the customer? Who might still be excluded? What evidence would make you reject your current design?

**Next Pre-Foundation experiment:** define one subscription effective-date rule and its billing acceptance test.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniVerse executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md): fictional enterprise baseline. Existing targets remain targets.
- [Customer-experience blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/02-customer-experience.md): retail/digital services, outage communication and Customer 360 scope; inherited anchors OVE-M02, OVE-M10, OVE-M12 and OVE-M20.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md): existing names, designations and OVE-P identifiers.
- [CRM academy source](https://app.notion.com/p/b65e0b41255b4fcaa6c4fea15197f44a): twelve curriculum theme definitions.
- **New material:** OVE-CRM07-OS is a new sprint-local namespace. Scenario, requirement, alternative, tests and measure are proposed learning designs, not an already-approved enterprise implementation.

**Trace:** source blueprint → OVE-CRM07-OS-CAP01 → OVE-CRM07-OS-VS01 → OVE-CRM07-OS-REQ01 → OVE-CRM07-OS-ADR01 → OVE-CRM07-OS-EXP01 (this tabletop experiment) → OVE-CRM07-OS-T01/T02/T03 → OVE-CRM07-OS-KPI01. OVE-CRM07-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value distinction; BABOK need-to-acceptance trace; DAMA ownership/quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** GitHub sprint with matching manually published Google Doc and Notion edition. No live implementation, achieved customer outcome or unattended synchronization is claimed.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/02-CRM-Customer-Experience-Capability-Academy-Revenue-Tuesday/CRM07-APR7-Architecting-Recurring-Revenue-Enterprises/01-CRM07-ENE-energy/0-The-Origin-Story/sprint/energy-crm07-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1hkJet-XPilgSrtHHwaOlxn2mByR0tOKxdgLoznyNQmc/edit?usp=drivesdk) · [Notion edition](https://app.notion.com/p/409ce6de608981fbae61efcf9e50611f?pvs=204)
