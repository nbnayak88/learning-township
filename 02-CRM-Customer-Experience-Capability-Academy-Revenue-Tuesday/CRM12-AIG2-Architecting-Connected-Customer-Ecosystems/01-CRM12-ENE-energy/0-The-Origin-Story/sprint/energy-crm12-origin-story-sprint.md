# The message arrived; the customer's service did not change
## CRM12 — Architecting Connected Customer Ecosystems

**SuccessLabs Academy · OmniVerse Energy Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 31 October 2026**  
**Planning reference:** HUB-ORIGIN-CRM12-ENE-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one observable customer event exchange with safe retry and confirmed business outcome.

**One story · One build card · Three tabletop tests**

## 1. Start with the customer

Elena changes a billing contact. The integration monitor reports success, but one receiving application rejects the account relationship and another replays an older address.

**Lead:** Rajiv Kapoor — Chief Digital and Information Officer (OVE-P05).  
**Counterpart:** Hannah Fischer — Director of Enterprise Architecture (OVE-P12).  
**Customer voice:** Elena Brooks — VP Energy Procurement (OVE-P15).

Rajiv asks whether the platform delivered bytes or completed a business change. Hannah asks which source owns the contact and what 'latest' means when messages arrive out of order.

The team defines event identity, source authority, effective time, schema version and receiving acceptance. A technical acknowledgment becomes one checkpoint rather than the final outcome.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniVerse is a fictional integrated energy enterprise with 68,000 employees in 42 countries. These new incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniVerse history.

- **1970s–1980s:** Paper transfers and re-entry move facts slowly; discrepancies are found by reconciliation.
- **1980s–1990s:** Batch files and EDI automate exchanges; silent rejects and timing gaps remain.
- **2000s–2010s:** APIs and event services connect channels and ERP; transport success still differs from application acceptance.
- **2020s–2026:** Observable orchestration and assisted recovery reduce delays; ordering, authority and safe replay remain essential.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost: customer, frontline colleague or community?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine a 2050 multi-party energy-services ecosystem. Agents may negotiate exchanges, but participants must still agree identifiers, contracts, ownership and accountable failure handling.

**Competing future:** In a fragmented or disconnected ecosystem, durable queues, versioned contracts and manual reconciliation remain useful.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OVE-CRM12-OS-CAP01:** governed customer ecosystem exchange. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OVE-CRM12-OS-VS01:** Authorize change → emit → validate → apply once → acknowledge outcome → reconcile → recover.

**Objects to distinguish:** source object ID, event ID, business key, effective time, processing time, schema version and business acknowledgment.

**Proposed responsibility:** Domain applications own business facts; integration owns delivery/validation/recovery; receivers own application acceptance; domain owners resolve conflicting meaning. CRM12 does not redefine CRM01 identity policy or CRM07 billing rules.

**Protected boundary:** HTTP success, broker delivery and business completion are different. No message may directly bypass OT security boundaries.

Use SAP CX and adjacent services as optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. CRM01–CRM12 are curriculum themes; the twelve architecture streams are a separate axis. This sprint focuses application responsibility while referencing data, experience, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OVE-CRM12-OS-SYN001**. Keep everything on one card or screen.

1. **Need:** customer outcome, affected population and one missing fact.
2. **Evidence:** relevant object IDs, source, validity/effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and customer-visible message.
5. **Alternative:** Compare transport-only monitoring with business acknowledgments and reconciliation by stable event/business key.
6. **Exception:** one failure state, escalation owner and safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop/revise/proceed decision.

**Requirement — OVE-CRM12-OS-REQ01:** trace one authorized source change through receiving outcomes, visible exceptions and a controlled replay.

**Decision — OVE-CRM12-OS-ADR01:** record your chosen option and alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — Target rejects a validly delivered message

**Expected:** Keep the business change incomplete, assign the exception and reconcile after repair.

### T02 — Duplicate or older event arrives

**Expected:** Avoid duplicate effects and stale overwrite using the agreed idempotency/order rule.

### T03 — Recovery replays a previously accepted event

**Expected:** Prove replay safety and confirm final business state; quarantine conflicts rather than force overwrite.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OVE-CRM12-OS-T01/T02/T03, supporting OVE-CRM12-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OVE-CRM12-OS-KPI01:** Business acknowledgment coverage: in-scope events with confirmed receiver outcome / events due, with aging of unresolved exceptions. Assign the lead as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

- [SAP CX learning portfolio](https://learning.sap.com/products/customer-experience): select the resource for experience integration and lead-to-cash handoffs. Which responsibility belongs to which application?
- [SAP lead-to-cash integration lesson](https://learning.sap.com/courses/exploring-ai-driven-lead-to-cash-in-sap-customer-experience/integrating-sap-customer-experience-solutions-within-the-lead-to-cash-process_f21f46c5-96bf-4d39-852d-f14814b55db8): inspect the relevant handoff. What does the receiver need to confirm?
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework): optional next-step references. Who owns risk and permitted information use?

Official reference pages checked 31 October 2026; access, product versions and licensed capabilities can vary. The historical periodization and future stories are educational synthesis, not claims established by these product pages.

## 9. Reflect and continue

What became easier for the customer? Who might still be excluded? What evidence would make you reject your current design?

**Next Pre-Foundation experiment:** write one event contract and demonstrate safe duplicate/reordered processing.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniVerse executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md): fictional enterprise baseline. Existing targets remain targets.
- [Customer-experience blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/02-customer-experience.md): retail/digital services, outage communication and Customer 360 scope; inherited anchors OVE-M02, OVE-M10, OVE-M12 and OVE-M20.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md): existing names, designations and OVE-P identifiers.
- [CRM academy source](https://app.notion.com/p/b65e0b41255b4fcaa6c4fea15197f44a): twelve curriculum theme definitions.
- **New material:** OVE-CRM12-OS is a new sprint-local namespace. Scenario, requirement, alternative, tests and measure are proposed learning designs, not an already-approved enterprise implementation.

**Trace:** source blueprint → OVE-CRM12-OS-CAP01 → OVE-CRM12-OS-VS01 → OVE-CRM12-OS-REQ01 → OVE-CRM12-OS-ADR01 → OVE-CRM12-OS-EXP01 (this tabletop experiment) → OVE-CRM12-OS-T01/T02/T03 → OVE-CRM12-OS-KPI01. OVE-CRM12-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value distinction; BABOK need-to-acceptance trace; DAMA ownership/quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** GitHub sprint with matching manually published Google Doc and Notion edition. No live implementation, achieved customer outcome or unattended synchronization is claimed.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/02-CRM-Customer-Experience-Capability-Academy-Revenue-Tuesday/CRM12-AIG2-Architecting-Connected-Customer-Ecosystems/01-CRM12-ENE-energy/0-The-Origin-Story/sprint/energy-crm12-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1TR7x2jLUypeRPgG67I1zeLBiR1gE5YHc3naYkpRSCi8/edit?usp=drivesdk) · [Notion edition](https://app.notion.com/p/409ce6de60898134b1b7d9292a35ca66?pvs=204)
