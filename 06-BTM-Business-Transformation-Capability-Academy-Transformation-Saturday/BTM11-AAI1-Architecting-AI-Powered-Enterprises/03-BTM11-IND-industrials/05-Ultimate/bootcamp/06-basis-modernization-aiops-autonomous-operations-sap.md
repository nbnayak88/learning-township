# OmniWorks Industrial Systems Ltd. — SAP Basis Modernization, AIOps and Autonomous Operations

## Demo 06 of the BTM11 Industrials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Industrials (IND) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniworks-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md)

> **Evidence boundary:** OmniWorks Industrial Systems Ltd. is a **fictional educational case**. The case source contains almost no run-operations detail, so the landscape, signals and rhythm below are synthetic design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IND-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Basis, HANA monitoring, transport automation, high availability and disaster recovery, and AI-driven operations: what may be automated, and what must stay with a person?*

**What this file shows:** a synthetic operations landscape for OmniWorks, six signals with a response and an autonomy tier, a change and transport policy, and the HA and DR questions to settle.

**What it does not show:** a monitored system, a tested failover or an automated remediation.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 48B revenue; 74,000 employees; 36 countries; 61 plants and facilities; 320 service depots; 7,200 suppliers |
| Business mix | Industrial automation 27%; aerospace and defence 23%; transport and mobility 19%; infrastructure 16%; aftermarket and lifecycle services 15% |
| Burning platform | Recurring transport asset failures cannot be consistently traced across configuration, telemetry, supplier batches and maintenance history |

**Decision under discussion (source):** Turn a USD 575M transformation envelope into credible customer, operational and financial value without disrupting safety-critical operations.

**Illustrative trigger (source):** Repeat customer asset failures expose fragmented engineering-to-service information, and the business wants to sell uptime rather than equipment (hero story).

**Scenario used in this demo:** Service peaks overload the enterprise landscape while an engineering release is being transported; operators need to know whether the issue is capacity, a transport or an interface.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Landscape, signals, tiers, rhythm, HA and DR questions, tests | **New design (synthetic)** |
| SAP operations tooling behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which operational responses may OmniWorks automate, which need human approval, and which are never automated?

**Accountable owner (proposed):** OW-P12 Daniel Okafor for operational risk, OW-P05 Priya Nair for the platform, OW-P06 Marcus Vogel for access and security.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OW-P05 | Priya Nair, CIDO | Funds operations modernization; accepts residual risk with F |
| OW-P11 | Hannah Fischer, Director, Enterprise Architecture | Owns the operations and transport standard |
| OW-P06 | Marcus Vogel, CISO | Approves privileged access and automation boundaries |
| OW-P15 | Dr. Leila Haddad, Head of Data Governance & AI | Data and AI governance for operational data |
| OW-P09 | Isabel Torres, Chief Customer & Service Officer | Business owner of the first protected service |
| OW-P10 | Ravi Deshpande, VP Manufacturing, Pune Operations | Business owner of the second protected service |
| OW-P12 | Daniel Okafor, Field Service Operations Manager | Operational authority; veto where operations or safety are at risk |

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
| Field service application | High: dispatch and parts |
| PLM system | High: configuration baseline |
| Integration platform | High |
| Customer portal | Medium |
| Non-production systems | Low |

## 8. Signals, responses and autonomy tiers

**Tiers:** A answer or recommend only; B human-approved action; C never automated.

| Signal | Response | Tier |
|---|---|---|
| Field service dispatch latency rises | Correlate with recent transports and queue depth | A answer or recommend only |
| Integration errors after an engineering release | Propose rollback candidates | B human-approved action |
| HANA expensive statement spike | Recommend analysis; DBA decides | A answer or recommend only |
| Transport import error in the quality system | Summarize the object and owner | A answer or recommend only |
| Portal availability drops | Open an incident; notify the service owner | B human-approved action |
| Request to import to production out of window | Refused; change policy applies | C never automated |

**Always tier C:** production HA failover, restore from backup, upgrades, production transport imports and authorization changes.

## 9. Change and transport policy (new design)

| Rule | Design |
|---|---|
| Pipeline | Development, quality, production; no direct production changes |
| Collision check | The pipeline shows two changes touching the same object |
| Freeze windows | Peak service seasons and engineering release trains (illustrative). |
| Exceptions | Named approver, expiry date and rollback plan recorded |
| Evidence | Each import records who approved and when |

## 10. High availability and disaster recovery questions

**Focus:** Dispatch and configuration baseline services first.

| Question | Owner (proposed) | Value |
|---|---|---|
| Recovery time objective per service | OW-P12 Daniel Okafor | To be decided |
| Recovery point objective per service | OW-P12 Daniel Okafor | To be decided |
| Last restore test and its result | OW-P11 Hannah Fischer | Evidence slot empty |
| Last failover test and its result | OW-P11 Hannah Fischer | Evidence slot empty |
| Who approves a production failover | OW-P05 Priya Nair | To be named |

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
| T1 Release plus peak | A transport lands at a service peak | Freeze policy blocks; exception needs named approver |
| T2 Wrong correlation | Agent blames capacity when an interface is at fault | Evidence links required; operator verifies |
| T3 Out-of-window request | A request skips the pipeline | Refused; logged |

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

- [OmniWorks Industrial Systems Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/03-industrials/omniworks-industrial-systems)
- [OmniWorks Industrial Systems Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md)

