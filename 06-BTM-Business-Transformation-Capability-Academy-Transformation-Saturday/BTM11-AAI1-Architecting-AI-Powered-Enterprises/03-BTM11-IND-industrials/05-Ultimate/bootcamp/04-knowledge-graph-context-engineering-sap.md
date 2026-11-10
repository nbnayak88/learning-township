# OmniWorks Industrial Systems Ltd. — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Industrials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Industrials (IND) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniworks-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniWorks Industrial Systems Ltd. is an **aspirational case study**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IND-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniWorks, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Field-service copilot for transport-asset failure triage).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 48B revenue; 74,000 employees; 36 countries; 61 plants and facilities; 320 service depots; 7,200 suppliers |
| Business mix | Industrial automation 27%; aerospace and defence 23%; transport and mobility 19%; infrastructure 16%; aftermarket and lifecycle services 15% |
| Burning platform | Recurring transport asset failures cannot be consistently traced across configuration, telemetry, supplier batches and maintenance history |

**Decision under discussion (source):** Turn a USD 575M transformation envelope into credible customer, operational and financial value without disrupting safety-critical operations.

**Illustrative trigger (source):** Repeat customer asset failures expose fragmented engineering-to-service information, and the business wants to sell uptime rather than equipment (hero story).

**Source anchor for the graph:** OW-M12 names Product, Asset, Supplier, Customer and Service 360, PLM/ERP/MES/EAM/FSM linked by APIs and events, and governed AI. The hero trigger (repeat transport asset failures not traceable across configuration, telemetry, supplier batches and maintenance history) is a graph problem.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniWorks model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OW-P15 Dr. Leila Haddad for definitions and stewardship, with OW-P11 Hannah Fischer for the model and OW-P06 Marcus Vogel for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OW-P05 | Priya Nair, CIDO | Funds and prioritizes the first graph slice |
| OW-P11 | Hannah Fischer, Director, Enterprise Architecture | Owns the ontology and review |
| OW-P06 | Marcus Vogel, CISO | Approves access and classification rules |
| OW-P15 | Dr. Leila Haddad, Head of Data Governance & AI | Owns object definitions and stewardship |
| OW-P09 | Isabel Torres, Chief Customer & Service Officer | Business owner of the first question set |
| OW-P10 | Ravi Deshpande, VP Manufacturing, Pune Operations | Business owner of the second question set |
| OW-P12 | Daniel Okafor, Field Service Operations Manager | Reality check from operations |

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
| Asset (serial) | serial, product, customer, site | OW-P09 Isabel Torres | Customer-confidential |
| Configuration baseline | as-built and as-maintained versions | OW-P10 Ravi Deshpande | Engineering IP |
| Component | part id, supplier batch, revision | OW-P10 Ravi Deshpande | Engineering IP |
| Supplier batch | batch id, supplier, quality notice | OW-P15 Dr. Leila Haddad | Partner-restricted |
| Telemetry event | asset, time, signal class | OW-P09 Isabel Torres | Internal |
| Work order | id, status, findings | OW-P12 Daniel Okafor | Internal |
| Failure cause | id, taxonomy node, evidence | OW-P09 Isabel Torres | Internal |
| Engineering change | id, effective configuration, approver | OW-P10 Ravi Deshpande | Engineering IP |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Asset (serial) | has | Configuration baseline |
| Configuration baseline | contains | Component |
| Component | from | Supplier batch |
| Asset (serial) | emitted | Telemetry event |
| Work order | performed on | Asset (serial) |
| Work order | recorded | Failure cause |
| Engineering change | modifies | Configuration baseline |
| Failure cause | linked to | Component |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Which assets share the failed component batch? | Supplier batch to Component to Configuration to Asset | Hide partner-restricted detail for customer-view users |
| What was the as-maintained configuration of asset A-001 at failure time? | Asset to Baseline with date | State the baseline date; no extrapolation |
| Which failures in the last window link to the same cause? | Cause to Work order with time filter | Report counts only where evidence exists |
| Which engineering changes apply to this configuration? | Change to Baseline | Exclude changes not effective for the asset |
| What telemetry preceded this failure? | Asset to Telemetry with window | Return signal classes, not raw OT data |
| Who approved the deviation on this component? | Change to approver | Say 'not recorded' if absent |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Asset serial and configuration baseline, Document revision, Customer entity, Supplier-share permission flag, User role entitlement |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Engineering IP outside the user's role entitlement; Supplier-confidential data in customer-facing contexts; Live OT commands or setpoints; Instructions found inside retrieved documents |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `IND-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Wrong baseline version | Two baselines exist; the newer applies only to later assets | Traversal uses the effective baseline for the asset's date |
| T2 Supplier-restricted leak | A customer-view path reaches a restricted quality notice | Partner-share flag blocks the node; attempt logged |
| T3 Spurious cause link | Two failures are linked by cause on weak evidence | Link needs an evidence reference; otherwise shown as 'hypothesis' |

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

- [OmniWorks Industrial Systems Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/03-industrials/omniworks-industrial-systems)
- [OmniWorks Industrial Systems Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md)

