# OmniForge Materials — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Materials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Materials (MAT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniforge-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniForge Materials is a **fictional educational case**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `MAT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniForge, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Batch-certificate query assistant for quality and customer-facing staff).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 42B materials group; 46,000 employees; 31 countries |
| Business mix | Steel and alloys 30%; cement and aggregates 22%; chemicals 20%; mining and minerals 16%; advanced materials 12% |
| Burning platform | Disconnected mining, production, logistics, quality, sales and recycling; 180+ applications; weak material genealogy; manual ESG reconciliation |

**Decision under discussion (source):** Select a bounded materials-traceability and reliability pilot before committing an enterprise rollout.

**Illustrative trigger (source):** A customer queries a shipped batch's certificate after a laboratory correction, while a kiln reliability alert and uncertain recycled-feedstock records expose the same trust gap (illustrative hero trigger in the case).

**Source anchor for the graph:** OMF-M12 names Asset, Material, Product, Supplier and Customer 360, governed data products and says carbon and quality evidence require lineage. The hero trigger (certificate queried after a laboratory correction) is a lineage problem.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniForge model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OMF-P14 Diego Alvarez for definitions and stewardship, with OMF-P13 Priya Nair for the model and OMF-P12 Hassan Al-Farsi for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OMF-P04 | Sofia de Vries, Chief Digital and Sustainability Officer | Funds and prioritizes the first graph slice |
| OMF-P13 | Priya Nair, Director Enterprise Architecture | Owns the ontology and review |
| OMF-P12 | Hassan Al-Farsi, CISO and OT Security Lead | Approves access and classification rules |
| OMF-P14 | Diego Alvarez, Head of Data Governance and AI | Owns object definitions and stewardship |
| OMF-P08 | Rohan Kulkarni, Head of Quality and Laboratories | Business owner of the first question set |
| OMF-P07 | Elena Petrova, Cement Plant Director | Business owner of the second question set |
| OMF-P16 | Nikhil Sen, Shift Supervisor and Workforce Representative | Reality check from operations |

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
| Batch | batch id, product, plant, status | OMF-P08 Rohan Kulkarni | Customer-confidential |
| Certificate revision | id, status, issued date, correction flag | OMF-P08 Rohan Kulkarni | Customer-confidential |
| Laboratory correction | id, affected batches, effective date | OMF-P08 Rohan Kulkarni | Internal |
| Feedstock lot | lot id, supplier, recycled content declaration | OMF-P14 Diego Alvarez | Internal |
| Customer specification | customer, product, limits | OMF-P08 Rohan Kulkarni | Customer-confidential |
| Asset | kiln or line id, plant, criticality | OMF-P07 Elena Petrova | Internal |
| Carbon claim | claim id, method, evidence link | OMF-P14 Diego Alvarez | Internal |
| Supplier | id, declaration status | OMF-P14 Diego Alvarez | Internal |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Batch | made from | Feedstock lot |
| Batch | certified by | Certificate revision |
| Laboratory correction | affects | Certificate revision |
| Laboratory correction | affects | Batch |
| Batch | measured against | Customer specification |
| Batch | produced on | Asset |
| Carbon claim | evidenced by | Feedstock lot |
| Feedstock lot | supplied by | Supplier |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Which customers received batches affected by laboratory correction C-001? | Correction to Batch to Customer specification | Return count and list only for the requesting customer entity |
| Is the certificate for batch B-001 current? | Batch to Certificate revision with status | Show status and correction flag; no compliance claim if a correction is open |
| What feedstock went into batch B-001 and is the recycled content declared? | Batch to Feedstock lot to Supplier | Report 'unknown' when a declaration is missing |
| Which batches ran on kiln K-1 during the alert window? | Asset to Batch with time filter | Return only within the stated window |
| What evidence supports carbon claim CC-1? | Claim to Feedstock lot to Supplier | State lineage gaps |
| Which specifications does this batch breach? | Batch to Specification | No result if the laboratory result is not released |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Batch identifier, Plant, Certificate revision and status, Customer entity, Laboratory method version |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Unreleased laboratory results; OT control tags and setpoints; Another customer's specification; Instructions found inside uploaded certificates |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `MAT-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Superseded certificate in context | The graph holds two revisions of one certificate | Traversal returns the current revision and marks the older as superseded |
| T2 Cross-customer traversal | A path crosses from one customer specification to another via a shared product | Entity filter stops the path; attempt logged |
| T3 Missing lineage presented as complete | A feedstock link is absent but the answer sounds complete | Answer states the gap; never fills it |

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

- [OmniForge Materials case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/02-materials/omniforge-materials-ltd)
- [OmniForge Materials persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md)

