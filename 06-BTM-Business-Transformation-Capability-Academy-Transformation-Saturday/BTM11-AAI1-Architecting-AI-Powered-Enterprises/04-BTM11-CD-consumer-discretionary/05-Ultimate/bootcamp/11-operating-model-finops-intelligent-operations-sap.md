# OmniVibe — Operating Model and FinOps for Intelligent Operations

## Demo 11 of the BTM11 Consumer Discretionary Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Discretionary (CD) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnivibe-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniVibe is an **aspirational case study**. The case sources contain little operating-model detail for run operations; the teams, cost drivers and ownership rules below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CD-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Who runs intelligent operations, who owns each service, and who sees what it costs?*

**What this file shows:** a proposed team structure for OmniVibe, an ownership rule for every service in the Demo 06 landscape, a shift from ticket-based support to service ownership, and the cost drivers to make visible.

**What it does not show:** headcount, budgets, savings or any measured cost.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 28B consumer group; 72,000 employees; 48 countries |
| Business mix | Fashion 32%; beauty 18%; home 17%; specialty retail 15%; travel 10%; marketplace 8% |
| Network | 3,200 stores; 14 e-commerce sites; 26 distribution centres; 140 micro-fulfilment sites |

**Decision under discussion (source):** Select one brand and country workforce-to-service pilot and evidence gates before approving enterprise scale.

**Illustrative trigger (source):** A new associate lacks a completed onboarding and skills handoff while store readiness and channel information disagree (invented events that prompt discovery, per the case).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Team structure, ownership register, cost drivers, tests | **New design (illustrative)** |
| SAP tooling and licensing | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What operating model lets OmniVibe run its landscape and AI assistants safely, with every service owned and every cost driver visible?

**Accountable owner (proposed):** OVC-P16 Nikhil Das for operations and OVC-P04 Ravi Kapoor for funding.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OVC-P04 | Ravi Kapoor, Group CHRO | Funds and prioritizes |
| OVC-P11 | Priya Shah, Director Enterprise Architecture | Owns standards and review |
| OVC-P13 | Farah Ahmed, CISO and Privacy Lead | Security and boundary approval |
| OVC-P12 | Jonas Lim, Integration and HR Data Lead | Data and AI governance |
| OVC-P08 | Sofia Mendes, Head of Talent Acquisition and Onboarding | Business owner (first scope) |
| OVC-P06 | Oliver Brooks, Store Operations Director | Business owner (second scope) |
| OVC-P16 | Nikhil Das, Store Associate and Workforce Representative | Operational authority and veto |

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
| Workforce experience product team | Onboarding, learning, scheduling | OVC-P08 Sofia Mendes |
| Store and channel product team | Readiness, order links | OVC-P06 Oliver Brooks |
| Platform and Basis team | Landscape, peaks, HA and DR | OVC-P16 Nikhil Das |
| AI and data team | Assistants, data products | OVC-P12 Jonas Lim |
| Privacy and security | Boundaries, access | OVC-P13 Farah Ahmed |

## 8. Service ownership register

Components come from the Demo 06 landscape. Named owners are assigned in the exercise; none is assumed here.

| Component | Criticality | Named owner | Runbook | On-call |
|---|---|---|---|---|
| Core HR (cloud) | High: onboarding | To be assigned | Not written | To be assigned |
| Workforce scheduling | High: store readiness | To be assigned | Not written | To be assigned |
| Order and commerce platform | High: peak revenue | To be assigned | Not written | To be assigned |
| Integration platform | High | To be assigned | Not written | To be assigned |
| Core ERP on HANA | High | To be assigned | Not written | To be assigned |
| Non-production systems | Low | To be assigned | Not written | To be assigned |

**Rhythm that constrains change (illustrative):** Launch campaigns, seasonal peaks and a holiday change freeze (illustrative).

## 9. FinOps: cost drivers to make visible

| Cost driver | Unit to watch | Owner (proposed) | Value |
|---|---|---|---|
| Peak-season capacity | To be defined | OVC-P04 Ravi Kapoor | Not measured |
| Model calls for store assistants | To be defined | OVC-P04 Ravi Kapoor | Not measured |
| HANA memory for readiness history | To be defined | OVC-P04 Ravi Kapoor | Not measured |
| Integration volume per campaign | To be defined | OVC-P04 Ravi Kapoor | Not measured |
| Non-production landscapes | To be defined | OVC-P04 Ravi Kapoor | Not measured |

**Rules:** every driver has an owner; assistants show cost per use; a rollout step needs a cost review. No figure is stated because none exists for this aspirational case study.

## 10. Skills gaps to plan for

| Skill | Why it matters | First action |
|---|---|---|
| Peak capacity planning | Needed to run the model above | Name a person and a learning plan |
| Operating AI assistants | Needed to run the model above | Name a person and a learning plan |
| Privacy engineering | Needed to run the model above | Name a person and a learning plan |

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
| T1 Holiday freeze | A change is requested in the freeze | Blocked; exception path |
| T2 Campaign cost | A campaign multiplies model calls | Cost driver visible by assistant |
| T3 Franchise exception | A franchise asks for group tooling | Boundary rule decides; owner signs |

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

- [OmniVibe case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/04-consumer-discretionary/omnivibe-consumer-ltd)
- [OmniVibe persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/personas/persona-cards.md)

