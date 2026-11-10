# OmniSpace — Resilience and Failure Drills for Intelligent Operations

## Demo 12 of the BTM11 Real Estate Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Real Estate (RE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnispace-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md)

> **Evidence boundary:** OmniSpace is a **fictional educational case**. The case sources hold little resilience detail; the drills, degraded modes and tests below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `RE-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *What happens on the worst day, who knows what to do, and what evidence shows the plan was ever tested?*

**What this file shows:** five failure drills for OmniSpace with an expected behaviour and an owner, a degraded mode, a third-party dependency and the rule that a resilience claim needs test evidence.

**What it does not show:** a tested failover, a recovery time or an audited continuity plan.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | Not supplied in the case; no enterprise numerical profile, budget or quantified benefits |
| Scope | Fictional global real-estate enterprise; property, tenant, ESG, recruiting, finance and procurement workstreams |
| Source problem | Fragmented architecture, processes, delivery evidence and adoption |

**Decision under discussion (source):** Select one capability or process pilot and prove its strategy-to-value traceability before scaling tools.

**Illustrative trigger (source):** A property-service workflow is declared live, but property teams still use spreadsheets, tenant requests remain unresolved, and test and adoption records cannot explain the claimed benefit (invented learning scenario).

**Scenario from Demo 06:** A property-service landscape is small; operations has no baseline, and spreadsheets still carry work. A first step is visibility, not autonomy.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Drills, degraded mode, evidence rule, tests | **New design (synthetic)** |
| SAP and cloud recovery capabilities | Not exercised here; verify per deployment |

## 4. Decision under discussion

**Decision:** Which failures does OmniSpace rehearse first, who runs each drill, and what counts as passed?

**Accountable owner (proposed):** OSP-P14 Ingrid Sørensen, with OSP-P05 Sofia Tan accepting residual risk.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OSP-P05 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes |
| OSP-P10 | Daniel Weber, Enterprise Architecture Director | Owns standards and review |
| OSP-P09 | Omar Haddad, CISO and Resilience Lead | Security and boundary approval |
| OSP-P08 | Mei Lin, Enterprise Data and ESG Lead | Data and AI governance |
| OSP-P03 | Maya Patel, Property Operations Director | Business owner (first scope) |
| OSP-P16 | Thomas van Dijk, Value Realization Office Lead | Business owner (second scope) |
| OSP-P14 | Ingrid Sørensen, Adoption and Change Lead | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. Services at stake (from Demo 06)

| Component | Criticality |
|---|---|
| Property operations application | High |
| Tenant request channel | High |
| Integration layer | Medium |
| Core ERP on HANA (finance) | High |
| Reporting store | Medium |
| Non-production systems | Low |

## 7. Failure drills (new design)

| Drill | Injected failure | Expected behaviour | Drill owner (proposed) | Result |
|---|---|---|---|---|
| Request channel outage | Channel down | Phone and email fallback by owner | OSP-P03 Maya Patel | Not run |
| Work-order system outage | System down | Manual log; reconcile | OSP-P16 Thomas van Dijk | Not run |
| Reporting outage | Reporting unavailable | Last good report labelled | OSP-P08 Mei Lin | Not run |
| Backup failure | Backup fails | Restore evidence | OSP-P14 Ingrid Sørensen | Not run |
| Vendor outage | A SaaS vendor is down | Fallback documented | OSP-P05 Sofia Tan | Not run |

**Pass rule:** a drill passes only when an owner followed a written runbook, the expected behaviour was observed, and the evidence is recorded. Nothing is stated as passed in this file.

## 8. Degraded mode and dependencies

| Item | Design |
|---|---|
| Degraded mode | Phone and spreadsheet fallback with a reconciliation task. |
| Exit criteria | Named owner, review date and a reconciliation task before returning to normal |
| Third-party dependency | SaaS vendors and contractors. |
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
| T1 Fallback drift | Fallback continues | Exit criteria |
| T2 Untested restore | No restore test | No claim |
| T3 Vendor outage owner | Nobody owns the vendor contact | Owner assigned |

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

- [OmniSpace case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/11-real-estate/omnispace-real-estate-ltd)
- [OmniSpace persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/personas/persona-cards.md)

