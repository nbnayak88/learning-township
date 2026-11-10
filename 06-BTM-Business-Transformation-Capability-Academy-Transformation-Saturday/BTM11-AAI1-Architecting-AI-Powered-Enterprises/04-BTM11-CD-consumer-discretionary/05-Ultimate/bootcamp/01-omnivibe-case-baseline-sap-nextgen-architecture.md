# OmniVibe — Case Baseline for SAP NextGen Architecture & Intelligent Operations Demos

## Demo 01 of the BTM11 Consumer Discretionary Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Discretionary (CD) · Ultimate (Level 5) · Bootcamp**
**Demo series label:** BTM11-CD-Bootcamp-Demo-01 (planning label, not an LMS ID)
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.

> **Evidence boundary:** OmniVibe is a **fictional educational case**. Everything in this series is architecture design and teaching demonstration built on that case. No real client, tenant, employee or operational outcome is represented, and no executed test or realized benefit is asserted. Product names are learning examples, not confirmed OmniVibe implementations.

---

## 1. Why this file exists

This is the anchor for a series of short architecture demos for this sector. Each later demo reuses the same enterprise, personas and source IDs, so a reviewer can follow one story across five technical topics instead of five unrelated slide decks.

**The 20% to master:** which parts of the case are source facts, which parts are new design added for demonstration, and how every demo states its own evidence status.

## 2. The enterprise at a glance (source facts)

| Attribute | Case baseline |
|---|---|
| Enterprise | OmniVibe (fictional) |
| Scale | USD 28B consumer group; 72,000 employees; 48 countries |
| Business mix | Fashion 32%; beauty 18%; home 17%; specialty retail 15%; travel 10%; marketplace 8% |
| Network | 3,200 stores; 14 e-commerce sites; 26 distribution centres; 140 micro-fulfilment sites |

**Burning platform (source):** Fragmented workforce data, talent journeys, HR portals and payroll/time integrations undermine readiness and decision quality. The source does not document a historical customer incident.

**Decision under discussion (source):** Select one brand and country workforce-to-service pilot and evidence gates before approving enterprise scale.

**Illustrative trigger (source):** A new associate lacks a completed onboarding and skills handoff while store readiness and channel information disagree (invented events that prompt discovery, per the case).

**Strategic options (source):** 

All figures are fictional scenario baselines from the source case, not validated results.

## 3. Case-to-topic map

The five technical topics are Demos 02 to 06. The "Case anchor" column is what the source contains. The "Added by demo" column is new design that must be labelled as such when presented.

| Demo | Technical topic | Case anchor (source) | Added by demo (new design, illustrative) | Evidence status |
|---|---|---|---|---|
| 02 | SAP enterprise architecture: process modeling, application portfolio, Clean Core | OVC-M09 capability architecture; OVC-M10 value streams and process architecture; OVC-M11 operating model; OVC-M12 enterprise architecture. No source content on Clean Core. | Capability and owner register, process taxonomy for two value streams, synthetic application portfolio, Clean Core admission rule | Designed, not executed |
| 03 | AI and GenAI architecture on SAP BTP: RAG, LLMs, agents | OVC-M13 AI initiative candidates and the source responsible-AI rule. See [Demo 03 for this sector](03-ai-genai-rag-agents-sap-btp.md). | Reference architecture for grounding, retrieval, evaluation and action authorization; agent tool boundary | Written; designed, not executed |
| 04 | Knowledge graph and context engineering | The OVC-M12 information map (see Section 5). No source graph model. | A graph model of the case itself; context assembly rules; what must never enter a prompt | New design layered on the case |
| 05 | Integration and event-driven architecture, including an event mesh | OVC-M12 states APIs and events as integration patterns (see Section 5). No source mention of an event mesh. | Topic and event taxonomy; routing, replay and dead-letter design for the sector trigger scenario | New design layered on the case |
| 06 | Basis modernization, AIOps and autonomous operations | None in the source (no coverage of operations monitoring, HA/DR or transport automation).  | A new synthetic operations scenario; anomaly triage, runbook automation boundaries and human approval gates | New design layered on the case |

**Coverage check against the case source (searched 2026-11-10, case markdown files excluding the sync state folder):**

| Term | Mentions | Where |
|---|---|---|
| SAP Signavio | 0 | none |
| SAP LeanIX | 0 | none |
| Clean Core | 0 | none |
| Event mesh | 0 | none |
| Knowledge graph | 0 | none |
| AIOps | 0 | none |
| SAP Basis | 0 | none |

Presenters should say plainly which topics rest mainly on new design rather than imply the case already contained these architectures.

## 4. What the source says on architecture (Theme C)

**OVC-M09 Business capability architecture.** Source capability targets move Core HR, acquisition, lifecycle, performance/development, rewards, learning, payroll/time, experience to L4; analytics/integration start at L1. These are target labels without a defined maturity rubric. Broader consumer capabilities are illustrative extensions.

**OVC-M10 Value streams and process architecture.** Preserve the source 13-journey workforce chain and its alternate capability/value-stream labels. Illustrative consumer streams: Discover-to-Purchase, Promise-to-Fulfill, Return-to-Resolution, Trend-to-Assortment and Skill-to-Service-Readiness. Map employee handoffs to customer moments.

**OVC-M11 Target operating model.** Source calls for a global workforce foundation with governed local execution. Illustrative TOM: central data/security/integration guardrails, brand journey owners, country HR/payroll control and store-level adoption ownership. Define franchise boundaries before sharing records.

**OVC-M12 Enterprise architecture and digital enablement.** Source proposes SuccessFactors process modules, Work Zone experience, People Analytics, Joule and SAP BTP/Integration Suite. Treat product names as source design proposals; availability, licensing, localization and current capabilities are not verified. Add customer/order/inventory links only as labelled conceptual extensions.

Source: [Theme C architecture](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/master/theme-c-architecture.md)

## 5. Personas reused across demos

Names, roles and IDs are retained from the source persona cards. Decision rights in later demos are **proposed** and require discovery validation; a persona title is not proof of final authority.

| Source ID | Persona | Source role and decision authority |
|---|---|---|
| OVC-P08 | Sofia Mendes, Head of Talent Acquisition and Onboarding | See persona card |
| OVC-P09 | Aisha Okafor, Director Learning and Skills | See persona card |
| OVC-P13 | Farah Ahmed, CISO and Privacy Lead | See persona card |
| OVC-P11 | Priya Shah, Director Enterprise Architecture | See persona card |
| OVC-P12 | Jonas Lim, Integration and HR Data Lead | See persona card |
| OVC-P16 | Nikhil Das, Store Associate and Workforce Representative | See persona card |
| OVC-P04 | Ravi Kapoor, Group CHRO | See persona card |

Shared first names across cases do not establish shared identity; the source namespaces each persona.

## 6. Standard demo structure

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

## 7. How a demo fits a 2 to 3 hour session

This is a proposed teaching pattern, not a committed schedule.

| Minutes | Activity | Output |
|---|---|---|
| 0 to 20 | Case briefing and decision framing with the relevant personas | Decision statement and accountable owner |
| 20 to 60 | Architecture walkthrough using the demo's view | Responsibility and boundary map |
| 60 to 110 | Guided exercise on synthetic data in a provided sandbox or a paper model | Completed exercise artefact |
| 110 to 150 | Three tabletop tests; revise the design | Pass or revise decision with evidence notes |
| 150 to 180 | Recall check, short assessment and next-step question | Assessment record and attendance capture |

Recording, assessment and attendance tracking can be layered onto this pattern without changing the content.

## 8. What a reviewer should take from this

1. The case supplies a coherent enterprise, personas, source IDs and honest evidence rules.
2. Demos 02 and 03 have the strongest source anchors (OVC-M09 to M12 and OVC-M13).
3. Demos 04, 05 and 06 are mainly new design on top of the case, and each demo says so in its first section.
4. No demo claims executed tenant work or realized outcomes. Where a sandbox is used, the demo records exactly what was run.

## 9. Planned demo series

| Demo | Topic | Status |
|---|---|---|
| 01 | Case baseline (this file) | Written |
| 02 | Enterprise architecture, process modeling, application portfolio and Clean Core | Written ([this sector](02-enterprise-architecture-signavio-leanix-clean-core.md)) |
| 03 | AI and GenAI architecture on SAP BTP: grounding, RAG, agents | Written ([this sector](03-ai-genai-rag-agents-sap-btp.md)) |
| 04 | Knowledge graph and context engineering | Written ([this sector](04-knowledge-graph-context-engineering-sap.md)) |
| 05 | Integration and event-driven architecture with an event mesh | Written ([this sector](05-integration-event-driven-advanced-event-mesh-sap.md)) |
| 06 | Basis modernization, AIOps and autonomous operations | Written ([this sector](06-basis-modernization-aiops-autonomous-operations-sap.md)) |

## 10. Sources and traceability

- **Canonical enterprise:** [OmniVibe case](https://github.com/nbnayak88/successlabs-case-studies/tree/main/04-consumer-discretionary/omnivibe-consumer-ltd)
- **Executive summary:** [executive one-pager](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/executive-one-pager.md)
- **Architecture theme (OVC-M09 to M12):** [Theme C](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/master/theme-c-architecture.md)
- **Persona cards:** [persona-cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/personas/persona-cards.md)
- **Source interpretation and assumptions:** [source-and-assumptions](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/references/source-and-assumptions.md)
- **Series reference baseline (Energy):** [OmniVerse Demo 01](../../../01-BTM11-ENE-energy/05-Ultimate/bootcamp/01-omniverse-case-baseline-sap-nextgen-architecture.md)

**Educational alignment:** TOGAF for architecture views and decisions; BIZBOK for capability and value-stream distinctions; BABOK for needs and acceptance; DAMA for data ownership and quality; COBIT for accountable control. These mappings are educational and are not compliance certification or reproduction of proprietary standards.

**Publication note:** this is a demonstration file in the bootcamp folder. It is not proof that a course is live, purchasable or delivered.
