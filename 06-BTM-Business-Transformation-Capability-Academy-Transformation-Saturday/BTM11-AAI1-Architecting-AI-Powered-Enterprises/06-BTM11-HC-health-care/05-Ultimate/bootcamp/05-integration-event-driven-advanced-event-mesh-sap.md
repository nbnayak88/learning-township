# OmniHealth — Integration and Event-Driven Architecture with SAP Integration Suite and Advanced Event Mesh

## Demo 05 of the BTM11 Health Care Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Health Care (HC) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnihealth-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02 EA](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03 AI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md)

> **Evidence boundary:** OmniHealth is an **aspirational case study**. This file is an architecture design and teaching demonstration. The source gives integration statements only; topics, events and rules are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `HC-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Integration architecture and event-driven design with SAP Advanced Event Mesh: when is an event the right answer, and how do you make it reliable?*

**What this file shows:** a six-event catalogue for OmniHealth, a rule for choosing API, event or batch, a delivery design (retention, replay, dead-message handling, reconciliation) and six evaluation scenarios.

**What it does not show:** a configured broker, a measured latency or a conformance result.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 34B healthcare group; 126,000 staff; 19 countries |
| Network | 86 hospitals; 440 clinics; 670 diagnostic centres |
| Business mix | Acute 38%; primary 22%; diagnostics 18%; digital and pharmacy 12%; research and value-based 10% |

**Decision under discussion (source):** Select a bounded, non-clinical care-coordination pilot and evidence gates before enterprise expansion.

**Illustrative trigger (source):** A referral crosses facilities without clear ownership; the patient repeats information and a dashboard cannot reconcile episode status (invented; no actual patient incident is asserted).

**Source anchor:** OHS-M12 proposes a FHIR-aligned gateway, APIs, iPaaS and events over EHR, LIMS, RIS/PACS, ERP, CRM and care management (conceptual source proposals, not validated conformance). No event-mesh design in the source. Administrative flows only.

**Scenario used in this demo:** A referral crosses facilities without clear ownership; the patient repeats information and a dashboard cannot reconcile episode status.

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas, integration statements | **Source** |
| Event catalogue, topic names, routing and replay rules, evaluation scenarios, tests | **New design (illustrative)** |
| SAP Advanced Event Mesh behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Which interactions in OmniHealth become events, which stay APIs or batches, and who owns delivery, replay and reconciliation?

**Accountable owner (proposed):** OHS-P13 Daniel Weber for the integration standard, OHS-P05 Sofia Tan for the platform decision, OHS-P10 Omar Haddad for trust boundaries.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OHS-P05 | Sofia Tan, Chief Digital and Information Officer | Platform and funding decision |
| OHS-P13 | Daniel Weber, Enterprise Architecture Director | Owns integration standards and the topic convention |
| OHS-P10 | Omar Haddad, CISO and Privacy Lead | Approves boundaries, access and payload rules |
| OHS-P09 | Priya Nair, Patient Identity and Data Governance Lead | Owns event payload definitions |
| OHS-P07 | Dr. Amina Okafor, Nursing and Care Coordination Director | Business owner of the first event stream |
| OHS-P04 | Dr. Arjun Mehta, Chief Clinical Operations Officer | Business owner of the second event stream |
| OHS-P03 | Dr. Leila Morgan, Chief Medical Officer | Operational reality check; replay and recovery impact |

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
| Event | Something happened that several consumers care about, and order or timing matters | referral/referral/created/v1 |
| Batch | Large volume, no timing need, reconciliation or history load | Nightly reconciliation of acknowledgements |

## 8. Event catalogue (new design)

Topic convention: `hc/<domain>/<object>/<event>/v<version>` (the catalogue below shows the part after the root). Payloads carry an event id, a sequence or effective time, a schema version and a correlation id. Personal data is minimized (pseudonyms only).

| Topic | Producer | Consumers | Key fields | Why it matters |
|---|---|---|---|---|
| referral/referral/created/v1 | Scheduling and referral application | Receiving facility, care coordination | referral id, patient pseudonym, owner facility, time | Missing owner leaves a referral unseen |
| referral/referral/owner-changed/v1 | Referral application | Coordinators, dashboards | referral id, from and to facility, time | Hand-off must be visible |
| scheduling/appointment/booked/v1 | Scheduling application | Referral application, patient communications | appointment id, referral id, slot, time | Duplicate booking risk |
| scheduling/appointment/cancelled/v1 | Scheduling application | Referral application, coordinators | appointment id, reason class, time | Reordering can hide a cancellation |
| identity/match/confidence-changed/v1 | Identity service | All consumers | pseudonym, confidence, time | Low confidence stops downstream use |
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
| E1 | Owner-changed events arrive out of order | Sequence decides; coordinator sees the latest owner |
| E2 | A booking is published twice | Idempotent by appointment id |
| E3 | Identity confidence drops below the threshold | Consumers stop using the patient pseudonym until resolved |
| E4 | The referral application is unavailable | Events retained and replayed; no lost referral |
| E5 | A consumer requests clinical payload fields | Payload excludes clinical content by design; request refused |
| E6 | A malformed event | Dead-message path with reason; owner alerted |

## 11. Hands-on exercise (synthetic data)

1. Write one JSON event for each topic in the catalogue with synthetic ids (prefix `HC-SYN`).
2. Walk the six evaluation scenarios on paper and mark where the design rule decides.
3. Draw the producer, broker and consumers for the first scenario and mark the acknowledgement path.
4. Name the owner of the dead-message path and of reconciliation.
5. Record open decisions (retention, redelivery) in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Ownerless referral | A referral event has no owner facility | Rejected to dead-message path; coordinator alerted |
| T2 Cancellation hidden by reordering | Cancelled arrives before booked | Sequence logic keeps final state correct |
| T3 Identity drop mid-flow | Confidence falls after referral creation | Downstream use paused; manual verification route |

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

- [OmniHealth case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/06-health-care/omnihealth-systems-ltd)
- [OmniHealth persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/06-health-care/omnihealth-systems-ltd/personas/persona-cards.md)

