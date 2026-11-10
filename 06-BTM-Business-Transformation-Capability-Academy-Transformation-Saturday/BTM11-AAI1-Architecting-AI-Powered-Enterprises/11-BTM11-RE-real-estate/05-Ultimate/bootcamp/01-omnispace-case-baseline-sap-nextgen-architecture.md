# OmniSpace — Case Baseline for SAP NextGen Architecture & Intelligent Operations Demos

## Demo 01 of the BTM11 Real Estate Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Real Estate (RE) · Ultimate (Level 5) · Bootcamp**
**Demo series label:** BTM11-RE-Bootcamp-Demo-01 (planning label, not an LMS ID)
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.

> **Evidence boundary:** OmniSpace is a **fictional educational case**. Everything in this series is architecture design and teaching demonstration built on that case. No real client, tenant, employee or operational outcome is represented, and no executed test or realized benefit is asserted. Product names are learning examples, not confirmed OmniSpace implementations.

---

## 1. Why this file exists

This is the anchor for a series of short architecture demos for this sector. Each later demo reuses the same enterprise, personas and source IDs, so a reviewer can follow one story across five technical topics instead of five unrelated slide decks.

**The 20% to master:** which parts of the case are source facts, which parts are new design added for demonstration, and how every demo states its own evidence status.

## 2. The enterprise at a glance (source facts)

| Attribute | Case baseline |
|---|---|
| Enterprise | OmniSpace (fictional) |
| Scale | Not supplied in the case; no enterprise numerical profile, budget or quantified benefits |
| Scope | Fictional global real-estate enterprise; property, tenant, ESG, recruiting, finance and procurement workstreams |
| Source problem | Fragmented architecture, processes, delivery evidence and adoption |

**Decision under discussion (source):** Select one capability or process pilot and prove its strategy-to-value traceability before scaling tools.

**Illustrative trigger (source):** A property-service workflow is declared live, but property teams still use spreadsheets, tenant requests remain unresolved, and test and adoption records cannot explain the claimed benefit (invented learning scenario).

**Strategic options (source):** Independent tool/workstream pilots; central suite first; capability-led pilots joined by the source digital thread. Third option provisional.

All figures are fictional scenario baselines from the source case, not validated results.

## 3. Case-to-topic map

The five technical topics are Demos 02 to 06. The "Case anchor" column is what the source contains. The "Added by demo" column is new design that must be labelled as such when presented.

| Demo | Technical topic | Case anchor (source) | Added by demo (new design, illustrative) | Evidence status |
|---|---|---|---|---|
| 02 | SAP enterprise architecture: process modeling, application portfolio, Clean Core | OSP-M09 capability architecture; OSP-M10 value streams and process architecture; OSP-M11 operating model; OSP-M12 enterprise architecture. The source proposes tool roles (LeanIX architecture, Signavio processes, Cloud ALM delivery) without verifying configured integration or product capability. No source content on Clean Core. | Capability and owner register, process taxonomy for two value streams, synthetic application portfolio, Clean Core admission rule | Designed, not executed |
| 03 | AI and GenAI architecture on SAP BTP: RAG, LLMs, agents | OSP-M13 AI initiative candidates and the source responsible-AI rule. See [Demo 03 for this sector](03-ai-genai-rag-agents-sap-btp.md). | Reference architecture for grounding, retrieval, evaluation and action authorization; agent tool boundary | Written; designed, not executed |
| 04 | Knowledge graph and context engineering | The OSP-M12 information map (see Section 5). No source graph model. | A graph model of the case itself; context assembly rules; what must never enter a prompt | New design layered on the case |
| 05 | Integration and event-driven architecture, including an event mesh | OSP-M12 states APIs and events as integration patterns (see Section 5). No source mention of an event mesh. | Topic and event taxonomy; routing, replay and dead-letter design for the sector trigger scenario | New design layered on the case |
| 06 | Basis modernization, AIOps and autonomous operations | None in the source (no coverage of operations monitoring, HA/DR or transport automation).  | A new synthetic operations scenario; anomaly triage, runbook automation boundaries and human approval gates | New design layered on the case |

**Coverage check against the case source (searched 2026-11-10, case markdown files excluding the sync state folder):**

| Term | Mentions | Where |
|---|---|---|
| SAP Signavio | 4 | `executive-one-pager.md`, `delivery-report-2026-10-19.md`, `master/theme-c-architecture.md`, `personas/persona-cards.md` |
| SAP LeanIX | 5 | `executive-one-pager.md`, `delivery-report-2026-10-19.md`, `master/theme-c-architecture.md`, `simulations/scenario-scripts.md` |
| Clean Core | 0 | none |
| Event mesh | 0 | none |
| Knowledge graph | 0 | none |
| AIOps | 0 | none |
| SAP Basis | 0 | none |

Presenters should say plainly which topics rest mainly on new design rather than imply the case already contained these architectures.

## 4. What the source says on architecture (Theme C)

**OSP-M09 Business capability architecture.** Source capability mapping covers real estate, HR, finance, procurement, operations, ESG and technology. Use named owners and scope before tool inventories. Maturity model L1fragmented→L5adaptive is conceptual; no assessed capability scores.

**OSP-M10 Value streams and process architecture.** Source process discovery/redesign/governance and workstreams span recruiting, property work orders, source-to-pay, record-to-report and ESG. Illustrative streams:Request-to-Resolved-Property-Service, Requisition-to-Ready-Hire and Strategy-to-Verified-Value. Detailed lease/tenant lifecycle requires discovery.

**OSP-M11 Target operating model.** Source integrated model joins architecture, process, delivery, quality, adoption, change and analytics. Forums include steering, architecture board, process council, delivery tower, adoption/change council and value office. Define decision rights and exception routes.

**OSP-M12 Enterprise architecture and digital enablement.** Source tool-role proposals:LeanIX architecture, Signavio processes, Cloud ALM delivery, Tricentis quality, WalkMe adoption, Reftrack/Revtrack change; Integration Suite/APIs/events, analytics, governance and identity. No configured integration or current product capability verified.

Source: [Theme C architecture](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/master/theme-c-architecture.md)

## 5. Personas reused across demos

Names, roles and IDs are retained from the source persona cards. Decision rights in later demos are **proposed** and require discovery validation; a persona title is not proof of final authority.

| Source ID | Persona | Source role and decision authority |
|---|---|---|
| OSP-P03 | Maya Patel, Property Operations Director | See persona card |
| OSP-P04 | Elena Brooks, Tenant and Resident Experience Lead | See persona card |
| OSP-P05 | Sofia Tan, Chief Digital and Information Officer | See persona card |
| OSP-P08 | Mei Lin, Enterprise Data and ESG Lead | See persona card |
| OSP-P09 | Omar Haddad, CISO and Resilience Lead | See persona card |
| OSP-P10 | Daniel Weber, Enterprise Architecture Director | See persona card |
| OSP-P13 | Grace Costa, Quality Engineering Lead | See persona card |
| OSP-P14 | Ingrid Sørensen, Adoption and Change Lead | See persona card |

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
2. Demos 02 and 03 have the strongest source anchors (OSP-M09 to M12 and OSP-M13).
3. Demos 04, 05 and 06 are mainly new design on top of the case, and each demo says so in its first section.
4. No demo claims executed tenant work or realized outcomes. Where a sandbox is used, the demo records exactly what was run.

## 9. Planned demo series

| Demo | Topic | Status |
|---|---|---|
| 01 | Case baseline (this file) | Written |
| 02 | Enterprise architecture, process modeling, application portfolio and Clean Core | Written ([this sector](02-enterprise-architecture-signavio-leanix-clean-core.md)) |
| 03 | AI and GenAI architecture on SAP BTP: grounding, RAG, agents | Written ([this sector](03-ai-genai-rag-agents-sap-btp.md)) |
| 04 | Knowledge graph and context engineering | Planned |
| 05 | Integration and event-driven architecture with an event mesh | Planned |
| 06 | Basis modernization, AIOps and autonomous operations | Planned |

## 10. Sources and traceability

- **Canonical enterprise:** [OmniSpace case](https://github.com/nbnayak88/successlabs-case-studies/tree/main/11-real-estate/omnispace-real-estate-ltd)
- **Executive summary:** [executive one-pager](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/executive-one-pager.md)
- **Architecture theme (OSP-M09 to M12):** [Theme C](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/master/theme-c-architecture.md)
- **Persona cards:** [persona-cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/personas/persona-cards.md)
- **Source interpretation and assumptions:** [source-and-assumptions](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/references/source-and-assumptions.md)
- **Series reference baseline (Energy):** [OmniVerse Demo 01](../../../01-BTM11-ENE-energy/05-Ultimate/bootcamp/01-omniverse-case-baseline-sap-nextgen-architecture.md)

**Educational alignment:** TOGAF for architecture views and decisions; BIZBOK for capability and value-stream distinctions; BABOK for needs and acceptance; DAMA for data ownership and quality; COBIT for accountable control. These mappings are educational and are not compliance certification or reproduction of proprietary standards.

**Publication note:** this is a demonstration file in the bootcamp folder. It is not proof that a course is live, purchasable or delivered.
