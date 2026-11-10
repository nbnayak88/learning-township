# OmniTech — Industry-Specific Regulation: Country-Anchored Design Questions

## Demo 15 of the BTM11 Information Technology Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Information Technology (IT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnitech-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md)

> **Evidence boundary:** OmniTech is an **aspirational case study**. The case sources name headquarters countries but almost no regulations; this file points to regimes to verify and does not state legal conclusions. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Which regulatory regimes touch the architecture, in the countries this case names, and what evidence would each need?*

**What this file shows:** the countries the case names, the regimes to verify for each, which design element each regime touches, and the evidence slot each would need.

**What it does not show:** legal advice, a compliance assessment or a claim that any regime is met. Every instrument is a pointer to verify with counsel.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 39B technology provider; 98,000 employees; 41 countries; 11,500 clients |
| Business mix | Cloud and platform 31%; software 25%; cyber 18%; AI and data 16%; managed services 10% |
| Source problem | Fragmented lifecycle tooling, bespoke integrations, poor data and AI reuse, late security and observability |

**Countries named by the case:** Bengaluru (India) and San Francisco (United States), per the case profile.

**Country rule for this series:** only countries named in the case are used. No other country is assumed.

**Illustrative trigger (source):** A client disputes an on-time delivery milestone; teams cannot reconcile release, incident and customer-success records (invented discovery context).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, headquarters countries | **Source** |
| Regime pointers, design touchpoints, evidence slots, tests | **New design (illustrative)** |
| Legal status of any instrument | Public sources reviewed 2026-11-10 for two items only (see section 6); everything else is **verify with counsel** |

## 4. Decision under discussion

**Decision:** Which regimes does OmniTech treat as design constraints from the start, who confirms them, and where does the evidence live?

**Accountable owner (proposed):** OTS-P10 Omar Haddad and OTS-P09 Mei Lin, with legal counsel confirming each regime. Counsel is not a persona in the case and is shown here as an external role.

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

## 6. Regimes to verify

| Area | Instrument or authority to verify | Touches this design | Evidence slot |
|---|---|---|---|
| Personal data (India) | Digital Personal Data Protection Act 2023 and Rules 2025 (phased) | Workforce and client contact data | Data map, consent and notice records |
| Incident reporting (India) | CERT-In cyber incident directions (verify timelines) | Incident flow in Demo 06 | Incident log and contact path |
| Personal data (United States, California) | California Consumer Privacy Act as amended (verify applicability) | Client and workforce data | Data map and rights process |
| Assurance reports | Industry attestation frameworks such as SOC 2 and ISO 27001 are customer expectations, not laws (verify) | Controls in Demos 06 and 08 | Control evidence |
| AI | No binding federal AI law is assumed; check state rules and client contracts | Assistants in Demo 03 | Use-case class and governance record |

**India personal data law: phased commencement reported by a law-firm summary (verify).** The Digital Personal Data Protection Rules 2025 were notified in November 2025. The summary reports: institutional provisions from 13 November 2025; consent manager registration from 12 November 2026; and the remaining provisions, including notice and consent, obligations of data fiduciaries, cross-border transfer rules, breach notification, security safeguards and retention and erasure, from 12 May 2027. Source: [AZB & Partners summary](https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/).

## 7. Design questions every regime raises

| Question | Design element | Owner (proposed) |
|---|---|---|
| Where does each data set live and who may move it? | Data products and residency rules (Demo 07) | OTS-P09 Mei Lin |
| What must be reported, to whom, and how fast? | Incident path (Demos 06 and 12) | OTS-P10 Omar Haddad |
| Which AI uses fall under a rule? | Use-case class and change control (Demo 09) | OTS-P09 Mei Lin |
| Which third parties are involved? | Dependency register (Demo 12) | OTS-P12 Daniel Weber |
| What evidence will an authority ask for? | Evidence slots in each demo | OTS-P13 Priya Shah |

**Cross-border flows:** the case names more than one country, so every flow between them needs a recorded basis and an owner. Do not assume one country's rule covers another.

## 8. Hands-on exercise (synthetic data)

1. List the data flows between the named countries (synthetic) and mark the owner of each.
2. For two regimes, write the evidence slot and who supplies it.
3. Walk the first tabletop test and mark who is told and in what order.
4. Mark every statement in the file that still needs counsel to confirm.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Two-country incident | An incident touches Indian and US operations | Both paths and one owner |
| T2 Client audit request | A client asks for control evidence | Evidence packs exist or the gap is stated |
| T3 Tenant data location | A tenant requires a data location | Residency rule and owner |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Regimes with an owner and an evidence slot | Count | Not measured |
| Cross-border flows with a recorded basis | Count | Not measured |
| Statements confirmed by counsel | Count of confirmed items | Not measured |
| Incident paths per named country | Count | Not measured |

No baseline, target or benefit is stated because none exists for this aspirational case study. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Why regulation shapes architecture | Shared problem statement |
| 0:20 to 1:00 | Countries and regime pointers | Verified list with gaps marked |
| 1:00 to 1:45 | Cross-border flows and evidence | Flow table and slots |
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

- [Demo 07 data foundation](07-data-foundation-data-products-sap-business-data-cloud.md)
- [Demo 09 AI governance](09-ai-governance-evaluation-llmops-sap.md)
- [Demo 12 resilience](12-resilience-failure-drills-sap.md)

- [OmniTech case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/08-information-technology/omnitech-solutions-ltd)
- [OmniTech persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/08-information-technology/omnitech-solutions-ltd/personas/persona-cards.md)

