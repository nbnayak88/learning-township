# OmniHealth — Industry-Specific Regulation: Country-Anchored Design Questions

## Demo 15 of the BTM11 Health Care Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Health Care (HC) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnihealth-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 08](08-security-zero-trust-ai-agents-sap-btp.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md)

> **Evidence boundary:** OmniHealth is a **fictional educational case**. The case sources name headquarters countries but almost no regulations; this file points to regimes to verify and does not state legal conclusions. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `HC-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Which regulatory regimes touch the architecture, in the countries this case names, and what evidence would each need?*

**What this file shows:** the countries the case names, the regimes to verify for each, which design element each regime touches, and the evidence slot each would need.

**What it does not show:** legal advice, a compliance assessment or a claim that any regime is met. Every instrument is a pointer to verify with counsel.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 34B healthcare group; 126,000 staff; 19 countries |
| Network | 86 hospitals; 440 clinics; 670 diagnostic centres |
| Business mix | Acute 38%; primary 22%; diagnostics 18%; digital and pharmacy 12%; research and value-based 10% |

**Countries named by the case:** Singapore and Boston (United States), per the case profile.

**Country rule for this series:** only countries named in the case are used. No other country is assumed.

**Illustrative trigger (source):** A referral crosses facilities without clear ownership; the patient repeats information and a dashboard cannot reconcile episode status (invented; no actual patient incident is asserted).

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, headquarters countries | **Source** |
| Regime pointers, design touchpoints, evidence slots, tests | **New design (illustrative)** |
| Legal status of any instrument | Public sources reviewed 2026-11-10 for two items only (see section 6); everything else is **verify with counsel** |

## 4. Decision under discussion

**Decision:** Which regimes does OmniHealth treat as design constraints from the start, who confirms them, and where does the evidence live?

**Accountable owner (proposed):** OHS-P10 Omar Haddad and OHS-P09 Priya Nair, with legal counsel confirming each regime. Counsel is not a persona in the case and is shown here as an external role.

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

## 6. Regimes to verify

| Area | Instrument or authority to verify | Touches this design | Evidence slot |
|---|---|---|---|
| Personal data (Singapore) | Personal Data Protection Act (verify) | Administrative patient and workforce data | Data map, notice and consent records |
| Healthcare services (Singapore) | Healthcare Services Act and Ministry of Health requirements (verify) | Administrative flows | Requirement trace |
| Health information privacy (United States) | HIPAA Privacy and Security Rules (verify applicability to each flow) | Any protected health information in scope | Access, audit and breach records |
| Breach notification | Per-country rules (verify) | Referral and identity systems | Incident path per country |
| AI | Check health-sector AI guidance in each country; none assumed here | Assistants in Demo 03 | Use-case class and governance record |

## 7. Design questions every regime raises

| Question | Design element | Owner (proposed) |
|---|---|---|
| Where does each data set live and who may move it? | Data products and residency rules (Demo 07) | OHS-P09 Priya Nair |
| What must be reported, to whom, and how fast? | Incident path (Demos 06 and 12) | OHS-P10 Omar Haddad |
| Which AI uses fall under a rule? | Use-case class and change control (Demo 09) | OHS-P09 Priya Nair |
| Which third parties are involved? | Dependency register (Demo 12) | OHS-P13 Daniel Weber |
| What evidence will an authority ask for? | Evidence slots in each demo | OHS-P03 Dr. Leila Morgan |

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
| T1 Two-country breach | An incident touches both countries | Both paths and one owner named |
| T2 PHI in a log | A log contains identifiable data | Scrubbing rule; incident |
| T3 Clinical request | An assistant is asked a clinical question | Refused |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Regimes with an owner and an evidence slot | Count | Not measured |
| Cross-border flows with a recorded basis | Count | Not measured |
| Statements confirmed by counsel | Count of confirmed items | Not measured |
| Incident paths per named country | Count | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

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
| Customer-confirmed requirements | Not applicable (fictional case) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [Demo 07 data foundation](07-data-foundation-data-products-sap-business-data-cloud.md)
- [Demo 09 AI governance](09-ai-governance-evaluation-llmops-sap.md)
- [Demo 12 resilience](12-resilience-failure-drills-sap.md)

- [OmniHealth case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/06-health-care/omnihealth-systems-ltd)
- [OmniHealth persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/personas/persona-cards.md)

