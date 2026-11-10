# OmniVerse Energy Ltd. — Integration and Event-Driven Architecture with SAP Integration Suite and Advanced Event Mesh

## Demo 05 of the BTM11 Energy Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Energy (ENE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniverse-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniVerse Energy Ltd. is an **aspirational case study**. This file is an architecture design and teaching demonstration. The source gives integration statements only; topics, events and rules are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `ENE-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Integration architecture and event-driven design with SAP Advanced Event Mesh: when is an event the right answer, and how do you make it reliable?*

**What this file shows:** a six-event catalogue for OmniVerse, a rule for choosing API, event or batch, a delivery design (retention, replay, dead-message handling, reconciliation) and six evaluation scenarios.

**What it does not show:** a configured broker, a measured latency or a conformance result.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 85B revenue; 68,000 employees; 42 countries |
| Business mix | Upstream 35%; refining and petrochemicals 28%; retail and marketing 18%; power 12%; renewables 7% |
| Assets | 8 refineries; 25,000 km pipelines; 12,500 retail sites; 15 GW generation |

**Decision under discussion (source):** Which AI use cases stay assistive, which may trigger human-approved actions, and which low-risk processes may be automated (OVE-HR11 strategic dilemma).

**Illustrative trigger (source):** In the OVE-HR11 decision scenes, an employee (Rina) receives incorrect promotion guidance from an assistant, while HR operations wants automatic data corrections and case closure and a worker representative challenges sentiment inference and productivity scoring.

**Source anchor:** OVE-HR12 supplies a strong source anchor: the event object model (event id, subject and employment id, effective timestamp, sequence, schema version, correlation id, acknowledgement), the value stream change approved, emit, validate, route, acknowledge, reconcile, recover, the access-incident scene (termination failed between Employee Central, identity and refinery access, leaving access active for 18 hours) and the OVE-HR12-T01 portfolio (lost termination; duplicate or reordered events; stale rehire; poison message; unavailable target; replay after recovery). The case names SAP Integration Suite and SAP BTP; it does not mention an event mesh.

**Scenario used in this demo:** A termination event fails between the employment system, identity and refinery access, and physical and digital access stay active.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, integration statements | **Source** |
| Event catalogue, topic names, routing and replay rules, evaluation scenarios, tests | **New design (illustrative)** |
| SAP Advanced Event Mesh behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which interactions in OmniVerse become events, which stay APIs or batches, and who owns delivery, replay and reconciliation?

**Accountable owner (proposed):** OVE-HR12-P01 Sameer Kulkarni as design owner; OVE-HR12-P05 Eric Thompson for operations; OVE-P05 Rajiv Kapoor for the platform decision.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OVE-HR12-P01 | Sameer Kulkarni, Enterprise HR Integration Architect | Canonical design owner |
| OVE-HR12-P02 | Helena Rossi, Chief HR Technology Officer | Pressure for quick delivery; the architecture-shortcut scene |
| OVE-HR12-P03 | David Park, Identity and Access Management Lead | Needs complete and timely lifecycle events |
| OVE-HR12-P04 | Zanele Dube, Refinery Security Director | Cannot tolerate delayed deprovisioning |
| OVE-HR12-P05 | Eric Thompson, Integration Operations Manager | Monitoring, reconciliation, retry, recovery, service levels |
| OVE-P13 | Omar Haddad, CISO | Security and assurance across the enterprise |
| OVE-P05 | Rajiv Kapoor, CDIO | Platform decisions |

Decision rights are **proposed** and need discovery validation.

## 6. What the SAP platform offers (public documentation, verify)

| Capability | What the documentation describes | Status in this design |
|---|---|---|
| SAP Integration Suite | Integration capabilities for APIs, processes and connectivity on SAP BTP | Used for API and process integration |
| SAP Integration Suite, Advanced Event Mesh | Publish and subscribe, queuing, streaming, replay, request-reply; an Event Portal for design and governance; Insights for monitoring; Dynamic Message Routing; Message VPN bridging between brokers | Used for events in this design |
| Dead-message queue, guaranteed delivery, time to live | Not confirmed on the pages reviewed | **Verify** before relying on them |
| Alternatives | Direct APIs, file or batch transfer, other brokers | Chosen per interaction by the rule below |

## 7. Choosing API, event or batch (new design)

| Use | When | Example from this case |
|---|---|---|
| API (request-reply) | The caller needs an answer now and the owner can serve it | Lookup of a current record |
| Event | Something happened that several consumers care about, and order or timing matters | hr/employee/terminated/v1 |
| Batch | Large volume, no timing need, reconciliation or history load | Nightly reconciliation of acknowledgements |

## 8. Event catalogue (new design)

Topic convention: `ene/<domain>/<object>/<event>/v<version>` (the catalogue below shows the part after the root). Payloads carry an event id, a sequence or effective time, a schema version and a correlation id. Personal data is minimized (pseudonyms only).

| Topic | Producer | Consumers | Key fields | Why it matters |
|---|---|---|---|---|
| hr/employee/terminated/v1 | Employment system | Identity and access, refinery access control, payroll, learning | event id, subject id, effective timestamp, sequence, schema version, correlation id | Delayed or lost delivery leaves access active (source scene) |
| hr/employee/hired/v1 | Employment system | Identity, payroll, learning, access | same envelope; position id | Late delivery delays safe onboarding |
| hr/employee/transferred/v1 | Employment system | Identity, payroll, finance | same envelope; from and to organization | Reordering can apply old and new state wrongly |
| hr/employee/rehired/v1 | Employment system | Identity, access, payroll | same envelope; prior employment link | Stale rehire test in source |
| access/account/deprovisioned/v1 | Identity and access | Employment system, security operations | event id, subject id, correlation id, completion time | Acknowledgement closes the loop |
| ops/integration/dead-lettered/v1 | Integration platform | Integration operations, owner of source | original event id, reason, attempts, first failure time | A silent drop cannot count as completion (source REQ02) |

## 9. Delivery design (decisions to make, not stated values)

| Topic | Design | Value |
|---|---|---|
| Idempotency | Consumers recognize an event id already processed | Rule |
| Ordering | Sequence or effective time decides; late older events do not overwrite newer state | Rule |
| Retention and replay window | How long events can be replayed after an outage | To be decided |
| Redelivery and time to live | Broker settings per queue | To be decided; verify product support |
| Dead-message handling | Owner, review cadence and replay approval for failed events | Owner to be named |
| Acknowledgement and reconciliation | A consumer confirms; a periodic job compares sent and acknowledged | Rule |
| Schema versioning | Backward-compatible changes only inside a version; new version for breaking changes | Rule |
| Security | Topic-level authorization; no secrets or unneeded personal data in payloads | Rule |

## 10. Evaluation scenarios

| ID | Scenario | Expected behaviour |
|---|---|---|
| E1 | Terminated event is published and the target is unavailable for a period | Event is retained and delivered on recovery; acknowledgement recorded; no duplicate action |
| E2 | The same terminated event is delivered twice after a retry | Second delivery is recognised by event id and not re-applied |
| E3 | Hired and transferred events for one person arrive out of order | Sequence number decides; late older event is not applied over newer state |
| E4 | A malformed event (poison message) is received | Moved to a dead-message path with reason; owner alerted; stream continues |
| E5 | A rehire event arrives after a stale terminated event is replayed | Effective timestamp and sequence prevent wrong final state |
| E6 | Acknowledgement never arrives for a terminated event | Reconciliation raises an exception to the access owner before any close |

## 11. Hands-on exercise (synthetic data)

1. Write one JSON event for each topic in the catalogue with synthetic ids (prefix `ENE-SYN`).
2. Walk the six evaluation scenarios on paper and mark where the design rule decides.
3. Draw the producer, broker and consumers for the first scenario and mark the acknowledgement path.
4. Name the owner of the dead-message path and of reconciliation.
5. Record open decisions (retention, redelivery) in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Lost termination | Delivery fails during an outage window | Event retained; replay after recovery; access owner sees the pending exception |
| T2 Duplicate and reordered events | Retries and out-of-order arrival occur together | Idempotency and sequence rules hold; no double downstream action |
| T3 Architecture shortcut | A team asks for a one-off file interface to meet a deadline | Standard pattern and ADR path offered; exception needs an expiry and owner |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Scenarios with a defined rule and owner | Count of the six | Not measured |
| Topics with a single named producer | Catalogue check | Not measured |
| Events with idempotency and sequence fields | Payload review | Not measured |
| Open broker settings with a named decider | Count of decisions to make | Not measured |

No baseline, target or benefit is stated because none exists for this aspirational case study. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Why events here, and where not | API, event or batch rule |
| 0:20 to 1:00 | Event catalogue walk-through | Six events with owners |
| 1:00 to 1:45 | Delivery design and scenarios | Decision list |
| 1:45 to 2:15 | Tabletop tests | Three findings |
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

- [SAP Integration Suite, Advanced Event Mesh documentation](https://help.sap.com/docs/sap-integration-suite)
- [SAP Integration Suite](https://www.sap.com/products/technology-platform/integration-suite.html)

- [OmniVerse Energy Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/01-energy/omniverse-energy-ltd)
- [OmniVerse Energy Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md)

