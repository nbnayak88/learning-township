# OmniHealth — Migration Path to NextGen Architecture: Waves, Custom Code and Clean Core Readiness

## Demo 10 of the BTM11 Health Care Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Health Care (HC) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnihealth-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniHealth is a **fictional educational case**. The case sources describe a target and a trigger but no current SAP estate; the options, waves and readiness questions below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `HC-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *How does an enterprise get from its current landscape to a clean-core, event-aware, AI-ready architecture without stopping the business?*

**What this file shows:** the path options, a sequence of waves for OmniHealth, the custom-code questions to ask before any wave, readiness gates and a rule for exceptions.

**What it does not show:** an inventory of a real estate, a migration estimate or a go-live plan. No durations or costs are stated.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 34B healthcare group; 126,000 staff; 19 countries |
| Network | 86 hospitals; 440 clinics; 670 diagnostic centres |
| Business mix | Acute 38%; primary 22%; diagnostics 18%; digital and pharmacy 12%; research and value-based 10% |

**Decision under discussion (source):** Select a bounded, non-clinical care-coordination pilot and evidence gates before enterprise expansion.

**Illustrative trigger (source):** A referral crosses facilities without clear ownership; the patient repeats information and a dashboard cannot reconcile episode status (invented; no actual patient incident is asserted).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, capabilities and value streams | **Source** |
| Path leaning, waves, readiness gates, tests | **New design (illustrative)** |
| SAP migration tooling and programmes | Public SAP documentation not reviewed in depth for this demo; **verify before use** |

## 4. Decision under discussion

**Decision:** Which path and which first wave does OmniHealth choose, and what must be true before each wave starts?

**Accountable owner (proposed):** OHS-P05 Sofia Tan, with OHS-P13 Daniel Weber for architecture and OHS-P03 Dr. Leila Morgan for operational readiness.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OHS-P05 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes |
| OHS-P13 | Daniel Weber, Enterprise Architecture Director | Owns standards and review |
| OHS-P10 | Omar Haddad, CISO and Privacy Lead | Security and boundary approval |
| OHS-P09 | Priya Nair, Patient Identity and Data Governance Lead | Data and AI governance |
| OHS-P07 | Dr. Amina Okafor, Nursing and Care Coordination Director | Business owner (first scope) |
| OHS-P04 | Dr. Arjun Mehta, Chief Clinical Operations Officer | Business owner (second scope) |
| OHS-P03 | Dr. Leila Morgan, Chief Medical Officer | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. Path options (new design, generic)

| Option | Idea | Favoured when | Main risk |
|---|---|---|---|
| Greenfield | Start a new system and move selected data | The current estate is hard to fix and the business can accept redesign | Loss of useful history; long parallel running |
| Brownfield (system conversion) | Convert the existing system in place | Processes are stable and custom code can be remediated | Carries old customisation forward |
| Selective or bluefield | Move chosen processes or data, redesign others | Some areas need change and others do not | Needs clear scope rules and data ownership |
| Side-by-side first | Build new capability on BTP and leave the core alone | The business need is new and the core is stable | Integration sprawl without the admission rule |

**Leaning for this case:** Selective path for administrative systems; clinical systems are out of scope. This is a hypothesis for discovery, not a recommendation.

## 7. Waves (new design)

| Wave | Scope |
|---|---|
| Wave 1 | referral and scheduling |
| Wave 2 | identity matching and reporting |
| Wave 3 | supply and finance |

**Wave entry gates:** inventory complete for the wave; owners named; Clean Core admission rule applied to every extension; rollback path written; freeze calendar checked; evidence slots for tests prepared.

## 8. Custom code and extension readiness

| Question | Why it matters | Evidence needed | Value |
|---|---|---|---|
| Which custom objects touch this wave? | Hidden dependencies stop a wave | Usage and owner for each | Not collected |
| Which are still used? | Unused code is retired, not migrated | Usage evidence | Not collected |
| Which extensions fit the Clean Core levels? | Decides migrate, rebuild or retire (Demo 02) | Level assessment | Not collected |
| Which interfaces must stay unchanged? | Protects partners and operations | Interface list with owners | Not collected |

**Sector readiness questions:**

- Which administrative systems share patient pseudonyms?
- Which clinical dependencies exist?
- What are the clinic peak times?
- Which custom reports exist?

## 9. Exceptions

An exception to a gate needs a named approver, an expiry date, a rollback plan and a note in the decision record. Exceptions that repeat become a design review item.

## 10. Hands-on exercise (synthetic data)

1. List ten synthetic custom objects (prefix `HC-SYN`) and place each in migrate, rebuild or retire with a reason.
2. Order the three waves and write the entry gate for the first.
3. Mark the freeze calendar and test the first wave date against it.
4. Write one exception and its expiry.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Clinical dependency | A wave touches a clinical link | Out of scope; owner decides |
| T2 Clinic peak | A wave meets a peak | Calendar rule |
| T3 Identity change | Identity rules change | Privacy owner approves |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Waves with all entry gates met on paper | Review of the gate list | Not measured |
| Custom objects with owner and usage evidence | Count against the inventory | Not measured |
| Exceptions with approver and expiry | Count | Not measured |
| Rollback paths written per wave | Count | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Path options and why not one answer | Shared options |
| 0:20 to 1:00 | Waves and gates | Wave plan without dates |
| 1:00 to 1:45 | Custom code triage | Ten objects placed |
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

- [SAP Clean Core guidance: see Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md)
- SAP Activate methodology (verify the current SAP page before citing)

- [OmniHealth case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/06-health-care/omnihealth-systems-ltd)
- [OmniHealth persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/personas/persona-cards.md)

