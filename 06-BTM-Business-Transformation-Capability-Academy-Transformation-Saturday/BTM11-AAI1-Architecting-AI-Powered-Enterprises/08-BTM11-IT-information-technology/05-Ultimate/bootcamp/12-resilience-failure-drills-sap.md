# OmniTech — Resilience and Failure Drills for Intelligent Operations

## Demo 12 of the BTM11 Information Technology Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Information Technology (IT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnitech-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniTech is an **aspirational case study**. The case sources hold little resilience detail; the drills, degraded modes and tests below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *What happens on the worst day, who knows what to do, and what evidence shows the plan was ever tested?*

**What this file shows:** five failure drills for OmniTech with an expected behaviour and an owner, a degraded mode, a third-party dependency and the rule that a resilience claim needs test evidence.

**What it does not show:** a tested failover, a recovery time or an audited continuity plan.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 39B technology provider; 98,000 employees; 41 countries; 11,500 clients |
| Business mix | Cloud and platform 31%; software 25%; cyber 18%; AI and data 16%; managed services 10% |
| Source problem | Fragmented lifecycle tooling, bespoke integrations, poor data and AI reuse, late security and observability |

**Decision under discussion (source):** Fund a bounded platform-to-client-outcome pilot with security, recovery and economic evidence before wider rollout.

**Illustrative trigger (source):** A client disputes an on-time delivery milestone; teams cannot reconcile release, incident and customer-success records (invented discovery context).

**Scenario from Demo 06:** A multi-tenant delivery platform shows noisy alerts; operations must separate real incidents from noise without crossing tenant boundaries. The source has the most AIOps and SRE material of the series.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Drills, degraded mode, evidence rule, tests | **New design (synthetic)** |
| SAP and cloud recovery capabilities | Not exercised here; verify per deployment |

## 4. Decision under discussion

**Decision:** Which failures does OmniTech rehearse first, who runs each drill, and what counts as passed?

**Accountable owner (proposed):** OTS-P13 Priya Shah, with OTS-P04 Arjun Mehta accepting residual risk.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OTS-P04 | Arjun Mehta, Chief Technology Officer | Funds and prioritizes |
| OTS-P12 | Daniel Weber, Director Enterprise Architecture | Owns standards and review |
| OTS-P10 | Omar Haddad, CISO and Supply-Chain Security Lead | Security and boundary approval |
| OTS-P09 | Mei Lin, Data Governance and Knowledge Lead | Data and AI governance |
| OTS-P05 | Elena Fischer, Chief Customer Success Officer | Business owner (first scope) |
| OTS-P08 | Marcus Okoro, SRE and Managed Services Director | Business owner (second scope) |
| OTS-P13 | Priya Shah, DevSecOps and Release Director | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. Services at stake (from Demo 06)

| Component | Criticality |
|---|---|
| Delivery pipeline | High |
| ITSM | High |
| Customer-success application | Medium |
| Core ERP on HANA | High |
| Observability stack | High |
| Non-production systems | Low |

## 7. Failure drills (new design)

| Drill | Injected failure | Expected behaviour | Drill owner (proposed) | Result |
|---|---|---|---|---|
| Pipeline outage | Delivery pipeline down | Manual release freeze | OTS-P05 Elena Fischer | Not run |
| Observability loss | Telemetry unavailable | Degraded mode; owner | OTS-P13 Priya Shah | Not run |
| Tenant incident | Cross-tenant exposure suspected | Isolate; Security leads | OTS-P10 Omar Haddad | Not run |
| ITSM outage | ITSM down | Paper incident log | OTS-P08 Marcus Okoro | Not run |
| Backup failure | Backup fails | Restore evidence | OTS-P12 Daniel Weber | Not run |

**Pass rule:** a drill passes only when an owner followed a written runbook, the expected behaviour was observed, and the evidence is recorded. Nothing is stated as passed in this file.

## 8. Degraded mode and dependencies

| Item | Design |
|---|---|
| Degraded mode | Release freeze with manual incident logging. |
| Exit criteria | Named owner, review date and a reconciliation task before returning to normal |
| Third-party dependency | Cloud providers and client-hosted systems. |
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
| T1 Observability gap | No telemetry for hours | Degraded mode owner |
| T2 Tenant drill | Drill reveals a shared secret | Fix; incident |
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

- [OmniTech case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/08-information-technology/omnitech-solutions-ltd)
- [OmniTech persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/08-information-technology/omnitech-solutions-ltd/personas/persona-cards.md)

