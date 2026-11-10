# OmniVibe — Integration and Event-Driven Architecture with SAP Integration Suite and Advanced Event Mesh

## Demo 05 of the BTM11 Consumer Discretionary Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Discretionary (CD) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnivibe-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniVibe is an **aspirational case study**. This file is an architecture design and teaching demonstration. The source gives integration statements only; topics, events and rules are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CD-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Integration architecture and event-driven design with SAP Advanced Event Mesh: when is an event the right answer, and how do you make it reliable?*

**What this file shows:** a six-event catalogue for OmniVibe, a rule for choosing API, event or batch, a delivery design (retention, replay, dead-message handling, reconciliation) and six evaluation scenarios.

**What it does not show:** a configured broker, a measured latency or a conformance result.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 28B consumer group; 72,000 employees; 48 countries |
| Business mix | Fashion 32%; beauty 18%; home 17%; specialty retail 15%; travel 10%; marketplace 8% |
| Network | 3,200 stores; 14 e-commerce sites; 26 distribution centres; 140 micro-fulfilment sites |

**Decision under discussion (source):** Select one brand and country workforce-to-service pilot and evidence gates before approving enterprise scale.

**Illustrative trigger (source):** A new associate lacks a completed onboarding and skills handoff while store readiness and channel information disagree (invented events that prompt discovery, per the case).

**Source anchor:** OVC-M12 proposes an integration platform and a workforce experience layer around SuccessFactors modules; OVC-M11 says to define franchise boundaries before sharing records. The source has no event-mesh design, and customer, order and inventory links are conceptual extensions.

**Scenario used in this demo:** A new associate's onboarding and skills handoff is incomplete while store readiness and channel information disagree.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, integration statements | **Source** |
| Event catalogue, topic names, routing and replay rules, evaluation scenarios, tests | **New design (illustrative)** |
| SAP Advanced Event Mesh behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which interactions in OmniVibe become events, which stay APIs or batches, and who owns delivery, replay and reconciliation?

**Accountable owner (proposed):** OVC-P11 Priya Shah for the integration standard, OVC-P04 Ravi Kapoor for the platform decision, OVC-P13 Farah Ahmed for trust boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OVC-P04 | Ravi Kapoor, Group CHRO | Platform and funding decision |
| OVC-P11 | Priya Shah, Director Enterprise Architecture | Owns integration standards and the topic convention |
| OVC-P13 | Farah Ahmed, CISO and Privacy Lead | Approves boundaries, access and payload rules |
| OVC-P12 | Jonas Lim, Integration and HR Data Lead | Owns event payload definitions |
| OVC-P08 | Sofia Mendes, Head of Talent Acquisition and Onboarding | Business owner of the first event stream |
| OVC-P06 | Oliver Brooks, Store Operations Director | Business owner of the second event stream |
| OVC-P16 | Nikhil Das, Store Associate and Workforce Representative | Operational reality check; replay and recovery impact |

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
| Event | Something happened that several consumers care about, and order or timing matters | workforce/associate/onboarding-started/v1 |
| Batch | Large volume, no timing need, reconciliation or history load | Nightly reconciliation of acknowledgements |

## 8. Event catalogue (new design)

Topic convention: `cd/<domain>/<object>/<event>/v<version>` (the catalogue below shows the part after the root). Payloads carry an event id, a sequence or effective time, a schema version and a correlation id. Personal data is minimized (pseudonyms only).

| Topic | Producer | Consumers | Key fields | Why it matters |
|---|---|---|---|---|
| workforce/associate/onboarding-started/v1 | Core HR | Learning, scheduling, store manager view | event id, associate pseudonym, country, brand, role, time | Late start delays readiness |
| workforce/associate/task-completed/v1 | Onboarding application | Store readiness, manager view | task id, associate pseudonym, completion time | Duplicates inflate completion |
| learning/course/completed/v1 | Learning application | Skills record, manager view | course id, version, associate pseudonym, time | Version matters for readiness |
| store/readiness/changed/v1 | Store application | Operations dashboard, scheduling | store id, status, as-of time | Conflicts with channel view |
| order/promise/updated/v1 (conceptual) | Order application | Store, customer channels | order id, promise date, status | Not in source; conceptual extension |
| ops/integration/dead-lettered/v1 | Integration platform | Integration operations, source owner | original event id, reason, attempts | No silent drop |

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
| E1 | A task-completed event is delivered twice | Idempotent by task id; one completion |
| E2 | A course-completed event refers to a superseded course version | Accepted with version noted; readiness rule uses the required version |
| E3 | A franchise-store event reaches the mesh | Boundary rule blocks routing to group consumers until a sharing basis exists |
| E4 | The store dashboard is unavailable during a readiness change | Event retained and replayed; dashboard converges |
| E5 | A consumer asks for personal fields beyond need | Payload minimization; pseudonym only |
| E6 | A malformed onboarding event | Dead-message path with reason; owner alerted |

## 11. Hands-on exercise (synthetic data)

1. Write one JSON event for each topic in the catalogue with synthetic ids (prefix `CD-SYN`).
2. Walk the six evaluation scenarios on paper and mark where the design rule decides.
3. Draw the producer, broker and consumers for the first scenario and mark the acknowledgement path.
4. Name the owner of the dead-message path and of reconciliation.
5. Record open decisions (retention, redelivery) in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Duplicate completion | Retries create double completion | Idempotency holds; one record |
| T2 Franchise boundary | Franchise events are routed to group analytics | Routing rule blocks; steward decides |
| T3 Out-of-order readiness | An older readiness status arrives after a newer one | Sequence or timestamp rule keeps the newer status |

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

- [OmniVibe case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/04-consumer-discretionary/omnivibe-consumer-ltd)
- [OmniVibe persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/04-consumer-discretionary/omnivibe-consumer-ltd/personas/persona-cards.md)

