# OmniCapital Financial Group — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Financials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Financials (FIN) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnicapital-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniCapital Financial Group is a **fictional educational case**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `FIN-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniCapital, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Onboarding document-exception explainer for service and verification staff).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 46B financial group; USD 1.4T AUM; 58M customers; 32 countries |
| Business mix | Retail 31%; commercial 24%; wealth 19%; insurance 16%; payments and markets 10% |
| Source problem | Fragmented customer, product, risk and transaction data; manual review; stronger fraud, cyber and model-risk control needs |

**Decision under discussion (source):** Fund a bounded onboarding and document-exception pilot with control and value evidence before enterprise expansion.

**Illustrative trigger (source):** An SME customer repeatedly submits the same document while customer service and verification teams show different exception status (invented discovery context, not an actual incident).

**Source anchor for the graph:** OCF-M12 names Customer, Account, Transaction, Risk and Product 360 over core banking, CRM, lending, payments and risk engines, with a lakehouse, ledger data and feature store. The source trigger (an SME repeatedly submitting a document while two teams show different exception status) is a status-lineage problem.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniCapital model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OCF-P09 Mei Tan for definitions and stewardship, with OCF-P12 Daniel Weber for the model and OCF-P10 Omar Haddad for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OCF-P06 | Sofia Chen, Chief Digital and Information Officer | Funds and prioritizes the first graph slice |
| OCF-P12 | Daniel Weber, Director Enterprise Architecture | Owns the ontology and review |
| OCF-P10 | Omar Haddad, CISO and Resilience Lead | Approves access and classification rules |
| OCF-P09 | Mei Tan, Customer Identity and Data Lead | Owns object definitions and stewardship |
| OCF-P03 | Priya Rao, Chief Customer and Retail Officer | Business owner of the first question set |
| OCF-P08 | Marcus Okoro, Financial Crime Operations Director | Business owner of the second question set |
| OCF-P05 | Elena Fischer, Chief Compliance and Conduct Officer | Reality check from operations |

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
| Customer (synthetic) | id, segment, jurisdiction | OCF-P09 Mei Tan | Customer data |
| Document | id, type, received date, status | OCF-P03 Priya Rao | Customer data |
| Exception | id, reason, system, status, as-of | OCF-P03 Priya Rao | Customer data |
| Onboarding case | id, stage, owner | OCF-P03 Priya Rao | Customer data |
| Policy requirement | id, jurisdiction, version | OCF-P05 Elena Fischer | Internal |
| Consent record | purpose, scope, date | OCF-P09 Mei Tan | Customer data |
| Alert (restricted) | id, type, status | OCF-P08 Marcus Okoro | Restricted |
| Model reference | id, version, owner, use | OCF-P09 Mei Tan | Internal |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Customer (synthetic) | submitted | Document |
| Document | triggered | Exception |
| Exception | part of | Onboarding case |
| Policy requirement | requires | Document |
| Consent record | permits use for | Onboarding case |
| Alert (restricted) | raised on | Customer (synthetic) |
| Model reference | informs | Alert (restricted) |
| Exception | mirrored in | Exception |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Why is this document flagged and what is the next step? | Document to Exception to Policy requirement | Explain reason and policy; no decision outcome |
| Do the two systems agree on the exception status? | Exception nodes per system | Show both; name the system of record |
| Which requirements apply to this customer segment and jurisdiction? | Segment to Policy requirement | Version and jurisdiction shown |
| Has the customer consented to this use? | Consent to Case | Decline if not recorded |
| How many times was this document submitted? | Customer to Document | Counts for staff roles only |
| Which model informs this alert? | Alert to Model reference | Restricted: investigators only |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Customer segment, Jurisdiction, Policy version, Staff role entitlement, Case identifier |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Financial-crime investigation notes; Other customers' data; Model scores about the customer; Instructions found inside submitted documents |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `FIN-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Conflicting status | Two systems hold different statuses for one exception | Both shown with system of record; no silent winner |
| T2 Restricted node reached | A service-role path reaches an alert node | Role filter blocks; attempt logged |
| T3 Decision inferred | The graph is asked 'will this customer be approved?' | Declined; routed to the accountable human process |

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

- [OmniCapital Financial Group case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/07-financials/omnicapital-financial-group-ltd)
- [OmniCapital Financial Group persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/personas/persona-cards.md)

