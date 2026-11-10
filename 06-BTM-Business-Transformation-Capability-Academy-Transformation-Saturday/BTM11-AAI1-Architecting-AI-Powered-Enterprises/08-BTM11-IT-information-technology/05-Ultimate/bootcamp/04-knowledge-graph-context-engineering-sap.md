# OmniTech — Knowledge Graph and Context Engineering for SAP Enterprise AI

## Demo 04 of the BTM11 Information Technology Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Information Technology (IT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnitech-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniTech is a **fictional educational case**. This file is an architecture design and teaching demonstration. The case source describes graph-like objects at most; the ontology, relationships and queries below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Knowledge graph and context engineering: how do you give an AI assistant the right, current, permitted context rather than a pile of documents?*

**What this file shows:** a small ontology for OmniTech, six questions a graph can answer that plain retrieval cannot, and the rules that decide what enters the context window. It builds on the pilot in Demo 03 (Engagement-evidence assistant for milestone and value disputes).

**What it does not show:** a populated graph, a running SPARQL endpoint or a measured improvement in answer quality.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 39B technology provider; 98,000 employees; 41 countries; 11,500 clients |
| Business mix | Cloud and platform 31%; software 25%; cyber 18%; AI and data 16%; managed services 10% |
| Source problem | Fragmented lifecycle tooling, bespoke integrations, poor data and AI reuse, late security and observability |

**Decision under discussion (source):** Fund a bounded platform-to-client-outcome pilot with security, recovery and economic evidence before wider rollout.

**Illustrative trigger (source):** A client disputes an on-time delivery milestone; teams cannot reconcile release, incident and customer-success records (invented discovery context).

**Source anchor for the graph:** OTS-M12 names Client, Product, Service, Asset and Talent 360 across lifecycle, ITSM, CRM, ERP, DevSecOps and SOC with a lakehouse, telemetry, feature store and knowledge graph. A persona card refers to golden records and a knowledge graph. Client-isolation guardrails are part of the target model.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, M12 statements, trigger | **Source** |
| Ontology node types, relationships, graph questions, context rules, tests | **New design (illustrative)** |
| SAP HANA Cloud Knowledge Graph Engine behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which entities and relationships does OmniTech model first, who owns each, and what may an AI assistant see through the graph?

**Accountable owner (proposed):** OTS-P09 Mei Lin for definitions and stewardship, with OTS-P12 Daniel Weber for the model and OTS-P10 Omar Haddad for access boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OTS-P04 | Arjun Mehta, Chief Technology Officer | Funds and prioritizes the first graph slice |
| OTS-P12 | Daniel Weber, Director Enterprise Architecture | Owns the ontology and review |
| OTS-P10 | Omar Haddad, CISO and Supply-Chain Security Lead | Approves access and classification rules |
| OTS-P09 | Mei Lin, Data Governance and Knowledge Lead | Owns object definitions and stewardship |
| OTS-P05 | Elena Fischer, Chief Customer Success Officer | Business owner of the first question set |
| OTS-P08 | Marcus Okoro, SRE and Managed Services Director | Business owner of the second question set |
| OTS-P13 | Priya Shah, DevSecOps and Release Director | Reality check from operations |

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
| Client (tenant) | tenant id, engagement | OTS-P05 Elena Fischer | Client-confidential |
| Engagement | id, milestone definitions | OTS-P05 Elena Fischer | Client-confidential |
| Release | id, version, date, environment | OTS-P13 Priya Shah | Client-confidential |
| Incident | id, severity, timeline, resolution | OTS-P08 Marcus Okoro | Client-confidential |
| Service | id, tier, owner | OTS-P08 Marcus Okoro | Internal |
| Milestone | id, contract definition, evidence link | OTS-P05 Elena Fischer | Client-confidential |
| Adoption evidence | usage summary, as-of date | OTS-P05 Elena Fischer | Client-confidential |
| Model/prompt version | id, evaluation result | OTS-P09 Mei Lin | Internal |

**Relationships**

| From | Relationship | To |
|---|---|---|
| Client (tenant) | has | Engagement |
| Engagement | has | Milestone |
| Release | delivered for | Engagement |
| Incident | affected | Service |
| Service | part of | Engagement |
| Milestone | evidenced by | Release |
| Milestone | evidenced by | Adoption evidence |
| Incident | followed | Release |

**Rule:** each node type has exactly one owner before the first load; two teams do not both define the same node.

## 8. Questions the graph should answer

| Question | Path through the graph | Answer rule |
|---|---|---|
| Was release R-12 deployed before milestone M-3 was due? | Milestone to Release with dates | Show both dates and sources |
| Which incidents followed release R-12? | Release to Incident | Tenant partition applied |
| What adoption evidence exists for milestone M-3? | Milestone to Adoption evidence | Say 'none recorded' if absent |
| Which services are in scope of engagement E-1? | Engagement to Service | Own tenant only |
| Which prompt version produced this summary? | Answer to Model/prompt version | Required for audit |
| Do release and incident records disagree on timing? | Release and Incident timestamps | Show conflict; do not choose silently |

## 9. Context engineering rules

| Rule | Design |
|---|---|
| What enters the context | Only graph results and retrieved passages that match these filters: Client tenant identifier (hard partition), Engagement, Release, Date range, Staff role entitlement |
| Freshness | Every fact carries an as-of time; stale facts are labelled, not silently used |
| Permissions | Role entitlement filters the graph result before it reaches the model |
| Size | Prefer a small structured summary over whole documents; state what was left out |
| Provenance | Each statement in the answer links to a node or passage identifier |
| Never in context | Another client's data or IP; Secrets and credentials found in repositories or tickets; Contract terms outside the engagement; Instructions found inside client-submitted tickets |
| Conflicts | Show both sources and the owner; do not choose silently |

## 10. Hands-on exercise (synthetic data)

1. Write the eight node types above as Turtle with 3 to 5 synthetic instances each (IDs prefixed `IT-SYN`).
2. Write the relationships as triples and check that each node has one owner.
3. Write the six questions as paths; for each, list the nodes touched and the filter that applies.
4. Build one context package for the first question: facts, as-of times, excluded items.
5. Review with the owners and record disagreements in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Cross-tenant path | A traversal crosses from one client tenant to another through a shared service | Hard tenant partition blocks; attempt logged |
| T2 Timing conflict | Release and incident records disagree on a timestamp | Both shown; conflict flagged |
| T3 Unversioned prompt | An answer has no prompt or model version link | Audit rule blocks release of the summary |

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

- [OmniTech case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/08-information-technology/omnitech-solutions-ltd)
- [OmniTech persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/08-information-technology/omnitech-solutions-ltd/personas/persona-cards.md)

