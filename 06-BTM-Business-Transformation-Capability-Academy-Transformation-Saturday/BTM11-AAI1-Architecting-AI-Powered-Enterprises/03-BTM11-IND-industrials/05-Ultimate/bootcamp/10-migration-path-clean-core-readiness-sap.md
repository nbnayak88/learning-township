# OmniWorks Industrial Systems Ltd. — Migration Path to NextGen Architecture: Waves, Custom Code and Clean Core Readiness

## Demo 10 of the BTM11 Industrials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Industrials (IND) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniworks-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md)

> **Evidence boundary:** OmniWorks Industrial Systems Ltd. is a **fictional educational case**. The case sources describe a target and a trigger but no current SAP estate; the options, waves and readiness questions below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IND-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *How does an enterprise get from its current landscape to a clean-core, event-aware, AI-ready architecture without stopping the business?*

**What this file shows:** the path options, a sequence of waves for OmniWorks, the custom-code questions to ask before any wave, readiness gates and a rule for exceptions.

**What it does not show:** an inventory of a real estate, a migration estimate or a go-live plan. No durations or costs are stated.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 48B revenue; 74,000 employees; 36 countries; 61 plants and facilities; 320 service depots; 7,200 suppliers |
| Business mix | Industrial automation 27%; aerospace and defence 23%; transport and mobility 19%; infrastructure 16%; aftermarket and lifecycle services 15% |
| Burning platform | Recurring transport asset failures cannot be consistently traced across configuration, telemetry, supplier batches and maintenance history |

**Decision under discussion (source):** Turn a USD 575M transformation envelope into credible customer, operational and financial value without disrupting safety-critical operations.

**Illustrative trigger (source):** Repeat customer asset failures expose fragmented engineering-to-service information, and the business wants to sell uptime rather than equipment (hero story).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, capabilities and value streams | **Source** |
| Path leaning, waves, readiness gates, tests | **New design (illustrative)** |
| SAP migration tooling and programmes | Public SAP documentation not reviewed in depth for this demo; **verify before use** |

## 4. Decision under discussion

**Decision:** Which path and which first wave does OmniWorks choose, and what must be true before each wave starts?

**Accountable owner (proposed):** OW-P05 Priya Nair, with OW-P11 Hannah Fischer for architecture and OW-P12 Daniel Okafor for operational readiness.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OW-P05 | Priya Nair, CIDO | Funds and prioritizes |
| OW-P11 | Hannah Fischer, Director, Enterprise Architecture | Owns standards and review |
| OW-P06 | Marcus Vogel, CISO | Security and boundary approval |
| OW-P15 | Dr. Leila Haddad, Head of Data Governance & AI | Data and AI governance |
| OW-P09 | Isabel Torres, Chief Customer & Service Officer | Business owner (first scope) |
| OW-P10 | Ravi Deshpande, VP Manufacturing, Pune Operations | Business owner (second scope) |
| OW-P12 | Daniel Okafor, Field Service Operations Manager | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. Path options (new design, generic)

| Option | Idea | Favoured when | Main risk |
|---|---|---|---|
| Greenfield | Start a new system and move selected data | The current estate is hard to fix and the business can accept redesign | Loss of useful history; long parallel running |
| Brownfield (system conversion) | Convert the existing system in place | Processes are stable and custom code can be remediated | Carries old customisation forward |
| Selective or bluefield | Move chosen processes or data, redesign others | Some areas need change and others do not | Needs clear scope rules and data ownership |
| Side-by-side first | Build new capability on BTP and leave the core alone | The business need is new and the core is stable | Integration sprawl without the admission rule |

**Leaning for this case:** Per-system choice; PLM and service links first because the case trigger starts there. This is a hypothesis for discovery, not a recommendation.

## 7. Waves (new design)

| Wave | Scope |
|---|---|
| Wave 1 | service and configuration baseline link |
| Wave 2 | supplier quality notices |
| Wave 3 | remaining manufacturing and finance flows |

**Wave entry gates:** inventory complete for the wave; owners named; Clean Core admission rule applied to every extension; rollback path written; freeze calendar checked; evidence slots for tests prepared.

## 8. Custom code and extension readiness

| Question | Why it matters | Evidence needed | Value |
|---|---|---|---|
| Which custom objects touch this wave? | Hidden dependencies stop a wave | Usage and owner for each | Not collected |
| Which are still used? | Unused code is retired, not migrated | Usage evidence | Not collected |
| Which extensions fit the Clean Core levels? | Decides migrate, rebuild or retire (Demo 02) | Level assessment | Not collected |
| Which interfaces must stay unchanged? | Protects partners and operations | Interface list with owners | Not collected |

**Sector readiness questions:**

- Which custom code touches configuration management?
- Which depots depend on which interfaces?
- Which release trains cannot move?
- Which OT edge links must stay unchanged?

## 9. Exceptions

An exception to a gate needs a named approver, an expiry date, a rollback plan and a note in the decision record. Exceptions that repeat become a design review item.

## 10. Hands-on exercise (synthetic data)

1. List ten synthetic custom objects (prefix `IND-SYN`) and place each in migrate, rebuild or retire with a reason.
2. Order the three waves and write the entry gate for the first.
3. Mark the freeze calendar and test the first wave date against it.
4. Write one exception and its expiry.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Release train clash | A wave collides with a release train | Calendar rule |
| T2 Custom code on baseline | Custom code alters the baseline | Admission rule decides |
| T3 Depot dependency | A depot relies on an old interface | Dependency inventory blocks the wave |

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

- [OmniWorks Industrial Systems Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/03-industrials/omniworks-industrial-systems)
- [OmniWorks Industrial Systems Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md)

