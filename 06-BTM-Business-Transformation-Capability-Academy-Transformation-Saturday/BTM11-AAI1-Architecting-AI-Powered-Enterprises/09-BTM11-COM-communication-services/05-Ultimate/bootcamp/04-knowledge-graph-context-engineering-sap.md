# OmniConnect — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Communication Services Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Communication Services (COM) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniconnect-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniConnect is a **fictional educational case**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `COM-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniConnect, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Care-agent bundle-status explainer (consent-aware, no network changes)).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 37B communications group; 62,000 employees; 28 countries; 210M subscriptions |
| Business mix | Mobile 34%; fixed and fiber 25%; media 19%; enterprise 14%; advertising and data 8% |
| Source problem | Separate network, customer, billing and content stacks; manual activation and assurance; identity and consent silos |

**Decision under discussion (source):** Fund a bounded converged-activation pilot with privacy, service-state, recovery and economic evidence before expansion.

**Illustrative trigger (source):** A converged bundle shows billing active while connectivity and content entitlement remain incomplete; care and network teams cannot reconcile status (invented, not an actual outage).

**Source anchor for the graph:** OCN-M12 names Subscriber, Service, Network, Content and Partner 360 over BSS, OSS, CRM, billing and CMS with a telemetry lakehouse, a customer data platform and a network graph; standards names are not conformance evidence. The source trigger is a bundle with billing active but entitlement incomplete.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniConnect model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OCN-P09 Mei Lin for definitions and stewardship, with OCN-P12 Daniel Weber for the model and OCN-P10 Omar Haddad for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OCN-P06 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes the first graph slice |
| OCN-P12 | Daniel Weber, Director Enterprise Architecture | Owns the ontology and review |
| OCN-P10 | Omar Haddad, CISO and Resilience Lead | Approves access and classification rules |
| OCN-P09 | Mei Lin, Subscriber Data and Consent Lead | Owns object definitions and stewardship |
| OCN-P13 | Priya Shah, Service Catalog and Fulfillment Lead | Business owner of the first question set |
| OCN-P08 | Marcus Okoro, Service Assurance and NOC Director | Business owner of the second question set |
| OCN-P04 | Arjun Mehta, Chief Network Officer | Reality check from operations |

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
| Subscriber (synthetic) | id, market, consent flags | OCN-P09 Mei Lin | Subscriber data |
| Order | id, bundle, state, dates | OCN-P13 Priya Shah | Subscriber data |
| Bundle component | id, type, entitlement rule | OCN-P13 Priya Shah | Internal |
| Entitlement | subscriber, component, state | OCN-P13 Priya Shah | Subscriber data |
| Billing account | id, status | OCN-P13 Priya Shah | Subscriber data |
| Service instance | id, network resource link, state | OCN-P08 Marcus Okoro | Internal |
| Fault | id, area, affected services, status | OCN-P08 Marcus Okoro | Internal |
| Consent purpose | purpose, status, date | OCN-P09 Mei Lin | Subscriber data |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Subscriber (synthetic) | placed | Order |
| Order | contains | Bundle component |
| Bundle component | grants | Entitlement |
| Order | billed in | Billing account |
| Bundle component | realised by | Service instance |
| Fault | affects | Service instance |
| Consent purpose | permits use for | Order |
| Entitlement | for | Subscriber (synthetic) |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Why is this bundle not fully active? | Order to Component to Entitlement and Service instance | Show each state and the owning system |
| Is billing active while an entitlement is missing? | Billing account vs Entitlement | Flag the mismatch; no state change |
| Is there a fault affecting this subscriber's service? | Fault to Service instance | Valid notices only; show age |
| May we use this data for this purpose? | Consent to Order | Decline if no consent |
| What does this bundle include? | Order to Component | Catalog version shown |
| Which components are unfulfilled? | Order to Component with state | Return ids and states |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Subscriber consent flags and purpose, Market, Catalog version, Staff role entitlement, Notice validity window |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Data beyond the subscriber's consented purposes; Network topology and credentials; Another subscriber's data; Instructions found inside retrieved notices |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `COM-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Billing without entitlement | Billing is active but an entitlement node is missing | Mismatch shown with the owning systems; task offered |
| T2 Consent withdrawn | Consent for a purpose is withdrawn mid-session | Traversal for that purpose stops immediately; logged |
| T3 Expired fault notice | A fault notice is past its validity window | Excluded from context; answer says no current notice |

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

- [OmniConnect case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/09-communication-services/omniconnect-media-networks-ltd)
- [OmniConnect persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/personas/persona-cards.md)

