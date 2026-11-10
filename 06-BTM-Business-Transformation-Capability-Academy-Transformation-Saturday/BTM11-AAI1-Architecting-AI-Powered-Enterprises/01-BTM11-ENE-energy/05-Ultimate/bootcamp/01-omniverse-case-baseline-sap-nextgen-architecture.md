# OmniVerse Energy — Case Baseline for SAP NextGen Architecture & Intelligent Operations Demos

## Demo 01 of the BTM11 Energy Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Energy (ENE) · Ultimate (Level 5) · Bootcamp**
**Pathway context:** `PATH-BTM11-ENE-Ultimate-Bootcamp` (catalog record; see [README](README.md))
**Demo series label:** BTM11-ENE-Bootcamp-Demo-01 (planning label, not an LMS ID)
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.

> **Evidence boundary:** OmniVerse Energy Ltd. is a **fictional educational case**. Everything in this series is architecture design and teaching demonstration built on that case. No real client, tenant, employee or operational outcome is represented, and no executed test or realized benefit is asserted. Product names are learning examples, not confirmed OmniVerse implementations.

---

## 1. Why this file exists

This is the anchor for a series of short architecture demos. Each later demo reuses the same enterprise, personas and source IDs, so a reviewer can follow one story across five technical topics instead of five unrelated slide decks.

**The 20% to master:** which parts of the case are source facts, which parts are new design added for demonstration, and how every demo states its own evidence status.

## 2. The enterprise at a glance (source facts)

| Attribute | Case baseline |
|---|---|
| Enterprise | OmniVerse Energy Ltd. (alias "OmniEnergy" preserved in original research) |
| Founded / HQ | 1978 · Mumbai, India and Houston, USA |
| Scale | USD 85B revenue · 68,000 employees · 42 countries |
| Assets | 8 refineries · 25,000 km pipelines · 12,500 retail sites · 15 GW generation (5 GW renewables operating) |
| Three-year transformation budget | USD 900M (illustrative) |

**Transformation thesis (source):** from siloed energy assets to a connected, resilient, customer-centric energy enterprise.
**Burning platform (source):** disconnected operational data, reactive maintenance, inconsistent customer journeys, fragmented ESG reporting and technology silos.

All figures above are fictional scenario baselines from the source case, not validated results.

## 3. Case-to-topic map

The five technical topics below are Demos 02 to 06 of the series. The "Case anchor" column is what the source already contains. The "Added by demo" column is new design that must be labelled as such when presented.

| Demo | Technical topic | Case anchor (source) | Added by demo (new design, illustrative) | Evidence status |
|---|---|---|---|---|
| 02 | SAP enterprise architecture: process modeling, application portfolio, Clean Core | OVE-M09 capability architecture · OVE-M10 value streams and process architecture · OVE-M12 enterprise architecture and digital enablement · the resolution-category table in the enterprise source register (Configuration, Enhancement, Side-by-Side Extension on BTP, Custom Development, Process Change, Third-Party Solution, Deferred) | Process-model and application-portfolio views for two value streams; a Clean Core tiering laid over the source resolution categories | Designed, not executed |
| 03 | AI and GenAI architecture on SAP BTP: RAG, LLMs, agents | OVE-HR11 responsible AI: five personas, four source decision scenes (hallucinated policy, autonomy pressure, surveillance risk, production control), the six-test portfolio OVE-HR11-T01, and the assistive / human-approved / automated dilemma. The HR11 Origin Story lesson in this repository adds a no-AI versus answer-only versus bounded-tool-execution comparison and tabletop tests T1–T3 | Reference architecture for grounding, retrieval, evaluation and action authorization; an agent boundary design | Designed, not executed |
| 04 | Knowledge graph and context engineering | The case's own traceability chain (capability → value stream → requirement → decision → experiment → test → measure) and HR11 information objects (policy version, retrieval reference, model version, evaluation set, action authorization, incident) | A graph model of the case itself; context assembly rules and what must never enter a prompt | Designed, not executed |
| 05 | Integration and event-driven architecture, including an event mesh | OVE-HR12 integration: event object model, value stream (emit, validate, route, acknowledge, reconcile, recover), six-test portfolio including lost termination and duplicate or reordered events | Topic and event taxonomy; routing, replay and dead-letter design for the access-incident scenario | Designed, not executed |
| 06 | Basis modernization, AIOps and autonomous operations | None in the source case (no coverage of operations monitoring, HA/DR or transport automation) | A new synthetic operations scenario for an OmniVerse landscape; anomaly triage, runbook automation boundaries and human approval gates | New design layered on the case; to be flagged clearly in the demo |

**Coverage check against the case source (searched 2026-11-10):** the source mentions SAP Signavio once (a Process Navigator reference link), and contains no mention of LeanIX, an event mesh, knowledge graphs, AIOps or Basis. Demos 04 and 06 therefore rest mainly on new design, with only the case's data objects, personas and traceability reused. Demo 05 reuses the case's integration flows but adds an event-mesh design the case does not contain. Presenters should say this plainly rather than imply the case already contained these architectures.

## 4. Personas reused across demos

Names, roles and IDs are retained from the source. Decision rights are **proposed** and require discovery validation; a persona title is not proof of final authority.

| Source ID | Persona | Role in the demo series |
|---|---|---|
| OVE-P05 | Rajiv Kapoor, Chief Digital and Information Officer | Digital architecture and platforms; challenges disconnected pilots and brittle interfaces (Demo 02, 05) |
| OVE-P13 | Omar Haddad | Security and assurance voice across all demos |
| OVE-HR11-P01 | Dr. Tara Menon, Responsible Workforce AI Director | Owns AI policy, assurance and incidents (Demo 03, 04) |
| OVE-HR11-P04 | Dr. Felix Bauer, AI Security and Model Risk Lead | Testing, logging, release and rollback (Demo 03, 06) |
| OVE-HR12-P01 | Sameer Kulkarni, Enterprise HR Integration Architect | Canonical integration design owner (Demo 05) |
| OVE-HR12-P05 | Eric Thompson, Integration Operations Manager | Monitoring, retry, recovery and service levels (Demo 05, 06) |

Shared first names across streams do not establish shared identity; the source namespaces each persona.

## 5. Standard demo structure

Every demo in the series follows the same shape, adapted from the Build Card used in the HR11 Origin Story sprint, so participants learn one method and apply it five times.

| Section | Required content |
|---|---|
| Decision | The architecture decision under discussion and who is accountable for it |
| Source versus new design | What comes from the case, what this demo adds |
| Architecture view | One diagram or table showing responsibilities, boundaries and information objects |
| Hands-on exercise | A synthetic-data exercise a participant can complete in the session |
| Three tabletop tests | Input, expected result, actual paper result, correction, pass or revise |
| Acceptance | What must hold for the design to be accepted; which controls remain untested |
| Evidence status | Designed, executed on a sandbox, or not demonstrated; never implied |
| Resources | Official documentation with a review date; verify product version and licensing before use |

**Rule carried from the case:** a prototype proves only the behaviour actually exercised. Do not fabricate a baseline, achieved benefit or target.

## 6. How a demo fits a 2–3 hour session

This is a proposed teaching pattern, not a committed schedule.

| Minutes | Activity | Output |
|---|---|---|
| 0–20 | Case briefing and decision framing with the relevant personas | Decision statement and accountable owner |
| 20–60 | Architecture walkthrough using the demo's view | Responsibility and boundary map |
| 60–110 | Guided exercise on synthetic data in a provided sandbox or a paper model | Completed exercise artefact |
| 110–150 | Run three tabletop tests; revise the design | Pass or revise decision with evidence notes |
| 150–180 | Recall check, short assessment and next-step question | Assessment record and attendance capture |

Recording, assessment and attendance tracking can be layered onto this pattern without changing the content.

## 7. What a reviewer should take from this

1. The case supplies a coherent enterprise, personas, source IDs and honest evidence rules.
2. Demos 02, 03 and the integration flows in Demo 05 have strong source anchors in the case.
3. Demos 04 and 06, and the event-mesh design in Demo 05, are new design on top of the case, and each demo says so in its first section.
4. No demo claims executed tenant work or realized outcomes. Where a sandbox is used, the demo records exactly what was run.

## 8. Planned demo series

| Demo | Topic | Status |
|---|---|---|
| 01 | Case baseline (this file) | Written |
| 02 | Enterprise architecture, process modeling, application portfolio and Clean Core | Written (`02-enterprise-architecture-signavio-leanix-clean-core.md`) |
| 03 | AI and GenAI architecture on SAP BTP: grounding, RAG, agents | Written for all 11 sectors (`03-ai-genai-rag-agents-sap-btp.md` in each sector's bootcamp folder) |
| 04 | Knowledge graph and context engineering | Written (`04-knowledge-graph-context-engineering-sap.md`) |
| 05 | Integration and event-driven architecture with an event mesh | Written (`05-integration-event-driven-advanced-event-mesh-sap.md`) |
| 06 | Basis modernization, AIOps and autonomous operations | Written (`06-basis-modernization-aiops-autonomous-operations-sap.md`) |
| 07 | Data foundation for AI: data products, ownership, quality | Written (`07-data-foundation-data-products-sap-business-data-cloud.md`) |
| 08 | Security and zero trust for AI assistants and agents | Written (`08-security-zero-trust-ai-agents-sap-btp.md`) |
| 11 | Operating model and FinOps for intelligent operations | Written (`11-operating-model-finops-intelligent-operations-sap.md`) |

## 9. Sources and traceability

- **Canonical enterprise:** [OmniVerse case](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd)
- **Executive summary:** [executive one-pager](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md)
- **Architecture theme (OVE-M09 to M12):** [Theme C](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/master/theme-c-architecture.md)
- **Responsible AI domain (OVE-HR11):** [hr11-responsible-ai](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/hr/hr11-responsible-ai.md)
- **HR integration domain (OVE-HR12):** [hr12-hr-integration](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/hr/hr12-hr-integration.md)
- **Source interpretation and assumptions:** [source-and-assumptions](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/references/source-and-assumptions.md)
- **Related lesson in this repository:** HR11 Energy Origin Story sprint, `01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR11-AAI1-Architecting-AI-Powered-HR-Enterprises/01-HR11-ENE-energy/0-The-Origin-Story/sprint/energy-hr11-origin-evolution-sprint.md`

**Educational alignment:** TOGAF for architecture views and decisions; BIZBOK for capability and value-stream distinctions; BABOK for needs and acceptance; DAMA for data ownership and quality; COBIT for accountable control. These mappings are educational and are not compliance certification or reproduction of proprietary standards.

**Publication note:** this is a demonstration file in the bootcamp folder. It is not proof that a course is live, purchasable or delivered.
