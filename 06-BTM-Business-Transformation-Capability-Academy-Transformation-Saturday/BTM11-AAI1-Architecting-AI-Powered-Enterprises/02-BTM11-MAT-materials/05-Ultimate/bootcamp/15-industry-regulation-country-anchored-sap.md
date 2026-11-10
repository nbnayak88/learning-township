# OmniForge Materials — Industry-Specific Regulation: Country-Anchored Design Questions

## Demo 15 of the BTM11 Materials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Materials (MAT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniforge-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md)

> **Evidence boundary:** OmniForge Materials is an **aspirational case study**. The case sources name headquarters countries but almost no regulations; this file points to regimes to verify and does not state legal conclusions. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `MAT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Which regulatory regimes touch the architecture, in the countries this case names, and what evidence would each need?*

**What this file shows:** the countries the case names, the regimes to verify for each, which design element each regime touches, and the evidence slot each would need.

**What it does not show:** legal advice, a compliance assessment or a claim that any regime is met. Every instrument is a pointer to verify with counsel.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 42B materials group; 46,000 employees; 31 countries |
| Business mix | Steel and alloys 30%; cement and aggregates 22%; chemicals 20%; mining and minerals 16%; advanced materials 12% |
| Burning platform | Disconnected mining, production, logistics, quality, sales and recycling; 180+ applications; weak material genealogy; manual ESG reconciliation |

**Countries named by the case:** Mumbai (India) and Rotterdam (Netherlands), per the case profile.

**Country rule for this series:** only countries named in the case are used. No other country is assumed.

**Illustrative trigger (source):** A customer queries a shipped batch's certificate after a laboratory correction, while a kiln reliability alert and uncertain recycled-feedstock records expose the same trust gap (illustrative hero trigger in the case).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, headquarters countries | **Source** |
| Regime pointers, design touchpoints, evidence slots, tests | **New design (illustrative)** |
| Legal status of any instrument | Public sources reviewed 2026-11-10 for two items only (see section 6); everything else is **verify with counsel** |

## 4. Decision under discussion

**Decision:** Which regimes does OmniForge treat as design constraints from the start, who confirms them, and where does the evidence live?

**Accountable owner (proposed):** OMF-P12 Hassan Al-Farsi and OMF-P14 Diego Alvarez, with legal counsel confirming each regime. Counsel is not a persona in the case and is shown here as an external role.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OMF-P04 | Sofia de Vries, Chief Digital and Sustainability Officer | Funds and prioritizes |
| OMF-P13 | Priya Nair, Director Enterprise Architecture | Owns standards and review |
| OMF-P12 | Hassan Al-Farsi, CISO and OT Security Lead | Security and boundary approval |
| OMF-P14 | Diego Alvarez, Head of Data Governance and AI | Data and AI governance |
| OMF-P08 | Rohan Kulkarni, Head of Quality and Laboratories | Business owner (first scope) |
| OMF-P07 | Elena Petrova, Cement Plant Director | Business owner (second scope) |
| OMF-P16 | Nikhil Sen, Shift Supervisor and Workforce Representative | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. Regimes to verify

| Area | Instrument or authority to verify | Touches this design | Evidence slot |
|---|---|---|---|
| Personal data (India) | Digital Personal Data Protection Act 2023 and Rules 2025 (phased) | Workforce and contact data | Data map, consent and notice records |
| Personal data (Netherlands, EU) | General Data Protection Regulation; Dutch data protection authority guidance | Workforce, customer contacts | Records of processing, transfer basis |
| Cybersecurity (Netherlands, EU) | NIS2 Directive and its Dutch implementation (verify status) | Enterprise security measures and incident reporting | Risk measures and incident path |
| AI (EU) | EU AI Act; see section 6 for the dates reported | Assistants in Demo 03 | Use-case class and documentation |
| Chemicals product data (EU) | REACH and CLP requirements (verify applicability by product) | Product and batch data | Substance data lineage |
| Sustainability reporting (EU) | EU corporate sustainability reporting rules (under revision; verify) | Demo 13 data products | Evidence per figure |

**India personal data law: phased commencement reported by a law-firm summary (verify).** The Digital Personal Data Protection Rules 2025 were notified in November 2025. The summary reports: institutional provisions from 13 November 2025; consent manager registration from 12 November 2026; and the remaining provisions, including notice and consent, obligations of data fiduciaries, cross-border transfer rules, breach notification, security safeguards and retention and erasure, from 12 May 2027. Source: [AZB & Partners summary](https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/).

**EU AI Act timing reported by a law-firm summary (verify the final text).** A provisional political agreement of 6 May 2026 (the 'digital omnibus') reportedly moves high-risk obligations for stand-alone systems from 2 August 2026 to 2 December 2027, and for AI in regulated products to 2 August 2028; transparency obligations otherwise stay on schedule for 2 August 2026. The summary said new dates take legal effect only on publication of the amending act, so confirm that it has been published. Source: [Gibson Dunn summary](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/).

## 7. Design questions every regime raises

| Question | Design element | Owner (proposed) |
|---|---|---|
| Where does each data set live and who may move it? | Data products and residency rules (Demo 07) | OMF-P14 Diego Alvarez |
| What must be reported, to whom, and how fast? | Incident path (Demos 06 and 12) | OMF-P12 Hassan Al-Farsi |
| Which AI uses fall under a rule? | Use-case class and change control (Demo 09) | OMF-P14 Diego Alvarez |
| Which third parties are involved? | Dependency register (Demo 12) | OMF-P13 Priya Nair |
| What evidence will an authority ask for? | Evidence slots in each demo | OMF-P16 Nikhil Sen |

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
| T1 Cross-border data flow | Batch and workforce data move between India and the Netherlands | Transfer basis and residency recorded |
| T2 AI classification | A new assistant is classified | Use-case class recorded; documentation owner named |
| T3 Reporting evidence gap | A reported figure has no lineage | Held; evidence slot empty |

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

- [OmniForge Materials case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/02-materials/omniforge-materials-ltd)
- [OmniForge Materials persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md)

