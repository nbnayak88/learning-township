# OmniCapital Financial Group — Operating Model and FinOps for Intelligent Operations

## Demo 11 of the BTM11 Financials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Financials (FIN) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnicapital-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md)

> **Evidence boundary:** OmniCapital Financial Group is a **fictional educational case**. The case sources contain little operating-model detail for run operations; the teams, cost drivers and ownership rules below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `FIN-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Who runs intelligent operations, who owns each service, and who sees what it costs?*

**What this file shows:** a proposed team structure for OmniCapital, an ownership rule for every service in the Demo 06 landscape, a shift from ticket-based support to service ownership, and the cost drivers to make visible.

**What it does not show:** headcount, budgets, savings or any measured cost.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 46B financial group; USD 1.4T AUM; 58M customers; 32 countries |
| Business mix | Retail 31%; commercial 24%; wealth 19%; insurance 16%; payments and markets 10% |
| Source problem | Fragmented customer, product, risk and transaction data; manual review; stronger fraud, cyber and model-risk control needs |

**Decision under discussion (source):** Fund a bounded onboarding and document-exception pilot with control and value evidence before enterprise expansion.

**Illustrative trigger (source):** An SME customer repeatedly submits the same document while customer service and verification teams show different exception status (invented discovery context, not an actual incident).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Team structure, ownership register, cost drivers, tests | **New design (illustrative)** |
| SAP tooling and licensing | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What operating model lets OmniCapital run its landscape and AI assistants safely, with every service owned and every cost driver visible?

**Accountable owner (proposed):** OCF-P05 Elena Fischer for operations and OCF-P06 Sofia Chen for funding.

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
| Onboarding product team | Verification, documents, exceptions | OCF-P03 Priya Rao |
| Customer service product team | CRM, status views | OCF-P08 Marcus Okoro |
| Platform and Basis team | Landscape, resilience, month-end | OCF-P05 Elena Fischer |
| Data and AI team | Data products, assistants | OCF-P09 Mei Tan |
| Security and risk operations | Access, alerts | OCF-P10 Omar Haddad |

## 8. Service ownership register

Components come from the Demo 06 landscape. Named owners are assigned in the exercise; none is assumed here.

| Component | Criticality | Named owner | Runbook | On-call |
|---|---|---|---|---|
| Core banking interface layer | High | To be assigned | Not written | To be assigned |
| Onboarding and verification services | High | To be assigned | Not written | To be assigned |
| Integration platform and partner gateway | High | To be assigned | Not written | To be assigned |
| Core ERP on HANA (finance) | High | To be assigned | Not written | To be assigned |
| Risk and reporting store | Medium | To be assigned | Not written | To be assigned |
| Non-production systems | Low | To be assigned | Not written | To be assigned |

**Rhythm that constrains change (illustrative):** Month-end, quarter-end and regulatory reporting windows (illustrative).

## 9. FinOps: cost drivers to make visible

| Cost driver | Unit to watch | Owner (proposed) | Value |
|---|---|---|---|
| Month-end peak capacity | To be defined | OCF-P06 Sofia Chen | Not measured |
| HANA memory for reporting history | To be defined | OCF-P06 Sofia Chen | Not measured |
| Model calls for service assistants | To be defined | OCF-P06 Sofia Chen | Not measured |
| Partner gateway volume | To be defined | OCF-P06 Sofia Chen | Not measured |
| Non-production landscapes | To be defined | OCF-P06 Sofia Chen | Not measured |

**Rules:** every driver has an owner; assistants show cost per use; a rollout step needs a cost review. No figure is stated because none exists for this fictional case.

## 10. Skills gaps to plan for

| Skill | Why it matters | First action |
|---|---|---|
| Resilience engineering | Needed to run the model above | Name a person and a learning plan |
| Operating AI assistants | Needed to run the model above | Name a person and a learning plan |
| Regulatory data engineering | Needed to run the model above | Name a person and a learning plan |

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
| T1 Month-end freeze | A change is requested in the freeze | Blocked; exception path |
| T2 Unowned report job | A regulatory job has no owner | Owner assigned before the next cycle |
| T3 Cost by assistant | Model costs rise | Visible by assistant; owner reviews |

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

- [OmniCapital Financial Group case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/07-financials/omnicapital-financial-group-ltd)
- [OmniCapital Financial Group persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/personas/persona-cards.md)

