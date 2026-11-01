# A role change that reached only half the systems

SuccessLabs Academy · HR12 Connected HR Enterprises · GICS09 Communication Services

IIL — Industry Immersion Lab · The Origin Story · 120-minute Sprint

Mission: Architecting Experiences for a Better World.

Planning reference HUB-ORIGIN-HR12-COM-sprint (not an LMS ID). Published learning content does not establish a live or enrolled course.

## The story and learner promise

In 120 minutes: Design one recoverable workforce handoff with explicit per-system outcomes.

One persona-led story · One build card · Exactly three tabletop tests. Use synthetic records without a tenant.

Nadia Fernandes (OCN-P07), Group CHRO, approves a technician's new NOC assignment. Sofia Tan (OCN-P06), Chief Digital and Information Officer, sees the HR event delivered while IAM and scheduling show different roles. Marcus Okoro (OCN-P08), Service Assurance and NOC Director, asks whether the worker can join the shift.

**Choose first:** Declare success from the event broker, resend without checking, or reconcile each authoritative target?

**Evidence reveal:** IAM applied a newer revision but scheduling received an older event late. Transport delivery proves neither correct target state nor operational permission. Sofia proposes version checks and a controlled replay after reconciliation.

**Counterexample:** An HTTP success or broker acknowledgment cannot prove the intended business state.

OmniConnect is a fictional communication-services enterprise. The source stipulates 62,000 employees across 28 countries, spanning mobile and 5G, fiber, media and streaming, enterprise networks, and advertising. No new site or workforce counts are inferred. Existing source KPIs and financial figures are fictional baselines, proposals or targets, with no achieved result asserted.

This edition uses GICS09 Communication Services. The Industrials and GICS10 wording in the reusable brief is treated as a template carryover. Existing OCN-P persona identities and OCN-M master anchors remain unchanged. This incident, dialogue, synthetic records and OCN-XL IDs are new educational additions. Existing research remains separate from this sprint.

## Origins and responsibility

These closed historical windows are educational groupings, not universal invention dates or OmniConnect corporate biography. Adoption overlaps; older practices can coexist through the present.

| Teaching window | Process evolution |
|---|---|
| 1970–1984 | Manual handoffs reconcile local records |
| 1985–1994 | Batch files exchange employment changes |
| 1995–2004 | Managed interfaces standardize mappings |
| 2005–2014 | APIs and events coordinate services |
| 2015–2025 | Governed automation assists exception recovery |

| Application responsibility | Accountable owner | Data and human boundary |
|---|---|---|
| Core HR | HR steward | Approved lifecycle facts, effective date and revision |
| Integration service | Interface owner | Contract validation, correlation, delivery status and recoverable exceptions |
| Receiving domains | IAM, payroll, learning and scheduling owners | Independent target-state reconciliation and policy-controlled actions |

Integration Suite and BTP are source examples; interface versions and production conformance remain unvalidated.

A source-system record, receiving-system acknowledgment and human permission answer different questions. Provide a private, accessible correction or appeal route. Avoid personal-data joins with subscriber or audience data unless a legitimate purpose, access boundary and minimum data are established.

## One build card in 120 minutes

| Minutes | Activity |
|---|---|
| 0–10 | Frame the people and service problem |
| 10–30 | Explore origins and process evolution |
| 30–45 | Choose, reveal evidence and revise |
| 45–60 | Assign data ownership and decision rights |
| 60–90 | Complete the single build card |
| 90–110 | Discuss the three tabletop tests and record observations |
| 110–120 | Explain the decision and prepare the Pre-Foundation question |

| Build card field | Complete on the same card |
|---|---|
| Need and history | State the worker/service need and one enduring question from the historical windows. |
| Synthetic inputs | EVT1200, COM-P1200, employment COM-E1200, revision 2, effective 2 November 2026. Revision 1 arrives after revision 2 at scheduling. |
| Owners and rights | Record source of each fact, accountable owner, authorized decision role and minimum data viewers. |
| Decision and alternative | Write your first choice, reveal evidence, revise it and explain one defensible alternative. |
| Design and exception | One Connected Handoff Build Card with source key, event ID, schema/revision, effective time, minimum payload, per-target state, replay authority and evidence. Record the held action, exception owner, accessible worker notice and reconciliation route. |
| Evidence and measure | For each of T01–T03 record input, expected, observed, evidence reference and revision. Every receiving owner confirms intended state or an explicit exception; no integration execution claimed. |
| Next discovery | Specify one lifecycle contract, target responsibilities, idempotency, version rules and support ownership. |

Compare a common enterprise core with one justified local variant. State the local rule owner and evidence required; do not invent country rules. Discuss workload, accessibility, minimum data, recovery cost and avoiding unnecessary processing. Automation may assist low-risk administration; material decisions remain with the authorized role.

## Exactly three tabletop tests

| Test ID | Focus | Evidence reveal | Expected result in the proposed design |
|---|---|---|---|
| OCN-XL-HR12-T01 | Target unavailable | HR commits but IAM rejects the request. | Record partial completion, retain the exception and prevent unauthorized shift release. |
| OCN-XL-HR12-T02 | Duplicate or late event | Revision 1 follows revision 2 and EVT1200 is replayed. | Deduplicate and prevent stale overwrite; reconcile the intended state with the target owner. |
| OCN-XL-HR12-T03 | Bad schema and replay | Payload lacks employment ID and a support user requests bulk replay. | Quarantine the event, repair under change control and require authorized bounded replay with reconciliation. |

Record initial decision → expected result → observed paper result → evidence → revision. All observed-result fields start empty. Acceptance requires a reasoned card and all three reviewed results after revisions. A material authority or privacy bypass requires redesign. Publishing the exercise does not execute it or prove operational outcomes.

| New educational ID | Purpose | Existing connection | Evidence status |
|---|---|---|---|
| OCN-XL-HR12-REQ01 | Trace the business need to ownership and human authority. | OCN-M09 / OCN-M11 / OCN-M18; existing HR source | Card decision; T01–T02 |
| OCN-XL-HR12-ADR01 | Proposed option with alternative, trade-off and escalation. | OCN-M12 / OCN-M17; new learning decision | Card design; T02–T03 |
| OCN-XL-HR12-EXP01 | One synthetic experiment; no live system execution. | OCN-M19; new learning experiment | One card; T01–T03 |
| OCN-XL-HR12-MEAS01 | Every receiving owner confirms intended state or an explicit exception; no integration execution claimed. | OCN-M18 / OCN-M19; new acceptance criterion | Planned measure, unmeasured |
| OCN-XL-HR12-EV01 | Observed evidence and learner revisions. | New evidence slot | Unfilled until the learner runs the tabletop |

## AI driven curiosity and the next chapter

| Scenario window | Exploration |
|---|---|
| 2026–2030 — Assist | Explain interface exceptions |
| 2031–2040 — Connect | Connect policy-bounded recovery workflows |
| 2041–2050 — Adapt | Adapt mappings under versioned human review |

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. The time bands support curiosity about possible designs.

**Competing future:** fragmented rules, weak interoperability or low trust keep local expert judgment and simpler manual workflows more effective than connected AI. Compare that path with the scenario before choosing an experiment.

**Question that could disprove your hypothesis:** Would automated replay increase stale overwrites or silently grant privileges?

**Reflect:** What evidence changed your first choice? Who can challenge the decision? What would make the alternative better?

| Next level | Continuation of this same story |
|---|---|
| Pre-Foundation | Specify one lifecycle contract, target responsibilities, idempotency, version rules and support ownership. |
| Foundation | Model the workflow and data contract with owners and acceptance criteria. |
| Essentials | Build a bounded prototype and collect actual test evidence. |
| Advanced | Investigate exceptions, privacy, failure recovery and competing design choices. |
| Ultimate | Conclude at architect level with value realization, costs, ROI assumptions, troubleshooting and lessons learned. No ROI is achieved merely by completing a lesson. |

Only the Origin Story uses the 120-minute Sprint format in this edition. The later-level descriptions are handoffs and design intent, not claims of completed deeper learning editions.

## Sources and architecture learning

[Supporting source 1](https://app.notion.com/p/3d0ce6de6089813684e8ec2a8d854848)

[Enterprise workforce blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/derived-streams/01-workforce.md) · [Fictional persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/personas/persona-cards.md) · [Architecture anchors](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/master/theme-c-architecture.md) · [Execution anchors](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/master/theme-e-execution.md) · [Unresolved source gaps](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/references/source-and-assumptions.md)

[NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — Which risk, evidence and human oversight boundary should your proposed assistant preserve?

[W3C WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/) — Can the worker understand and complete the journey with an accessible alternative? These are selective learning references, not a compliance assessment.

Educational alignment: TOGAF supports architecture options and decisions; BIZBOK connects capabilities to value; BABOK connects needs and acceptance; DAMA-DMBOK supports ownership, quality and lineage; COBIT supports accountability and controls; relevant ISO/IEC security and quality principles support least privilege, controlled change and evidence. No certification or compliance is claimed. HR01–HR12 themes, the twelve architecture streams and the seven enterprise transformation streams are separate classification axes. Cross-reference them without treating them as interchangeable.

Source gaps retained: OCN-Q04 keeps 30% activation and 25% fulfillment targets distinct; OCN-Q10 distinguishes subscriptions from unique people; OCN-Q12 preserves unvalidated autonomy; OCN-Q14 distinguishes child-page presence from implementation evidence. HR-specific baselines, delegated approvers, rule versions and readiness criteria require discovery. 

Edition 1 November 2026 IST. Saved content is not evidence of automatic synchronization, public student access, executed tabletop tests or achieved business outcomes.

## Matching companions

[Google Doc](https://docs.google.com/document/d/1EHqOEJ8YyFFVvb6SuuHUH-iWKgJ7RhW5m8mBNHXZZzQ/edit?usp=drivesdk) · [Google Slides](https://docs.google.com/presentation/d/1gs71fxprATUBxEdGxsgOhIkfN0rD47T0KfmTJ_6XSUY/edit?usp=drivesdk) · [Google Sheet build card](https://docs.google.com/spreadsheets/d/1EgkMRCUCD16oJbZm8YDq8LAIfOgYcDMCT2HzP4hnpnE/edit?usp=drivesdk)
