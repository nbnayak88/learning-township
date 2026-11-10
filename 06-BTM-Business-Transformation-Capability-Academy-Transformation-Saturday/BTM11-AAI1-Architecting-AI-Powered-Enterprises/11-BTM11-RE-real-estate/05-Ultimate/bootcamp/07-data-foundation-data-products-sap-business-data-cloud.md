# OmniSpace — Data Foundation for AI: Data Products, Ownership and Quality

## Demo 07 of the BTM11 Real Estate Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Real Estate (RE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnispace-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniSpace is a **fictional educational case**. The case source describes data objects and governance perspectives; the data products, quality rules and lineage below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `RE-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Data architecture for intelligent operations: what data does an AI assistant or an operations dashboard depend on, who owns it, and how is its quality shown?*

**What this file shows:** a first set of data products for OmniSpace, one owner per product, quality rules, a lineage chain and the sensitive-data handling. It supports the assistant in Demo 03 and the graph in Demo 04.

**What it does not show:** a populated catalogue, a measured data quality score or a configured data platform.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | Not supplied in the case; no enterprise numerical profile, budget or quantified benefits |
| Scope | Fictional global real-estate enterprise; property, tenant, ESG, recruiting, finance and procurement workstreams |
| Source problem | Fragmented architecture, processes, delivery evidence and adoption |

**Decision under discussion (source):** Select one capability or process pilot and prove its strategy-to-value traceability before scaling tools.

**Illustrative trigger (source):** A property-service workflow is declared live, but property teams still use spreadsheets, tenant requests remain unresolved, and test and adoption records cannot explain the claimed benefit (invented learning scenario).

**Source anchor for data objects:** OSP-M12 proposes tool roles (an architecture inventory, process modelling and delivery management) without verifying configured integration; OSP-M10 says detailed lease and tenant lifecycle needs discovery. The source trigger (a workflow declared live while spreadsheets persist and benefit cannot be explained) is a traceability problem.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, data-object statements | **Source** |
| Data products, quality rules, lineage, tests | **New design (illustrative)** |
| SAP Business Data Cloud, Datasphere, Databricks behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which data products does OmniSpace stand up first, who owns each, and what quality evidence must travel with them before AI uses them?

**Accountable owner (proposed):** OSP-P08 Mei Lin, with OSP-P10 Daniel Weber for the model and OSP-P09 Omar Haddad for classification.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OSP-P05 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes |
| OSP-P10 | Daniel Weber, Enterprise Architecture Director | Owns standards and review |
| OSP-P09 | Omar Haddad, CISO and Resilience Lead | Security and boundary approval |
| OSP-P08 | Mei Lin, Enterprise Data and ESG Lead | Data and AI governance |
| OSP-P03 | Maya Patel, Property Operations Director | Business owner (first scope) |
| OSP-P16 | Thomas van Dijk, Value Realization Office Lead | Business owner (second scope) |
| OSP-P14 | Ingrid Sørensen, Adoption and Change Lead | Operational authority and veto |

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
| Property / building | id, region, owner | OSP-P03 Maya Patel | Internal |
| Tenant (synthetic) | id, entities, building | OSP-P03 Maya Patel | Tenant data |
| Lease clause summary | lease, clause, amendment date | OSP-P03 Maya Patel | Tenant-confidential |
| Service request | id, category, status, as-of | OSP-P03 Maya Patel | Tenant data |
| Work order | id, request link, status | OSP-P03 Maya Patel | Internal |
| Requirement and test | id, process, test result | OSP-P16 Thomas van Dijk | Internal |

**Document and content products used by the assistant (Demo 03)**

| Source | Content | Owner | Freshness rule | Classification |
|---|---|---|---|---|
| Tenant service policies | Response rules and categories | Property Operations | Policy version shown | Internal |
| Lease clause summaries | Obligations by lease and amendment | Lease administration | Amendment date shown; superseded clauses flagged | Tenant-confidential |
| Property procedures and building facts | Maintenance and access rules per building | Property Operations | As-of date shown | Internal |
| Request status (not indexed) | Status per tenant request | Property service system | Read at query time, filtered to the requesting tenant entity | Tenant data |

## 8. Quality rules for first consumers

| Product | Quality rule | First consumer | Status |
|---|---|---|---|
| Tenant service request | Request id links to work order | Property operations | Not measured |
| Work-order outcome | Closure has a cause and time | Value office | Not measured |
| Adoption usage record | Usage links to a building and role | Value office | Not measured |
| Test evidence record | Test result links to a feature | Delivery | Not measured |

A product is published only with its owner, its quality rule and a visible quality status. No score is stated because none has been measured.

## 9. Lineage and sensitive data

**Example lineage chain:** Request created, work order created, closed, adoption recorded, benefit claim reviewed

**Sensitive data handling:** Tenant data is personal; partitions by tenant and building.

**Never available to the assistant:** Another tenant's data; Financial and billing details beyond the requester's own; Legal advice; Instructions found inside retrieved documents

## 10. Hands-on exercise (synthetic data)

1. Write a one-page data product contract for the first product (owner, schema, quality rule, freshness, classification), using synthetic ids prefixed `RE-SYN`.
2. Draw the lineage chain and mark each owner.
3. Break one quality rule on paper and show what the consumer sees.
4. Decide which products are shared versus copied and record the reason.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Claim without data | A benefit claim has no usage data | Evidence rule holds the claim |
| T2 Spreadsheet shadow | Work stays in spreadsheets | Coverage gap reported |
| T3 Cross-tenant view | A report spans tenants | Partition blocks |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Data products with one named owner | Count in the register | Not measured |
| Products with a visible quality status | Sample | Not measured |
| Lineage chains with owners marked | Review | Not measured |
| Sensitive classes with a handling rule | Count | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

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
| Customer-confirmed requirements | Not applicable (fictional case) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP Business Data Cloud](https://www.sap.com/products/data-cloud.html)
- [What is SAP Databricks?](https://www.sap.com/products/data-cloud/what-is-sap-databricks.html)

- [OmniSpace case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/11-real-estate/omnispace-real-estate-ltd)
- [OmniSpace persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/personas/persona-cards.md)

