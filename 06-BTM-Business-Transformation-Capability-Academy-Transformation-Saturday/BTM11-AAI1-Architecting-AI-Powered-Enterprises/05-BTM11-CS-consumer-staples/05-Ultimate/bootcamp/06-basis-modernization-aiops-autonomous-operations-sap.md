# OmniDaily — SAP Basis Modernization, AIOps and Autonomous Operations

## Demo 06 of the BTM11 Consumer Staples Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Staples (CS) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnidaily-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md)

> **Evidence boundary:** OmniDaily is a **fictional educational case**. The case source contains almost no run-operations detail, so the landscape, signals and rhythm below are synthetic design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CS-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Basis, HANA monitoring, transport automation, high availability and disaster recovery, and AI-driven operations: what may be automated, and what must stay with a person?*

**What this file shows:** a synthetic operations landscape for OmniDaily, six signals with a response and an autonomy tier, a change and transport policy, and the HA and DR questions to settle.

**What it does not show:** a monitored system, a tested failover or an automated remediation.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 51B staples group; 84,000 employees; 57 countries; 420M households served |
| Business mix | Foods 30%; beverages 23%; home care 19%; personal care 18%; wellness 10% |
| Burning platform | Demand, promotion, planning, product and ingredient data, quality and route-to-market execution fragmented across 160+ applications |

**Decision under discussion (source):** Fund a bounded demand-to-shelf and quality-evidence pilot before approving enterprise scale.

**Illustrative trigger (source):** A promotion creates a shelf gap while a quality-held batch appears available in a delayed distributor feed (invented; no real safety event is claimed).

**Scenario used in this demo:** A promotion peak and a quality hold coincide with a delayed distributor interface; operations must tell which delays are system faults and which are partner feeds.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Landscape, signals, tiers, rhythm, HA and DR questions, tests | **New design (synthetic)** |
| SAP operations tooling behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which operational responses may OmniDaily automate, which need human approval, and which are never automated?

**Accountable owner (proposed):** ODG-P09 Elena Petrović for operational risk, ODG-P05 Sofia Alvarez for the platform, ODG-P12 Omar Haddad for access and security.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| ODG-P05 | Sofia Alvarez, Chief Digital and Data Officer | Funds operations modernization; accepts residual risk with F |
| ODG-P13 | Priya Nair, Director Enterprise Architecture | Owns the operations and transport standard |
| ODG-P12 | Omar Haddad, CISO and Privacy Lead | Approves privileged access and automation boundaries |
| ODG-P08 | Mei Lin, Head of Product and Ingredient Stewardship | Data and AI governance for operational data |
| ODG-P07 | David Okoro, Global Quality and Product Safety Director | Business owner of the first protected service |
| ODG-P10 | Rohan Shah, Distributor and Field Execution Director | Business owner of the second protected service |
| ODG-P09 | Elena Petrović, Plant Operations Director | Operational authority; veto where operations or safety are at risk |

Decision rights are **proposed** and need discovery validation.

## 6. Tooling (public documentation, verify)

| Tool | Documented role | Note |
|---|---|---|
| SAP Cloud ALM | Operations and implementation tooling positioned as the successor to SAP Solution Manager | Does not fully cover change request and ITSM scope; verify |
| SAP Focused Run | Monitoring for large or complex landscapes | Verify fit and licensing |
| SAP HANA Cloud Central or HANA cockpit | Database monitoring and administration | Verify for the deployment model |
| SAP Solution Manager 7.2 | Mainstream maintenance reported to end 2027 with extended maintenance to about 2030 (third-party source) | **Confirm against SAP before planning** |

## 7. Landscape (synthetic)

| Component | Criticality |
|---|---|
| Core ERP on HANA | High |
| Planning and promotion application | High |
| Quality system | High: holds and releases |
| Distributor feed interface | High: external partners |
| Manufacturing execution link | High |
| Non-production systems | Low |

## 8. Signals, responses and autonomy tiers

**Tiers:** A answer or recommend only; B human-approved action; C never automated.

| Signal | Response | Tier |
|---|---|---|
| Distributor feed older than the agreed window | Mark stale; notify partner manager | B human-approved action |
| Quality hold event not acknowledged | Open an incident; owner informed | B human-approved action |
| Planning run duration grows | Compare to norm | A answer or recommend only |
| Interface error spike after a transport | Propose rollback candidates | B human-approved action |
| HANA backup duration trend | Recommend review | A answer or recommend only |
| Request to bypass a hold in a system job | Refused; Quality authority | C never automated |

**Always tier C:** production HA failover, restore from backup, upgrades, production transport imports and authorization changes.

## 9. Change and transport policy (new design)

| Rule | Design |
|---|---|
| Pipeline | Development, quality, production; no direct production changes |
| Collision check | The pipeline shows two changes touching the same object |
| Freeze windows | Promotion calendars, plant changeovers and month-end (illustrative). |
| Exceptions | Named approver, expiry date and rollback plan recorded |
| Evidence | Each import records who approved and when |

## 10. High availability and disaster recovery questions

**Focus:** Quality and planning services first.

| Question | Owner (proposed) | Value |
|---|---|---|
| Recovery time objective per service | ODG-P09 Elena Petrović | To be decided |
| Recovery point objective per service | ODG-P09 Elena Petrović | To be decided |
| Last restore test and its result | ODG-P13 Priya Nair | Evidence slot empty |
| Last failover test and its result | ODG-P13 Priya Nair | Evidence slot empty |
| Who approves a production failover | ODG-P05 Sofia Alvarez | To be named |

## 11. Hands-on exercise (synthetic data)

1. Take the six signals and write a one-page runbook for the first, including who is called and what is checked.
2. For each signal, confirm the tier and what evidence the operator needs before approving.
3. Draw the change pipeline and mark one collision.
4. List what is missing before any tier B action could be automated further.
5. Record decisions and gaps in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Partner feed delay | A feed is late | Labelled as partner delay, not internal fault |
| T2 Hold bypass | A job tries to ignore a hold | Refused; incident raised |
| T3 Transport after hold event | A transport changes a hold interface | Pipeline requires Quality sign-off |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Signals with a runbook, owner and tier | Count of the six | Not measured |
| Tier C actions with no automated path | Review of the action list | Not measured |
| HA and DR questions with a named owner | Count of five | Not measured |
| Changes with approver and rollback recorded | Sample of the register | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | From monitoring to autonomy: the tiers | Shared vocabulary |
| 0:20 to 1:00 | Landscape and signals | Six runbook outlines |
| 1:00 to 1:45 | Change pipeline and HA and DR | Policy draft and question list |
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
- [SAP Focused Run](https://www.sap.com/products/technology-platform/focused-run.html)

- [OmniDaily case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/05-consumer-staples/omnidaily-consumer-goods-ltd)
- [OmniDaily persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md)

