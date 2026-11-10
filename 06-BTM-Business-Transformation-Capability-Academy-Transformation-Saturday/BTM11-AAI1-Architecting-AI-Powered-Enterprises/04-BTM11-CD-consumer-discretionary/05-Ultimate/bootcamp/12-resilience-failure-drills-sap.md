# OmniVibe — Resilience and Failure Drills for Intelligent Operations

## Demo 12 of the BTM11 Consumer Discretionary Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Discretionary (CD) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnivibe-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniVibe is a **fictional educational case**. The case sources hold little resilience detail; the drills, degraded modes and tests below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CD-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *What happens on the worst day, who knows what to do, and what evidence shows the plan was ever tested?*

**What this file shows:** five failure drills for OmniVibe with an expected behaviour and an owner, a degraded mode, a third-party dependency and the rule that a resilience claim needs test evidence.

**What it does not show:** a tested failover, a recovery time or an audited continuity plan.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 28B consumer group; 72,000 employees; 48 countries |
| Business mix | Fashion 32%; beauty 18%; home 17%; specialty retail 15%; travel 10%; marketplace 8% |
| Network | 3,200 stores; 14 e-commerce sites; 26 distribution centres; 140 micro-fulfilment sites |

**Decision under discussion (source):** Select one brand and country workforce-to-service pilot and evidence gates before approving enterprise scale.

**Illustrative trigger (source):** A new associate lacks a completed onboarding and skills handoff while store readiness and channel information disagree (invented events that prompt discovery, per the case).

**Scenario from Demo 06:** Campaign and holiday peaks stress commerce and workforce systems at the same time; operations needs to protect store readiness and onboarding services.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Drills, degraded mode, evidence rule, tests | **New design (synthetic)** |
| SAP and cloud recovery capabilities | Not exercised here; verify per deployment |

## 4. Decision under discussion

**Decision:** Which failures does OmniVibe rehearse first, who runs each drill, and what counts as passed?

**Accountable owner (proposed):** OVC-P16 Nikhil Das, with OVC-P04 Ravi Kapoor accepting residual risk.

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

## 6. Services at stake (from Demo 06)

| Component | Criticality |
|---|---|
| Core HR (cloud) | High: onboarding |
| Workforce scheduling | High: store readiness |
| Order and commerce platform | High: peak revenue |
| Integration platform | High |
| Core ERP on HANA | High |
| Non-production systems | Low |

## 7. Failure drills (new design)

| Drill | Injected failure | Expected behaviour | Drill owner (proposed) | Result |
|---|---|---|---|---|
| Core HR outage | HR system down at a hiring peak | Onboarding pauses safely; manual route | OVC-P08 Sofia Mendes | Not run |
| Commerce outage | Commerce platform degraded in a campaign | Priority services protected | OVC-P06 Oliver Brooks | Not run |
| Scheduling failure | Scheduling unavailable | Manager roster fallback | OVC-P16 Nikhil Das | Not run |
| Integration failure | Events delayed | Replay and reconcile | OVC-P11 Priya Shah | Not run |
| Partner outage | Payment or logistics partner down | Fallback documented | OVC-P04 Ravi Kapoor | Not run |

**Pass rule:** a drill passes only when an owner followed a written runbook, the expected behaviour was observed, and the evidence is recorded. Nothing is stated as passed in this file.

## 8. Degraded mode and dependencies

| Item | Design |
|---|---|
| Degraded mode | Manager-run rosters and paper onboarding checklists, reconciled afterwards. |
| Exit criteria | Named owner, review date and a reconciliation task before returning to normal |
| Third-party dependency | Logistics, payment and franchise partners. |
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
| T1 Peak outage | Outage during a campaign | Priority services and owner |
| T2 Manual onboarding drift | Paper onboarding continues | Exit criteria |
| T3 Franchise gap | Franchise store loses access | Boundary and fallback |

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

- [OmniVibe case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/04-consumer-discretionary/omnivibe-consumer-ltd)
- [OmniVibe persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/personas/persona-cards.md)

