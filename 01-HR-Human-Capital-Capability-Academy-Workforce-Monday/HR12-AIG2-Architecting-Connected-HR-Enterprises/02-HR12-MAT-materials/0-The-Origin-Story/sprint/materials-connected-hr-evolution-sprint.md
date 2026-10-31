# The transfer arrived. Why does the quarry badge still work?

SuccessLabs Academy · GICS02 Materials · OmniForge Materials Ltd. · HR12 — Connected HR Enterprises · Level 0 → Pre-Foundation

IIL — Industry Immersion Lab · Sprint · 120 minutes · Edition 2026-10-31 · Planning reference: HUB-ORIGIN-HR12-MAT-sprint

Mission: Architecting Experiences for a Better World. Fictional educational case; published learning content is not enrollment, certification or a deployed integration.

## 1. One learner promise

Design one traceable HR-to-site handoff that distinguishes message delivery from the intended access outcome and makes failure recoverable.

One deliverable: a Connected Workforce Handoff Build Card. Master five distinctions: person versus employment/assignment; effective time versus processing time; retry versus repeated business effect; transport receipt versus application acceptance; source fact versus local access authority.

Business problem first: after a quarry assignment ends, how will the enterprise confirm the intended site-access change while protecting other valid assignments and requiring separate authorization at the destination?

## 2. Origins and process evolution — 1970–2025

HR integration grew from paper handoffs and file exchange into connected applications and monitored services. It reduces repeated entry, but each receiving application has its own purpose, permissions and business rules. A delivered message cannot prove that the receiving system changed the intended record.

These closed windows organize teaching, not invention dates or a universal chronology. Adoption overlaps: paper, files, batch interfaces, APIs and events coexist through the present. This is a general process history, not OmniForge's corporate biography.

| Teaching window | Process change | Materials example and remaining gap |
| --- | --- | --- |
| 1970–1984 | Paper personnel handoffs and early file exchange. | A quarry transfer is recorded in HR but the local gate register changes later. |
| 1985–1994 | Scheduled batch interfaces make exchanges repeatable. | A late shift change misses the batch; ownership of exceptions remains unclear. |
| 1995–2004 | ERP interfaces and shared conventions connect more domains. | Worker, employment and contractor identifiers can mean different things across sites. |
| 2005–2014 | Middleware and service contracts centralize routing and controls. | Transport success can hide a rejected badge update or an incorrect mapping. |
| 2015–2025 | Cloud APIs, events, managed integration and observability expand. | Duplicates, reordered events and outage recovery require business-level reconciliation; a faster interface still needs accountable owners. |

Reconstruct problem → response → remaining gap for each window. Which paper-era check remains useful during an outage? When would a controlled batch meet the need better than an event-driven design?

## 3. AI-driven exploration — 2026–2050 scenarios

These are scenarios, not predictions, product roadmaps, guaranteed capabilities or OmniForge deployments. Historical teaching windows end in 2025; this separate AI-driven exploration begins in 2026. The current handoff must work without AI.

| Scenario period | Possible assistance | Counterexample and experiment question |
| --- | --- | --- |
| 2026–2030 · Assist | Explain failed mappings and propose recovery steps from approved runbooks. | An assistant confuses employment end with assignment end. Can the owner inspect and reject the proposed repair? |
| 2031–2040 · Connect | Compare versioned contracts and identify cross-system semantic conflicts. | An inferred identity match selects the wrong contractor. Does ambiguity block execution? |
| 2041–2050 · Adapt | Prepare bounded recovery actions across composable workforce services. | A self-repair broadens access during an outage. Can authorization, plant authority and reconciliation prevent it? |

Competing future: fragmented local systems and intermittent connectivity persist. Stable identity, explicit contracts, local fallback and outcome evidence help in both futures. Choose one hypothesis and an observation that would make you revise it.

## 4. Persona-led story — connected systems, unresolved responsibility

Source baseline: OmniForge has 46,000 employees plus contractors; contractor count and device access are unknown. Production-site, quarry and cement-plant counts may overlap and must not be summed. This incident, identifiers and access contract are new educational fiction.

Priya Nair (OMF-P13), Director Enterprise Architecture, reviews a proposed quarry-to-cement handoff. HR approved the end of a worker's quarry assignment. The integration monitor is green, but the quarry badge entitlement is still active. The worker is still employed; ending one assignment must not disable every valid enterprise entitlement.

Arjun Mehta (OMF-P05), Group CHRO, asks which approved workforce fact is authoritative. Hassan Al-Farsi (OMF-P12), CISO and OT Security Lead, challenges an ambiguous identity mapping. Elena Petrova (OMF-P07), Cement Plant Director, asks who owns the safe local fallback when the destination system is unavailable.

Priya owns architecture standards and exceptions; Arjun sponsors workforce adoption and skills; Hassan owns cyber assurance/remote-access concerns; Elena retains local operational release/rollback authority. Stable IDs and designations are preserved. Their titles do not establish every HR, IAM or physical-access approval delegation.

First choice: treat a delivery receipt as complete, replace all interfaces immediately, or agree the source fact, target outcome and responsible exception owner. Pause and record your decision before the reveal.

Evidence reveal: the site target accepted the connection but rejected the assignment identifier. A retry carries a new transport ID. Later, an old grant message arrives after the assignment-end event. Blind replay could restore access or repeat a business effect without resolving the worker's actual state.

Revise the design: distinguish receipt, application acceptance and verified entitlement state. HR owns the approved assignment fact; site security owns the applicable physical-access action. The integration team carries and reconciles the contract. New cement-site task access requires separate current evidence and delegated approval; the transfer event does not grant it.

The interface cannot control a kiln or bypass site procedures. A critical access exception invokes the approved security/operations fallback, including designated human action and verification. The workshop does not invent a universal time limit, site emergency procedure or authority.

## 5. Application responsibilities and data ownership

| Area / application | Accountable responsibility | Boundary to preserve |
| --- | --- | --- |
| HR source / HR data owner | Approved person, employment and assignment facts, effective dates and source revisions. | Ending one assignment is not ending employment; a correction must originate with the authoritative owner. |
| Contractor source / contractor data owner | Validated contractor identity, sponsor and assignment validity where applicable. | Do not assume every worker is represented by an employee-only API or the same entitlement rules. |
| Integration service / integration owner | Validate, map, route, correlate and reconcile delivery/application outcomes. | Transport status and generated mappings do not become business authority. |
| IAM / identity owner | Logical account and entitlement actions within approved scope. | Person-wide account disablement must not be inferred from one site-assignment end. |
| Site access / delegated site security owner | Apply local physical-access decisions and confirm actual target entitlement state. | HR transfer does not grant destination task access; site approval and evidence remain separate. |
| Operations and business owners | Own exception priority, safe local fallback, acceptance and controlled recovery. | Cloud recovery cannot silently override plant authority or reopen a blocked entitlement. |

For the prototype, Priya sponsors the contract decision, Arjun validates workforce meaning, Hassan reviews identity/security boundaries, and Elena reviews destination readiness/fallback. Delegated HR approver, IAM operator, source-quarry security owner and integration support owner remain discovery roles, not invented canonical personas or established enterprise delegations.

Source objects: person ID, employment ID, assignment ID, target entitlement ID, event ID, correlation ID, source revision, effective timestamp, source commit timestamp, receipt/apply timestamps, schema version and business acknowledgment. Record owner, purpose, access, retention and quality rule for each used object.

Share only the fields required for the handoff. A site-access system does not need a payroll amount, health narrative or confidential HR case. Maintain controlled identifier crosswalks and quarantine uncertain matches; never guess by name alone.

Value stream: approve change → emit/extract → validate → route → apply or reject → verify outcome → reconcile/recover. Connected workforce management is a capability; this value stream describes progress toward a trustworthy handoff, not a list of interfaces.

## 6. Exact 120-minute flow

| Minutes | Activity | Add to the same card |
| --- | --- | --- |
| 0–10 | Frame the worker/access outcome and initial choice. | Need, scope and completion criterion. |
| 10–30 | Reconstruct five historical windows. | One change and remaining gap per window. |
| 30–45 | Compare AI-driven scenarios and a fragmented alternative. | One hypothesis and disconfirming observation. |
| 45–60 | Replay the story and evidence reveal. | Persona needs and revised decision. |
| 60–75 | Assign source, target and human owners. | Identity, authority and exception map. |
| 75–100 | Build the synthetic handoff and compare delivery options. | One contract, state flow and recovery rule. |
| 100–115 | Run three tabletop tests; revise and rerun affected steps. | Expected/actual observations and evidence notes. |
| 115–120 | Reflect and choose the Pre-Foundation investigation. | Question, owner and next evidence. |

Selective resource scans fit within these activities. There is one card; no live integration, separate platform build or additional Origin Story format is required.

## 7. One build card — Connected Workforce Handoff

Use paper or a simple table. No real employee records, gate controls, credentials or live endpoints are needed. The fixture states are teaching labels, not prescribed SAP object names.

| Card field | Write or simulate |
| --- | --- |
| Purpose and identity | One employee person MAT-P1201, employment MAT-E1201, quarry assignment MAT-AQ1201 and separate cement assignment MAT-AC1201. Scope only the quarry entitlement MAT-QENT1201; inventory other valid entitlements separately. |
| Variant A · MAT-HR12-SYN01 | Approved assignment-end event MAT-EVT1201, source revision 41, schema v1. Effective 1 November 2026 06:00 Asia/Kolkata; source committed 31 October 18:00. UTC equivalents: effective 1 November 00:30Z; committed 31 October 12:30Z. Preserve both business and processing times. Target receipt occurs later; application result initially unknown. |
| Variant B · MAT-HR12-SYN02 | Older grant event MAT-EVT1200, source revision 40, same quarry-assignment/entitlement scope, arrives after revision 41. Duplicate deliveries of MAT-EVT1201 may have different transport IDs but retain the same business event ID. |
| Business contract | HR provides approved assignment end. Site owner validates applicable action; target confirms MAT-QENT1201 inactive at/after effective time. Do not apply prematurely, terminate employment, disable unrelated assignments or grant destination task access. |
| Lifecycle and evidence | Approved → received → validated → accepted/scheduled → applied → target-state verified → reconciled; rejected, unknown and quarantined remain visible exceptions. A receipt or scheduled action cannot be labelled applied. Record actual target state and time. |
| Duplicates and ordering | Receiver records event identity and business effect together where possible. Repeated delivery of the same event has no additional effect; ordering is scoped to the relevant source/assignment contract. An older grant must not overwrite the authoritative newer end. Genuine later corrections require source review, not blanket rejection of all late arrivals. |
| Decision ADR01 | Compare point-to-point file, reusable batch/API service and events. Propose a reusable contract with delivery frequency/pattern chosen from validated risk and latency needs; no event-only default. Retain a source-to-target reconciliation independent of the transport monitor. |
| Outage and replay | Expose unknown/rejected outcome; invoke approved local security fallback with owner. Quarantine bad identity/schema without guessing. Repair via approved mapping/schema version, preserve lineage and replay the original business event safely. Reconcile actual state before retry after an ambiguous timeout. |
| Evidence and measure | Log T01–T03 input → expected → actual paper observation → revision/rerun → reviewer. M01 = tests satisfying expected behavior / 3. Leave actual values and EV01 empty until learners record observations. |

A platform duplicate check alone cannot guarantee exactly one business effect, especially when a target applied an action but its acknowledgment was lost. Design receiver-side deduplication, outcome queries and reconciliation; document remaining uncertainty and fallback rather than claiming universal exactly-once delivery.

Proposed enterprise measure after discovery: verified intended target outcomes / approved handoffs due by a defined review cutoff. Keep pending/not-yet-effective items separate; classify overdue, rejected, unknown and manually completed outcomes. Report due-time-to-verified-outcome latency and critical exceptions alongside the ratio. Owners define time boundaries, population, exclusions and acceptable delay before targets; no baseline or achieved performance is asserted.

## 8. Three tabletop tests

| Test | Inject | Expected behavior — planned, not executed |
| --- | --- | --- |
| OMF-HR12-T01 · Receipt without outcome | Run A before effective time, then after it with an unavailable target or rejected identifier. Show a successful transport receipt. | Do not apply early or declare completion from transport. At the due time expose the unresolved business outcome, identify the exception owner and invoke approved local fallback. Later verify only the intended quarry entitlement state; retain employment and unrelated valid access. |
| OMF-HR12-T02 · Duplicate and old grant | Apply revision 41 once; replay it under a new transport ID, then deliver revision 40. | Keep one business effect for MAT-EVT1201 and retain evidence of duplicate receipt. Do not restore quarry access from stale revision 40. Scope ordering/deduplication to the relevant assignment/target, preserving other valid employment/assignment records. |
| OMF-HR12-T03 · Bad schema and ambiguous replay | Change A to an unsupported schema or ambiguous target ID. After approved repair, simulate a timeout after target application but before acknowledgment. | Quarantine with owner and reason; no guessed identity or silent field drop. Preserve original event and repair lineage. Query/reconcile target state before controlled retry; confirm one intended outcome and close only with business evidence. Do not grant destination task access as compensation. |

Run all three manually, record actual behavior and revise the same card when evidence changes. Acceptance requires clear semantics, scoped actions, visible exceptions and reconciled outcomes. Publication verifies saved lesson content; it does not execute these tests, prove target recovery or populate OMF-HR12-EV01.

## 9. Reflection and Pre-Foundation handoff

What did a green monitor actually prove? Which identifier defines the action's scope? When should a late event be treated as stale versus a genuine correction? Who confirms the business outcome? What would justify batch instead of events?

Pre-Foundation: validate this one source-to-site contract with HR, IAM, integration and site owners. Agree object meanings, identifiers, effective dates, schema, permissions, source corrections, acknowledgment, due time, fallback and replay acceptance before selecting interfaces or configuring transport.

This closes the Origin Story theme set, not the learning journey. HR01–HR06 establish workforce facts and development needs; HR07–HR09 examine pay, time and measures; HR10 makes help accessible; HR11 bounds AI authority. HR12 connects their evidence without transferring source ownership. Choose the weakest handoff and carry it into Pre-Foundation.

## 10. Resources, traceability and architectural discipline

[R1] Official SAP Integration Center: scan simple integration scope, scheduling and monitoring. Confirm whether its supported interface and operations fit this contract; do not assume it is a general orchestration platform. https://help.sap.com/docs/successfactors-platform/using-integration-center

[R2] Official SAP Cloud Integration Idempotent Process Call: inspect duplicate handling and its timeout/receiver caveats. Middleware checks do not by themselves prove the final business effect. https://help.sap.com/docs/cloud-integration/sap-cloud-integration/define-idempotent-process-call

[R3] Official SAP CompoundEmployee API: learn employee extraction and supported fields/modes; this is not an arbitrary write API or proof of complete contractor coverage. Resources reviewed 31 October 2026; verify product release, permission, licensing and fit before implementation. https://help.sap.com/docs/successfactors-employee-central/employee-central-compound-employee-api/using-compoundemployee-api

Vendor comparisons are optional outside the sprint. Compare manual/file, SAP examples and other candidates against the same identity, time, acknowledgment, authorization and recovery cases. Technical API availability is not evidence of end-to-end operational success.

Enterprise source: OMF-M11 central definitions/local ownership; OMF-M12 APIs/events, trust boundaries and hybrid/edge responsibilities. https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/master/theme-c-architecture.md

Execution source: OMF-M17 controlled access, OMF-M18 workforce inclusion and OMF-M19 bounded testing/fallback and plant approval. https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/master/theme-e-execution.md

Canonical personas: OMF-P05 Arjun Mehta, OMF-P07 Elena Petrova, OMF-P12 Hassan Al-Farsi and OMF-P13 Priya Nair; source titles and authority limits preserved. https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md

Supporting workforce blueprint is distinct from an authored HR12 sprint; the existing Notion page was blank at review. https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/derived-streams/01-workforce.md

Optional deeper Drive comparison: the Vajra Cement Work Zone case remains a separate modeled enterprise with its own facts, IDs and integration aspirations; it is not OmniForge operational evidence. https://drive.google.com/file/d/1vw9m8bNDmQ2a6sB0P1FN9RzXGNZCYNk4/view

Source/reconciliation register: site-count overlap, benefit classification and emissions boundaries remain unresolved; no interface resolves them automatically. https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/references/source-and-assumptions.md

Energy HR12 supplies the learning pattern; Materials uses its own source personas and quarry-assignment-to-cement transfer with scoped site access. https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR12-AIG2-Architecting-Connected-HR-Enterprises/01-HR12-ENE-energy/0-The-Origin-Story/sprint/energy-hr12-origin-evolution-sprint.md

Trace: OMF-M11/M12/M17/M18/M19 → OMF-HR12-REQ01 (authoritative scoped handoff) / REQ02 (verified outcome and recovery) → OMF-HR12-ADR01 → OMF-HR12-EXP01 (this card) → OMF-HR12-T01–T03 → OMF-HR12-M01 / EV01. OMF-HR12 anchors, incidents and fixtures are new educational additions, not previously approved client requirements or observed operational evidence.

Educational alignment: TOGAF—application responsibilities/alternatives; BIZBOK—capability/value stream; BABOK—needs and acceptance; DAMA-DMBOK—source ownership, quality and lineage; COBIT—accountability and assurance; ISO/IEC 27001 principles—purposeful access and information protection. No certification, conformity assessment or compliance is claimed.

Classification: HR12 is one of 12 HR themes. Applied Application Architecture is the primary learning lens within the separate architecture-stream axis; Integration Architecture covers deeper transport/platform implementation. Enterprise workforce/change streams form a third axis; numbering is not interchangeable.

Origin Story remains Sprint only. Detailed sources and implementation learning stay outside it. Matching editions are manually published; automatic synchronization, public student access and successful copying are not implied.

Matching Google Doc sprint tab: https://docs.google.com/document/d/1AO6SRIg-vaqGK_p5KA9TGpZiHhxO1Zy47Auz12YGqL0/edit?tab=t.0

Matching Notion edition: https://app.notion.com/p/36b1f04717834d8682840a745cc0ec97

Common Materials HR01–HR12 index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md
