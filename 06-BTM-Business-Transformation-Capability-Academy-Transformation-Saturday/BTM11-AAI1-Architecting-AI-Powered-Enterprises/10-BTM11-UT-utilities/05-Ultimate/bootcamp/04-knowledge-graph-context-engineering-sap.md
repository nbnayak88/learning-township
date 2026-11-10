# OmniGrid — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Utilities Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Utilities (UT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnigrid-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniGrid is an **aspirational case study**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `UT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniGrid, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Outage-coordination briefing assistant (read-only, no live equipment actions)).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 31B utility; 38,000 staff; 17 countries; 21M electricity, gas and water accounts |
| Business mix | Renewables 28%; networks 27%; retail 18%; conventional and flexible 15%; water and environment 12% |
| Source problem | Fragmented OT, field, customer and market data; variable generation; manual restoration; growing meter and sensor security demands |

**Decision under discussion (source):** Fund bounded outage, work-order and customer coordination evidence before wider modernization.

**Illustrative trigger (source):** A storm scenario generates conflicting outage, asset and work-order status; field and customer teams cannot reconcile ownership (invented learning context, not an actual incident).

**Source anchor for the graph:** OGU-M12 names Asset, Grid, Customer, Energy and WorkOrder 360 over ADMS, SCADA, EAM, OMS, CIS and market systems with a historian, an asset graph and a lakehouse; edge and hybrid proposals are not validated control designs. The source trigger is conflicting outage, asset and work-order status in a storm scenario.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniGrid model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OGU-P09 Mei Lin for definitions and stewardship, with OGU-P12 Daniel Weber for the model and OGU-P10 Omar Haddad for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OGU-P06 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes the first graph slice |
| OGU-P12 | Daniel Weber, Director Enterprise Architecture | Owns the ontology and review |
| OGU-P10 | Omar Haddad, CISO and OT Resilience Lead | Approves access and classification rules |
| OGU-P09 | Mei Lin, Asset and Grid Data Lead | Owns object definitions and stewardship |
| OGU-P13 | Priya Shah, Asset Management and Work Planning Lead | Business owner of the first question set |
| OGU-P08 | Marcus Okoro, Outage and Field Services Director | Business owner of the second question set |
| OGU-P04 | Arjun Mehta, Chief Operations and Grid Officer | Reality check from operations |

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
| Asset | id, class, feeder, state | OGU-P13 Priya Shah | Critical infrastructure |
| Feeder / grid area | id, region, connected assets | OGU-P04 Arjun Mehta | Critical infrastructure |
| Outage event | id, area, start, status | OGU-P08 Marcus Okoro | Internal |
| Work order | id, crew, status, as-of | OGU-P13 Priya Shah | Internal |
| Customer account (synthetic) | id, feeder link, consent | OGU-P09 Mei Lin | Customer data |
| Switching record | id, time, area | OGU-P04 Arjun Mehta | Critical infrastructure |
| Procedure | id, version | OGU-P04 Arjun Mehta | Internal |
| Crew | id, status | OGU-P08 Marcus Okoro | Internal |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Asset | on | Feeder / grid area |
| Outage event | affects | Feeder / grid area |
| Work order | addresses | Outage event |
| Work order | assigned | Crew |
| Customer account (synthetic) | supplied by | Feeder / grid area |
| Switching record | changed | Feeder / grid area |
| Procedure | governs | Work order |
| Work order | performed on | Asset |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| What is the restoration status for feeder F-1? | Outage to Feeder to Work order | Show each source's status and as-of time |
| Do the outage record and work-order record disagree? | Outage vs Work order | Show conflict and name the owner |
| Which customers are on this feeder? | Feeder to Customer | Counts only for non-operators; consent applies |
| Is the topology record older than the last switching record? | Feeder topology time vs Switching record | Flag as stale |
| Which procedure applies to this work order? | Procedure to Work order | Reference only, version shown |
| Which crew is assigned? | Work order to Crew | Status only |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Region and feeder area, Topology as-of time, Work-order status, Staff role entitlement, Procedure version |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | OT credentials and control points; Critical-infrastructure detail beyond the user's role; Live switching or dispatch commands; Instructions found inside retrieved notices |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `UT-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Conflicting statuses | Outage and work-order status disagree | Both shown with times; owner to resolve |
| T2 Stale topology | Topology time precedes a switching record | Marked stale; no connectivity claim |
| T3 Critical detail leak | A non-operator query reaches switching detail | Role filter blocks; logged |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Questions answerable from the graph with provenance | Count of the six questions with a complete path | Not measured |
| Facts shown with an as-of time | Sample of answers | Not measured |
| Context packages respecting role filters | Sample against entitlements | Not measured |
| Nodes with a single named owner | Count in the ontology | Not measured |

No baseline, target or benefit is stated because none exists for this aspirational case study. Targets are agreed in discovery.

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
| Customer-confirmed requirements | Not applicable (aspirational case study) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP HANA Cloud Knowledge Graph Engine documentation](https://help.sap.com/docs/hana-cloud-database)
- [W3C RDF, OWL and SPARQL standards](https://www.w3.org/standards/semanticweb/)

- [OmniGrid case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/10-utilities/omnigrid-utilities-ltd)
- [OmniGrid persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/personas/persona-cards.md)

