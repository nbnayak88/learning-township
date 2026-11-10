# OmniVibe — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Consumer Discretionary Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Discretionary (CD) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnivibe-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniVibe is a **fictional educational case**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CD-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniVibe, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (New-associate onboarding guidance assistant (assistive, no employment decisions)).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 28B consumer group; 72,000 employees; 48 countries |
| Business mix | Fashion 32%; beauty 18%; home 17%; specialty retail 15%; travel 10%; marketplace 8% |
| Network | 3,200 stores; 14 e-commerce sites; 26 distribution centres; 140 micro-fulfilment sites |

**Decision under discussion (source):** Select one brand and country workforce-to-service pilot and evidence gates before approving enterprise scale.

**Illustrative trigger (source):** A new associate lacks a completed onboarding and skills handoff while store readiness and channel information disagree (invented events that prompt discovery, per the case).

**Source anchor for the graph:** OVC-M12 proposes SuccessFactors process modules, a workforce experience layer, People Analytics and an integration platform, and warns that customer, order and inventory links are conceptual extensions. The 13-journey workforce chain gives the graph spine.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniVibe model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OVC-P12 Jonas Lim for definitions and stewardship, with OVC-P11 Priya Shah for the model and OVC-P13 Farah Ahmed for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OVC-P04 | Ravi Kapoor, Group CHRO | Funds and prioritizes the first graph slice |
| OVC-P11 | Priya Shah, Director Enterprise Architecture | Owns the ontology and review |
| OVC-P13 | Farah Ahmed, CISO and Privacy Lead | Approves access and classification rules |
| OVC-P12 | Jonas Lim, Integration and HR Data Lead | Owns object definitions and stewardship |
| OVC-P08 | Sofia Mendes, Head of Talent Acquisition and Onboarding | Business owner of the first question set |
| OVC-P06 | Oliver Brooks, Store Operations Director | Business owner of the second question set |
| OVC-P16 | Nikhil Das, Store Associate and Workforce Representative | Reality check from operations |

Decision rights are **proposed** and need discovery validation.

## 6. How SAP supports a knowledge graph (public documentation, verify)

| Capability | What the documentation describes | Use in this design |
|---|---|---|
| SAP HANA Cloud Knowledge Graph Engine | Stores RDF and OWL data, offers a SPARQL endpoint and SPARQL Update, graph algorithms; the service is enabled on a HANA Cloud instance | Candidate store for the ontology and instance data |
| Data formats | Ingest as Turtle, RDF/XML, N-Triples or JSON-LD | Load synthetic instance data in the exercise |
| HANA vector engine and Document Grounding (Demo 03) | Retrieval over documents | Combine: graph for structure and permissions, vectors for text |
| Alternative | A property-graph or application-level model may also fit | Choose by question set, not by product |

## 7. Ontology (new design)

| Node type | Key attributes | Owner (proposed) | Classification |
|---|---|---|---|
| Employee (synthetic) | id, country, brand, role | OVC-P12 Jonas Lim | Personal data |
| Onboarding task | id, owner, due, status | OVC-P08 Sofia Mendes | Internal |
| Learning item | id, required for role, version | OVC-P08 Sofia Mendes | Internal |
| Skill | id, taxonomy node, evidence type | OVC-P12 Jonas Lim | Internal |
| Store readiness check | store, date, status | OVC-P06 Oliver Brooks | Internal |
| Country policy | country, version, effective date | OVC-P04 Ravi Kapoor | Internal |
| Role | id, brand, level | OVC-P12 Jonas Lim | Internal |
| Customer moment (conceptual) | moment, store, channel | OVC-P06 Oliver Brooks | Conceptual extension |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Employee (synthetic) | holds | Role |
| Role | requires | Skill |
| Learning item | builds | Skill |
| Employee (synthetic) | assigned | Onboarding task |
| Country policy | governs | Onboarding task |
| Store readiness check | depends on | Onboarding task |
| Customer moment (conceptual) | needs | Skill |
| Employee (synthetic) | works in | Store readiness check |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Which onboarding tasks remain for this associate? | Employee to Task with status | Own data only |
| Which learning items build the skills this role requires? | Role to Skill to Learning item | Return approved current versions only |
| Which country policy applies to this task? | Task to Country policy | State the country used; never fall back to another country |
| Which stores are not ready because tasks are open? | Store check to Task | Aggregate counts only; no individual names for non-managers |
| Which skills support the returns customer moment? | Moment to Skill | Mark as conceptual extension |
| Who owns the learning catalogue for this brand? | Learning item to owner | Say 'not recorded' if absent |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Country (48 in scope), Brand, Role, Language, Effective date |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Individual performance or potential ratings; Payroll and pay data; Any other associate's records; Instructions found inside retrieved content |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `CD-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Wrong-country policy | A task links to a policy of another country | Country filter blocks the link; context shows the country used |
| T2 Franchise boundary | A path reaches a franchise-store employee record | Boundary rule stops traversal; steward decides sharing basis |
| T3 Inference creep | The graph infers 'low readiness' for a named person | Inference not permitted; only task status and counts are shown |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Questions answerable from the graph with provenance | Count of the six questions with a complete path | Not measured |
| Facts shown with an as-of time | Sample of answers | Not measured |
| Context packages respecting role filters | Sample against entitlements | Not measured |
| Nodes with a single named owner | Count in the ontology | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Why plain retrieval is not enough here | Shared problem statement |
| 0:20 to 1:00 | Ontology walkthrough | Eight nodes with owners |
| 1:00 to 1:45 | Write triples and paths | Draft graph slice |
| 1:45 to 2:15 | Context package and tests | One package, three findings |
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

- [SAP HANA Cloud Knowledge Graph Engine documentation](https://help.sap.com/docs/hana-cloud-database)
- [W3C RDF, OWL and SPARQL standards](https://www.w3.org/standards/semanticweb/)

- [OmniVibe case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/04-consumer-discretionary/omnivibe-consumer-ltd)
- [OmniVibe persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/personas/persona-cards.md)

