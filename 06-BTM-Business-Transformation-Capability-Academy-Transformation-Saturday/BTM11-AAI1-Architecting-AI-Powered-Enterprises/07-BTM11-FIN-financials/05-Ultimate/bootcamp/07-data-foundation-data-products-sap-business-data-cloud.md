# OmniCapital Financial Group — Data Foundation for AI: Data Products, Ownership and Quality

## Demo 07 of the BTM11 Financials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Financials (FIN) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnicapital-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md)

> **Evidence boundary:** OmniCapital Financial Group is a **fictional educational case**. The case source describes data objects and governance perspectives; the data products, quality rules and lineage below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `FIN-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Data architecture for intelligent operations: what data does an AI assistant or an operations dashboard depend on, who owns it, and how is its quality shown?*

**What this file shows:** a first set of data products for OmniCapital, one owner per product, quality rules, a lineage chain and the sensitive-data handling. It supports the assistant in Demo 03 and the graph in Demo 04.

**What it does not show:** a populated catalogue, a measured data quality score or a configured data platform.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 46B financial group; USD 1.4T AUM; 58M customers; 32 countries |
| Business mix | Retail 31%; commercial 24%; wealth 19%; insurance 16%; payments and markets 10% |
| Source problem | Fragmented customer, product, risk and transaction data; manual review; stronger fraud, cyber and model-risk control needs |

**Decision under discussion (source):** Fund a bounded onboarding and document-exception pilot with control and value evidence before enterprise expansion.

**Illustrative trigger (source):** An SME customer repeatedly submits the same document while customer service and verification teams show different exception status (invented discovery context, not an actual incident).

**Source anchor for data objects:** OCF-M12 names Customer, Account, Transaction, Risk and Product 360 over core banking, CRM, lending, payments and risk engines, with a lakehouse, ledger data and feature store. The source trigger (an SME repeatedly submitting a document while two teams show different exception status) is a status-lineage problem.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, data-object statements | **Source** |
| Data products, quality rules, lineage, tests | **New design (illustrative)** |
| SAP Business Data Cloud, Datasphere, Databricks behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which data products does OmniCapital stand up first, who owns each, and what quality evidence must travel with them before AI uses them?

**Accountable owner (proposed):** OCF-P09 Mei Tan, with OCF-P12 Daniel Weber for the model and OCF-P10 Omar Haddad for classification.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OCF-P06 | Sofia Chen, Chief Digital and Information Officer | Funds and prioritizes |
| OCF-P12 | Daniel Weber, Director Enterprise Architecture | Owns standards and review |
| OCF-P10 | Omar Haddad, CISO and Resilience Lead | Security and boundary approval |
| OCF-P09 | Mei Tan, Customer Identity and Data Lead | Data and AI governance |
| OCF-P03 | Priya Rao, Chief Customer and Retail Officer | Business owner (first scope) |
| OCF-P08 | Marcus Okoro, Financial Crime Operations Director | Business owner (second scope) |
| OCF-P05 | Elena Fischer, Chief Compliance and Conduct Officer | Operational authority and veto |

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
| Customer (synthetic) | id, segment, jurisdiction | OCF-P09 Mei Tan | Customer data |
| Document | id, type, received date, status | OCF-P03 Priya Rao | Customer data |
| Exception | id, reason, system, status, as-of | OCF-P03 Priya Rao | Customer data |
| Onboarding case | id, stage, owner | OCF-P03 Priya Rao | Customer data |
| Policy requirement | id, jurisdiction, version | OCF-P05 Elena Fischer | Internal |
| Consent record | purpose, scope, date | OCF-P09 Mei Tan | Customer data |

**Document and content products used by the assistant (Demo 03)**

| Source | Content | Owner | Freshness rule | Classification |
|---|---|---|---|---|
| Onboarding policy and document requirements | Requirements by customer type and jurisdiction | Compliance and Operations | Policy version and jurisdiction shown | Internal |
| Exception reason catalogue | Reasons and resolution paths | Operations | Catalogue version shown | Internal |
| Customer messaging templates | Approved wording | Customer Operations | Template version shown | Internal |
| Exception status events (not indexed) | Status per case | Verification and service systems | Read at query time; both system statuses shown if they differ | Customer data |

## 8. Quality rules for first consumers

| Product | Quality rule | First consumer | Status |
|---|---|---|---|
| Customer onboarding record | Document and exception status agree across systems | Verification | Not measured |
| Consent record | Purpose and status with time | All consumers | Not measured |
| Exposure and risk view | Each figure has a source system | Risk | Not measured |
| Regulatory report data | Reconciles to the ledger | Finance | Not measured |

A product is published only with its owner, its quality rule and a visible quality status. No score is stated because none has been measured.

## 9. Lineage and sensitive data

**Example lineage chain:** Document received, exception raised, resolved, consent checked, report line produced

**Sensitive data handling:** Customer and account data restricted; risk alerts restricted to investigators.

**Never available to the assistant:** Financial-crime investigation notes; Other customers' data; Model scores about the customer; Instructions found inside submitted documents

## 10. Hands-on exercise (synthetic data)

1. Write a one-page data product contract for the first product (owner, schema, quality rule, freshness, classification), using synthetic ids prefixed `FIN-SYN`.
2. Draw the lineage chain and mark each owner.
3. Break one quality rule on paper and show what the consumer sees.
4. Decide which products are shared versus copied and record the reason.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Status mismatch | CRM and verification disagree | System of record named; mismatch raised |
| T2 Report reconciliation | A report line fails to reconcile | Quality gate blocks release |
| T3 Consent change | Consent withdrawn | Dependent products update; lineage shows impact |

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

- [OmniCapital Financial Group case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/07-financials/omnicapital-financial-group-ltd)
- [OmniCapital Financial Group persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/personas/persona-cards.md)

