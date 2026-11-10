# OmniConnect — SAP Basis Modernization, AIOps and Autonomous Operations

## Demo 06 of the BTM11 Communication Services Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Communication Services (COM) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniconnect-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md)

> **Evidence boundary:** OmniConnect is an **aspirational case study**. The case source contains almost no run-operations detail, so the landscape, signals and rhythm below are synthetic design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `COM-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Basis, HANA monitoring, transport automation, high availability and disaster recovery, and AI-driven operations: what may be automated, and what must stay with a person?*

**What this file shows:** a synthetic operations landscape for OmniConnect, six signals with a response and an autonomy tier, a change and transport policy, and the HA and DR questions to settle.

**What it does not show:** a monitored system, a tested failover or an automated remediation.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 37B communications group; 62,000 employees; 28 countries; 210M subscriptions |
| Business mix | Mobile 34%; fixed and fiber 25%; media 19%; enterprise 14%; advertising and data 8% |
| Source problem | Separate network, customer, billing and content stacks; manual activation and assurance; identity and consent silos |

**Decision under discussion (source):** Fund a bounded converged-activation pilot with privacy, service-state, recovery and economic evidence before expansion.

**Illustrative trigger (source):** A converged bundle shows billing active while connectivity and content entitlement remain incomplete; care and network teams cannot reconcile status (invented, not an actual outage).

**Scenario used in this demo:** A telecom assurance landscape shows fault noise after a network event; enterprise IT operations must correlate customer-impact signals without controlling network elements. The source mentions AIOps once.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Landscape, signals, tiers, rhythm, HA and DR questions, tests | **New design (synthetic)** |
| SAP operations tooling behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which operational responses may OmniConnect automate, which need human approval, and which are never automated?

**Accountable owner (proposed):** OCN-P04 Arjun Mehta for operational risk, OCN-P06 Sofia Tan for the platform, OCN-P10 Omar Haddad for access and security.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OCN-P06 | Sofia Tan, Chief Digital and Information Officer | Funds operations modernization; accepts residual risk with F |
| OCN-P12 | Daniel Weber, Director Enterprise Architecture | Owns the operations and transport standard |
| OCN-P10 | Omar Haddad, CISO and Resilience Lead | Approves privileged access and automation boundaries |
| OCN-P09 | Mei Lin, Subscriber Data and Consent Lead | Data and AI governance for operational data |
| OCN-P13 | Priya Shah, Service Catalog and Fulfillment Lead | Business owner of the first protected service |
| OCN-P08 | Marcus Okoro, Service Assurance and NOC Director | Business owner of the second protected service |
| OCN-P04 | Arjun Mehta, Chief Network Officer | Operational authority; veto where operations or safety are at risk |

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
| Order and provisioning platform | High |
| Billing platform | High |
| Assurance and ticketing | High |
| Customer data platform | Medium |
| Core ERP on HANA | Medium |
| Non-production systems | Low |

## 8. Signals, responses and autonomy tiers

**Tiers:** A answer or recommend only; B human-approved action; C never automated.

| Signal | Response | Tier |
|---|---|---|
| Provisioning queue growth | Summarize; notify the fulfilment owner | A answer or recommend only |
| Billing job overrun | Recommend priority; owner decides | B human-approved action |
| Fault-noise burst after a network event | Group by fault id; one notice | A answer or recommend only |
| Care system latency | Page on-call | B human-approved action |
| Consent service errors | Open an incident; owner informed | B human-approved action |
| Request to change a network element via the IT toolchain | Refused; out of scope | C never automated |

**Always tier C:** production HA failover, restore from backup, upgrades, production transport imports and authorization changes.

## 9. Change and transport policy (new design)

| Rule | Design |
|---|---|
| Pipeline | Development, quality, production; no direct production changes |
| Collision check | The pipeline shows two changes touching the same object |
| Freeze windows | Product launches, billing cycles and storm seasons (illustrative). |
| Exceptions | Named approver, expiry date and rollback plan recorded |
| Evidence | Each import records who approved and when |

## 10. High availability and disaster recovery questions

**Focus:** Order, billing and consent services first.

| Question | Owner (proposed) | Value |
|---|---|---|
| Recovery time objective per service | OCN-P04 Arjun Mehta | To be decided |
| Recovery point objective per service | OCN-P04 Arjun Mehta | To be decided |
| Last restore test and its result | OCN-P12 Daniel Weber | Evidence slot empty |
| Last failover test and its result | OCN-P12 Daniel Weber | Evidence slot empty |
| Who approves a production failover | OCN-P06 Sofia Tan | To be named |

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
| T1 Network boundary | An agent proposes a network action | Refused; boundary holds |
| T2 Billing overrun | Billing overruns into customer hours | Advisory only; billing owner decides |
| T3 Consent errors | Consent service errors during a campaign | Campaign pauses for affected purposes; owner confirms |

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

- [OmniConnect case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/09-communication-services/omniconnect-media-networks-ltd)
- [OmniConnect persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/personas/persona-cards.md)

