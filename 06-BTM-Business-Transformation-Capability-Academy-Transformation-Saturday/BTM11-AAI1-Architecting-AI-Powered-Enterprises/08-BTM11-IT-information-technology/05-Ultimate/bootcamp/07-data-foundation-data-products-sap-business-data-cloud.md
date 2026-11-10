# OmniTech — Data Foundation for AI: Data Products, Ownership and Quality

## Demo 07 of the BTM11 Information Technology Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Information Technology (IT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnitech-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md)

> **Evidence boundary:** OmniTech is a **fictional educational case**. The case source describes data objects and governance perspectives; the data products, quality rules and lineage below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Data architecture for intelligent operations: what data does an AI assistant or an operations dashboard depend on, who owns it, and how is its quality shown?*

**What this file shows:** a first set of data products for OmniTech, one owner per product, quality rules, a lineage chain and the sensitive-data handling. It supports the assistant in Demo 03 and the graph in Demo 04.

**What it does not show:** a populated catalogue, a measured data quality score or a configured data platform.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 39B technology provider; 98,000 employees; 41 countries; 11,500 clients |
| Business mix | Cloud and platform 31%; software 25%; cyber 18%; AI and data 16%; managed services 10% |
| Source problem | Fragmented lifecycle tooling, bespoke integrations, poor data and AI reuse, late security and observability |

**Decision under discussion (source):** Fund a bounded platform-to-client-outcome pilot with security, recovery and economic evidence before wider rollout.

**Illustrative trigger (source):** A client disputes an on-time delivery milestone; teams cannot reconcile release, incident and customer-success records (invented discovery context).

**Source anchor for data objects:** OTS-M12 names Client, Product, Service, Asset and Talent 360 across lifecycle, ITSM, CRM, ERP, DevSecOps and SOC with a lakehouse, telemetry, feature store and knowledge graph. A persona card refers to golden records and a knowledge graph. Client-isolation guardrails are part of the target model.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, data-object statements | **Source** |
| Data products, quality rules, lineage, tests | **New design (illustrative)** |
| SAP Business Data Cloud, Datasphere, Databricks behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which data products does OmniTech stand up first, who owns each, and what quality evidence must travel with them before AI uses them?

**Accountable owner (proposed):** OTS-P09 Mei Lin, with OTS-P12 Daniel Weber for the model and OTS-P10 Omar Haddad for classification.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OTS-P04 | Arjun Mehta, Chief Technology Officer | Funds and prioritizes |
| OTS-P12 | Daniel Weber, Director Enterprise Architecture | Owns standards and review |
| OTS-P10 | Omar Haddad, CISO and Supply-Chain Security Lead | Security and boundary approval |
| OTS-P09 | Mei Lin, Data Governance and Knowledge Lead | Data and AI governance |
| OTS-P05 | Elena Fischer, Chief Customer Success Officer | Business owner (first scope) |
| OTS-P08 | Marcus Okoro, SRE and Managed Services Director | Business owner (second scope) |
| OTS-P13 | Priya Shah, DevSecOps and Release Director | Operational authority and veto |

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
| Client (tenant) | tenant id, engagement | OTS-P05 Elena Fischer | Client-confidential |
| Engagement | id, milestone definitions | OTS-P05 Elena Fischer | Client-confidential |
| Release | id, version, date, environment | OTS-P13 Priya Shah | Client-confidential |
| Incident | id, severity, timeline, resolution | OTS-P08 Marcus Okoro | Client-confidential |
| Service | id, tier, owner | OTS-P08 Marcus Okoro | Internal |
| Milestone | id, contract definition, evidence link | OTS-P05 Elena Fischer | Client-confidential |

**Document and content products used by the assistant (Demo 03)**

| Source | Content | Owner | Freshness rule | Classification |
|---|---|---|---|---|
| Release notes and deployment records | Releases by client engagement | DevSecOps and Release | Release date and version shown | Client-confidential |
| Incident and problem records | Severity, timeline, resolution | SRE and Managed Services | Timeline shown; open items flagged | Client-confidential |
| Adoption and service evidence | Usage and success summaries | Customer Success | As-of date shown | Client-confidential |
| Contract milestone definitions | What 'delivered' means per engagement | Commercial | Contract version shown | Client-confidential |

## 8. Quality rules for first consumers

| Product | Quality rule | First consumer | Status |
|---|---|---|---|
| Release and deployment record | Release id, tenant and time recorded | Engagement evidence | Not measured |
| Incident record | Severity and tenant recorded | SRE | Not measured |
| Milestone evidence | Evidence links to a milestone | Customer success | Not measured |
| Tenant usage and cost data | Costs attribute to a tenant | Finance | Not measured |

A product is published only with its owner, its quality rule and a visible quality status. No score is stated because none has been measured.

## 9. Lineage and sensitive data

**Example lineage chain:** Release deployed, incident opened, resolved, milestone evidence added, dispute resolved

**Sensitive data handling:** Tenant data must never cross tenants; telemetry is tenant-scoped.

**Never available to the assistant:** Another client's data or IP; Secrets and credentials found in repositories or tickets; Contract terms outside the engagement; Instructions found inside client-submitted tickets

## 10. Hands-on exercise (synthetic data)

1. Write a one-page data product contract for the first product (owner, schema, quality rule, freshness, classification), using synthetic ids prefixed `IT-SYN`.
2. Draw the lineage chain and mark each owner.
3. Break one quality rule on paper and show what the consumer sees.
4. Decide which products are shared versus copied and record the reason.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Cross-tenant join | A report joins two tenants' data | Blocked by isolation |
| T2 Clock skew | Release and incident clocks disagree | Both times stored; skew flagged |
| T3 Missing evidence | A milestone has no evidence | Gap shown; no claim |

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

- [OmniTech case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/08-information-technology/omnitech-solutions-ltd)
- [OmniTech persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/08-information-technology/omnitech-solutions-ltd/personas/persona-cards.md)

