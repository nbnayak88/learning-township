# OmniGrid — Resilience and Failure Drills for Intelligent Operations

## Demo 12 of the BTM11 Utilities Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Utilities (UT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnigrid-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniGrid is an **aspirational case study**. The case sources hold little resilience detail; the drills, degraded modes and tests below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `UT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *What happens on the worst day, who knows what to do, and what evidence shows the plan was ever tested?*

**What this file shows:** five failure drills for OmniGrid with an expected behaviour and an owner, a degraded mode, a third-party dependency and the rule that a resilience claim needs test evidence.

**What it does not show:** a tested failover, a recovery time or an audited continuity plan.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 31B utility; 38,000 staff; 17 countries; 21M electricity, gas and water accounts |
| Business mix | Renewables 28%; networks 27%; retail 18%; conventional and flexible 15%; water and environment 12% |
| Source problem | Fragmented OT, field, customer and market data; variable generation; manual restoration; growing meter and sensor security demands |

**Decision under discussion (source):** Fund bounded outage, work-order and customer coordination evidence before wider modernization.

**Illustrative trigger (source):** A storm scenario generates conflicting outage, asset and work-order status; field and customer teams cannot reconcile ownership (invented learning context, not an actual incident).

**Scenario from Demo 06:** A storm exposes load on outage, work and customer-communication systems; enterprise operations must stay clearly apart from grid control (SCADA and ADMS control actions are out of scope).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Drills, degraded mode, evidence rule, tests | **New design (synthetic)** |
| SAP and cloud recovery capabilities | Not exercised here; verify per deployment |

## 4. Decision under discussion

**Decision:** Which failures does OmniGrid rehearse first, who runs each drill, and what counts as passed?

**Accountable owner (proposed):** OGU-P04 Arjun Mehta, with OGU-P06 Sofia Tan accepting residual risk.

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

## 6. Services at stake (from Demo 06)

| Component | Criticality |
|---|---|
| Outage management | High |
| Work and asset management | High |
| Customer communications | High |
| Integration gateway and event broker | High |
| Core ERP on HANA | Medium |
| Non-production systems | Low |

## 7. Failure drills (new design)

| Drill | Injected failure | Expected behaviour | Drill owner (proposed) | Result |
|---|---|---|---|---|
| Outage system failure | Outage management down | Manual log; restoration continues | OGU-P13 Priya Shah | Not run |
| Communications outage | Notification system down | Alternate channels by owner | OGU-P08 Marcus Okoro | Not run |
| Broker backlog | Event backlog in a storm | Priority classes; replay | OGU-P12 Daniel Weber | Not run |
| Backup failure | Backup fails | Restore evidence | OGU-P04 Arjun Mehta | Not run |
| Cyber incident | Suspected compromise | Separation from control systems | OGU-P10 Omar Haddad | Not run |

**Pass rule:** a drill passes only when an owner followed a written runbook, the expected behaviour was observed, and the evidence is recorded. Nothing is stated as passed in this file.

## 8. Degraded mode and dependencies

| Item | Design |
|---|---|
| Degraded mode | Manual outage log and phone dispatch. |
| Exit criteria | Named owner, review date and a reconciliation task before returning to normal |
| Third-party dependency | Contractor crews and telecom links. |
| Owner of the third-party contact | To be named |
| Actions never automated | Production failover, restore from backup, upgrades, production transport imports and authorization changes (tier C, Demo 06) |

## 9. Evidence rule

| Claim | Evidence required | Status |
|---|---|---|
| Backup exists | Job log with date | Evidence slot empty |
| Restore works | Restore test record with result | Evidence slot empty |
| Failover works | Failover test record with result | Evidence slot empty |
| Staff know the runbook | Drill record with participants | Evidence slot empty |

A claim without evidence is written as untested.

## 10. Hands-on exercise (synthetic data)

1. Choose one drill and write its runbook in ten lines.
2. Assign the owner and a second person.
3. Run the drill on paper and mark where the runbook was unclear.
4. Write the exit criteria for the degraded mode.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Manual log drift | Manual log continues | Exit criteria |
| T2 Storm backlog | Backlog grows | Priority classes |
| T3 Untested restore | No restore test | No claim |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Drills with a runbook, owner and second person | Count of five | Not measured |
| Resilience claims with recorded evidence | Count against the evidence table | Not measured |
| Degraded modes with exit criteria | Review | Not measured |
| Third-party contacts with a named owner | Count | Not measured |

No baseline, target or benefit is stated because none exists for this aspirational case study. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | From DR plans to drills | Shared problem statement |
| 0:20 to 1:00 | The five drills | Owners and expected behaviour |
| 1:00 to 1:45 | Runbook and degraded mode | One runbook written |
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
- [Demo 06 operations design](06-basis-modernization-aiops-autonomous-operations-sap.md)

- [OmniGrid case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/10-utilities/omnigrid-utilities-ltd)
- [OmniGrid persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/personas/persona-cards.md)

