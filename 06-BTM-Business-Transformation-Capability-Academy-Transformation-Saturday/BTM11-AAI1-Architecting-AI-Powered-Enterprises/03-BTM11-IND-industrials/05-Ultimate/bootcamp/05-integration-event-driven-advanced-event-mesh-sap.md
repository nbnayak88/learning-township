# OmniWorks Industrial Systems Ltd. — Integration and Event-Driven Architecture with SAP Integration Suite and Advanced Event Mesh

## Demo 05 of the BTM11 Industrials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Industrials (IND) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniworks-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniWorks Industrial Systems Ltd. is an **aspirational case study**. This file is an architecture design and teaching demonstration. The source gives integration statements only; topics, events and rules are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IND-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Integration architecture and event-driven design with SAP Advanced Event Mesh: when is an event the right answer, and how do you make it reliable?*

**What this file shows:** a six-event catalogue for OmniWorks, a rule for choosing API, event or batch, a delivery design (retention, replay, dead-message handling, reconciliation) and six evaluation scenarios.

**What it does not show:** a configured broker, a measured latency or a conformance result.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 48B revenue; 74,000 employees; 36 countries; 61 plants and facilities; 320 service depots; 7,200 suppliers |
| Business mix | Industrial automation 27%; aerospace and defence 23%; transport and mobility 19%; infrastructure 16%; aftermarket and lifecycle services 15% |
| Burning platform | Recurring transport asset failures cannot be consistently traced across configuration, telemetry, supplier batches and maintenance history |

**Decision under discussion (source):** Turn a USD 575M transformation envelope into credible customer, operational and financial value without disrupting safety-critical operations.

**Illustrative trigger (source):** Repeat customer asset failures expose fragmented engineering-to-service information, and the business wants to sell uptime rather than equipment (hero story).

**Source anchor:** OW-M12 links PLM, ERP, MES, EAM, FSM and customer portals through APIs and events, with OPC UA and MQTT at the OT edge, segmentation, cloud and edge services (source). No event-mesh design in the source.

**Scenario used in this demo:** A transport asset fails repeatedly; configuration, telemetry, supplier batch and maintenance records arrive from different systems at different times.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, integration statements | **Source** |
| Event catalogue, topic names, routing and replay rules, evaluation scenarios, tests | **New design (illustrative)** |
| SAP Advanced Event Mesh behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which interactions in OmniWorks become events, which stay APIs or batches, and who owns delivery, replay and reconciliation?

**Accountable owner (proposed):** OW-P11 Hannah Fischer for the integration standard, OW-P05 Priya Nair for the platform decision, OW-P06 Marcus Vogel for trust boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OW-P05 | Priya Nair, CIDO | Platform and funding decision |
| OW-P11 | Hannah Fischer, Director, Enterprise Architecture | Owns integration standards and the topic convention |
| OW-P06 | Marcus Vogel, CISO | Approves boundaries, access and payload rules |
| OW-P15 | Dr. Leila Haddad, Head of Data Governance & AI | Owns event payload definitions |
| OW-P09 | Isabel Torres, Chief Customer & Service Officer | Business owner of the first event stream |
| OW-P10 | Ravi Deshpande, VP Manufacturing, Pune Operations | Business owner of the second event stream |
| OW-P12 | Daniel Okafor, Field Service Operations Manager | Operational reality check; replay and recovery impact |

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
| Event | Something happened that several consumers care about, and order or timing matters | asset/telemetry/fault-detected/v1 |
| Batch | Large volume, no timing need, reconciliation or history load | Nightly reconciliation of acknowledgements |

## 8. Event catalogue (new design)

Topic convention: `ind/<domain>/<object>/<event>/v<version>` (the catalogue below shows the part after the root). Payloads carry an event id, a sequence or effective time, a schema version and a correlation id. Personal data is minimized (pseudonyms only).

| Topic | Producer | Consumers | Key fields | Why it matters |
|---|---|---|---|---|
| asset/telemetry/fault-detected/v1 | OT edge gateway | Field service, reliability analytics | asset serial, signal class, severity, time, sequence | Edge to enterprise only |
| service/work-order/created/v1 | Field service | Planning, parts, customer portal | work order id, asset serial, category, time | Duplicates create duplicate dispatches |
| engineering/change/released/v1 | PLM | ERP, MES, field service | change id, effective configuration, approver | Order of changes decides the baseline |
| supply/batch/quality-notice/v1 | Supplier quality | Engineering, field service | batch id, supplier, notice, share permission | Partner-restricted data |
| service/work-order/closed/v1 | Field service | Customer portal, analytics, ERP | work order id, cause code, time | Closure drives outcome reporting |
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
| E1 | A fault event repeats several times from a flapping signal | Collapsed by event id; one work order only |
| E2 | An engineering change event arrives after the work order that depends on it | Correlation shows the baseline in force at event time |
| E3 | A supplier notice is marked partner-restricted | Routed only to consumers with the share permission |
| E4 | The customer portal is down when a work order closes | Event retained and replayed; no lost closure |
| E5 | A consumer asks to publish a command to the OT edge | Refused; one-way flow at the edge |
| E6 | A work-order event has an unknown schema version | Dead-message path with reason; owner alerted |

## 11. Hands-on exercise (synthetic data)

1. Write one JSON event for each topic in the catalogue with synthetic ids (prefix `IND-SYN`).
2. Walk the six evaluation scenarios on paper and mark where the design rule decides.
3. Draw the producer, broker and consumers for the first scenario and mark the acknowledgement path.
4. Name the owner of the dead-message path and of reconciliation.
5. Record open decisions (retention, redelivery) in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Duplicate dispatch | Retries produce two work orders | Idempotency by work order id prevents duplicates |
| T2 Restricted notice leak | A restricted supplier notice reaches a customer-view consumer | Permission-based routing blocks; incident logged |
| T3 Late engineering change | A change event arrives after dependent service events | Effective-time logic recomputes the baseline view; discrepancy reported |

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

- [OmniWorks Industrial Systems Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/03-industrials/omniworks-industrial-systems)
- [OmniWorks Industrial Systems Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md)

