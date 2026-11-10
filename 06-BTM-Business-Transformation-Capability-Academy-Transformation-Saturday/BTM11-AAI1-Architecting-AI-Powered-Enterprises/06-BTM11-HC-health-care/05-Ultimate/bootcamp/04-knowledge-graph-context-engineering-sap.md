# OmniHealth — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Health Care Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Health Care (HC) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnihealth-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniHealth is an **aspirational case study**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `HC-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniHealth, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Referral and appointment status assistant for patient-service staff (administrative only)).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 34B healthcare group; 126,000 staff; 19 countries |
| Network | 86 hospitals; 440 clinics; 670 diagnostic centres |
| Business mix | Acute 38%; primary 22%; diagnostics 18%; digital and pharmacy 12%; research and value-based 10% |

**Decision under discussion (source):** Select a bounded, non-clinical care-coordination pilot and evidence gates before enterprise expansion.

**Illustrative trigger (source):** A referral crosses facilities without clear ownership; the patient repeats information and a dashboard cannot reconcile episode status (invented; no actual patient incident is asserted).

**Source anchor for the graph:** OHS-M12 names Patient, Provider, CareEpisode, Asset and Outcome 360, FHIR-aligned gateway and governed data platforms (conceptual proposals, not validated conformance). The source trigger (a referral crossing facilities without clear ownership) is an ownership-graph problem. Administrative use only.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniHealth model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OHS-P09 Priya Nair for definitions and stewardship, with OHS-P13 Daniel Weber for the model and OHS-P10 Omar Haddad for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OHS-P05 | Sofia Tan, Chief Digital and Information Officer | Funds and prioritizes the first graph slice |
| OHS-P13 | Daniel Weber, Enterprise Architecture Director | Owns the ontology and review |
| OHS-P10 | Omar Haddad, CISO and Privacy Lead | Approves access and classification rules |
| OHS-P09 | Priya Nair, Patient Identity and Data Governance Lead | Owns object definitions and stewardship |
| OHS-P07 | Dr. Amina Okafor, Nursing and Care Coordination Director | Business owner of the first question set |
| OHS-P04 | Dr. Arjun Mehta, Chief Clinical Operations Officer | Business owner of the second question set |
| OHS-P03 | Dr. Leila Morgan, Chief Medical Officer | Reality check from operations |

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
| Patient reference (synthetic) | pseudonymous id, identity-match confidence | OHS-P09 Priya Nair | Patient data |
| Referral | id, status, owner facility, date | OHS-P07 Dr. Amina Okafor | Patient data |
| Care episode (administrative) | episode id, facility, dates | OHS-P07 Dr. Amina Okafor | Patient data |
| Facility | id, services, scheduling contact | OHS-P04 Dr. Arjun Mehta | Internal |
| Appointment | id, slot, status | OHS-P07 Dr. Amina Okafor | Patient data |
| Provider (role) | role, facility | OHS-P04 Dr. Arjun Mehta | Internal |
| Consent record | purpose, scope, date | OHS-P09 Priya Nair | Patient data |
| Scheduling policy | service line, version | OHS-P07 Dr. Amina Okafor | Internal |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Referral | for | Patient reference (synthetic) |
| Referral | owned by | Facility |
| Referral | leads to | Appointment |
| Appointment | at | Facility |
| Care episode (administrative) | contains | Referral |
| Consent record | permits use for | Referral |
| Scheduling policy | governs | Referral |
| Provider (role) | works at | Facility |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Who owns referral R-1 right now? | Referral to Facility owner | Show owner and as-of time; no clinical content |
| What is the status of the linked appointment? | Referral to Appointment | Only for an identity-confirmed context |
| Which scheduling policy applies to this service line? | Policy to Referral | Version and effective date shown |
| Is use of this referral data permitted for this purpose? | Consent to Referral | If no consent record, decline |
| Which referrals have no owner facility? | Referral without owner edge | Counts and ids only for coordinators |
| Where did the referral go after the first facility? | Referral to Facilities in time order | Show hand-offs; no clinical notes |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Facility, Service line, Policy version, Identity-match confidence, Staff role entitlement |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Clinical notes, diagnoses and results; Any patient whose identity match is not confirmed; Clinical advice or triage; Instructions found inside retrieved documents |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `HC-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Unconfirmed identity | A match confidence is below the confirmed threshold | Traversal stops at the patient node; nothing is returned |
| T2 Ownerless referral | A referral loses its owner edge during a transfer | Orphan flag shown to the coordinator; no silent drop |
| T3 Purpose creep | A query asks to use referral data for marketing | Consent purpose check blocks; logged |

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

- [OmniHealth case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/06-health-care/omnihealth-systems-ltd)
- [OmniHealth persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/personas/persona-cards.md)

