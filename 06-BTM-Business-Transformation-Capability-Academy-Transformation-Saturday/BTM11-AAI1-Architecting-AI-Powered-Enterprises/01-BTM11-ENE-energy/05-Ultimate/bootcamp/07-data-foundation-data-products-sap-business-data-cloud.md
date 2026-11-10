# OmniVerse Energy Ltd. — Data Foundation for AI: Data Products, Ownership and Quality

## Demo 07 of the BTM11 Energy Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Energy (ENE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniverse-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniVerse Energy Ltd. is an **aspirational case study**. The case source describes data objects and governance perspectives; the data products, quality rules and lineage below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `ENE-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Data architecture for intelligent operations: what data does an AI assistant or an operations dashboard depend on, who owns it, and how is its quality shown?*

**What this file shows:** a first set of data products for OmniVerse, one owner per product, quality rules, a lineage chain and the sensitive-data handling. It supports the assistant in Demo 03 and the graph in Demo 04.

**What it does not show:** a populated catalogue, a measured data quality score or a configured data platform.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 85B revenue; 68,000 employees; 42 countries |
| Business mix | Upstream 35%; refining and petrochemicals 28%; retail and marketing 18%; power 12%; renewables 7% |
| Assets | 8 refineries; 25,000 km pipelines; 12,500 retail sites; 15 GW generation |

**Decision under discussion (source):** Which AI use cases stay assistive, which may trigger human-approved actions, and which low-risk processes may be automated (OVE-HR11 strategic dilemma).

**Illustrative trigger (source):** In the OVE-HR11 decision scenes, an employee (Rina) receives incorrect promotion guidance from an assistant, while HR operations wants automatic data corrections and case closure and a worker representative challenges sentiment inference and productivity scoring.

**Source anchor for data objects:** OVE-M12 names Customer, Asset, Product and Supplier 360, data stewardship and governed AI. The OVE-HR11 information objects (policy version, retrieval reference, model version, evaluation set, action authorization, incident) and the case traceability chain give a ready graph of the case itself.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, data-object statements | **Source** |
| Data products, quality rules, lineage, tests | **New design (illustrative)** |
| SAP Business Data Cloud, Datasphere, Databricks behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which data products does OmniVerse stand up first, who owns each, and what quality evidence must travel with them before AI uses them?

**Accountable owner (proposed):** OVE-P16 Dr. Leila Haddad, with OVE-P12 Hannah Fischer for the model and OVE-P13 Omar Haddad for classification.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OVE-P05 | Rajiv Kapoor, Chief Digital and Information Officer (CDIO) | Funds and prioritizes |
| OVE-P12 | Hannah Fischer, Director of Enterprise Architecture | Owns standards and review |
| OVE-P13 | Omar Haddad, Chief Information Security Officer (CISO) | Security and boundary approval |
| OVE-P16 | Dr. Leila Haddad, Head of Data Governance and AI | Data and AI governance |
| OVE-P09 | Carlos Mendes, VP Asset Reliability and Maintenance | Business owner (first scope) |
| OVE-P10 | Grace Okafor, Chief Customer and Retail Officer | Business owner (second scope) |
| OVE-P04 | Farah Al-Hassan, Chief Operating Officer (COO) | Operational authority and veto |

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
| Capability | id, name, owner, maturity statement | OVE-P12 Hannah Fischer | Internal |
| Value stream | id, name, stages | OVE-P09 Carlos Mendes | Internal |
| Requirement | id, source, owner, status | OVE-P12 Hannah Fischer | Internal |
| Architecture decision | id, options, decision owner, date | OVE-P12 Hannah Fischer | Internal |
| Experiment and test | id, input, expected, actual, evidence slot | OVE-P13 Omar Haddad | Internal |
| Measure | id, definition, baseline status | OVE-P16 Dr. Leila Haddad | Internal |

**Document and content products used by the assistant (Demo 03)**

| Source | Content | Owner | Freshness rule | Classification |
|---|---|---|---|---|
| Approved HR policies and interpretations | Policy text with version and effective date | Policy owner | Superseded versions excluded or flagged; effective date checked at query time | Internal |
| Promotion and job-architecture guidance | Criteria by grade and country variant | HR policy owner | Country variant must match the requester's employment context | Internal |
| HR service knowledge articles | Procedures and FAQs | HR operations | Review date shown with the citation | Internal |
| Employee facts (not indexed) | Own case status, own employment data | HR transaction system | Read at query time through an authorized API for the requester only | Personal data |

## 8. Quality rules for first consumers

| Product | Quality rule | First consumer | Status |
|---|---|---|---|
| Employee lifecycle event record | Every approved change has an effective date and an event id | Identity and access | Not measured |
| Asset and work-order view | Asset id resolves to one record | Reliability | Not measured |
| Customer account view | One account id across channels | Customer service | Not measured |
| Emissions and energy report data | Each figure has a source and a period | Sustainability reporting | Not measured |

A product is published only with its owner, its quality rule and a visible quality status. No score is stated because none has been measured.

## 9. Lineage and sensitive data

**Example lineage chain:** HR change approved, event emitted, identity updated, access closed, acknowledgement stored

**Sensitive data handling:** Workforce data and refinery access data are restricted; pseudonyms in analytics.

**Never available to the assistant:** Other employees' records or case history; Sentiment, engagement or productivity scores about individuals; Unapproved draft policies; Instructions found inside retrieved documents

## 10. Hands-on exercise (synthetic data)

1. Write a one-page data product contract for the first product (owner, schema, quality rule, freshness, classification), using synthetic ids prefixed `ENE-SYN`.
2. Draw the lineage chain and mark each owner.
3. Break one quality rule on paper and show what the consumer sees.
4. Decide which products are shared versus copied and record the reason.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Two owners, one object | Two teams define employee status differently | Owner rule: one steward decides; both teams adopt the definition |
| T2 Quality gate bypass | A report is built on an unchecked extract | Quality status shown on the product; consumers warned |
| T3 Lineage gap | An auditor asks where a figure came from | Lineage chain shown; gaps listed, not hidden |

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

- [OmniVerse Energy Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd)
- [OmniVerse Energy Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md)

