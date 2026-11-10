# OmniSpace — Integration and Event-Driven Architecture with SAP Integration Suite and Advanced Event Mesh

## Demo 05 of the BTM11 Real Estate Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Real Estate (RE) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnispace-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniSpace is an **aspirational case study**. This file is an architecture design and teaching demonstration. The source gives integration statements only; topics, events and rules are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `RE-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Integration architecture and event-driven design with SAP Advanced Event Mesh: when is an event the right answer, and how do you make it reliable?*

**What this file shows:** a six-event catalogue for OmniSpace, a rule for choosing API, event or batch, a delivery design (retention, replay, dead-message handling, reconciliation) and six evaluation scenarios.

**What it does not show:** a configured broker, a measured latency or a conformance result.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | Not supplied in the case; no enterprise numerical profile, budget or quantified benefits |
| Scope | Aspirational global real-estate enterprise; property, tenant, ESG, recruiting, finance and procurement workstreams |
| Source problem | Fragmented architecture, processes, delivery evidence and adoption |

**Decision under discussion (source):** Select one capability or process pilot and prove its strategy-to-value traceability before scaling tools.

**Illustrative trigger (source):** A property-service workflow is declared live, but property teams still use spreadsheets, tenant requests remain unresolved, and test and adoption records cannot explain the claimed benefit (invented learning scenario).

**Source anchor:** OSP-M12 proposes Integration Suite, APIs and events, analytics, governance and identity around tool roles; no configured integration or current product capability is verified. The source has no event-mesh design. A case this early in its integration thinking should start with few events.

**Scenario used in this demo:** A property-service workflow is declared live, but spreadsheets persist, tenant requests remain unresolved and test and adoption records cannot explain the claimed benefit.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, integration statements | **Source** |
| Event catalogue, topic names, routing and replay rules, evaluation scenarios, tests | **New design (illustrative)** |
| SAP Advanced Event Mesh behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which interactions in OmniSpace become events, which stay APIs or batches, and who owns delivery, replay and reconciliation?

**Accountable owner (proposed):** OSP-P10 Daniel Weber for the integration standard, OSP-P05 Sofia Tan for the platform decision, OSP-P09 Omar Haddad for trust boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OSP-P05 | Sofia Tan, Chief Digital and Information Officer | Platform and funding decision |
| OSP-P10 | Daniel Weber, Enterprise Architecture Director | Owns integration standards and the topic convention |
| OSP-P09 | Omar Haddad, CISO and Resilience Lead | Approves boundaries, access and payload rules |
| OSP-P08 | Mei Lin, Enterprise Data and ESG Lead | Owns event payload definitions |
| OSP-P03 | Maya Patel, Property Operations Director | Business owner of the first event stream |
| OSP-P16 | Thomas van Dijk, Value Realization Office Lead | Business owner of the second event stream |
| OSP-P14 | Ingrid Sørensen, Adoption and Change Lead | Operational reality check; replay and recovery impact |

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
| Event | Something happened that several consumers care about, and order or timing matters | service/request/created/v1 |
| Batch | Large volume, no timing need, reconciliation or history load | Nightly reconciliation of acknowledgements |

## 8. Event catalogue (new design)

Topic convention: `re/<domain>/<object>/<event>/v<version>` (the catalogue below shows the part after the root). Payloads carry an event id, a sequence or effective time, a schema version and a correlation id. Personal data is minimized (pseudonyms only).

| Topic | Producer | Consumers | Key fields | Why it matters |
|---|---|---|---|---|
| service/request/created/v1 | Tenant request channel | Property operations, adoption log | request id, tenant pseudonym, building, category, time | Origin of the workflow |
| service/work-order/created/v1 | Property operations | Tenant updates, delivery tracking | work order id, request id, time | Link to request |
| service/work-order/closed/v1 | Property operations | Tenant updates, value tracking | work order id, outcome, time | Closure |
| adoption/usage/recorded/v1 | Adoption tooling | Value office | workflow id, user role, time | Needed to explain benefit |
| quality/test/executed/v1 | Quality engineering | Delivery tracking, value office | test id, result, time | Evidence for the claim |
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
| E1 | A request is created and the work-order system is offline | Event retained; work order created after recovery; tenant told |
| E2 | Duplicate request created events | Idempotent by request id |
| E3 | Adoption usage events are not captured for a building | Gap visible in the value view; claim held |
| E4 | A tenant event is routed to another tenant's consumer | Tenant partition blocks; logged |
| E5 | Work order closed before created | Sequence rule holds closure until the create event is processed |
| E6 | A malformed event | Dead-message path with reason; owner alerted |

## 11. Hands-on exercise (synthetic data)

1. Write one JSON event for each topic in the catalogue with synthetic ids (prefix `RE-SYN`).
2. Walk the six evaluation scenarios on paper and mark where the design rule decides.
3. Draw the producer, broker and consumers for the first scenario and mark the acknowledgement path.
4. Name the owner of the dead-message path and of reconciliation.
5. Record open decisions (retention, redelivery) in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Spreadsheet shadow process | Work continues in spreadsheets while events show nothing | Coverage report shows events versus known volume; gap raised |
| T2 Cross-tenant routing | A topic subscription spans tenants | Partition blocks; logged |
| T3 Claim without events | A benefit claim has no adoption or test events | Evidence rule holds the claim |

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

- [OmniSpace case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/11-real-estate/omnispace-real-estate-ltd)
- [OmniSpace persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/11-real-estate/omnispace-real-estate-ltd/personas/persona-cards.md)

