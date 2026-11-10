# OmniCapital Financial Group — Migration Path to NextGen Architecture: Waves, Custom Code and Clean Core Readiness

## Demo 10 of the BTM11 Financials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Financials (FIN) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnicapital-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md)

> **Evidence boundary:** OmniCapital Financial Group is a **fictional educational case**. The case sources describe a target and a trigger but no current SAP estate; the options, waves and readiness questions below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `FIN-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *How does an enterprise get from its current landscape to a clean-core, event-aware, AI-ready architecture without stopping the business?*

**What this file shows:** the path options, a sequence of waves for OmniCapital, the custom-code questions to ask before any wave, readiness gates and a rule for exceptions.

**What it does not show:** an inventory of a real estate, a migration estimate or a go-live plan. No durations or costs are stated.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 46B financial group; USD 1.4T AUM; 58M customers; 32 countries |
| Business mix | Retail 31%; commercial 24%; wealth 19%; insurance 16%; payments and markets 10% |
| Source problem | Fragmented customer, product, risk and transaction data; manual review; stronger fraud, cyber and model-risk control needs |

**Decision under discussion (source):** Fund a bounded onboarding and document-exception pilot with control and value evidence before enterprise expansion.

**Illustrative trigger (source):** An SME customer repeatedly submits the same document while customer service and verification teams show different exception status (invented discovery context, not an actual incident).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, capabilities and value streams | **Source** |
| Path leaning, waves, readiness gates, tests | **New design (illustrative)** |
| SAP migration tooling and programmes | Public SAP documentation not reviewed in depth for this demo; **verify before use** |

## 4. Decision under discussion

**Decision:** Which path and which first wave does OmniCapital choose, and what must be true before each wave starts?

**Accountable owner (proposed):** OCF-P06 Sofia Chen, with OCF-P12 Daniel Weber for architecture and OCF-P05 Elena Fischer for operational readiness.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OCF-P06 | Sofia Chen, Chief Digital and Information Officer | Funds and prioritizes |
| OCF-P12 | Daniel Weber, Director Enterprise Architecture | Owns standards and review |
| OCF-P10 | Omar Haddad, CISO and Resilience Lead | Security and boundary approval |
| OCF-P09 | Mei Tan, Customer Identity and Data Lead | Data and AI governance |
| OCF-P03 | Priya Rao, Chief Customer and Retail Officer | Business owner (first scope) |
| OCF-P08 | Marcus Okoro, Financial Crime Operations Director | Business owner (second scope) |
| OCF-P05 | Elena Fischer, Chief Compliance and Conduct Officer | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. Path options (new design, generic)

| Option | Idea | Favoured when | Main risk |
|---|---|---|---|
| Greenfield | Start a new system and move selected data | The current estate is hard to fix and the business can accept redesign | Loss of useful history; long parallel running |
| Brownfield (system conversion) | Convert the existing system in place | Processes are stable and custom code can be remediated | Carries old customisation forward |
| Selective or bluefield | Move chosen processes or data, redesign others | Some areas need change and others do not | Needs clear scope rules and data ownership |
| Side-by-side first | Build new capability on BTP and leave the core alone | The business need is new and the core is stable | Integration sprawl without the admission rule |

**Leaning for this case:** Selective path with month-end and regulatory windows respected. This is a hypothesis for discovery, not a recommendation.

## 7. Waves (new design)

| Wave | Scope |
|---|---|
| Wave 1 | onboarding verification and exceptions |
| Wave 2 | customer service status views |
| Wave 3 | reporting and remaining flows |

**Wave entry gates:** inventory complete for the wave; owners named; Clean Core admission rule applied to every extension; rollback path written; freeze calendar checked; evidence slots for tests prepared.

## 8. Custom code and extension readiness

| Question | Why it matters | Evidence needed | Value |
|---|---|---|---|
| Which custom objects touch this wave? | Hidden dependencies stop a wave | Usage and owner for each | Not collected |
| Which are still used? | Unused code is retired, not migrated | Usage evidence | Not collected |
| Which extensions fit the Clean Core levels? | Decides migrate, rebuild or retire (Demo 02) | Level assessment | Not collected |
| Which interfaces must stay unchanged? | Protects partners and operations | Interface list with owners | Not collected |

**Sector readiness questions:**

- Which core interfaces cannot change?
- Which regulatory reports depend on custom code?
- What is the freeze calendar?
- Which partner gateways exist?

## 9. Exceptions

An exception to a gate needs a named approver, an expiry date, a rollback plan and a note in the decision record. Exceptions that repeat become a design review item.

## 10. Hands-on exercise (synthetic data)

1. List ten synthetic custom objects (prefix `FIN-SYN`) and place each in migrate, rebuild or retire with a reason.
2. Order the three waves and write the entry gate for the first.
3. Mark the freeze calendar and test the first wave date against it.
4. Write one exception and its expiry.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Month-end clash | A wave meets month-end | Calendar rule |
| T2 Report custom code | Custom code in a regulatory report | Admission rule and owner |
| T3 Gateway change | A partner gateway changes | Partner owner approves |

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

- [OmniCapital Financial Group case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/07-financials/omnicapital-financial-group-ltd)
- [OmniCapital Financial Group persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/personas/persona-cards.md)

