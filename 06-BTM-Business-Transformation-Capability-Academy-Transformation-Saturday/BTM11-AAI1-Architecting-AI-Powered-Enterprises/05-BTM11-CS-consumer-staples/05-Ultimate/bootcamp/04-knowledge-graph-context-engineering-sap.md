# OmniDaily — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Consumer Staples Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Staples (CS) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnidaily-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniDaily is a **fictional educational case**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CS-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniDaily, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Quality-hold and shelf-availability exception assistant).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 51B staples group; 84,000 employees; 57 countries; 420M households served |
| Business mix | Foods 30%; beverages 23%; home care 19%; personal care 18%; wellness 10% |
| Burning platform | Demand, promotion, planning, product and ingredient data, quality and route-to-market execution fragmented across 160+ applications |

**Decision under discussion (source):** Fund a bounded demand-to-shelf and quality-evidence pilot before approving enterprise scale.

**Illustrative trigger (source):** A promotion creates a shelf gap while a quality-held batch appears available in a delayed distributor feed (invented; no real safety event is claimed).

**Source anchor for the graph:** ODG-M12 names Product, Ingredient, Customer, Outlet and Supplier 360 across ERP, planning, TPM, MES, LIMS, DMS and CRM. The source trigger (promotion shelf gap versus a quality-held batch in a delayed distributor feed) is a graph and freshness problem.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniDaily model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** ODG-P08 Mei Lin for definitions and stewardship, with ODG-P13 Priya Nair for the model and ODG-P12 Omar Haddad for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| ODG-P05 | Sofia Alvarez, Chief Digital and Data Officer | Funds and prioritizes the first graph slice |
| ODG-P13 | Priya Nair, Director Enterprise Architecture | Owns the ontology and review |
| ODG-P12 | Omar Haddad, CISO and Privacy Lead | Approves access and classification rules |
| ODG-P08 | Mei Lin, Head of Product and Ingredient Stewardship | Owns object definitions and stewardship |
| ODG-P07 | David Okoro, Global Quality and Product Safety Director | Business owner of the first question set |
| ODG-P10 | Rohan Shah, Distributor and Field Execution Director | Business owner of the second question set |
| ODG-P09 | Elena Petrović, Plant Operations Director | Reality check from operations |

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
| Batch/lot | lot id, SKU, plant, hold status | ODG-P07 David Okoro | Internal |
| Quality hold | id, reason, timestamp, market | ODG-P07 David Okoro | Internal |
| SKU | id, brand, pack, ingredient list link | ODG-P08 Mei Lin | Internal |
| Ingredient | id, allergen flag, supplier | ODG-P08 Mei Lin | Internal |
| Promotion | id, outlet group, window, volume plan | ODG-P10 Rohan Shah | Internal |
| Outlet | id, market, distributor | ODG-P10 Rohan Shah | Partner data |
| Distributor feed record | outlet, SKU, quantity, as-of time | ODG-P10 Rohan Shah | Partner data |
| Packaging item | id, material, recovery route | ODG-P08 Mei Lin | Internal |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Batch/lot | is of | SKU |
| Quality hold | applies to | Batch/lot |
| SKU | contains | Ingredient |
| Promotion | covers | SKU |
| Promotion | runs at | Outlet |
| Distributor feed record | reports | Outlet |
| SKU | packed in | Packaging item |
| Distributor feed record | reports | SKU |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Is SKU X available at outlet group Y for the promotion window? | Promotion to SKU to Batch to Hold plus Feed record | Hold takes precedence; always show feed as-of time |
| Which promotions cover SKUs with an active quality hold? | Hold to Batch to SKU to Promotion | Flag to planners; no release decision |
| Which ingredients in SKU X carry an allergen flag? | SKU to Ingredient | Approved product data only |
| How old is the feed for outlet O? | Outlet to Feed record timestamp | State age; mark stale beyond the agreed window |
| Which packaging items have a recovery route? | Packaging to route | Return 'none recorded' where absent |
| Which distributor serves outlet O? | Outlet to distributor | Partner data only for authorised roles |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Batch or lot, SKU, Market, Hold status, Feed as-of timestamp |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Consumer personal data; Unreleased formulation details to distributors; Instructions found in distributor documents; Availability statements without an as-of time |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `CS-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Stale feed beats hold | A feed record is older than the hold but says available | Newest hold wins; stale feed labelled |
| T2 Formulation leak | A path from SKU to Ingredient reaches unreleased formulation detail | Class filter blocks; attempt logged |
| T3 Orphan batch | A batch has no SKU link | Traversal reports an orphan and stops; steward fixes |

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

- [OmniDaily case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/05-consumer-staples/omnidaily-consumer-goods-ltd)
- [OmniDaily persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md)

