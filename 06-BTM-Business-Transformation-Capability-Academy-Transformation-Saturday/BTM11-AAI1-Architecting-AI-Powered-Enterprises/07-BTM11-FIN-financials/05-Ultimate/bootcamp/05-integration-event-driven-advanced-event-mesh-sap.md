# OmniCapital Financial Group — Integration and Event-Driven Architecture with SAP Integration Suite and Advanced Event Mesh

## Demo 05 of the BTM11 Financials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Financials (FIN) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnicapital-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniCapital Financial Group is an **aspirational case study**. This file is an architecture design and teaching demonstration. The source gives integration statements only; topics, events and rules are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `FIN-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Integration architecture and event-driven design with SAP Advanced Event Mesh: when is an event the right answer, and how do you make it reliable?*

**What this file shows:** a six-event catalogue for OmniCapital, a rule for choosing API, event or batch, a delivery design (retention, replay, dead-message handling, reconciliation) and six evaluation scenarios.

**What it does not show:** a configured broker, a measured latency or a conformance result.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 46B financial group; USD 1.4T AUM; 58M customers; 32 countries |
| Business mix | Retail 31%; commercial 24%; wealth 19%; insurance 16%; payments and markets 10% |
| Source problem | Fragmented customer, product, risk and transaction data; manual review; stronger fraud, cyber and model-risk control needs |

**Decision under discussion (source):** Fund a bounded onboarding and document-exception pilot with control and value evidence before enterprise expansion.

**Illustrative trigger (source):** An SME customer repeatedly submits the same document while customer service and verification teams show different exception status (invented discovery context, not an actual incident).

**Source anchor:** OCF-M12 names open APIs, events and a partner gateway over core banking, CRM, lending, payments and risk engines, with a lakehouse and ledger data; hybrid and resilience proposals are not tested implementation evidence. No event-mesh design in the source.

**Scenario used in this demo:** An SME customer repeatedly submits the same document while customer service and verification show different exception status.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, integration statements | **Source** |
| Event catalogue, topic names, routing and replay rules, evaluation scenarios, tests | **New design (illustrative)** |
| SAP Advanced Event Mesh behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which interactions in OmniCapital become events, which stay APIs or batches, and who owns delivery, replay and reconciliation?

**Accountable owner (proposed):** OCF-P12 Daniel Weber for the integration standard, OCF-P06 Sofia Chen for the platform decision, OCF-P10 Omar Haddad for trust boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OCF-P06 | Sofia Chen, Chief Digital and Information Officer | Platform and funding decision |
| OCF-P12 | Daniel Weber, Director Enterprise Architecture | Owns integration standards and the topic convention |
| OCF-P10 | Omar Haddad, CISO and Resilience Lead | Approves boundaries, access and payload rules |
| OCF-P09 | Mei Tan, Customer Identity and Data Lead | Owns event payload definitions |
| OCF-P03 | Priya Rao, Chief Customer and Retail Officer | Business owner of the first event stream |
| OCF-P08 | Marcus Okoro, Financial Crime Operations Director | Business owner of the second event stream |
| OCF-P05 | Elena Fischer, Chief Compliance and Conduct Officer | Operational reality check; replay and recovery impact |

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
| Event | Something happened that several consumers care about, and order or timing matters | onboarding/document/received/v1 |
| Batch | Large volume, no timing need, reconciliation or history load | Nightly reconciliation of acknowledgements |

## 8. Event catalogue (new design)

Topic convention: `fin/<domain>/<object>/<event>/v<version>` (the catalogue below shows the part after the root). Payloads carry an event id, a sequence or effective time, a schema version and a correlation id. Personal data is minimized (pseudonyms only).

| Topic | Producer | Consumers | Key fields | Why it matters |
|---|---|---|---|---|
| onboarding/document/received/v1 | Document intake | Verification, CRM | document id, customer pseudonym, type, time | Duplicates cause repeated work |
| onboarding/exception/raised/v1 | Verification | CRM, service, case management | exception id, reason class, system, time | Two systems must agree |
| onboarding/exception/resolved/v1 | Verification | CRM, service | exception id, resolution, approver, time | Resolution authority stays with people |
| customer/consent/changed/v1 | Consent service | All consumers | customer pseudonym, purpose, status, time | Consent change must propagate fast |
| risk/alert/raised/v1 (restricted) | Risk engine | Investigators only | alert id, class, time | Restricted routing |
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
| E1 | Document received event published twice | Idempotent by document id; one exception only |
| E2 | Exception raised and resolved events arrive out of order | Sequence decides; final status is resolved |
| E3 | Consent withdrawn while events are in flight | Consumers stop using affected purposes immediately |
| E4 | A service-role consumer subscribes to a restricted alert topic | Subscription denied; attempt logged |
| E5 | The CRM is unavailable during resolution | Event retained and replayed; both systems converge |
| E6 | Resolution event lacks an approver | Rejected to dead-message path; verification owner alerted |

## 11. Hands-on exercise (synthetic data)

1. Write one JSON event for each topic in the catalogue with synthetic ids (prefix `FIN-SYN`).
2. Walk the six evaluation scenarios on paper and mark where the design rule decides.
3. Draw the producer, broker and consumers for the first scenario and mark the acknowledgement path.
4. Name the owner of the dead-message path and of reconciliation.
5. Record open decisions (retention, redelivery) in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Status mismatch between systems | CRM shows open while verification shows resolved | Reconciliation raises the mismatch with system of record |
| T2 Restricted topic access | A service consumer asks for alert events | Access control blocks; security informed |
| T3 Consent change in flight | Consent is withdrawn between publish and delivery | Delivery filter drops affected content; logged |

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

- [OmniCapital Financial Group case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/07-financials/omnicapital-financial-group-ltd)
- [OmniCapital Financial Group persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/personas/persona-cards.md)

