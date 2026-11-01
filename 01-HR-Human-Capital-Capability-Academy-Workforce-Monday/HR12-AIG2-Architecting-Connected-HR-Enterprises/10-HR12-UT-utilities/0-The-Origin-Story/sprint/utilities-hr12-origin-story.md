# Message delivered. Access still unconfirmed.

HR12 — Connected HR Enterprises

SuccessLabs Academy · GICS10 Utilities · OmniGrid Utilities Ltd. · IIL — Industry Immersion Lab

## One learner promise

Design a recoverable workforce event handoff that distinguishes transport receipt from business completion. In 120 minutes, complete one Connected Workforce Handoff Build Card and exactly three tabletop tests. All work uses synthetic data; no tenant configuration or live utility action is required.

## Read the case accurately

OmniGrid is a fictional utility. The existing case stipulates 38,000 staff across 17 countries, covering generation, networks, retail energy and water services. These are fictional source baselines, not verified real-world facts. Existing persona names and IDs below are preserved. This incident, records and choices are newly introduced educational material. The source case owns enterprise facts; its success measures are targets, not achieved results. The 20% versus 30% restoration targets, metric populations, and USD970M investment / USD360M annual-value assumptions remain unresolved in the source register. No site counts, country laws, payroll rates or operational authority are invented.

## Origins and process evolution

| Teaching window | Typical administrative response | Question carried forward |
|---|---|---|
| 1970–1984 | Paper handoffs and payroll files | Who owns the record? |
| 1985–1994 | Batch interfaces | Which identity and period apply? |
| 1995–2004 | Shared HR objects and middleware | Who may approve the change? |
| 2005–2014 | APIs, events and monitored workflows | Did the receiving owner confirm the outcome? |
| 2015–2025 | Assisted exception handling with controlled recovery | What evidence and authority bound assistance? |

These closed windows are educational groupings, not universal invention dates or OmniGrid’s corporate biography. Adoption overlaps: paper, databases, ERP, cloud and older practices can coexist through the present. Digitizing an incomplete record does not make it reliable.

## One persona-led story

Sofia Tan (OGU-P06), Chief Digital and Information Officer works with Omar Haddad (OGU-P10), CISO and OT Resilience Lead.

A synthetic field assignment ends, while the worker remains employed in a different role. Sofia’s integration monitor reports success after sending the event. Omar cannot confirm whether the old site access was removed. Sending a termination instead would corrupt employment and payroll. The handoff must carry the right business meaning and expose target outcomes.

Choose before the reveal: Treat transport success as closure, terminate employment to force access removal, or separate assignment end, employment state and target confirmation? Write your first answer on the card.

Evidence reveal: The event is an assignment-end change, and one target is offline. A duplicate and an older event arrive later. Sofia requires event identity, version ordering, target reconciliation and a controlled replay. Omar owns the access exception and applies the approved containment process. HR cannot assert that access has been removed until the target confirms it.

Counterexample: Exactly one successful transport response can still leave a rejected, stale or unapplied business change.

Revise the answer on the same card. What changed, what remains unknown and whose decision is protected? The proposed response is open to challenge when learners provide better evidence.

## Application responsibility, data ownership and decision rights

| Application responsibility | Accountable owner | Human decision and boundary |
|---|---|---|
| Core HR | HR data owner | Owns employment and assignment semantics; assignment end does not imply employment termination. |
| Integration | Integration service owner | Owns transport, mapping, observability and replay; Integration Suite/BTP are source examples. |
| IAM / field / payroll targets | Target business owners | Confirm application and reconcile exceptions; security owns access containment and local work authority remains separate. |

Business owners define policy and authoritative facts; software stores or processes them. Detailed health, pay and candidate data stay outside the shared card unless necessary and authorized. Local delegations, jurisdiction and operational procedures need discovery. AI may draft a reminder or flag an inconsistency within permission; it cannot approve hiring, ratings, pay, work or access. HR, learning, IAM and utility operational systems retain distinct responsibilities.

## The exact 120-minute Origin Story

| Minutes | Activity on the same card |
|---|---|
| 0–10 | Understand the promise and people problem |
| 10–30 | Explore history and its unfinished question |
| 30–45 | Choose, reveal evidence and revise |
| 45–60 | Map application, data and human authority |
| 60–90 | Build the single card and compare an alternative |
| 90–110 | Walk through exactly three tabletop tests |
| 110–120 | Explain the decision and Pre-Foundation question |

Resource lookups fit within the activities. No extra deliverable is required. Publishing the lesson does not execute these activities.

## One synthetic build experiment

Connected Workforce Handoff Build Card.

Synthetic inputs: UT-EVT1200, person UT-P1200, active employment, ending assignment A1200, event version 2, duplicate v2, late v1 and unavailable access target.

| Single build card | Complete once |
|---|---|
| Purpose and evolution | State the people problem, one lasting historical lesson and the decision being supported. |
| Design 1 | Business event, authoritative object owner and effective time |
| Design 2 | Event identity, correlation, schema and minimum consumer data |
| Design 3 | Per-target received/applied/rejected/unknown states |
| Design 4 | Idempotency, ordering, controlled replay and accountable containment |
| Choice and counterexample | Record the initial choice, an alternative, the evidence reveal, the revised decision and a reason to reject your preferred design. |
| Exception and recovery | Name the accountable role, worker notification, escalation, approved fallback and the condition for reconciliation. Missing connectivity or evidence grants no additional authority. |
| Privacy and local variation | Record minimum data, purpose, permitted viewers, retention question and one justified local variant. Offer a route without a personal device. |
| Tests and learning evidence | For T01–T03 record input → expected → observed → evidence → revision. Leave observations unfilled until the exercise is actually performed. |

Learning acceptance: one defensible card, three observed tabletop records after any revision, and a 60-second explanation of owners, dates/states and human authority. A protected-decision bypass requires redesign. Completeness alone does not prove correctness.

## Exactly three tabletop tests

| Test | Proposed expected result | Record evidence; observations initially blank |
|---|---|---|
| OGU-EDU-HR12-T01 — Target unavailable | Keep business application unknown, name the exception owner and invoke approved containment without claiming deprovisioning. | Per-target status and escalation; observed result and revision to be recorded by learner. |
| OGU-EDU-HR12-T02 — Duplicate and late event | Apply a defined idempotency/version rule without reverting to stale state. | Event ledger and target comparison; observed result and revision to be recorded by learner. |
| OGU-EDU-HR12-T03 — Bad schema and replay | Quarantine invalid input, repair under change control and reconcile before replay/closure. | Schema error, authorized correction and confirmed target state; observed result and revision to be recorded by learner. |

These are planned learning tests, not executed system, security, operational-safety or legal validations. Publication creates no pass results.

## Traceability and measures

| New educational ID | Meaning | Existing connection / evidence state |
|---|---|---|
| OGU-EDU-HR12-REQ01 | Support the theme-specific decision without crossing human authority | OGU-M18 workforce/adoption; existing HR12 source case |
| OGU-EDU-HR12-REQ02 | Keep source identity, evidence and business-completion state explicit | OGU-M17 risk/security; OGU-M19 execution/readiness |
| OGU-EDU-HR12-ADR01 | Prefer explicit ownership and conditional state over inferred completion; learner may reject with evidence | Options, counterexample and revised choice on the card |
| OGU-EDU-HR12-EXP01 | Run one synthetic card exercise | T01–T03; planned and unexecuted |
| OGU-EDU-HR12-M01 | Confirmed target business applications / expected target applications; transport success is reported separately. | Definition and baseline to be confirmed; no operational results |
| OGU-EDU-HR12-EV01 | Capture input, expected, observed, evidence and revision | Unfilled until learners perform the exercise |

All OGU-EDU-HR12 identifiers are new educational IDs, not pre-existing approved client requirements. Existing OGU-M17, OGU-M18 and OGU-M19 anchors and OGU-P persona IDs remain unchanged. Match each test to REQ01/REQ02, record the ADR01 trade-off and store observations under EV01. Measure learning evidence separately from utility reliability, cost and sustainability outcomes.

## AI-driven exploration: scenarios, not predictions

| Scenario window | Possibility to investigate | Question or boundary |
|---|---|---|
| 2026–2030 — Assist | An assistant flags missing or inconsistent HR12 evidence. | Can it explain the gap using current, authorized sources? |
| 2031–2040 — Connect | Governed services exchange relevant evidence across owners. | Does each target confirm the right business state without excess personal data? |
| 2041–2050 — Adapt | A system proposes revised workflows as utility roles and conditions change. | Can accountable people inspect, challenge, stop and reverse the proposal? |

These are scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps. Competing future: fragmented regional systems and local human coordination remain more workable than a broadly connected assistant because evidence, trust or connectivity are insufficient. Falsification question: in a comparison using the same synthetic cases, would the proposed assistance produce more unsupported decisions, privacy exposure or unresolved exceptions than a simpler governed process? If yes, revise or reject the hypothesis.

## Reflection and the continuing story

Which evidence changed your first choice? Which record could be accurate but irrelevant? How could a worker challenge the decision without a personal device?

| Learning stage | Continuation outside this Origin Story |
|---|---|
| Origin Story | Discover the dilemma and complete this 120-minute card. |
| Pre-Foundation | Define a canonical event contract, data minimization, failure semantics and target reconciliation. |
| Foundation | Establish the domain model, baseline, owners and controlled local variants. |
| Essentials | Build the smallest governed workflow and collect observed test evidence. |
| Advanced | Troubleshoot failures, integration boundaries and exceptions using the same story. |
| Ultimate | Close the story with value-realization evidence, costs, counterfactuals, limitations and lessons learned. ROI requires dated cash flows and attribution; do not turn proposals into results. |

These later-stage handoffs describe progression; they are not full authored or published later-stage courses. Sprint format applies only to the Origin Story edition. Deeper research and implementation material remain outside it.

## Official resources and standards lenses

Use a few resources with a question, rather than adding a vendor comparison catalogue.

R1 — ILO-OSH 2001: how should accountable ownership and worker participation shape the proposal? https://www.ilo.org/resource/guidelines-occupational-safety-and-health-management-systems-ilo-osh-2001

R2 — NIST AI Risk Management Framework: what evidence should bound assistance and escalation? https://www.nist.gov/itl/ai-risk-management-framework

R3 — W3C WCAG 2.2: which access barriers matter for field, shared-device and support journeys? https://www.w3.org/TR/WCAG22/

Educational alignment: TOGAF for architecture options and decisions; BIZBOK for capabilities and value streams; BABOK for needs and acceptance; DAMA-DMBOK for ownership, quality and lineage; COBIT for accountability and controls; relevant ISO/IEC principles for access control, managed change and evidence. This is conceptual alignment, not certification or compliance assurance.

Classification axes are separate: HR theme = HR12 Connected HR Enterprises; architecture streams = Enterprise, Business, Data, Application, Technology, AI, Security, UI/UX, Infrastructure, Integration, Domain and Industry views with distinct responsibilities; enterprise transformation stream = Workforce. A theme may use several architecture views without renaming the axes.

## Source and edition record

Edition 2026-11-01 IST. IIL — Industry Immersion Lab. Mission: Architecting Experiences for a Better World.

Supporting source cases, preserved separately from the matching sprint:

S1 — HR12 source case: https://app.notion.com/p/3d0ce6de608981cf904addab2798895b

Enterprise hub: https://app.notion.com/p/54586cda6f744a6f8e0d96f674a7ddb0

Persona source: https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/personas/persona-cards.md

Risk/workforce/readiness anchors: https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/master/theme-e-execution.md

Source and unresolved assumptions: https://github.com/nbnayak88/successlabs-case-studies/blob/main/10-utilities/omnigrid-utilities-ltd/references/source-and-assumptions.md

Reference pattern: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md

Stable planning reference: HUB-ORIGIN-HR12-UT-sprint (not an LMS ID). Community/Citizen Edition learning content. No live enrollment, certification, public companion access, successful copying, unattended synchronization, executed tests or achieved utility outcomes is implied.


## Companion workspace

GitHub matching sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR12-AIG2-Architecting-Connected-HR-Enterprises/10-HR12-UT-utilities/0-The-Origin-Story/sprint/utilities-hr12-origin-story.md

Google Doc matching edition: https://docs.google.com/document/d/1v3AehaF5fSsiVCahcoOW-PwBAPu9RnnAPdtqxIHKpxA/edit?usp=drivesdk

Google Slides teaching deck: https://docs.google.com/presentation/d/1HI8Mkz7LDFRaVM9pzOeXeA4moIGrKtFJG_A4qEaA4HU/edit?usp=drivesdk

Google Sheets build card: https://docs.google.com/spreadsheets/d/13ZOOTyME2xdJnhRO50zk-HbH65u1fn0u3bnTHLtlW48/edit?usp=drivesdk

Notion matching edition: https://app.notion.com/p/3d0ce6de608981cf904addab2798895b

Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/utilities-origin-stories.md
