# OmniDaily — Integration and Event-Driven Architecture with SAP Integration Suite and Advanced Event Mesh

## Demo 05 of the BTM11 Consumer Staples Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Staples (CS) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnidaily-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniDaily is a **fictional educational case**. This file is an architecture design and teaching demonstration. The source gives integration statements only; topics, events and rules are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `CS-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Integration architecture and event-driven design with SAP Advanced Event Mesh: when is an event the right answer, and how do you make it reliable?*

**What this file shows:** a six-event catalogue for OmniDaily, a rule for choosing API, event or batch, a delivery design (retention, replay, dead-message handling, reconciliation) and six evaluation scenarios.

**What it does not show:** a configured broker, a measured latency or a conformance result.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 51B staples group; 84,000 employees; 57 countries; 420M households served |
| Business mix | Foods 30%; beverages 23%; home care 19%; personal care 18%; wellness 10% |
| Burning platform | Demand, promotion, planning, product and ingredient data, quality and route-to-market execution fragmented across 160+ applications |

**Decision under discussion (source):** Fund a bounded demand-to-shelf and quality-evidence pilot before approving enterprise scale.

**Illustrative trigger (source):** A promotion creates a shelf gap while a quality-held batch appears available in a delayed distributor feed (invented; no real safety event is claimed).

**Source anchor:** ODG-M12 names API, B2B and event integration across ERP, planning, TPM, MES, LIMS, DMS, CRM and e-commerce, with edge and private cloud for factory workloads (source). No event-mesh design in the source.

**Scenario used in this demo:** A promotion creates a shelf gap while a quality-held batch looks available in a delayed distributor feed.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, integration statements | **Source** |
| Event catalogue, topic names, routing and replay rules, evaluation scenarios, tests | **New design (illustrative)** |
| SAP Advanced Event Mesh behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which interactions in OmniDaily become events, which stay APIs or batches, and who owns delivery, replay and reconciliation?

**Accountable owner (proposed):** ODG-P13 Priya Nair for the integration standard, ODG-P05 Sofia Alvarez for the platform decision, ODG-P12 Omar Haddad for trust boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| ODG-P05 | Sofia Alvarez, Chief Digital and Data Officer | Platform and funding decision |
| ODG-P13 | Priya Nair, Director Enterprise Architecture | Owns integration standards and the topic convention |
| ODG-P12 | Omar Haddad, CISO and Privacy Lead | Approves boundaries, access and payload rules |
| ODG-P08 | Mei Lin, Head of Product and Ingredient Stewardship | Owns event payload definitions |
| ODG-P07 | David Okoro, Global Quality and Product Safety Director | Business owner of the first event stream |
| ODG-P10 | Rohan Shah, Distributor and Field Execution Director | Business owner of the second event stream |
| ODG-P09 | Elena Petrović, Plant Operations Director | Operational reality check; replay and recovery impact |

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
| Event | Something happened that several consumers care about, and order or timing matters | quality/hold/placed/v1 |
| Batch | Large volume, no timing need, reconciliation or history load | Nightly reconciliation of acknowledgements |

## 8. Event catalogue (new design)

Topic convention: `cs/<domain>/<object>/<event>/v<version>` (the catalogue below shows the part after the root). Payloads carry an event id, a sequence or effective time, a schema version and a correlation id. Personal data is minimized (pseudonyms only).

| Topic | Producer | Consumers | Key fields | Why it matters |
|---|---|---|---|---|
| quality/hold/placed/v1 | Quality system | ERP, distributor management, planning, field execution | hold id, lot id, market, reason, time | Late delivery lets held stock appear available |
| quality/hold/released/v1 | Quality system | ERP, distributor management, planning | hold id, lot id, release time, approver | Release authority stays with Quality |
| distribution/stock/reported/v1 | Distributor feed | Planning, availability service | outlet, SKU, quantity, as-of time | Delay is a known risk |
| commercial/promotion/activated/v1 | Trade promotion | Planning, field execution | promotion id, SKU, outlet group, window | Must be checked against holds |
| plant/batch/completed/v1 | Manufacturing execution | ERP, quality, planning | lot id, SKU, plant, time | Starts the trace chain |
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
| E1 | A hold event and a stock report for the same lot arrive in the wrong order | Newest hold wins; stock report labelled stale |
| E2 | A hold release is published but the approver is missing | Rejected into the dead-message path; Quality alerted |
| E3 | A feed event is hours old | Marked stale by as-of time; planners warned |
| E4 | The planning consumer is offline during a hold | Replay after recovery; no missed hold |
| E5 | A consumer asks to publish a release event | Refused unless produced by Quality system with approver |
| E6 | Duplicate promotion activation | Idempotent by promotion id |

## 11. Hands-on exercise (synthetic data)

1. Write one JSON event for each topic in the catalogue with synthetic ids (prefix `CS-SYN`).
2. Walk the six evaluation scenarios on paper and mark where the design rule decides.
3. Draw the producer, broker and consumers for the first scenario and mark the acknowledgement path.
4. Name the owner of the dead-message path and of reconciliation.
5. Record open decisions (retention, redelivery) in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Hold versus delayed feed | A hold follows a stale 'available' feed record | Hold takes precedence; availability service shows as-of and hold |
| T2 Unauthorized release event | A non-Quality producer publishes a release | Producer authorization blocks; incident logged |
| T3 Replay after outage | Planning was offline during several holds | Replay delivers all holds in order; planners reconcile |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Scenarios with a defined rule and owner | Count of the six | Not measured |
| Topics with a single named producer | Catalogue check | Not measured |
| Events with idempotency and sequence fields | Payload review | Not measured |
| Open broker settings with a named decider | Count of decisions to make | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

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
| Customer-confirmed requirements | Not applicable (fictional case) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP Integration Suite, Advanced Event Mesh documentation](https://help.sap.com/docs/sap-integration-suite)
- [SAP Integration Suite](https://www.sap.com/products/technology-platform/integration-suite.html)

- [OmniDaily case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/05-consumer-staples/omnidaily-consumer-goods-ltd)
- [OmniDaily persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md)

