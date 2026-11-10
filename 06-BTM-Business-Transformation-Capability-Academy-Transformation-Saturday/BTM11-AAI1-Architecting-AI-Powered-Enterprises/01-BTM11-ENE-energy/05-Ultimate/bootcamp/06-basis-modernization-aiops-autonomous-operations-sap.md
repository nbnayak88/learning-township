# OmniVerse Energy Ltd. — SAP Basis Modernization, AIOps and Autonomous Operations

## Demo 06 of the BTM11 Energy Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Energy (ENE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniverse-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md)

> **Evidence boundary:** OmniVerse Energy Ltd. is an **aspirational case study**. The case source contains almost no run-operations detail, so the landscape, signals and rhythm below are synthetic design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `ENE-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Basis, HANA monitoring, transport automation, high availability and disaster recovery, and AI-driven operations: what may be automated, and what must stay with a person?*

**What this file shows:** a synthetic operations landscape for OmniVerse, six signals with a response and an autonomy tier, a change and transport policy, and the HA and DR questions to settle.

**What it does not show:** a monitored system, a tested failover or an automated remediation.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 85B revenue; 68,000 employees; 42 countries |
| Business mix | Upstream 35%; refining and petrochemicals 28%; retail and marketing 18%; power 12%; renewables 7% |
| Assets | 8 refineries; 25,000 km pipelines; 12,500 retail sites; 15 GW generation |

**Decision under discussion (source):** Which AI use cases stay assistive, which may trigger human-approved actions, and which low-risk processes may be automated (OVE-HR11 strategic dilemma).

**Illustrative trigger (source):** In the OVE-HR11 decision scenes, an employee (Rina) receives incorrect promotion guidance from an assistant, while HR operations wants automatic data corrections and case closure and a worker representative challenges sentiment inference and productivity scoring.

**Scenario used in this demo:** A refinery access change fails to propagate and the operations team has no single view of the integration, identity and HR landscape health (new design on the HR12 incident scene).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Landscape, signals, tiers, rhythm, HA and DR questions, tests | **New design (synthetic)** |
| SAP operations tooling behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which operational responses may OmniVerse automate, which need human approval, and which are never automated?

**Accountable owner (proposed):** OVE-P04 Farah Al-Hassan for operational risk, OVE-P05 Rajiv Kapoor for the platform, OVE-P13 Omar Haddad for access and security.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OVE-P05 | Rajiv Kapoor, Chief Digital and Information Officer (CDIO) | Funds operations modernization; accepts residual risk with F |
| OVE-P12 | Hannah Fischer, Director of Enterprise Architecture | Owns the operations and transport standard |
| OVE-P13 | Omar Haddad, Chief Information Security Officer (CISO) | Approves privileged access and automation boundaries |
| OVE-P16 | Dr. Leila Haddad, Head of Data Governance and AI | Data and AI governance for operational data |
| OVE-P09 | Carlos Mendes, VP Asset Reliability and Maintenance | Business owner of the first protected service |
| OVE-P10 | Grace Okafor, Chief Customer and Retail Officer | Business owner of the second protected service |
| OVE-P04 | Farah Al-Hassan, Chief Operating Officer (COO) | Operational authority; veto where operations or safety are at risk |

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
| HR core system (cloud) | High: lifecycle source |
| Identity and access system | High: access decisions |
| Integration platform and event broker | High: carries lifecycle events |
| Core ERP on HANA | High: payroll, finance links |
| Reporting and analytics store | Medium |
| Non-production systems | Low: but source of transport risk |

## 8. Signals, responses and autonomy tiers

**Tiers:** A answer or recommend only; B human-approved action; C never automated.

| Signal | Response | Tier |
|---|---|---|
| Lifecycle events pending longer than the agreed window | Open an incident, notify the access owner with the event ids | B human-approved action |
| Dead-message queue depth rising | Group by reason, propose owner; replay only after approval | B human-approved action |
| HANA memory growth trend | Recommend capacity review | A answer or recommend only |
| Failed overnight job in the integration chain | Summarize the failure and the last good run | A answer or recommend only |
| Certificate nearing expiry on an interface | Create a renewal task with owner | B human-approved action |
| Request to restart a production component | Prepare the runbook; a named operator executes | C never automated |

**Always tier C:** production HA failover, restore from backup, upgrades, production transport imports and authorization changes.

## 9. Change and transport policy (new design)

| Rule | Design |
|---|---|
| Pipeline | Development, quality, production; no direct production changes |
| Collision check | The pipeline shows two changes touching the same object |
| Freeze windows | Payroll cycles and shift changes at refineries; no change during a payroll close or a turnaround handover (illustrative). |
| Exceptions | Named approver, expiry date and rollback plan recorded |
| Evidence | Each import records who approved and when |

## 10. High availability and disaster recovery questions

**Focus:** Access-related interfaces and the event broker are the first HA and DR candidates; targets are decisions to make, not stated values.

| Question | Owner (proposed) | Value |
|---|---|---|
| Recovery time objective per service | OVE-P04 Farah Al-Hassan | To be decided |
| Recovery point objective per service | OVE-P04 Farah Al-Hassan | To be decided |
| Last restore test and its result | OVE-P12 Hannah Fischer | Evidence slot empty |
| Last failover test and its result | OVE-P12 Hannah Fischer | Evidence slot empty |
| Who approves a production failover | OVE-P05 Rajiv Kapoor | To be named |

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
| T1 Silent event backlog | Events pend for hours while dashboards stay green | Age-of-oldest-event alert and owner notification are required, not CPU or uptime alone |
| T2 Unsafe auto-restart | An agent proposes restarting the broker during a shift change | Tier C; operator and change owner approve; freeze window respected |
| T3 Transport collision | Two changes target the same interface | Pipeline shows the collision; release manager decides order |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Signals with a runbook, owner and tier | Count of the six | Not measured |
| Tier C actions with no automated path | Review of the action list | Not measured |
| HA and DR questions with a named owner | Count of five | Not measured |
| Changes with approver and rollback recorded | Sample of the register | Not measured |

No baseline, target or benefit is stated because none exists for this aspirational case study. Targets are agreed in discovery.

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
| Customer-confirmed requirements | Not applicable (aspirational case study) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP Cloud ALM](https://www.sap.com/products/technology-platform/cloud-alm.html)
- [SAP Focused Run](https://www.sap.com/products/technology-platform/focused-run.html)

- [OmniVerse Energy Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd)
- [OmniVerse Energy Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md)

