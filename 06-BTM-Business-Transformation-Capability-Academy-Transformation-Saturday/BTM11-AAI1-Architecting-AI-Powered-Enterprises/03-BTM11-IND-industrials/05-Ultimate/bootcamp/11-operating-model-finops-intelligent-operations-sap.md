# OmniWorks Industrial Systems Ltd. — Operating Model and FinOps for Intelligent Operations

## Demo 11 of the BTM11 Industrials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Industrials (IND) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniworks-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniWorks Industrial Systems Ltd. is a **fictional educational case**. The case sources contain little operating-model detail for run operations; the teams, cost drivers and ownership rules below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IND-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Who runs intelligent operations, who owns each service, and who sees what it costs?*

**What this file shows:** a proposed team structure for OmniWorks, an ownership rule for every service in the Demo 06 landscape, a shift from ticket-based support to service ownership, and the cost drivers to make visible.

**What it does not show:** headcount, budgets, savings or any measured cost.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 48B revenue; 74,000 employees; 36 countries; 61 plants and facilities; 320 service depots; 7,200 suppliers |
| Business mix | Industrial automation 27%; aerospace and defence 23%; transport and mobility 19%; infrastructure 16%; aftermarket and lifecycle services 15% |
| Burning platform | Recurring transport asset failures cannot be consistently traced across configuration, telemetry, supplier batches and maintenance history |

**Decision under discussion (source):** Turn a USD 575M transformation envelope into credible customer, operational and financial value without disrupting safety-critical operations.

**Illustrative trigger (source):** Repeat customer asset failures expose fragmented engineering-to-service information, and the business wants to sell uptime rather than equipment (hero story).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Team structure, ownership register, cost drivers, tests | **New design (illustrative)** |
| SAP tooling and licensing | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What operating model lets OmniWorks run its landscape and AI assistants safely, with every service owned and every cost driver visible?

**Accountable owner (proposed):** OW-P12 Daniel Okafor for operations and OW-P05 Priya Nair for funding.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OW-P05 | Priya Nair, CIDO | Funds and prioritizes |
| OW-P11 | Hannah Fischer, Director, Enterprise Architecture | Owns standards and review |
| OW-P06 | Marcus Vogel, CISO | Security and boundary approval |
| OW-P15 | Dr. Leila Haddad, Head of Data Governance & AI | Data and AI governance |
| OW-P09 | Isabel Torres, Chief Customer & Service Officer | Business owner (first scope) |
| OW-P10 | Ravi Deshpande, VP Manufacturing, Pune Operations | Business owner (second scope) |
| OW-P12 | Daniel Okafor, Field Service Operations Manager | Operational authority and veto |

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
| Service and field product team | Dispatch, parts, portal | OW-P09 Isabel Torres |
| Engineering data team | PLM links, baseline data | OW-P10 Ravi Deshpande |
| Platform and Basis team | Landscape, transports, HA and DR | OW-P12 Daniel Okafor |
| AI and data team | Assistants, graph, data products | OW-P15 Dr. Leila Haddad |
| OT liaison and security | Edge boundary and monitoring | OW-P06 Marcus Vogel |

## 8. Service ownership register

Components come from the Demo 06 landscape. Named owners are assigned in the exercise; none is assumed here.

| Component | Criticality | Named owner | Runbook | On-call |
|---|---|---|---|---|
| Core ERP on HANA | High | To be assigned | Not written | To be assigned |
| Field service application | High: dispatch and parts | To be assigned | Not written | To be assigned |
| PLM system | High: configuration baseline | To be assigned | Not written | To be assigned |
| Integration platform | High | To be assigned | Not written | To be assigned |
| Customer portal | Medium | To be assigned | Not written | To be assigned |
| Non-production systems | Low | To be assigned | Not written | To be assigned |

**Rhythm that constrains change (illustrative):** Peak service seasons and engineering release trains (illustrative).

## 9. FinOps: cost drivers to make visible

| Cost driver | Unit to watch | Owner (proposed) | Value |
|---|---|---|---|
| Telemetry ingestion and storage | To be defined | OW-P05 Priya Nair | Not measured |
| Model calls for service assistants | To be defined | OW-P05 Priya Nair | Not measured |
| HANA memory for configuration history | To be defined | OW-P05 Priya Nair | Not measured |
| Edge gateway fleet | To be defined | OW-P05 Priya Nair | Not measured |
| Non-production landscapes | To be defined | OW-P05 Priya Nair | Not measured |

**Rules:** every driver has an owner; assistants show cost per use; a rollout step needs a cost review. No figure is stated because none exists for this fictional case.

## 10. Skills gaps to plan for

| Skill | Why it matters | First action |
|---|---|---|
| Telemetry data engineering | Needed to run the model above | Name a person and a learning plan |
| Operating AI assistants | Needed to run the model above | Name a person and a learning plan |
| Integration reliability | Needed to run the model above | Name a person and a learning plan |

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
| T1 Peak service season | A release train meets a service peak | Freeze rule; exception needs named approver |
| T2 Telemetry cost | Ingestion grows with fleet size | Retention and sampling decision by owner |
| T3 Orphan interface | An old interface has no owner | Owner assigned or retirement plan |

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

- [OmniWorks Industrial Systems Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/03-industrials/omniworks-industrial-systems)
- [OmniWorks Industrial Systems Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md)

