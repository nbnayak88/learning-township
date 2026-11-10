# OmniVerse Energy Ltd. — Operating Model and FinOps for Intelligent Operations

## Demo 11 of the BTM11 Energy Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Energy (ENE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniverse-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md)

> **Evidence boundary:** OmniVerse Energy Ltd. is a **fictional educational case**. The case sources contain little operating-model detail for run operations; the teams, cost drivers and ownership rules below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `ENE-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Who runs intelligent operations, who owns each service, and who sees what it costs?*

**What this file shows:** a proposed team structure for OmniVerse, an ownership rule for every service in the Demo 06 landscape, a shift from ticket-based support to service ownership, and the cost drivers to make visible.

**What it does not show:** headcount, budgets, savings or any measured cost.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 85B revenue; 68,000 employees; 42 countries |
| Business mix | Upstream 35%; refining and petrochemicals 28%; retail and marketing 18%; power 12%; renewables 7% |
| Assets | 8 refineries; 25,000 km pipelines; 12,500 retail sites; 15 GW generation |

**Decision under discussion (source):** Which AI use cases stay assistive, which may trigger human-approved actions, and which low-risk processes may be automated (OVE-HR11 strategic dilemma).

**Illustrative trigger (source):** In the OVE-HR11 decision scenes, an employee (Rina) receives incorrect promotion guidance from an assistant, while HR operations wants automatic data corrections and case closure and a worker representative challenges sentiment inference and productivity scoring.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Team structure, ownership register, cost drivers, tests | **New design (illustrative)** |
| SAP tooling and licensing | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What operating model lets OmniVerse run its landscape and AI assistants safely, with every service owned and every cost driver visible?

**Accountable owner (proposed):** OVE-P04 Farah Al-Hassan for operations and OVE-P05 Rajiv Kapoor for funding.

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

## 6. From ticket support to service ownership (new design)

| Dimension | Ticket-based support | Service ownership |
|---|---|---|
| Unit of work | Ticket | Service with an owner and a runbook |
| Accountability | Queue | Named owner per service |
| Improvement | Close the ticket | Fix the cause; update the runbook |
| Automation | Ad hoc scripts | Tiered A, B or C as in Demo 06 |
| Cost view | Hours by queue | Cost drivers by service |

## 7. Proposed teams

| Team | Scope | Accountable role (proposed) |
|---|---|---|
| HR integration product team | Employment events, interfaces, replay | OVE-P12 Hannah Fischer |
| Identity and access operations | Access lifecycle, reconciliation | OVE-P13 Omar Haddad |
| Platform and Basis team | Landscape, transports, HA and DR | OVE-P04 Farah Al-Hassan |
| AI and data product team | Assistant, graph, data products | OVE-P16 Dr. Leila Haddad |
| Refinery operations liaison | Plant-side requirements and change windows | OVE-P09 Carlos Mendes |

## 8. Service ownership register

Components come from the Demo 06 landscape. Named owners are assigned in the exercise; none is assumed here.

| Component | Criticality | Named owner | Runbook | On-call |
|---|---|---|---|---|
| HR core system (cloud) | High: lifecycle source | To be assigned | Not written | To be assigned |
| Identity and access system | High: access decisions | To be assigned | Not written | To be assigned |
| Integration platform and event broker | High: carries lifecycle events | To be assigned | Not written | To be assigned |
| Core ERP on HANA | High: payroll, finance links | To be assigned | Not written | To be assigned |
| Reporting and analytics store | Medium | To be assigned | Not written | To be assigned |
| Non-production systems | Low: but source of transport risk | To be assigned | Not written | To be assigned |

**Rhythm that constrains change (illustrative):** Payroll cycles and shift changes at refineries; no change during a payroll close or a turnaround handover (illustrative).

## 9. FinOps: cost drivers to make visible

| Cost driver | Unit to watch | Owner (proposed) | Value |
|---|---|---|---|
| Event broker capacity and retention | To be defined | OVE-P05 Rajiv Kapoor | Not measured |
| Model calls and embeddings per assistant | To be defined | OVE-P05 Rajiv Kapoor | Not measured |
| HANA memory for vector and graph data | To be defined | OVE-P05 Rajiv Kapoor | Not measured |
| Non-production landscape sizing | To be defined | OVE-P05 Rajiv Kapoor | Not measured |
| Monitoring and log volume | To be defined | OVE-P05 Rajiv Kapoor | Not measured |

**Rules:** every driver has an owner; assistants show cost per use; a rollout step needs a cost review. No figure is stated because none exists for this fictional case.

## 10. Skills gaps to plan for

| Skill | Why it matters | First action |
|---|---|---|
| Event reliability engineering | Needed to run the model above | Name a person and a learning plan |
| Operations of AI assistants | Needed to run the model above | Name a person and a learning plan |
| Identity governance | Needed to run the model above | Name a person and a learning plan |

## 11. Hands-on exercise (synthetic data)

1. Assign a named owner and an on-call role to each component in the register.
2. Write the first lines of a runbook for the highest-criticality component.
3. Rank the cost drivers by who can act on them and name a review date.
4. Mark which team changes are needed from today's structure.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Unowned service | An interface has no named owner at 02:00 | Operating model names an on-call owner for every service |
| T2 Cost spike | Model calls double after a feature release | Cost driver shows by assistant; owner reviews before more rollout |
| T3 Skills gap | Only one person understands replay | Cross-training task and a documented runbook |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Services with a named owner and on-call role | Count in the register | Not measured |
| Services with a runbook | Count | Not measured |
| Cost drivers with an owner | Count | Not measured |
| Skills gaps with a named person | Count | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Why operations fails without owners | Shared problem statement |
| 0:20 to 1:00 | Teams and ownership register | Assigned owners |
| 1:00 to 1:45 | Cost drivers and skills | Driver list and plan |
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

- [SAP Cloud ALM](https://www.sap.com/products/technology-platform/cloud-alm.html)
- [FinOps Foundation framework](https://www.finops.org/framework/)

- [OmniVerse Energy Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd)
- [OmniVerse Energy Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md)

