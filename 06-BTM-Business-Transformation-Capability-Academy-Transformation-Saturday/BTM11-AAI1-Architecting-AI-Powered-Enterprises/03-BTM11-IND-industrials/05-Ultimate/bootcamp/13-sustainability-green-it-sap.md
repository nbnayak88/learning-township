# OmniWorks Industrial Systems Ltd. — Sustainability and Green IT for Intelligent Operations

## Demo 13 of the BTM11 Industrials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Industrials (IND) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniworks-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniWorks Industrial Systems Ltd. is a **fictional educational case**. The case sources hold little sustainability data for the IT estate; the data products, levers and tests below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IND-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *How does the architecture support sustainability reporting, and how does it keep the footprint of IT and AI itself visible?*

**What this file shows:** two separate topics for OmniWorks: (1) data products that support sustainability reporting, and (2) the footprint of the IT and AI estate, with levers, an owner and an evidence rule.

**What it does not show:** an emissions figure, a footprint measurement or a reduction claim.

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
| Case facts, personas | **Source** |
| Sustainability data products, green IT levers, owners, tests | **New design (illustrative)** |
| SAP sustainability and cost tooling | Not exercised here; verify product names and scope on SAP's pages before use |

## 4. Decision under discussion

**Decision:** Which sustainability data does OmniWorks treat as governed data products, and who owns the footprint of its IT and AI estate?

**Accountable owner (proposed):** OW-P15 Dr. Leila Haddad for data and OW-P12 Daniel Okafor for the footprint of operations.

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

## 6. Two topics, kept apart

| Topic | What it covers | Why separate |
|---|---|---|
| Reporting data | Business data used for sustainability reporting (energy, emissions, supplier evidence) | Owned by business functions; follows reporting rules |
| IT and AI footprint | Energy and emissions from hosting, pipelines and model usage | Owned by technology and operations; different data sources |

**Sector emphasis:** Product-in-use data and repair-versus-replace decisions are the sector lever; tie them to the service baseline.

## 7. Sustainability data products (new design)

| Data product | Main source | Main risk |
|---|---|---|
| Product energy-in-use data | Telemetry and configuration | Unvalidated field data |
| Plant and depot energy view | Facilities and ERP data | Gaps across 61 plants and 320 depots |
| IT and AI footprint | Hosting records | Unmeasured assumptions |

Each product follows the Demo 07 rule: one owner, a quality rule and a visible status. Every figure shown carries its basis (measured, allocated or estimated) and its period.

## 8. Green IT levers (new design)

| Lever | Idea | Link to other demos | Owner (proposed) |
|---|---|---|---|
| Right-size non-production | Switch off or shrink unused systems | Demo 11 cost drivers | OW-P12 Daniel Okafor |
| Retention rules | Delete data nobody needs | Demo 07 data products | OW-P15 Dr. Leila Haddad |
| AI cost per use | Choose the smallest model that passes evaluation; cache repeated answers | Demos 03 and 09 | OW-P15 Dr. Leila Haddad |
| Event and batch volume | Avoid chatty integrations; reduce redundant replays | Demo 05 | OW-P11 Hannah Fischer |
| Peak scheduling | Move heavy jobs away from peaks where the business allows | Demo 06 rhythm | OW-P12 Daniel Okafor |
| Hosting choices | Ask providers for footprint data; record the method | Demo 10 paths | OW-P05 Priya Nair |

## 9. Measurement approach (no values stated)

| Item | Design | Value |
|---|---|---|
| Method | Use a recognised accounting method (for example the Greenhouse Gas Protocol corporate standard) and record which scopes are in or out | Method to be agreed |
| Data centre efficiency | Ask providers for facility efficiency data (ISO/IEC 30134 series is reading material; verify) | Not collected |
| Per-assistant footprint | Estimate from usage and provider data; label as estimate | Not measured |
| Reporting basis | measured, allocated or estimated, shown with each figure | Rule |

## 10. Hands-on exercise (synthetic data)

1. Pick one data product and write its contract with the basis for each figure.
2. List the footprint drivers of the Demo 03 assistant and mark which can be measured.
3. Choose two levers and name the owner and the trade-off.
4. Write the gate question for new assistants.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Unvalidated telemetry | Field data feeds a claim | Validation status shown |
| T2 Depot gap | A depot has no energy record | Gap shown; no total claimed |
| T3 AI footprint ignored | A new assistant skips footprint | Gate asks for an estimate |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Reported figures with basis and period shown | Sample | Not measured |
| Data products with one owner and quality status | Count | Not measured |
| Assistants with a footprint estimate before approval | Count | Not measured |
| Levers with a named owner | Count | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Two topics, kept apart | Shared problem statement |
| 0:20 to 1:00 | Data products and basis rule | Two contracts |
| 1:00 to 1:45 | Footprint drivers and levers | Driver list, two levers |
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

- [Greenhouse Gas Protocol](https://ghgprotocol.org/)
- [Demo 07 data foundation](07-data-foundation-data-products-sap-business-data-cloud.md)
- [Demo 11 operating model and FinOps](11-operating-model-finops-intelligent-operations-sap.md)

- [OmniWorks Industrial Systems Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/03-industrials/omniworks-industrial-systems)
- [OmniWorks Industrial Systems Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md)

