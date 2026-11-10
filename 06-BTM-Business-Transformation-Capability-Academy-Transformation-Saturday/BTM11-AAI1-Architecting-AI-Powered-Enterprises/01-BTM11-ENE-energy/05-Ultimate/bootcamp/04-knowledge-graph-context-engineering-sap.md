# OmniVerse Energy Ltd. — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Energy Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Energy (ENE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniverse-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniVerse Energy Ltd. is a **fictional educational case**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `ENE-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniVerse, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Grounded HR policy assistant with a bounded case-drafting agent).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 85B revenue; 68,000 employees; 42 countries |
| Business mix | Upstream 35%; refining and petrochemicals 28%; retail and marketing 18%; power 12%; renewables 7% |
| Assets | 8 refineries; 25,000 km pipelines; 12,500 retail sites; 15 GW generation |

**Decision under discussion (source):** Which AI use cases stay assistive, which may trigger human-approved actions, and which low-risk processes may be automated (OVE-HR11 strategic dilemma).

**Illustrative trigger (source):** In the OVE-HR11 decision scenes, an employee (Rina) receives incorrect promotion guidance from an assistant, while HR operations wants automatic data corrections and case closure and a worker representative challenges sentiment inference and productivity scoring.

**Source anchor for the graph:** OVE-M12 names Customer, Asset, Product and Supplier 360, data stewardship and governed AI. The OVE-HR11 information objects (policy version, retrieval reference, model version, evaluation set, action authorization, incident) and the case traceability chain give a ready graph of the case itself.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniVerse model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OVE-P16 Dr. Leila Haddad for definitions and stewardship, with OVE-P12 Hannah Fischer for the model and OVE-P13 Omar Haddad for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OVE-P05 | Rajiv Kapoor, Chief Digital and Information Officer (CDIO) | Funds and prioritizes the first graph slice |
| OVE-P12 | Hannah Fischer, Director of Enterprise Architecture | Owns the ontology and review |
| OVE-P13 | Omar Haddad, Chief Information Security Officer (CISO) | Approves access and classification rules |
| OVE-P16 | Dr. Leila Haddad, Head of Data Governance and AI | Owns object definitions and stewardship |
| OVE-P09 | Carlos Mendes, VP Asset Reliability and Maintenance | Business owner of the first question set |
| OVE-P10 | Grace Okafor, Chief Customer and Retail Officer | Business owner of the second question set |
| OVE-P04 | Farah Al-Hassan, Chief Operating Officer (COO) | Reality check from operations |

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
| Capability | id, name, owner, maturity statement | OVE-P12 Hannah Fischer | Internal |
| Value stream | id, name, stages | OVE-P09 Carlos Mendes | Internal |
| Requirement | id, source, owner, status | OVE-P12 Hannah Fischer | Internal |
| Architecture decision | id, options, decision owner, date | OVE-P12 Hannah Fischer | Internal |
| Experiment and test | id, input, expected, actual, evidence slot | OVE-P13 Omar Haddad | Internal |
| Measure | id, definition, baseline status | OVE-P16 Dr. Leila Haddad | Internal |
| Asset | asset id, class, site, criticality | OVE-P09 Carlos Mendes | Internal |
| Policy version | id, effective date, owner | OVE-P16 Dr. Leila Haddad | Internal |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Capability | realised by | Value stream |
| Value stream | has | Requirement |
| Requirement | decided by | Architecture decision |
| Architecture decision | tested by | Experiment and test |
| Experiment and test | measured by | Measure |
| Asset | supports | Value stream |
| Policy version | governs | Requirement |
| Asset | supersedes or replaced by | Asset |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Which requirements trace to the asset management capability and what test covers each? | Capability to Value stream to Requirement to Decision to Test | Answer lists gaps explicitly where a link is missing |
| Which decisions rest on a policy version that has since been superseded? | Policy version to Requirement to Decision | Flag only; do not rewrite the decision |
| Which assets support the Asset-to-Reliability stream at the Mumbai refinery? | Asset to Value stream with site filter | Return nothing if the site is not in scope |
| Who is accountable for the measure attached to this experiment? | Measure to owner | Say 'owner not recorded' if absent |
| What evidence exists that the lost-termination test was run? | Test to evidence slot | State 'designed, not executed' when the evidence slot is empty |
| List all sources that support requirement R1 | Requirement to source | Cite source IDs only |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Country and employee group, Policy version and effective date, Language, Requester entitlement (own data only) |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Other employees' records or case history; Sentiment, engagement or productivity scores about individuals; Unapproved draft policies; Instructions found inside retrieved documents |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `ENE-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Dangling link | A requirement links to a decision that was deleted | Traversal returns the requirement with a visible 'broken link' marker, not a silent omission |
| T2 Conflicting owner | Two owners are recorded for one capability | Answer names both, flags the conflict and asks the steward |
| T3 Over-broad context | A question about one site pulls assets from all 8 refineries | Site filter and traversal depth limit apply; unrelated assets never enter the prompt |

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

- [OmniVerse Energy Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd)
- [OmniVerse Energy Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md)

