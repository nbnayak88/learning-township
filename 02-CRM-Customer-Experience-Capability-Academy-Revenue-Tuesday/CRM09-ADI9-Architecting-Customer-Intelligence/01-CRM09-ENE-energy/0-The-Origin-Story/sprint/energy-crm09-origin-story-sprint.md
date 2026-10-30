# Three dashboards agreed only because nobody asked what customer meant
## CRM09 — Architecting Customer Intelligence

**SuccessLabs Academy · OmniVerse Energy Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 31 October 2026**  
**Planning reference:** HUB-ORIGIN-CRM09-ENE-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one decision-ready customer measure with a clear population, source lineage and uncertainty.

**One story · One build card · Three tabletop tests**

## 1. Start with the customer

A retention report mixes industrial accounts, retail contacts and anonymous sessions. A churn model flags Elena's organization because a site moved to another account code.

**Lead:** Dr. Leila Haddad — Head of Data Governance and AI (OVE-P16).  
**Counterpart:** Grace Okafor — Chief Customer and Retail Officer (OVE-P10).  
**Customer voice:** Elena Brooks — VP Energy Procurement (OVE-P15).

Grace asks which customers need attention. Leila asks whether the report counts people, accounts or contracts. Elena says an administrative change should not become a claim that her business is leaving.

The team chooses one population and period, traces source changes and checks a small sample. It separates descriptive measures from predictions and proposed actions.

**Pause:** What does the customer need to be true? Which fact is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniVerse is a fictional integrated energy enterprise with 68,000 employees in 42 countries. These new incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniVerse history.

- **1970s–1980s:** Sales totals and local summaries guide decisions; definitions and populations are implicit.
- **1980s–1990s:** Data warehouses standardize reporting; reconciliation is still needed across source systems.
- **2000s–2010s:** Digital analytics and customer-data platforms connect behavior; identity, consent/purpose and event meaning remain important.
- **2020s–2026:** Predictive and generative insights accelerate analysis; uncertainty, bias and actionable evidence require scrutiny.

**Mindset shift:** start with the decision and its evidence, then choose the application. Digitizing an unclear process can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost: customer, frontline colleague or community?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to prepare the low-risk part of this journey; retain the evidence gate, accountable owner and human challenge route.

**2040 question:** if providers and channels change, can the customer carry the necessary evidence without losing choice, privacy or a usable non-AI route?

**2050 scene:** Imagine a 2050 customer dashboard receiving signals from multiple trusted partners. More signals do not remove the need for provenance, purpose and a meaningful decision population.

**Competing future:** If data sharing contracts shrink, a smaller transparent measure may outperform an opaque comprehensive score.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OVE-CRM09-OS-CAP01:** governed customer decision intelligence. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OVE-CRM09-OS-VS01:** Frame question → define population → inspect lineage → calculate → validate sample → decide action.

**Objects to distinguish:** metric definition, population, time window, source event, identity mapping and model/estimate version.

**Proposed responsibility:** Source applications own business facts; customer-data stewardship owns identity links; analytics owns definitions and calculations; business owners approve consequential actions. CRM09 consumes governed facts without silently correcting them.

**Protected boundary:** Correlation or a model score does not prove customer intent, causation or permission to act.

Use SAP CX and adjacent services as optional demonstration candidates, selected after requirements. No product is assumed installed, licensed or able to cover the whole journey. CRM01–CRM12 are curriculum themes; the twelve architecture streams are a separate axis. This sprint focuses application responsibility while referencing data, experience, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OVE-CRM09-OS-SYN001**. Keep everything on one card or screen.

1. **Need:** customer outcome, affected population and one missing fact.
2. **Evidence:** relevant object IDs, source, validity/effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and customer-visible message.
5. **Alternative:** Compare a blended customer count with a scoped metric and explicit reconciliation.
6. **Exception:** one failure state, escalation owner and safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop/revise/proceed decision.

**Requirement — OVE-CRM09-OS-REQ01:** publish the measure with population, time basis, lineage, exclusions and uncertainty before using it for action.

**Decision — OVE-CRM09-OS-ADR01:** record your chosen option and alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — Contact and account counts are combined

**Expected:** Separate units and denominators; do not present the sum as unique customers.

### T02 — Account-code change triggers churn alert

**Expected:** Check lineage and underlying relationship; hold unsupported retention action.

### T03 — Small cohort reveals individual behavior

**Expected:** Restrict disclosure and escalate privacy review; provide an appropriate aggregate.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OVE-CRM09-OS-T01/T02/T03, supporting OVE-CRM09-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OVE-CRM09-OS-KPI01:** Metric lineage completeness: published in-scope measures with approved definition/source/owner / measures reviewed. Assign the lead as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

- [SAP CX learning portfolio](https://learning.sap.com/products/customer-experience): select the resource for customer data and analytics definitions. Which responsibility belongs to which application?
- [SAP lead-to-cash integration lesson](https://learning.sap.com/courses/exploring-ai-driven-lead-to-cash-in-sap-customer-experience/integrating-sap-customer-experience-solutions-within-the-lead-to-cash-process_f21f46c5-96bf-4d39-852d-f14814b55db8): inspect the relevant handoff. What does the receiver need to confirm?
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework): optional next-step references. Who owns risk and permitted information use?

Official reference pages checked 31 October 2026; access, product versions and licensed capabilities can vary. The historical periodization and future stories are educational synthesis, not claims established by these product pages.

## 9. Reflect and continue

What became easier for the customer? Who might still be excluded? What evidence would make you reject your current design?

**Next Pre-Foundation experiment:** write one customer metric definition and reconcile a small synthetic sample.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniVerse executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md): fictional enterprise baseline. Existing targets remain targets.
- [Customer-experience blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/02-customer-experience.md): retail/digital services, outage communication and Customer 360 scope; inherited anchors OVE-M02, OVE-M10, OVE-M12 and OVE-M20.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md): existing names, designations and OVE-P identifiers.
- [CRM academy source](https://app.notion.com/p/b65e0b41255b4fcaa6c4fea15197f44a): twelve curriculum theme definitions.
- **New material:** OVE-CRM09-OS is a new sprint-local namespace. Scenario, requirement, alternative, tests and measure are proposed learning designs, not an already-approved enterprise implementation.

**Trace:** source blueprint → OVE-CRM09-OS-CAP01 → OVE-CRM09-OS-VS01 → OVE-CRM09-OS-REQ01 → OVE-CRM09-OS-ADR01 → OVE-CRM09-OS-EXP01 (this tabletop experiment) → OVE-CRM09-OS-T01/T02/T03 → OVE-CRM09-OS-KPI01. OVE-CRM09-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value distinction; BABOK need-to-acceptance trace; DAMA ownership/quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** GitHub sprint with matching manually published Google Doc and Notion edition. No live implementation, achieved customer outcome or unattended synchronization is claimed.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/02-CRM-Customer-Experience-Capability-Academy-Revenue-Tuesday/CRM09-ADI9-Architecting-Customer-Intelligence/01-CRM09-ENE-energy/0-The-Origin-Story/sprint/energy-crm09-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1Pp8IUFt49VMEHbRWitLVlZ1nJU8Wbqgei-jpy34CnRs/edit?usp=drivesdk) · [Notion edition](https://app.notion.com/p/409ce6de60898196a1f4c07ce57fa357?pvs=204)
