# OmniDaily — Resilience and Failure Drills for Intelligent Operations

## Demo 12 of the BTM11 Consumer Staples Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Staples (CS) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnidaily-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md)

> **Evidence boundary:** OmniDaily is a **fictional educational case**. The case sources hold little resilience detail; the drills, degraded modes and tests below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CS-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *What happens on the worst day, who knows what to do, and what evidence shows the plan was ever tested?*

**What this file shows:** five failure drills for OmniDaily with an expected behaviour and an owner, a degraded mode, a third-party dependency and the rule that a resilience claim needs test evidence.

**What it does not show:** a tested failover, a recovery time or an audited continuity plan.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 51B staples group; 84,000 employees; 57 countries; 420M households served |
| Business mix | Foods 30%; beverages 23%; home care 19%; personal care 18%; wellness 10% |
| Burning platform | Demand, promotion, planning, product and ingredient data, quality and route-to-market execution fragmented across 160+ applications |

**Decision under discussion (source):** Fund a bounded demand-to-shelf and quality-evidence pilot before approving enterprise scale.

**Illustrative trigger (source):** A promotion creates a shelf gap while a quality-held batch appears available in a delayed distributor feed (invented; no real safety event is claimed).

**Scenario from Demo 06:** A promotion peak and a quality hold coincide with a delayed distributor interface; operations must tell which delays are system faults and which are partner feeds.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Drills, degraded mode, evidence rule, tests | **New design (synthetic)** |
| SAP and cloud recovery capabilities | Not exercised here; verify per deployment |

## 4. Decision under discussion

**Decision:** Which failures does OmniDaily rehearse first, who runs each drill, and what counts as passed?

**Accountable owner (proposed):** ODG-P09 Elena Petrović, with ODG-P05 Sofia Alvarez accepting residual risk.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| ODG-P05 | Sofia Alvarez, Chief Digital and Data Officer | Funds and prioritizes |
| ODG-P13 | Priya Nair, Director Enterprise Architecture | Owns standards and review |
| ODG-P12 | Omar Haddad, CISO and Privacy Lead | Security and boundary approval |
| ODG-P08 | Mei Lin, Head of Product and Ingredient Stewardship | Data and AI governance |
| ODG-P07 | David Okoro, Global Quality and Product Safety Director | Business owner (first scope) |
| ODG-P10 | Rohan Shah, Distributor and Field Execution Director | Business owner (second scope) |
| ODG-P09 | Elena Petrović, Plant Operations Director | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. Services at stake (from Demo 06)

| Component | Criticality |
|---|---|
| Core ERP on HANA | High |
| Planning and promotion application | High |
| Quality system | High: holds and releases |
| Distributor feed interface | High: external partners |
| Manufacturing execution link | High |
| Non-production systems | Low |

## 7. Failure drills (new design)

| Drill | Injected failure | Expected behaviour | Drill owner (proposed) | Result |
|---|---|---|---|---|
| Distributor feed outage | Feed unavailable | Stale label; partner owner contacted | ODG-P10 Rohan Shah | Not run |
| Quality system outage | Holds cannot be recorded | Paper hold log; all releases paused | ODG-P07 David Okoro | Not run |
| Planning run failure | Planning fails overnight | Last good plan with label | ODG-P09 Elena Petrović | Not run |
| Promotion peak overload | Peak load | Priority classes | ODG-P13 Priya Nair | Not run |
| Backup failure | Backup fails | Restore evidence reviewed | ODG-P05 Sofia Alvarez | Not run |

**Pass rule:** a drill passes only when an owner followed a written runbook, the expected behaviour was observed, and the evidence is recorded. Nothing is stated as passed in this file.

## 8. Degraded mode and dependencies

| Item | Design |
|---|---|
| Degraded mode | Paper hold log and manual release pause, reconciled afterwards. |
| Exit criteria | Named owner, review date and a reconciliation task before returning to normal |
| Third-party dependency | Distributors and logistics partners. |
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
| T1 Hold during outage | A hold arises while the system is down | Paper log; release paused |
| T2 Stale plan used | Last good plan is old | As-of label |
| T3 Partner outage ownership | Nobody owns the partner contact | Owner assigned |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Drills with a runbook, owner and second person | Count of five | Not measured |
| Resilience claims with recorded evidence | Count against the evidence table | Not measured |
| Degraded modes with exit criteria | Review | Not measured |
| Third-party contacts with a named owner | Count | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

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
| Customer-confirmed requirements | Not applicable (fictional case) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP Cloud ALM](https://www.sap.com/products/technology-platform/cloud-alm.html)
- [Demo 06 operations design](06-basis-modernization-aiops-autonomous-operations-sap.md)

- [OmniDaily case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/05-consumer-staples/omnidaily-consumer-goods-ltd)
- [OmniDaily persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md)

