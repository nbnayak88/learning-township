# OmniHealth — Operating Model and FinOps for Intelligent Operations

## Demo 11 of the BTM11 Health Care Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Health Care (HC) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnihealth-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniHealth is an **aspirational case study**. The case sources contain little operating-model detail for run operations; the teams, cost drivers and ownership rules below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `HC-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Who runs intelligent operations, who owns each service, and who sees what it costs?*

**What this file shows:** a proposed team structure for OmniHealth, an ownership rule for every service in the Demo 06 landscape, a shift from ticket-based support to service ownership, and the cost drivers to make visible.

**What it does not show:** headcount, budgets, savings or any measured cost.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 34B healthcare group; 126,000 staff; 19 countries |
| Network | 86 hospitals; 440 clinics; 670 diagnostic centres |
| Business mix | Acute 38%; primary 22%; diagnostics 18%; digital and pharmacy 12%; research and value-based 10% |

**Decision under discussion (source):** Select a bounded, non-clinical care-coordination pilot and evidence gates before enterprise expansion.

**Illustrative trigger (source):** A referral crosses facilities without clear ownership; the patient repeats information and a dashboard cannot reconcile episode status (invented; no actual patient incident is asserted).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Team structure, ownership register, cost drivers, tests | **New design (illustrative)** |
| SAP tooling and licensing | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What operating model lets OmniHealth run its landscape and AI assistants safely, with every service owned and every cost driver visible?

**Accountable owner (proposed):** OHS-P03 Dr. Leila Morgan for operations and OHS-P05 Sofia Tan for funding.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OHS-P05 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes |
| OHS-P13 | Daniel Weber, Enterprise Architecture Director | Owns standards and review |
| OHS-P10 | Omar Haddad, CISO and Privacy Lead | Security and boundary approval |
| OHS-P09 | Priya Nair, Patient Identity and Data Governance Lead | Data and AI governance |
| OHS-P07 | Dr. Amina Okafor, Nursing and Care Coordination Director | Business owner (first scope) |
| OHS-P04 | Dr. Arjun Mehta, Chief Clinical Operations Officer | Business owner (second scope) |
| OHS-P03 | Dr. Leila Morgan, Chief Medical Officer | Operational authority and veto |

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
| Referral and scheduling product team | Referral, booking, coordination | OHS-P07 Dr. Amina Okafor |
| Care operations liaison | Facility needs, change windows | OHS-P04 Dr. Arjun Mehta |
| Platform and Basis team | Landscape, HA and DR | OHS-P03 Dr. Leila Morgan |
| Data and AI team | Data products, assistants | OHS-P09 Priya Nair |
| Privacy and security | Pseudonymization, access | OHS-P10 Omar Haddad |

## 8. Service ownership register

Components come from the Demo 06 landscape. Named owners are assigned in the exercise; none is assumed here.

| Component | Criticality | Named owner | Runbook | On-call |
|---|---|---|---|---|
| Scheduling and referral application | High | To be assigned | Not written | To be assigned |
| Identity matching service | High | To be assigned | Not written | To be assigned |
| Integration gateway | High | To be assigned | Not written | To be assigned |
| Core ERP on HANA (supply and finance) | Medium | To be assigned | Not written | To be assigned |
| Reporting store | Medium | To be assigned | Not written | To be assigned |
| Non-production systems | Low | To be assigned | Not written | To be assigned |

**Rhythm that constrains change (illustrative):** Clinic schedules and reporting cycles (illustrative).

## 9. FinOps: cost drivers to make visible

| Cost driver | Unit to watch | Owner (proposed) | Value |
|---|---|---|---|
| HANA memory for referral history | To be defined | OHS-P05 Sofia Tan | Not measured |
| Model calls for coordinators | To be defined | OHS-P05 Sofia Tan | Not measured |
| Identity service capacity | To be defined | OHS-P05 Sofia Tan | Not measured |
| Integration volume | To be defined | OHS-P05 Sofia Tan | Not measured |
| Non-production landscapes | To be defined | OHS-P05 Sofia Tan | Not measured |

**Rules:** every driver has an owner; assistants show cost per use; a rollout step needs a cost review. No figure is stated because none exists for this aspirational case study.

## 10. Skills gaps to plan for

| Skill | Why it matters | First action |
|---|---|---|
| Privacy engineering | Needed to run the model above | Name a person and a learning plan |
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
| T1 Clinic peak | A release meets a clinic peak | Rhythm calendar blocks |
| T2 Identity outage ownership | Identity service fails at night | On-call owner and manual route documented |
| T3 Unreviewed assistant | An assistant runs with no owner | Owner named before use |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Services with a named owner and on-call role | Count in the register | Not measured |
| Services with a runbook | Count | Not measured |
| Cost drivers with an owner | Count | Not measured |
| Skills gaps with a named person | Count | Not measured |

No baseline, target or benefit is stated because none exists for this aspirational case study. Targets are agreed in discovery.

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
| Customer-confirmed requirements | Not applicable (aspirational case study) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP Cloud ALM](https://www.sap.com/products/technology-platform/cloud-alm.html)
- [FinOps Foundation framework](https://www.finops.org/framework/)

- [OmniHealth case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/06-health-care/omnihealth-systems-ltd)
- [OmniHealth persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/personas/persona-cards.md)

