# The payment timed out. Should payroll send it again?

HR07 — Autonomous Payroll Enterprises · GICS07 Financials · OmniCapital Financial Group Ltd.
IIL — Industry Immersion Lab · TOS — The Origin Story · 120-minute Sprint · Edition 2026-10-31
Mission: Architecting Experiences for a Better World.
Planning reference: HUB-ORIGIN-HR07-FIN-sprint (not an LMS ID). Published educational edition; no enrollment, certification or public access implied.

## 1. One learner promise

In 120 minutes: Design one payroll exception decision that protects payment continuity and prevents blind retries.
One persona-led story · One Decision Build Card · Exactly three tabletop tests. Use only synthetic data; no tenant or production action is required.

## 2. Source boundaries

OmniCapital is a fictional financial-services enterprise spanning banking, insurance, wealth, payments and markets across 32 countries. Source figures describe a fictional case, proposed targets or assumptions, not verified operational results. Existing OCF persona and master IDs retain their meanings. This incident, synthetic worker IDs, dialogue, proposed controls and OCF-HR07 IDs are new educational additions.

The existing Employee Central Doc states 100K+ employees while OCF-Q11 says staff counts are unspecified: unresolved scope/baseline conflict. The Doc's benefit rows total 81.9M but its summary states 81.0M; listed implementation components including contingency sum to 60M against a stated 55M; its 287% ROI is not supported by the displayed 81M benefits and 63M total costs. Timing and cash flows do not establish NPV, IRR or payback. Keep original research intact and do not use these figures as validated returns. Enterprise OCF-Q04 retains 35% automation versus 30% Year 3; OCF-Q05 retains distinct 90% digital completion and 70% self-service without assuming equivalent denominators. Product comparisons, localization coverage and success checkmarks in supporting material are unverified proposals, not evidence of achieved capability.

## 3. Origins and process evolution

These closed windows are educational groupings, not universal invention dates or OmniCapital corporate biography. Adoption overlaps; paper, spreadsheets, ERP and cloud practices can coexist through the present.

| Teaching window | Process response and persistent question |
|---|---|
| 1970–1984 | Wage registers and manual bank instructions rely on separate approvals. |
| 1985–1994 | Computerized payroll speeds calculation; payment confirmation remains separate. |
| 1995–2004 | ERP payroll links accounting; retroactivity and reconciliation still matter. |
| 2005–2014 | Self-service and electronic banking improve delivery but create interface uncertainty. |
| 2015–2025 | Cloud payroll controls highlight exceptions; settlement and jurisdictional rules need evidence. |

Counterexample: digitizing an incomplete record makes it easier to retrieve, not more trustworthy. Which decision was the original record intended to support?

## 4. One persona-led story

Ravi Patel (OCF-P14), Payments and Treasury Operations Lead, sees a synthetic payroll batch time out near cut-off. David Morgan (OCF-P02), Group CFO, wants employees paid on time. Nadia Fernandes (OCF-P07), Group CHRO, also receives an approved late allowance correction. Nobody yet knows whether the bank accepted the first batch.

Choose before revealing: Resend immediately, stop every employee payment, or reconcile payment state and isolate the correction under approved procedures? Record your first reason on the card.

Evidence reveal: The synthetic transport timed out after transmission; no bank outcome is confirmed. The allowance correction has an approval but belongs to a separately reviewed period. Ravi retains the batch identity and asks the authorized payment owner to reconcile status; David does not treat a timeout as rejection.

Revise your decision: Calculated payroll, approved payroll, transmitted payment and confirmed settlement are different states. Autonomy can flag exceptions; it does not remove maker-checker controls or local statutory review. Preserve an accessible human route to challenge errors. Financial service continuity matters, but an urgent cut-off does not create authority. Customer KYC and employee readiness are different processes; do not copy customer identity checks into HR without purpose and policy review.

## 5. Application responsibilities and human authority

Frame the business need first; applications implement the chosen operating model. The following is a proposed teaching architecture. Confirm named delegates, country policy, legal basis and actual product scope before implementation.

| Application responsibility | Accountable data owner | Human decision right |
|---|---|---|
| Payroll; Employee Central Payroll example | Payroll owner maintains calculation, period, retroactivity and reconciliation records | Authorized payroll approver releases a reconciled run; local specialists validate country rules. |
| Reward and time inputs | Reward/Time owners own approved source components and effective dates | Source approvers authorize corrections; Payroll decides processing under approved policy. |
| Banking and finance outputs | Payment owner owns bank status; Finance owns posting and funding evidence | Maker-checker payment approvers authorize retry only after state reconciliation. |

Core HR owns workforce facts; domain owners own performance, learning, rewards, time or payroll facts as applicable. IAM executes access policy; integration transports and reconciles states; analytics reads authorized data and does not become its owner. AI may summarize permitted evidence or draft a reminder, but cannot approve consequential employment, regulated duties, payments or access. An interface acknowledgment is not proof of the business outcome. SAP examples illustrate responsibilities, not guaranteed features or universal localization.

## 6. The 120-minute learning experience

| Minutes | Activity on the same card |
|---|---|
| 0–10 | Frame the promise, business need and affected person. |
| 10–25 | Explore historical windows and one enduring problem. |
| 25–45 | Choose, reveal evidence and revise the story decision. |
| 45–65 | Build the card; assign data ownership and human rights. |
| 65–100 | Run T01, T02 and T03 as tabletop discussions; record observations and revisions. |
| 100–110 | Challenge the future hypothesis and competing future. |
| 110–120 | Reflect, explain the design in 60 seconds and prepare the next level. |

## 7. One Decision Build Card

Synthetic input: Batch FIN-PAY700; approved net total 1,000,000 fictional units; bank outcome unknown; correction COR700 approved for 100 units but period treatment unresolved; no actual bank instruction.

Keep all work in this one card. Capture: business problem; initial and revised choice with reason; entity/identity/date semantics; authoritative source and accountable owner; human approval boundary; one justified local variant with purpose/minimum data/viewers; known versus unknown downstream state; exception owner and approved fallback; all three test observations and evidence references. Missing evidence stays blank or unknown, never silently becomes approval.

Compare one alternative: a manual controlled handoff may be preferable to automation when exception ownership or recovery is absent. State the evidence needed to change your mind. Avoid collecting real screening, health, payroll, customer or conduct records in this learning card.

## 8. Exactly three tabletop tests

| Test | Input / reveal | Expected proposed behavior | Evidence to record |
|---|---|---|---|
| OCF-HR07-T01 — Late correction | Approved allowance arrives after payroll input freeze. | Determine valid period and adjustment route; do not silently rewrite an approved run. | Approval, dates, affected component and controlled adjustment decision. |
| OCF-HR07-T02 — Unknown bank outcome | Transmission times out after the request was sent. | Do not blindly resend; retain batch identity and reconcile bank status before approved recovery. | Correlation ID, known/unknown state, owner and no-duplicate condition. |
| OCF-HR07-T03 — Output mismatch | Approved payroll net total is 1,000,000; proposed bank file totals 999,900. | Hold the discrepant output for reconciliation under continuity procedures; do not declare payment complete. | Control totals, difference, exception owner and release evidence. |

For each test, record input → expected → observed → revision/evidence → Pass, Revise or Blocked. All observed results are initially unfilled. Publication does not execute any tabletop, system test, approval or operational transaction. Acceptance requires a defensible card and all three observed tabletop results with revisions; bypassing a protected human decision requires redesign.

## 9. Traceability and learning measures

Existing anchors: OCF-M17 (risk/security), OCF-M18 (workforce/adoption), OCF-M19 (delivery readiness), OCF-M10 (value/process) and OCF-M11 (operating model). The workforce blueprint remains supporting research. The following are newly introduced educational IDs, not approved client requirements.

| New educational ID | Connection | Evidence / status |
|---|---|---|
| OCF-HR07-REQ01 | OCF-M18 → preserve correct domain facts and accountable readiness | T01; planned acceptance, no achieved result |
| OCF-HR07-REQ02 | OCF-M17/M19 → retain human authority and recoverable exceptions | T02/T03; planned controls |
| OCF-HR07-ADR01 | OCF-M11 → bounded automation with explicit domain ownership | Compare manual and automated alternatives; learner may reject with evidence |
| OCF-HR07-EXP01 | OCF-M19 → one synthetic decision-card experiment | Exactly T01–T03; unexecuted |
| OCF-HR07-M01 | OCF-M18 → learning measure | Record control-total discrepancies, unauthorized retries and unresolved payment states in the tabletop; no actual payroll run, settlement or savings is claimed. |
| OCF-HR07-EV01 | OCF-HR07-EXP01 → observation and revision evidence | Unfilled until learner records actual tabletop observations |

## 10. Separate AI-driven exploration: 2026–2050

Scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps.

| Scenario window | Question to explore |
|---|---|
| 2026–2030 — Assist | Could approved-source assistance explain evidence gaps and draft next steps without approving the decision? |
| 2031–2040 — Connect | Could separately authorized services coordinate this handoff while keeping unknown states and local rights visible? |
| 2041–2050 — Adapt | Could reviewed feedback propose reversible process changes while people retain consequential authority? |

Competing future: fragmented systems, uneven access, policy restrictions and manual review persist; a simpler controlled workflow outperforms orchestration. Falsifiable hypothesis question: Would automated retries improve payroll reliability when bank acceptance is unknown? Define an observation that would disprove your claim—for example fewer steps but more unresolved exceptions or worse worker outcomes. Compare against a manual baseline before claiming value.

## 11. Reflect and move to Pre-Foundation

What evidence changed your first decision? Which authority did you initially assume? Who bears the exception burden? What would make you stop this design?
Pre-Foundation handoff: Define input period, calculation result, approval, payment batch, bank status and posting. Draw the permitted correction and retry states.
Continue the same semi-fiction through Pre-Foundation (concepts/data), Foundation (small working model), Essentials (end-to-end handoffs), Advanced (exceptions and resilience), and Ultimate (architect-level value realization, troubleshooting, lessons and evidence-based ROI). These are future learning handoffs, not published deeper editions or additional Origin Story formats.

## 12. Architecture alignment and separate axes

TOGAF: compare architecture options and document decisions. BIZBOK: connect capability and value. BABOK: identify needs, requirements and acceptance evidence. DAMA-DMBOK: assign ownership, definitions, quality and lineage. COBIT: distinguish accountability, controls and monitoring. Relevant ISO/IEC information-security principles: confidentiality, integrity, availability, access and controlled change. Alignment is educational; no certification, conformance or compliance is claimed.

HR classification = HR07 Autonomous Payroll Enterprises. Architecture classification = the 12 distinct streams (Enterprise, Business, Data, Application, Technology, AI, Security, UI-UX, Infrastructure, Integration, Domain, Industry), applied selectively. Enterprise transformation classification = Workforce. These axes relate but are not interchangeable.

## 13. A few official resources

- SAP Help Portal — Employee Central: https://help.sap.com/docs/successfactors-employee-central — Ask which workforce object owns a fact and what separate evidence proves downstream authorization. Other SAP examples remain conceptual until their product documentation is reviewed.
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework — Ask who owns risk, which evidence supports use and when to stop assistance.
- ISO/IEC 27001 overview: https://www.iso.org/standard/27001 — Apply confidentiality, integrity and availability questions; reading the overview does not establish conformance.

## 14. Source and edition record

S1 — Existing HR07 source case: https://app.notion.com/p/d617cfaddf154d7786e850f3719d3b84

Enterprise hub: https://app.notion.com/p/ad26929126a047afa591f9c7d75cbab9
Workforce scope: https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/derived-streams/01-workforce.md
Existing personas: https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/personas/persona-cards.md
Master risk/workforce/readiness: https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/master/theme-e-execution.md
Source/conflict register: https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/references/source-and-assumptions.md
Supporting EC business case: https://docs.google.com/document/d/1KUqAVQUQnyzlP-1mA8JjhFAWbhqzBAhrhJp6xq4-JII
GICS02 format reference: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md

Source review: 31 October 2026 IST. Preserve supporting case bodies and stable source identities. This edition adds an Origin Story section rather than replacing deeper research. HR02a and HR02b remain separate source cases connected within one HR02 120-minute sprint.

## Companion workspace

GitHub matching sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR07-APE7-Architecting-Autonomous-Payroll-Enterprises/07-HR07-FIN-financials/0-The-Origin-Story/sprint/financials-payroll-evolution-sprint.md
Notion matching edition: https://app.notion.com/p/d617cfaddf154d7786e850f3719d3b84
Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/financials-origin-stories.md
Google Doc, slide and sheet links are recorded in the sector index after completed saves and readback. Slides are facilitator companions; the Sheet is the build-card workspace. No automatic synchronization, public student access, successful copying, executed tests or realized operational benefits are implied.
