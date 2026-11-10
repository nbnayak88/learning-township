# OmniTech — SAP Basis Modernization, AIOps and Autonomous Operations

## Demo 06 of the BTM11 Information Technology Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Information Technology (IT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnitech-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md)

> **Evidence boundary:** OmniTech is a **fictional educational case**. The case source contains almost no run-operations detail, so the landscape, signals and rhythm below are synthetic design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Basis, HANA monitoring, transport automation, high availability and disaster recovery, and AI-driven operations: what may be automated, and what must stay with a person?*

**What this file shows:** a synthetic operations landscape for OmniTech, six signals with a response and an autonomy tier, a change and transport policy, and the HA and DR questions to settle.

**What it does not show:** a monitored system, a tested failover or an automated remediation.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 39B technology provider; 98,000 employees; 41 countries; 11,500 clients |
| Business mix | Cloud and platform 31%; software 25%; cyber 18%; AI and data 16%; managed services 10% |
| Source problem | Fragmented lifecycle tooling, bespoke integrations, poor data and AI reuse, late security and observability |

**Decision under discussion (source):** Fund a bounded platform-to-client-outcome pilot with security, recovery and economic evidence before wider rollout.

**Illustrative trigger (source):** A client disputes an on-time delivery milestone; teams cannot reconcile release, incident and customer-success records (invented discovery context).

**Scenario used in this demo:** A multi-tenant delivery platform shows noisy alerts; operations must separate real incidents from noise without crossing tenant boundaries. The source has the most AIOps and SRE material of the series.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Landscape, signals, tiers, rhythm, HA and DR questions, tests | **New design (synthetic)** |
| SAP operations tooling behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which operational responses may OmniTech automate, which need human approval, and which are never automated?

**Accountable owner (proposed):** OTS-P13 Priya Shah for operational risk, OTS-P04 Arjun Mehta for the platform, OTS-P10 Omar Haddad for access and security.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OTS-P04 | Arjun Mehta, Chief Technology Officer | Funds operations modernization; accepts residual risk with F |
| OTS-P12 | Daniel Weber, Director Enterprise Architecture | Owns the operations and transport standard |
| OTS-P10 | Omar Haddad, CISO and Supply-Chain Security Lead | Approves privileged access and automation boundaries |
| OTS-P09 | Mei Lin, Data Governance and Knowledge Lead | Data and AI governance for operational data |
| OTS-P05 | Elena Fischer, Chief Customer Success Officer | Business owner of the first protected service |
| OTS-P08 | Marcus Okoro, SRE and Managed Services Director | Business owner of the second protected service |
| OTS-P13 | Priya Shah, DevSecOps and Release Director | Operational authority; veto where operations or safety are at risk |

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
| Delivery pipeline | High |
| ITSM | High |
| Customer-success application | Medium |
| Core ERP on HANA | High |
| Observability stack | High |
| Non-production systems | Low |

## 8. Signals, responses and autonomy tiers

**Tiers:** A answer or recommend only; B human-approved action; C never automated.

| Signal | Response | Tier |
|---|---|---|
| Alert storm on one service | Group and deduplicate; propose one incident | A answer or recommend only |
| Error budget burn | Recommend release slowdown | A answer or recommend only |
| Pipeline failure on a release train | Summarize; notify the release owner | B human-approved action |
| Cross-tenant data access pattern | Open a security incident; no automatic block without approval | B human-approved action |
| Request to roll back a production release | Prepared; release owner executes | C never automated |
| Request to widen telemetry access across tenants | Refused | C never automated |

**Always tier C:** production HA failover, restore from backup, upgrades, production transport imports and authorization changes.

## 9. Change and transport policy (new design)

| Rule | Design |
|---|---|
| Pipeline | Development, quality, production; no direct production changes |
| Collision check | The pipeline shows two changes touching the same object |
| Freeze windows | Release trains and customer milestone dates (illustrative). |
| Exceptions | Named approver, expiry date and rollback plan recorded |
| Evidence | Each import records who approved and when |

## 10. High availability and disaster recovery questions

**Focus:** Delivery and ITSM first; tenant isolation applies to recovery tooling as well.

| Question | Owner (proposed) | Value |
|---|---|---|
| Recovery time objective per service | OTS-P13 Priya Shah | To be decided |
| Recovery point objective per service | OTS-P13 Priya Shah | To be decided |
| Last restore test and its result | OTS-P12 Daniel Weber | Evidence slot empty |
| Last failover test and its result | OTS-P12 Daniel Weber | Evidence slot empty |
| Who approves a production failover | OTS-P04 Arjun Mehta | To be named |

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
| T1 Alert storm | Hundreds of alerts for one cause | One grouped incident; reviewer confirms the cause |
| T2 Tenant boundary | An agent proposes cross-tenant correlation | Refused; isolation holds |
| T3 Rollback request | A rollback is requested during a milestone | Tier C; release owner decides |

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

- [OmniTech case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/08-information-technology/omnitech-solutions-ltd)
- [OmniTech persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/08-information-technology/omnitech-solutions-ltd/personas/persona-cards.md)

