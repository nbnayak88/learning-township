# OmniGrid — Operating Model and FinOps for Intelligent Operations

## Demo 11 of the BTM11 Utilities Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Utilities (UT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnigrid-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md)

> **Evidence boundary:** OmniGrid is a **fictional educational case**. The case sources contain little operating-model detail for run operations; the teams, cost drivers and ownership rules below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `UT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Who runs intelligent operations, who owns each service, and who sees what it costs?*

**What this file shows:** a proposed team structure for OmniGrid, an ownership rule for every service in the Demo 06 landscape, a shift from ticket-based support to service ownership, and the cost drivers to make visible.

**What it does not show:** headcount, budgets, savings or any measured cost.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 31B utility; 38,000 staff; 17 countries; 21M electricity, gas and water accounts |
| Business mix | Renewables 28%; networks 27%; retail 18%; conventional and flexible 15%; water and environment 12% |
| Source problem | Fragmented OT, field, customer and market data; variable generation; manual restoration; growing meter and sensor security demands |

**Decision under discussion (source):** Fund bounded outage, work-order and customer coordination evidence before wider modernization.

**Illustrative trigger (source):** A storm scenario generates conflicting outage, asset and work-order status; field and customer teams cannot reconcile ownership (invented learning context, not an actual incident).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Team structure, ownership register, cost drivers, tests | **New design (illustrative)** |
| SAP tooling and licensing | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What operating model lets OmniGrid run its landscape and AI assistants safely, with every service owned and every cost driver visible?

**Accountable owner (proposed):** OGU-P04 Arjun Mehta for operations and OGU-P06 Sofia Tan for funding.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OGU-P06 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes |
| OGU-P12 | Daniel Weber, Director Enterprise Architecture | Owns standards and review |
| OGU-P10 | Omar Haddad, CISO and OT Resilience Lead | Security and boundary approval |
| OGU-P09 | Mei Lin, Asset and Grid Data Lead | Data and AI governance |
| OGU-P13 | Priya Shah, Asset Management and Work Planning Lead | Business owner (first scope) |
| OGU-P08 | Marcus Okoro, Outage and Field Services Director | Business owner (second scope) |
| OGU-P04 | Arjun Mehta, Chief Operations and Grid Officer | Operational authority and veto |

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
| Outage coordination product team | Outage, restoration views | OGU-P13 Priya Shah |
| Field and work management team | Work orders, crews | OGU-P08 Marcus Okoro |
| Platform and Basis team | Landscape, storm readiness, HA and DR | OGU-P04 Arjun Mehta |
| Data and AI team | Data products, assistants | OGU-P09 Mei Lin |
| Security operations | Critical-infrastructure access | OGU-P10 Omar Haddad |

## 8. Service ownership register

Components come from the Demo 06 landscape. Named owners are assigned in the exercise; none is assumed here.

| Component | Criticality | Named owner | Runbook | On-call |
|---|---|---|---|---|
| Outage management | High | To be assigned | Not written | To be assigned |
| Work and asset management | High | To be assigned | Not written | To be assigned |
| Customer communications | High | To be assigned | Not written | To be assigned |
| Integration gateway and event broker | High | To be assigned | Not written | To be assigned |
| Core ERP on HANA | Medium | To be assigned | Not written | To be assigned |
| Non-production systems | Low | To be assigned | Not written | To be assigned |

**Rhythm that constrains change (illustrative):** Storm season and restoration periods; no change during a restoration event (illustrative).

## 9. FinOps: cost drivers to make visible

| Cost driver | Unit to watch | Owner (proposed) | Value |
|---|---|---|---|
| Storm-season capacity | To be defined | OGU-P06 Sofia Tan | Not measured |
| Event volume during restoration | To be defined | OGU-P06 Sofia Tan | Not measured |
| HANA memory for topology history | To be defined | OGU-P06 Sofia Tan | Not measured |
| Model calls for coordination assistants | To be defined | OGU-P06 Sofia Tan | Not measured |
| Non-production landscapes | To be defined | OGU-P06 Sofia Tan | Not measured |

**Rules:** every driver has an owner; assistants show cost per use; a rollout step needs a cost review. No figure is stated because none exists for this fictional case.

## 10. Skills gaps to plan for

| Skill | Why it matters | First action |
|---|---|---|
| Storm readiness engineering | Needed to run the model above | Name a person and a learning plan |
| Operating AI assistants | Needed to run the model above | Name a person and a learning plan |
| Event reliability | Needed to run the model above | Name a person and a learning plan |

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
| T1 Restoration freeze | A change is requested mid-restoration | Blocked; exception path |
| T2 Storm cost | Event volume surges | Cost driver visible; capacity decision |
| T3 Orphan service | A service has no on-call | Owner assigned |

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

- [OmniGrid case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/10-utilities/omnigrid-utilities-ltd)
- [OmniGrid persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/personas/persona-cards.md)

