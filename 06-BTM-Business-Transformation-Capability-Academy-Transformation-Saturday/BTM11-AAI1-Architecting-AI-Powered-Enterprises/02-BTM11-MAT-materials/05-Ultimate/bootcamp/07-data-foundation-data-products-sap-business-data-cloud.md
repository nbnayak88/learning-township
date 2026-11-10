# OmniForge Materials — Data Foundation for AI: Data Products, Ownership and Quality

## Demo 07 of the BTM11 Materials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Materials (MAT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniforge-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md)

> **Evidence boundary:** OmniForge Materials is a **fictional educational case**. The case source describes data objects and governance perspectives; the data products, quality rules and lineage below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `MAT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Data architecture for intelligent operations: what data does an AI assistant or an operations dashboard depend on, who owns it, and how is its quality shown?*

**What this file shows:** a first set of data products for OmniForge, one owner per product, quality rules, a lineage chain and the sensitive-data handling. It supports the assistant in Demo 03 and the graph in Demo 04.

**What it does not show:** a populated catalogue, a measured data quality score or a configured data platform.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 42B materials group; 46,000 employees; 31 countries |
| Business mix | Steel and alloys 30%; cement and aggregates 22%; chemicals 20%; mining and minerals 16%; advanced materials 12% |
| Burning platform | Disconnected mining, production, logistics, quality, sales and recycling; 180+ applications; weak material genealogy; manual ESG reconciliation |

**Decision under discussion (source):** Select a bounded materials-traceability and reliability pilot before committing an enterprise rollout.

**Illustrative trigger (source):** A customer queries a shipped batch's certificate after a laboratory correction, while a kiln reliability alert and uncertain recycled-feedstock records expose the same trust gap (illustrative hero trigger in the case).

**Source anchor for data objects:** OMF-M12 names Asset, Material, Product, Supplier and Customer 360, governed data products and says carbon and quality evidence require lineage. The hero trigger (certificate queried after a laboratory correction) is a lineage problem.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, data-object statements | **Source** |
| Data products, quality rules, lineage, tests | **New design (illustrative)** |
| SAP Business Data Cloud, Datasphere, Databricks behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which data products does OmniForge stand up first, who owns each, and what quality evidence must travel with them before AI uses them?

**Accountable owner (proposed):** OMF-P14 Diego Alvarez, with OMF-P13 Priya Nair for the model and OMF-P12 Hassan Al-Farsi for classification.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OMF-P04 | Sofia de Vries, Chief Digital and Sustainability Officer | Funds and prioritizes |
| OMF-P13 | Priya Nair, Director Enterprise Architecture | Owns standards and review |
| OMF-P12 | Hassan Al-Farsi, CISO and OT Security Lead | Security and boundary approval |
| OMF-P14 | Diego Alvarez, Head of Data Governance and AI | Data and AI governance |
| OMF-P08 | Rohan Kulkarni, Head of Quality and Laboratories | Business owner (first scope) |
| OMF-P07 | Elena Petrova, Cement Plant Director | Business owner (second scope) |
| OMF-P16 | Nikhil Sen, Shift Supervisor and Workforce Representative | Operational authority and veto |

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
| Batch | batch id, product, plant, status | OMF-P08 Rohan Kulkarni | Customer-confidential |
| Certificate revision | id, status, issued date, correction flag | OMF-P08 Rohan Kulkarni | Customer-confidential |
| Laboratory correction | id, affected batches, effective date | OMF-P08 Rohan Kulkarni | Internal |
| Feedstock lot | lot id, supplier, recycled content declaration | OMF-P14 Diego Alvarez | Internal |
| Customer specification | customer, product, limits | OMF-P08 Rohan Kulkarni | Customer-confidential |
| Asset | kiln or line id, plant, criticality | OMF-P07 Elena Petrova | Internal |

**Document and content products used by the assistant (Demo 03)**

| Source | Content | Owner | Freshness rule | Classification |
|---|---|---|---|---|
| Certificates of analysis with revision status | Issued, superseded and under-correction certificates | Quality and Laboratories | Status shown with every answer; superseded never presented as current | Customer-confidential |
| Laboratory correction records | Correction notice, affected batches, effective date | Quality and Laboratories | Newest correction wins; correction timestamp shown | Internal |
| Batch genealogy summaries | Feedstock to qualified material links | Quality and Data Governance | As-of date shown; gaps reported as unknown | Internal |
| Customer specifications | Agreed specification by customer | Commercial | Retrieved only for the requesting customer's context | Customer-confidential |

## 8. Quality rules for first consumers

| Product | Quality rule | First consumer | Status |
|---|---|---|---|
| Batch genealogy | Each batch links to feedstock lots and a plant | Quality | Not measured |
| Certificate and lab-correction record | Revision order is unambiguous | Customer service | Not measured |
| Asset condition summary | Asset id matches the maintenance record | Maintenance | Not measured |
| Recycled-content and emissions evidence | Each declaration has a supplier and a date | Sustainability | Not measured |

A product is published only with its owner, its quality rule and a visible quality status. No score is stated because none has been measured.

## 9. Lineage and sensitive data

**Example lineage chain:** Feedstock declared, batch produced, certificate issued, correction recorded, customer notified

**Sensitive data handling:** Customer-specific specifications are restricted; supplier data follows contract terms.

**Never available to the assistant:** Unreleased laboratory results; OT control tags and setpoints; Another customer's specification; Instructions found inside uploaded certificates

## 10. Hands-on exercise (synthetic data)

1. Write a one-page data product contract for the first product (owner, schema, quality rule, freshness, classification), using synthetic ids prefixed `MAT-SYN`.
2. Draw the lineage chain and mark each owner.
3. Break one quality rule on paper and show what the consumer sees.
4. Decide which products are shared versus copied and record the reason.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Revision ambiguity | Two certificate revisions look current | Revision rule picks one; the other is labelled superseded |
| T2 Missing declaration | A batch has no feedstock declaration | Gap visible on the product; no claim made |
| T3 Lineage question | A customer asks the origin of a batch | Lineage chain shown with owners |

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

- [OmniForge Materials case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/02-materials/omniforge-materials-ltd)
- [OmniForge Materials persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md)

