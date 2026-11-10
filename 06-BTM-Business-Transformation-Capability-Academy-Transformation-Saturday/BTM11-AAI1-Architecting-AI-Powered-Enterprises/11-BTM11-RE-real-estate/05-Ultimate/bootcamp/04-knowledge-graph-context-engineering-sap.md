# OmniSpace — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Real Estate Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Real Estate (RE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnispace-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniSpace is an **aspirational case study**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `RE-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniSpace, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Tenant service-request triage assistant (tests whether AI earns a place)).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | Not supplied in the case; no enterprise numerical profile, budget or quantified benefits |
| Scope | Aspirational global real-estate enterprise; property, tenant, ESG, recruiting, finance and procurement workstreams |
| Source problem | Fragmented architecture, processes, delivery evidence and adoption |

**Decision under discussion (source):** Select one capability or process pilot and prove its strategy-to-value traceability before scaling tools.

**Illustrative trigger (source):** A property-service workflow is declared live, but property teams still use spreadsheets, tenant requests remain unresolved, and test and adoption records cannot explain the claimed benefit (invented learning scenario).

**Source anchor for the graph:** OSP-M12 proposes tool roles (an architecture inventory, process modelling and delivery management) without verifying configured integration; OSP-M10 says detailed lease and tenant lifecycle needs discovery. The source trigger (a workflow declared live while spreadsheets persist and benefit cannot be explained) is a traceability problem.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniSpace model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OSP-P08 Mei Lin for definitions and stewardship, with OSP-P10 Daniel Weber for the model and OSP-P09 Omar Haddad for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OSP-P05 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes the first graph slice |
| OSP-P10 | Daniel Weber, Enterprise Architecture Director | Owns the ontology and review |
| OSP-P09 | Omar Haddad, CISO and Resilience Lead | Approves access and classification rules |
| OSP-P08 | Mei Lin, Enterprise Data and ESG Lead | Owns object definitions and stewardship |
| OSP-P03 | Maya Patel, Property Operations Director | Business owner of the first question set |
| OSP-P16 | Thomas van Dijk, Value Realization Office Lead | Business owner of the second question set |
| OSP-P14 | Ingrid Sørensen, Adoption and Change Lead | Reality check from operations |

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
| Property / building | id, region, owner | OSP-P03 Maya Patel | Internal |
| Tenant (synthetic) | id, entities, building | OSP-P03 Maya Patel | Tenant data |
| Lease clause summary | lease, clause, amendment date | OSP-P03 Maya Patel | Tenant-confidential |
| Service request | id, category, status, as-of | OSP-P03 Maya Patel | Tenant data |
| Work order | id, request link, status | OSP-P03 Maya Patel | Internal |
| Requirement and test | id, process, test result | OSP-P16 Thomas van Dijk | Internal |
| Adoption evidence | usage record, date | OSP-P14 Ingrid Sørensen | Internal |
| Value claim | id, claim, evidence links | OSP-P16 Thomas van Dijk | Internal |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Tenant (synthetic) | occupies | Property / building |
| Lease clause summary | binds | Tenant (synthetic) |
| Service request | raised by | Tenant (synthetic) |
| Work order | resolves | Service request |
| Requirement and test | covers | Service request |
| Adoption evidence | supports | Value claim |
| Requirement and test | supports | Value claim |
| Work order | at | Property / building |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Who is responsible for this repair under the current lease? | Request to Tenant to Lease clause (current amendment) | Cite clause and amendment date |
| What is the status of this tenant's request? | Request to Work order | Own tenant only |
| Which evidence supports value claim VC-1? | Claim to Test and Adoption evidence | State missing links; no claim without both |
| Which requests lack a test? | Request without Requirement and test edge | Counts and ids |
| Which clauses were superseded by amendments? | Clause with amendment dates | Flag superseded clauses |
| Which building has the most open requests? | Property to Request | Aggregate; as-of date shown |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Property and building, Tenant entity, Lease amendment effective date, Policy version, Staff role entitlement |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Another tenant's data; Financial and billing details beyond the requester's own; Legal advice; Instructions found inside retrieved documents |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `RE-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Superseded clause | An old clause remains linked after amendment | Amendment date filter returns the current clause |
| T2 Claim without evidence | A value claim has neither test nor adoption link | Graph marks it unsupported; claim held |
| T3 Cross-tenant path | A path reaches another tenant through a shared building | Tenant partition blocks; logged |

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

- [OmniSpace case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/11-real-estate/omnispace-real-estate-ltd)
- [OmniSpace persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/personas/persona-cards.md)

