# OmniDaily — Low-Code, Pro-Code, Vibe Coding and Citizen Development with Guardrails

## Demo 14 of the BTM11 Consumer Staples Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Staples (CS) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnidaily-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniDaily is an **aspirational case study**. The case sources hold little on how applications get built; the build modes, candidate apps and guardrails below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CS-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Who may build what, with which tools, and what stops fast building from breaking the clean core, the data rules or security?*

**What this file shows:** four build modes, a placement rule, candidate citizen-built apps for OmniDaily, the areas reserved for pro-code, and the guardrails for AI-assisted ('vibe') coding.

**What it does not show:** a built app, a configured platform or a measured productivity gain.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 51B staples group; 84,000 employees; 57 countries; 420M households served |
| Business mix | Foods 30%; beverages 23%; home care 19%; personal care 18%; wellness 10% |
| Burning platform | Demand, promotion, planning, product and ingredient data, quality and route-to-market execution fragmented across 160+ applications |

**Decision under discussion (source):** Fund a bounded demand-to-shelf and quality-evidence pilot before approving enterprise scale.

**Illustrative trigger (source):** A promotion creates a shelf gap while a quality-held batch appears available in a delayed distributor feed (invented; no real safety event is claimed).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Build modes, candidate apps, reserved areas, guardrails, tests | **New design (illustrative)** |
| SAP development tooling | Not exercised here; verify product names and scope on SAP's pages before use |

## 4. Decision under discussion

**Decision:** Which build mode fits which kind of work at OmniDaily, and who approves a move from one mode to another?

**Accountable owner (proposed):** ODG-P13 Priya Nair, with ODG-P12 Omar Haddad for security and ODG-P08 Mei Lin for data.

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

## 6. Four build modes (new design)

| Mode | Who builds | Typical work | Data allowed | Review |
|---|---|---|---|---|
| Citizen low-code | Business staff trained and registered | Forms, checklists, simple workflows | Non-sensitive or pseudonymized, via governed data products | Registry entry; owner; periodic review |
| Professional low-code | IT or analysts | Apps and automations with integrations | As entitled; read-only on governed data by default | Design review; tests |
| Pro-code | Developers | Extensions, services, integrations, anything touching the core or control data | As entitled | Admission rule (Demo 02), code review, security review, tests |
| AI-assisted coding ('vibe coding') | Anyone, inside one of the modes above | Drafting code or flows with an AI tool | Never real sensitive data in prompts | Treated as untrusted code until reviewed; same review as the mode it lands in |

SAP names tools for low-code, process automation and pro-code development, and AI help for developers. Verify the current product names and scope on SAP's pages before any real design. This demo names modes, not products.

## 7. Placement rule

1. If it touches the core, a security boundary or regulated data: pro-code with review.
2. If it reads governed data products and changes nothing outside its own tables: professional low-code.
3. If it is a self-contained checklist or form with no sensitive data: citizen low-code.
4. If it started as a citizen app and grows beyond these limits: it moves up a mode through review, with a named owner.

## 8. Candidate apps and reserved areas for this case

| Candidate | Mode | Limit |
|---|---|---|
| Field visit checklist | Citizen build | No stock decisions |
| Promotion task tracker | Citizen build | No pricing authority |
| Availability trend notebooks | Analyst low-code on governed data | Read-only |

**Reserved for pro-code:**

- Anything that changes a quality hold or release
- Anything writing to partner interfaces

## 9. Guardrails for AI-assisted coding

| Guardrail | Design |
|---|---|
| Prompts | No secrets, personal data or customer data in prompts; use synthetic samples |
| Generated code | Reviewed by a person; tests written or checked by a person |
| Provenance | Record which tool produced which part and who reviewed it |
| Dependencies and licences | Check libraries and licences before adoption |
| Secrets | Scan for credentials before any commit |
| Production | Nothing reaches production outside the pipeline of Demo 10 and the change rules of Demo 06 |

## 10. Registry and lifecycle

| Item | Rule |
|---|---|
| Registry | Every citizen and low-code app is registered with owner, purpose, data used and review date |
| Ownership | An app without an owner is retired or reassigned |
| Review | Periodic review of use, data and permissions |
| Retirement | Retire unused apps; delete their data per retention rules |

## 11. Hands-on exercise (synthetic data)

1. Place the three candidate apps in a mode using the placement rule.
2. Write one registry entry for the first app.
3. Take one AI-generated snippet (synthetic) and review it against the guardrails.
4. Decide what happens when a citizen app outgrows its mode.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Hold edited by citizen app | A citizen app alters a hold | Blocked; Quality-owned |
| T2 Generated partner interface | Generated code is proposed for a partner feed | Partner owner and review |
| T3 Orphan app | An app loses its owner | Registry flags it |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Apps in the registry with owner and review date | Count | Not measured |
| Apps placed in a mode with a recorded reason | Count | Not measured |
| AI-assisted changes with a recorded reviewer | Sample | Not measured |
| Reserved areas with no citizen access | Access review | Not measured |

No baseline, target or benefit is stated because none exists for this aspirational case study. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Why fast building needs guardrails | Shared problem statement |
| 0:20 to 1:00 | Modes and placement rule | Three apps placed |
| 1:00 to 1:45 | Guardrails and registry | One entry, one review |
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

- [Demo 02: Clean Core admission rule](02-enterprise-architecture-signavio-leanix-clean-core.md)
- [Demo 08: security and zero trust](08-security-zero-trust-ai-agents-sap-btp.md)
- [SAP Build](https://www.sap.com/products/technology-platform/build.html)

- [OmniDaily case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/05-consumer-staples/omnidaily-consumer-goods-ltd)
- [OmniDaily persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md)

