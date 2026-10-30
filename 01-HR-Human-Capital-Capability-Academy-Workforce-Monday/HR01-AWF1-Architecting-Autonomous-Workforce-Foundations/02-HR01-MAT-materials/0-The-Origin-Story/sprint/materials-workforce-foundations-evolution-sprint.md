# A transfer is more than a new location

A two-hour Origin Story sprint: Architecting Autonomous Workforce Foundations

SuccessLabs Academy · HR01-AWF1 · GICS02 Materials · OmniForge Materials Ltd. · Level 0 → Pre-Foundation

IIL — Industry Immersion Lab · Format: Sprint · Edition: 2026-10-31

Mission: Architecting Experiences for a Better World.

Planning reference: HUB-ORIGIN-HR01-MAT-sprint (not an LMS ID). Community/Citizen Edition. Published learning content; no live course, enrollment, certification or public companion access is implied.

## 1. One promise

In 120 minutes, design and explain one trusted workforce transfer that preserves employment history and keeps restricted-work authorization explicit.

One persona-led story · One Workforce Evolution Build Card · Three tabletop tests. Use synthetic records; no tenant configuration is required. All notes and test evidence belong on the same card.

## 2. Read the case accurately

OmniForge is fictional. Its enterprise case stipulates 46,000 employees plus contractors across materials operations. Contractor numbers, device access and comparable site populations remain unconfirmed. The source counts for production sites, mines/quarries and cement plants may overlap; do not add them.

The enterprise case owns company facts. Existing persona IDs are preserved. The transfer incident, worker identifiers, dialogue and design controls below are new illustrative learning material, not historical events or an approved deployed architecture. Financial, operational and sustainability figures in the deeper case remain fictional baselines, proposals or targets.

## 3. From 1970 to the present: why the foundation exists

These overlapping periods are teaching lenses, not universal adoption dates or OmniForge corporate history. Paper, spreadsheets, ERP and cloud can coexist. Each new medium carries forward an old question.

| Period / lens | Application response | Unfinished question |
|---|---|---|
| 1970s–1990s: record the worker | Personnel files, wage registers, local rosters and early computing | Who is this person, and is the assignment current? |
| 1980s–2000s: administer employment | Personnel databases and computerized payroll | Do separate records describe the same person and employment? |
| 1990s–2010s: coordinate transactions | HRIS/ERP, position structures and workflow | When does a change become valid, and who approved it? |
| 2000s–present: connect services | Cloud HCM, self-service, learning and access services | Which source owns each fact, and who may use it? |
| 2020s–present: assist decisions | Rules and AI-supported checks | Is the evidence current, and is the action authorized? |

Counterexample: replacing a paper roster with an app improves availability, but does not prove the roster is correct. Ask which decision each record exists to support.

## 4. One story: Nikhil's night-shift question

Nikhil Sen (OMF-P16), Shift Supervisor and Workforce Representative, receives a future roster for a synthetic quarry-to-cement-plant transfer. The employee will support a team working with recovered feedstock. The same legal employer is assumed solely for this experiment; a real case must verify it.

The core HR record shows active employment. A learning record shows a course completion. The receiving site's restricted-task authorization is missing. Nikhil asks: “Which record tells me what this person can do on the receiving shift?”

Elena Petrova (OMF-P07), Cement Plant Director, needs reliable staffing while protecting kiln stability. Arjun Mehta (OMF-P05), Group CHRO, wants development opportunities that preserve workforce history and remain usable for people without personal devices.

Choose first: hold the whole transfer, release everything, or separate the employment change from restricted-work permission. Write your reason before reading the new evidence.

New evidence: the HR transfer is approved, the employee has not changed legal employer, and restricted-task authorization is still absent. Under the proposed policy, the employment change may take effect on its approved date while the restricted task remains held. Nikhil revises his initial blanket hold and requests a safe alternative assignment through the designated site authority.

He does not invent authorization, assume that a badge proves competence, or change pay because a course record is incomplete. An accessible notification and a human escalation route help the worker understand and challenge errors. Operational need cannot silently turn missing evidence into permission.

Materials connection: circular production changes feedstock, roles and skill needs. A successful personnel transfer alone proves neither safe operation nor lower emissions; those require their own evidence.

## 5. Application responsibility, data ownership and decision rights

This is the proposed learning architecture. The accountable business owner defines the authoritative record and access policy; the application stores or processes it. Names of delegated HR approvers and site safety authorities must be established before real use.

| Application responsibility | Accountable data / process owner | Human authority and boundary |
|---|---|---|
| Core HR; Employee Central as an example | HR owns person/employment/job facts and organization/position structures | Delegated HR/management approvers authorize the employment transaction; the CHRO sponsors the model, not every transaction. |
| Learning and competence evidence | Learning owner and designated assessors own relevant completion, assessment and validity evidence | Course completion alone does not authorize restricted work. |
| Site safety / work authorization | Designated site safety and operational owners own task-specific authorization and conditions | Authorized site personnel grant or withhold restricted work. Plant leadership cannot bypass required specialist approval. |
| IAM and physical access | Security owns identity/access records and provisioning under approved policy | Access is granted within policy; an account or badge is not competence or work authorization. |
| Payroll — HR07; Time — HR08 | Payroll owns pay processing/reconciliation; Time owns approved time/absence inputs | Downstream owners confirm business outcomes; an HR screen does not prove receipt or correct payment. |

SAP precision: person, employment and assignment identifiers serve different purposes. Job Information is effective-dated; Employment Information is not an effective-dated entity. Define date semantics per object rather than assuming every EC object keeps effective-dated history. An event reason explains why a transaction occurred; it is not an approval, effective date or receiving-system acknowledgment. Consult R1–R2.

Automation boundary: allow an authorized assistant to flag missing evidence or draft a reminder. It cannot approve this transfer, authorize restricted work, grant access or declare downstream completion. HR11 deepens AI controls; HR12 deepens event delivery and recovery.

## 6. Your exact 120-minute sprint

| Minutes | Activity on the same card |
|---|---|
| 0–10 | Read the promise and story setup; state the people and operational need. |
| 10–30 | Reconstruct the evolution lenses; identify one problem that survives digitization. |
| 30–45 | Choose an initial response, reveal the new evidence and revise your decision. |
| 45–60 | Assign application responsibilities, data owners and human decision rights. |
| 60–90 | Complete the transfer build card; compare one alternative and one local variant. |
| 90–110 | Run the three tabletop tests; record observed paper results and revisions. |
| 110–120 | Give a 60-second explanation; reflect and identify the Pre-Foundation question. |

Resource lookups are selective within these activities, not additional homework. Use one card throughout; no extra deliverable is required.

## 7. One build experiment: a future-dated transfer

Synthetic inputs: person MAT-P100; employment MAT-E100; worker label MAT-W100; positions QUARRY-OP and PLANT-OP; locations QUARRY-A and CEMENT-A. These are teaching labels, not prescribed SAP field mappings. The approved same-employer transfer is effective 1 November 2026; the entry date is 31 October 2026. Site restricted-task authorization is absent. Real plant, task, timezone, shift boundary and delegated authority remain to be defined.

| Workforce Evolution Build Card | Complete once |
|---|---|
| Purpose and history | State the employee opportunity, operational need and one enduring lesson from the timeline. |
| Identity and transaction | Preserve MAT-P100/MAT-E100 under the stated same-employer assumption; identify evidence that would require another transaction. |
| Time | Record entry, approval and effective dates; show the 31 October and 1 November job views. Do not infer retroactive pay treatment. |
| Owners and authority | Map HR, Learning, Site safety, IAM, Payroll and Time. Name the roles that can approve each decision; flag unfilled delegations. |
| Decision and alternative | Explain what proceeds, what remains held and why. Compare one alternative. Choose a common core with justified local variants, or defend another approach. |
| Local variant and privacy | Choose one site-specific readiness field; state its purpose, owner, minimum data, permitted viewers and evidence needed. Keep detailed health information out of the general card. |
| Exception and recovery | Record missing authorization or downstream confirmation, an accountable exception role, accessible notice and site-approved fallback. Connectivity failure grants no extra authority. |
| Automation | One permitted low-risk task, one protected human decision and the escalation route. |
| Tests, measures and evidence | For T01–T03 record input → expected → observed tabletop result → evidence note → pass/revise. Measure completeness and state uncertainty. |

## 8. Three tabletop tests

| Test | Expected result in this proposed design | Evidence to record |
|---|---|---|
| OMF-HR01-T01 — Before/on effective date | 31 October retains the quarry job view; 1 November shows the approved plant job. Person/employment identity and prior history remain intact. Restricted-task status stays separate. | Both dated views; approval reference; observed result and any revision. |
| OMF-HR01-T02 — Completion without authorization | A completed course does not release the restricted task. No assistant or badge overrides the hold. Request the designated site authority's decision and an authorized alternative assignment. | Missing authorization, exception owner, worker notice and observed paper decision. |
| OMF-HR01-T03 — Receiving-site outage | The approved HR transaction and unconfirmed downstream outcomes remain separately visible. Do not declare full completion or grant new work/access authority. Invoke the site's approved reconciliation/fallback route; if none exists, escalate and keep the affected action held. | Per-system status, escalation, fallback gap, reconciliation condition and observed result. |

Acceptance: one complete card, all three tabletop results after revisions, and a 60-second explanation covering identity, dates, ownership and decision rights. A restricted-work bypass requires redesign. No tests have been executed by publishing this lesson; learner evidence remains empty until observed.

## 9. Traceability: extend the case without inventing results

Existing anchors OMF-M17 (risk/security), OMF-M18 (workforce/adoption) and OMF-M19 (readiness/execution) come from the enterprise master. The following HR01 IDs are newly established educational design anchors in this sprint, not pre-existing approved enterprise requirements.

| Learning anchor | Source connection | Card evidence / status |
|---|---|---|
| OMF-HR01-REQ01 — Preserve identity and time | OMF-M18; workforce blueprint | Approved change and dated views; assessed by T01. |
| OMF-HR01-REQ02 — Separate authorization and completion | OMF-M17 / OMF-M19 | Readiness hold and receiving-system exceptions; assessed by T02–T03. |
| OMF-HR01-ADR01 — Govern a common core with justified local variants | OMF-M18 / OMF-M19; illustrative design choice | Option, alternative, trade-off, owner and missing evidence. Learner may reject with reasons. |
| OMF-HR01-EXP01 — Synthetic transfer experiment | OMF-M19; new HR01 application | One card and T01–T03. Planned tabletop exercise; no tenant or live operational validation. |
| OMF-HR01-M01 — Card completeness | OMF-M18; learning measure only | Completed mandatory card sections / 9 × 100; blank results remain blank, not zero or success. A complete card can still be wrong. |
| OMF-HR01-M02 — Authorization boundary | OMF-M17; learning acceptance criterion | Record whether T02 preserved the hold and why. A paper result is not a measured plant safety outcome. |
| OMF-HR01-EV01 — Evidence slot | OMF-HR01-EXP01 | Initially unfilled. Store observed tabletop results, revisions and reviewer questions; no achieved benefits claimed. |

## 10. Future curiosity: 2035 and 2050

Scenarios, not predictions: in 2035 an assistant might flag missing readiness evidence before a transfer. In 2050 portable skills records might support movement across materials enterprises. Neither scene is a product promise or an achieved OmniForge state.

Counterexample: a portable certificate can be authentic yet irrelevant to the receiving plant's current task conditions. Choose one future capability worth experimenting with and one human decision right to retain. State what new evidence would make you revise the choice.

## 11. Official resources: read with a question

R1 — SAP: Managing events and event reasons. Why did the transaction occur, and what separate evidence proves approval? https://learning.sap.com/courses/sap-successfactors-employee-central-core-administration/managing-events-and-event-reasons

R2 — SAP: Introducing Person and Employment Objects. Distinguish person/employment identifiers and effective-dated from non-effective-dated objects. https://learning.sap.com/courses/sap-successfactors-employee-central-core-academy/using-special-hr-transactions-for-hires-and-terminations_e8c3ec4e-0435-4920-89ce-29ded46e87bf

R3 — ILO: Safety and Health in Mines Convention, 1995 (No. 176). What should worker information, training and participation change in your design? Use as an educational reference; applicability must be determined for a real jurisdiction. https://wwwex.ilo.org/dyn/f?p=NORMLEXPUB%3A12100%3A0%3A%3ANO%3A%3AP12100_INSTRUMENT_ID%3A312321

R4 — NIST AI Risk Management Framework. What evidence and authority should bound assistance? https://www.nist.gov/itl/ai-risk-management-framework

## 12. Reflection and Pre-Foundation handoff

What evidence changed your first answer? Which digitized record could still be wrong? How can a worker challenge it without a personal device?

Carry the same card into Pre-Foundation: define person, employment, organization, position and location relationships; confirm the transaction and data dictionary before configuration. Ask what you need to discover next rather than adding more technology.

Educational alignment: TOGAF — options and architecture decisions; BIZBOK — capabilities and value; BABOK — needs, requirements and acceptance criteria; DAMA-DMBOK — ownership, quality and lineage; COBIT — accountability and controls; relevant ISO/IEC principles — least privilege, controlled change and evidence. This is conceptual alignment, not certification, conformance assessment or compliance assurance.

Classification axes remain separate: HR theme = HR01 Workforce Foundations; architecture streams = cross-cutting Business, Data, Application, Security, Integration and other applicable views; enterprise transformation stream = Workforce. Their relationships are intentional; they are not interchangeable labels.

## Source and edition record

S01 — Enterprise hub: https://app.notion.com/p/9e83f25576814c87998709be3338092b

S02 — Existing workforce blueprint: https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/derived-streams/01-workforce.md

S03 — Existing persona cards: https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md

S04 — Master risk, workforce and readiness anchors: https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/master/theme-e-execution.md

S05 — Source/reconciliation register: https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/references/source-and-assumptions.md

S06 — Energy reference pattern: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR01-AWF1-Architecting-Autonomous-Workforce-Foundations/01-HR01-ENE-energy/0-The-Origin-Story/sprint/energy-workforce-foundations-evolution-sprint.md

Source snapshot: S02 blob a6d67c22756b243b76cf18536412a8a5f7b0bf45; S03 blob 864f5490b08a7102597a31b9212624ecacb11e75; S04 blob 33ff7a8a127eb95c97029847747c68324bf54e02; S05 blob 79872e6816fb8d2f03df94ffd846f2764e6fc743. Source and persona facts were reviewed on 31 October 2026 IST. The Notion HR01 body was blank before this edition.

Open enterprise issues remain in S05: overlapping site counts, benefit classifications, emissions boundaries and unvalidated target definitions. This sprint avoids using them as achieved results. Deeper research remains outside the Origin Story.

## Companion workspace

GitHub sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR01-AWF1-Architecting-Autonomous-Workforce-Foundations/02-HR01-MAT-materials/0-The-Origin-Story/sprint/materials-workforce-foundations-evolution-sprint.md

Google Doc: https://docs.google.com/document/d/14dv6HY-vLiGIq9EO8_kW9EdvrVPp4Zdofr73wxwq9wg/edit

Existing Notion HR01: https://app.notion.com/p/562c4dc0bf6c49148f3227d6779fd2b5

Materials HR01–HR12 index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md

Matching edition content is maintained through explicit publication and verification. No automatic synchronization, public student access or successful learner copying is claimed.
