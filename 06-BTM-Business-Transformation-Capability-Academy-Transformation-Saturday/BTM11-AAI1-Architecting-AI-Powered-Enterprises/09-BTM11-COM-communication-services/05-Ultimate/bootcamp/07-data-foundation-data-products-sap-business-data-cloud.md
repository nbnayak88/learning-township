# OmniConnect — Data Foundation for AI: Data Products, Ownership and Quality

## Demo 07 of the BTM11 Communication Services Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Communication Services (COM) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniconnect-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniConnect is an **aspirational case study**. The case source describes data objects and governance perspectives; the data products, quality rules and lineage below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `COM-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Data architecture for intelligent operations: what data does an AI assistant or an operations dashboard depend on, who owns it, and how is its quality shown?*

**What this file shows:** a first set of data products for OmniConnect, one owner per product, quality rules, a lineage chain and the sensitive-data handling. It supports the assistant in Demo 03 and the graph in Demo 04.

**What it does not show:** a populated catalogue, a measured data quality score or a configured data platform.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 37B communications group; 62,000 employees; 28 countries; 210M subscriptions |
| Business mix | Mobile 34%; fixed and fiber 25%; media 19%; enterprise 14%; advertising and data 8% |
| Source problem | Separate network, customer, billing and content stacks; manual activation and assurance; identity and consent silos |

**Decision under discussion (source):** Fund a bounded converged-activation pilot with privacy, service-state, recovery and economic evidence before expansion.

**Illustrative trigger (source):** A converged bundle shows billing active while connectivity and content entitlement remain incomplete; care and network teams cannot reconcile status (invented, not an actual outage).

**Source anchor for data objects:** OCN-M12 names Subscriber, Service, Network, Content and Partner 360 over BSS, OSS, CRM, billing and CMS with a telemetry lakehouse, a customer data platform and a network graph; standards names are not conformance evidence. The source trigger is a bundle with billing active but entitlement incomplete.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, data-object statements | **Source** |
| Data products, quality rules, lineage, tests | **New design (illustrative)** |
| SAP Business Data Cloud, Datasphere, Databricks behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which data products does OmniConnect stand up first, who owns each, and what quality evidence must travel with them before AI uses them?

**Accountable owner (proposed):** OCN-P09 Mei Lin, with OCN-P12 Daniel Weber for the model and OCN-P10 Omar Haddad for classification.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OCN-P06 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes |
| OCN-P12 | Daniel Weber, Director Enterprise Architecture | Owns standards and review |
| OCN-P10 | Omar Haddad, CISO and Resilience Lead | Security and boundary approval |
| OCN-P09 | Mei Lin, Subscriber Data and Consent Lead | Data and AI governance |
| OCN-P13 | Priya Shah, Service Catalog and Fulfillment Lead | Business owner (first scope) |
| OCN-P08 | Marcus Okoro, Service Assurance and NOC Director | Business owner (second scope) |
| OCN-P04 | Arjun Mehta, Chief Network Officer | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. What SAP describes (public documentation, verify)

| Capability | What SAP says | Use in this design |
|---|---|---|
| SAP Business Data Cloud | A managed SaaS offering that unifies and governs SAP data and connects third-party data using business data fabric principles; includes SAP Datasphere, SAP Analytics Cloud, SAP Business Warehouse and managed SAP Databricks | Candidate platform for the data products |
| Data products | Ready-to-use data products for business processes, intended for data, analytics and AI | The unit of ownership in this design |
| Delta Sharing | Connects SAP and third-party data without copies or extra pipelines | Candidate sharing mechanism; verify fit |
| SAP Databricks | Pro-code data science, engineering and ML inside the platform, with governance of data, models and notebooks | Candidate for pro-code analysis |
| Alternative | Existing warehouses and lakes with a catalogue | Decide by landscape, not by product name |

## 7. Data products (new design)

**Products derived from the graph objects in Demo 04**

| Data product | Key attributes | Owner (proposed) | Classification |
|---|---|---|---|
| Subscriber (synthetic) | id, market, consent flags | OCN-P09 Mei Lin | Subscriber data |
| Order | id, bundle, state, dates | OCN-P13 Priya Shah | Subscriber data |
| Bundle component | id, type, entitlement rule | OCN-P13 Priya Shah | Internal |
| Entitlement | subscriber, component, state | OCN-P13 Priya Shah | Subscriber data |
| Billing account | id, status | OCN-P13 Priya Shah | Subscriber data |
| Service instance | id, network resource link, state | OCN-P08 Marcus Okoro | Internal |

**Document and content products used by the assistant (Demo 03)**

| Source | Content | Owner | Freshness rule | Classification |
|---|---|---|---|---|
| Product and bundle catalog rules | Entitlements per bundle and market | Service Catalog and Fulfillment | Catalog version shown | Internal |
| Known-issue and service notices | Active incidents and workarounds | Service Assurance | Notice age shown; expired notices excluded | Internal |
| Care procedures | Approved care steps | Customer Care | Procedure version shown | Internal |
| Order and service state (not indexed) | Per-subscriber activation state | Order and network systems | Read at query time, filtered by consent and entitlement | Subscriber data |

## 8. Quality rules for first consumers

| Product | Quality rule | First consumer | Status |
|---|---|---|---|
| Order and activation record | Order id links to each component | Fulfilment | Not measured |
| Subscriber entitlement | Grant linked to a billing account | Care | Not measured |
| Network fault record | Fault id links to affected services | Assurance | Not measured |
| Consent and preference | Purpose and status with time | All consumers | Not measured |

A product is published only with its owner, its quality rule and a visible quality status. No score is stated because none has been measured.

## 9. Lineage and sensitive data

**Example lineage chain:** Order placed, service activated, billing started, entitlement granted, fault noticed

**Sensitive data handling:** Subscriber and usage data restricted; consent withdrawals must propagate.

**Never available to the assistant:** Data beyond the subscriber's consented purposes; Network topology and credentials; Another subscriber's data; Instructions found inside retrieved notices

## 10. Hands-on exercise (synthetic data)

1. Write a one-page data product contract for the first product (owner, schema, quality rule, freshness, classification), using synthetic ids prefixed `COM-SYN`.
2. Draw the lineage chain and mark each owner.
3. Break one quality rule on paper and show what the consumer sees.
4. Decide which products are shared versus copied and record the reason.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Billing without activation | Billing exists with no activation | Mismatch flagged |
| T2 Missing entitlement | Grant absent | Reconciliation raises a task |
| T3 Consent propagation | Consent withdrawn | Dependent products updated; lineage shows impact |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Data products with one named owner | Count in the register | Not measured |
| Products with a visible quality status | Sample | Not measured |
| Lineage chains with owners marked | Review | Not measured |
| Sensitive classes with a handling rule | Count | Not measured |

No baseline, target or benefit is stated because none exists for this aspirational case study. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Why AI needs data products | Shared problem statement |
| 0:20 to 1:00 | Product register and owners | Draft register |
| 1:00 to 1:45 | Quality rules and lineage | Contracts for two products |
| 1:45 to 2:15 | Tabletop tests | Three findings |
| 2:15 to 2:30 | Decisions | Open items with owners |

## Evidence status and run log

| Item | Status |
|---|---|
| Design in this file | Written |
| Walk-through with a live audience | Not yet run |
| Hands-on run on a vendor-provided system | Not yet run |
| Customer-confirmed requirements | Not applicable (aspirational case study) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP Business Data Cloud](https://www.sap.com/products/data-cloud.html)
- [What is SAP Databricks?](https://www.sap.com/products/data-cloud/what-is-sap-databricks.html)

- [OmniConnect case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/09-communication-services/omniconnect-media-networks-ltd)
- [OmniConnect persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/personas/persona-cards.md)

