# OmniForge Materials — Operating Model and FinOps for Intelligent Operations

## Demo 11 of the BTM11 Materials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Materials (MAT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniforge-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md)

> **Evidence boundary:** OmniForge Materials is a **fictional educational case**. The case sources contain little operating-model detail for run operations; the teams, cost drivers and ownership rules below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `MAT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Who runs intelligent operations, who owns each service, and who sees what it costs?*

**What this file shows:** a proposed team structure for OmniForge, an ownership rule for every service in the Demo 06 landscape, a shift from ticket-based support to service ownership, and the cost drivers to make visible.

**What it does not show:** headcount, budgets, savings or any measured cost.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 42B materials group; 46,000 employees; 31 countries |
| Business mix | Steel and alloys 30%; cement and aggregates 22%; chemicals 20%; mining and minerals 16%; advanced materials 12% |
| Burning platform | Disconnected mining, production, logistics, quality, sales and recycling; 180+ applications; weak material genealogy; manual ESG reconciliation |

**Decision under discussion (source):** Select a bounded materials-traceability and reliability pilot before committing an enterprise rollout.

**Illustrative trigger (source):** A customer queries a shipped batch's certificate after a laboratory correction, while a kiln reliability alert and uncertain recycled-feedstock records expose the same trust gap (illustrative hero trigger in the case).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Team structure, ownership register, cost drivers, tests | **New design (illustrative)** |
| SAP tooling and licensing | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What operating model lets OmniForge run its landscape and AI assistants safely, with every service owned and every cost driver visible?

**Accountable owner (proposed):** OMF-P16 Nikhil Sen for operations and OMF-P04 Sofia de Vries for funding.

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
| Quality and certificate product team | Lab, certificate, correction flows | OMF-P08 Rohan Kulkarni |
| Plant integration team | Edge gateway, plant-to-enterprise data | OMF-P07 Elena Petrova |
| Platform and Basis team | Landscape, transports, HA and DR | OMF-P16 Nikhil Sen |
| Data and AI team | Data products, assistants, graph | OMF-P14 Diego Alvarez |
| Security operations | Access, OT boundary monitoring | OMF-P12 Hassan Al-Farsi |

## 8. Service ownership register

Components come from the Demo 06 landscape. Named owners are assigned in the exercise; none is assumed here.

| Component | Criticality | Named owner | Runbook | On-call |
|---|---|---|---|---|
| Core ERP on HANA | High: batch, quality, finance | To be assigned | Not written | To be assigned |
| Laboratory and certificate system | High: customer commitments | To be assigned | Not written | To be assigned |
| Plant edge gateway | High: only passive data exchange from OT | To be assigned | Not written | To be assigned |
| Integration platform | High | To be assigned | Not written | To be assigned |
| Analytics and ESG data store | Medium | To be assigned | Not written | To be assigned |
| Non-production systems | Low | To be assigned | Not written | To be assigned |

**Rhythm that constrains change (illustrative):** Campaign and shutdown calendars; month-end and customer certificate peaks (illustrative).

## 9. FinOps: cost drivers to make visible

| Cost driver | Unit to watch | Owner (proposed) | Value |
|---|---|---|---|
| HANA memory for batch history | To be defined | OMF-P04 Sofia de Vries | Not measured |
| Edge to cloud data volume | To be defined | OMF-P04 Sofia de Vries | Not measured |
| Model calls for assistants | To be defined | OMF-P04 Sofia de Vries | Not measured |
| Storage for sensor history | To be defined | OMF-P04 Sofia de Vries | Not measured |
| Non-production landscapes | To be defined | OMF-P04 Sofia de Vries | Not measured |

**Rules:** every driver has an owner; assistants show cost per use; a rollout step needs a cost review. No figure is stated because none exists for this fictional case.

## 10. Skills gaps to plan for

| Skill | Why it matters | First action |
|---|---|---|
| Operating AI assistants safely | Needed to run the model above | Name a person and a learning plan |
| Edge data engineering | Needed to run the model above | Name a person and a learning plan |
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
| T1 Campaign peak support | A plant campaign overlaps a release | Rhythm calendar blocks the release; owner signs an exception |
| T2 Sensor data cost | Sensor history grows without a retention rule | Retention decision and owner named |
| T3 Single expert | One person knows the edge gateway | Runbook and a second owner |

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

- [OmniForge Materials case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/02-materials/omniforge-materials-ltd)
- [OmniForge Materials persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md)

