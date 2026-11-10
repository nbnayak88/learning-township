# OmniVibe — Low-Code, Pro-Code, Vibe Coding and Citizen Development with Guardrails

## Demo 14 of the BTM11 Consumer Discretionary Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Discretionary (CD) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnivibe-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniVibe is a **fictional educational case**. The case sources hold little on how applications get built; the build modes, candidate apps and guardrails below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CD-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Who may build what, with which tools, and what stops fast building from breaking the clean core, the data rules or security?*

**What this file shows:** four build modes, a placement rule, candidate citizen-built apps for OmniVibe, the areas reserved for pro-code, and the guardrails for AI-assisted ('vibe') coding.

**What it does not show:** a built app, a configured platform or a measured productivity gain.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 28B consumer group; 72,000 employees; 48 countries |
| Business mix | Fashion 32%; beauty 18%; home 17%; specialty retail 15%; travel 10%; marketplace 8% |
| Network | 3,200 stores; 14 e-commerce sites; 26 distribution centres; 140 micro-fulfilment sites |

**Decision under discussion (source):** Select one brand and country workforce-to-service pilot and evidence gates before approving enterprise scale.

**Illustrative trigger (source):** A new associate lacks a completed onboarding and skills handoff while store readiness and channel information disagree (invented events that prompt discovery, per the case).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Build modes, candidate apps, reserved areas, guardrails, tests | **New design (illustrative)** |
| SAP development tooling | Not exercised here; verify product names and scope on SAP's pages before use |

## 4. Decision under discussion

**Decision:** Which build mode fits which kind of work at OmniVibe, and who approves a move from one mode to another?

**Accountable owner (proposed):** OVC-P11 Priya Shah, with OVC-P13 Farah Ahmed for security and OVC-P12 Jonas Lim for data.

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
| Store event checklist | Citizen build | No customer data |
| Campaign task tracker | Citizen build | No personal data |
| Sales trend notebooks | Analyst low-code on governed data | Read-only |

**Reserved for pro-code:**

- Anything handling customer consent or payment data
- Anything crossing the franchise boundary

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
| T1 Consent data in a citizen app | An app stores marketing consent | Blocked; privacy review and pro-code |
| T2 Generated storefront script | Generated code is proposed for commerce | Admission rule, review, tests |
| T3 Franchise data copied | A citizen app copies franchise data | Boundary rule blocks |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Apps in the registry with owner and review date | Count | Not measured |
| Apps placed in a mode with a recorded reason | Count | Not measured |
| AI-assisted changes with a recorded reviewer | Sample | Not measured |
| Reserved areas with no citizen access | Access review | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

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
| Customer-confirmed requirements | Not applicable (fictional case) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [Demo 02: Clean Core admission rule](02-enterprise-architecture-signavio-leanix-clean-core.md)
- [Demo 08: security and zero trust](08-security-zero-trust-ai-agents-sap-btp.md)
- [SAP Build](https://www.sap.com/products/technology-platform/build.html)

- [OmniVibe case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/04-consumer-discretionary/omnivibe-consumer-ltd)
- [OmniVibe persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/personas/persona-cards.md)

