# The event was delivered. The access change was not.

HR12 — Connected HR Enterprises · GICS07 Financials · OmniCapital Financial Group Ltd.
IIL — Industry Immersion Lab · TOS — The Origin Story · 120-minute Sprint · Edition 2026-10-31
Mission: Architecting Experiences for a Better World.
Planning reference: HUB-ORIGIN-HR12-FIN-sprint (not an LMS ID). Published educational edition; no enrollment, certification or public access implied.

## 1. One learner promise

In 120 minutes: Design one recoverable workforce handoff with explicit contracts, owners and outcome evidence.
One persona-led story · One Decision Build Card · Exactly three tabletop tests. Use only synthetic data; no tenant or production action is required.

## 2. Source boundaries

OmniCapital is a fictional financial-services enterprise spanning banking, insurance, wealth, payments and markets across 32 countries. Source figures describe a fictional case, proposed targets or assumptions, not verified operational results. Existing OCF persona and master IDs retain their meanings. This incident, synthetic worker IDs, dialogue, proposed controls and OCF-HR12 IDs are new educational additions.

The existing Employee Central Doc states 100K+ employees while OCF-Q11 says staff counts are unspecified: unresolved scope/baseline conflict. The Doc's benefit rows total 81.9M but its summary states 81.0M; listed implementation components including contingency sum to 60M against a stated 55M; its 287% ROI is not supported by the displayed 81M benefits and 63M total costs. Timing and cash flows do not establish NPV, IRR or payback. Keep original research intact and do not use these figures as validated returns. Enterprise OCF-Q04 retains 35% automation versus 30% Year 3; OCF-Q05 retains distinct 90% digital completion and 70% self-service without assuming equivalent denominators. Product comparisons, localization coverage and success checkmarks in supporting material are unverified proposals, not evidence of achieved capability.

## 3. Origins and process evolution

These closed windows are educational groupings, not universal invention dates or OmniCapital corporate biography. Adoption overlaps; paper, spreadsheets, ERP and cloud practices can coexist through the present.

| Teaching window | Process response and persistent question |
|---|---|
| 1970–1984 | Personnel forms and courier handoffs depend on manual confirmation. |
| 1985–1994 | Batch files connect payroll and HR but delay exception discovery. |
| 1995–2004 | Enterprise interfaces standardize mappings; transport errors still need owners. |
| 2005–2014 | APIs and shared integration platforms speed handoffs; target acceptance remains separate. |
| 2015–2025 | Events and monitoring distribute work; idempotency, ordering and reconciliation become essential. |

Counterexample: digitizing an incomplete record makes it easier to retrieve, not more trustworthy. Which decision was the original record intended to support?

## 4. One persona-led story

Daniel Weber (OCF-P12), Director Enterprise Architecture, reviews a synthetic transfer from branch support to payments control. Sofia Chen (OCF-P06), Chief Digital and Information Officer, sees a green integration dashboard. Omar Haddad (OCF-P10), CISO and Resilience Lead, finds the target rejected a required access change. Ravi Patel (OCF-P14), Payments and Treasury Operations Lead, needs a trustworthy cut-off decision.

Choose before revealing: Trust delivery status, resend every event, or reconcile source intent, target state and authorized recovery? Record your first reason on the card.

Evidence reveal: The broker accepted the synthetic event, but the target rejected an unknown role code. A duplicate older transfer then arrived. Daniel keeps transport and business completion separate; Sofia routes the mapping failure to its owner; Omar contains unauthorized access under approved policy rather than assuming a retry fixes it.

Revise your decision: A connected enterprise needs authoritative objects, state contracts, idempotency and business reconciliation. Delivery does not prove permission or successful target state. Preserve an accessible human route to challenge errors. Financial service continuity matters, but an urgent cut-off does not create authority. Customer KYC and employee readiness are different processes; do not copy customer identity checks into HR without purpose and policy review.

## 5. Application responsibilities and human authority

Frame the business need first; applications implement the chosen operating model. The following is a proposed teaching architecture. Confirm named delegates, country policy, legal basis and actual product scope before implementation.

| Application responsibility | Accountable data owner | Human decision right |
|---|---|---|
| Core HR and domain producers | HR owns approved workforce change and object/date semantics | Delegated HR authority approves employment transactions; producer emits only authorized facts. |
| Integration; Integration Suite/BTP examples | Integration owner maintains mapping, schema, delivery and error evidence | Platform operations follows approved retry/quarantine procedures; architecture owner approves contract changes. |
| IAM and target operations | Security owns target access state; receiving domain owns business acceptance | Authorized target owner confirms outcome and containment; no broker or AI approval substitutes for it. |

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

Synthetic input: Event FIN-EVT1200, person FIN-P1200, source version 2; target rejects role code; older version 1 arrives later; access outcome unconfirmed; synthetic records only.

Keep all work in this one card. Capture: business problem; initial and revised choice with reason; entity/identity/date semantics; authoritative source and accountable owner; human approval boundary; one justified local variant with purpose/minimum data/viewers; known versus unknown downstream state; exception owner and approved fallback; all three test observations and evidence references. Missing evidence stays blank or unknown, never silently becomes approval.

Compare one alternative: a manual controlled handoff may be preferable to automation when exception ownership or recovery is absent. State the evidence needed to change your mind. Avoid collecting real screening, health, payroll, customer or conduct records in this learning card.

## 8. Exactly three tabletop tests

| Test | Input / reveal | Expected proposed behavior | Evidence to record |
|---|---|---|---|
| OCF-HR12-T01 — Target rejection or outage | Broker accepts event but target rejects the role mapping or is unavailable. | Keep completion unconfirmed; route the owned exception and apply approved containment/fallback. | Source intent, transport status, target rejection and responsible owner. |
| OCF-HR12-T02 — Duplicates and reordering | Version 1 arrives after version 2, then version 2 repeats. | Use entity/version and idempotency rules; prevent older state overwrite and duplicate action. | Event IDs, ordering policy, target version and reconciliation evidence. |
| OCF-HR12-T03 — Bad schema and replay | An incompatible event is quarantined; operator proposes broad replay. | Validate contract/mapping and bounded recovery approval; reconcile affected targets before closing. | Schema version, quarantine reason, approved replay scope and target outcome. |

For each test, record input → expected → observed → revision/evidence → Pass, Revise or Blocked. All observed results are initially unfilled. Publication does not execute any tabletop, system test, approval or operational transaction. Acceptance requires a defensible card and all three observed tabletop results with revisions; bypassing a protected human decision requires redesign.

## 9. Traceability and learning measures

Existing anchors: OCF-M17 (risk/security), OCF-M18 (workforce/adoption), OCF-M19 (delivery readiness), OCF-M10 (value/process) and OCF-M11 (operating model). The workforce blueprint remains supporting research. The following are newly introduced educational IDs, not approved client requirements.

| New educational ID | Connection | Evidence / status |
|---|---|---|
| OCF-HR12-REQ01 | OCF-M18 → preserve correct domain facts and accountable readiness | T01; planned acceptance, no achieved result |
| OCF-HR12-REQ02 | OCF-M17/M19 → retain human authority and recoverable exceptions | T02/T03; planned controls |
| OCF-HR12-ADR01 | OCF-M11 → bounded automation with explicit domain ownership | Compare manual and automated alternatives; learner may reject with evidence |
| OCF-HR12-EXP01 | OCF-M19 → one synthetic decision-card experiment | Exactly T01–T03; unexecuted |
| OCF-HR12-M01 | OCF-M18 → learning measure | Record unknown target states, duplicate actions prevented in the proposed design and unresolved recovery ownership; no actual integration run or resilience outcome is claimed. |
| OCF-HR12-EV01 | OCF-HR12-EXP01 → observation and revision evidence | Unfilled until learner records actual tabletop observations |

## 10. Separate AI-driven exploration: 2026–2050

Scenarios, not predictions, guaranteed capabilities, deployments or product roadmaps.

| Scenario window | Question to explore |
|---|---|
| 2026–2030 — Assist | Could approved-source assistance explain evidence gaps and draft next steps without approving the decision? |
| 2031–2040 — Connect | Could separately authorized services coordinate this handoff while keeping unknown states and local rights visible? |
| 2041–2050 — Adapt | Could reviewed feedback propose reversible process changes while people retain consequential authority? |

Competing future: fragmented systems, uneven access, policy restrictions and manual review persist; a simpler controlled workflow outperforms orchestration. Falsifiable hypothesis question: Would faster event delivery improve workforce readiness if targets still reject mappings and nobody owns reconciliation? Define an observation that would disprove your claim—for example fewer steps but more unresolved exceptions or worse worker outcomes. Compare against a manual baseline before claiming value.

## 11. Reflect and move to Pre-Foundation

What evidence changed your first decision? Which authority did you initially assume? Who bears the exception burden? What would make you stop this design?
Pre-Foundation handoff: Define authoritative object, event, entity key, version, target acceptance, exception and replay. Draw one contract and state transition before selecting middleware.
Continue the same semi-fiction through Pre-Foundation (concepts/data), Foundation (small working model), Essentials (end-to-end handoffs), Advanced (exceptions and resilience), and Ultimate (architect-level value realization, troubleshooting, lessons and evidence-based ROI). These are future learning handoffs, not published deeper editions or additional Origin Story formats.

## 12. Architecture alignment and separate axes

TOGAF: compare architecture options and document decisions. BIZBOK: connect capability and value. BABOK: identify needs, requirements and acceptance evidence. DAMA-DMBOK: assign ownership, definitions, quality and lineage. COBIT: distinguish accountability, controls and monitoring. Relevant ISO/IEC information-security principles: confidentiality, integrity, availability, access and controlled change. Alignment is educational; no certification, conformance or compliance is claimed.

HR classification = HR12 Connected HR Enterprises. Architecture classification = the 12 distinct streams (Enterprise, Business, Data, Application, Technology, AI, Security, UI-UX, Infrastructure, Integration, Domain, Industry), applied selectively. Enterprise transformation classification = Workforce. These axes relate but are not interchangeable.

## 13. A few official resources

- SAP Help Portal — Employee Central: https://help.sap.com/docs/successfactors-employee-central — Ask which workforce object owns a fact and what separate evidence proves downstream authorization. Other SAP examples remain conceptual until their product documentation is reviewed.
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework — Ask who owns risk, which evidence supports use and when to stop assistance.
- ISO/IEC 27001 overview: https://www.iso.org/standard/27001 — Apply confidentiality, integrity and availability questions; reading the overview does not establish conformance.

## 14. Source and edition record

S1 — Existing HR12 source case: https://app.notion.com/p/e4d08f7fd6364bcbab7179b472912cbb

Enterprise hub: https://app.notion.com/p/ad26929126a047afa591f9c7d75cbab9
Workforce scope: https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/derived-streams/01-workforce.md
Existing personas: https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/personas/persona-cards.md
Master risk/workforce/readiness: https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/master/theme-e-execution.md
Source/conflict register: https://github.com/nbnayak88/successlabs-case-studies/blob/main/07-financials/omnicapital-financial-group-ltd/references/source-and-assumptions.md
Supporting EC business case: https://docs.google.com/document/d/1KUqAVQUQnyzlP-1mA8JjhFAWbhqzBAhrhJp6xq4-JII
GICS02 format reference: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/materials-origin-stories.md

Source review: 31 October 2026 IST. Preserve supporting case bodies and stable source identities. This edition adds an Origin Story section rather than replacing deeper research. HR02a and HR02b remain separate source cases connected within one HR02 120-minute sprint.

## Companion workspace

GitHub matching sprint: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR12-AIG2-Architecting-Connected-HR-Enterprises/07-HR12-FIN-financials/0-The-Origin-Story/sprint/financials-connected-hr-evolution-sprint.md
Notion matching edition: https://app.notion.com/p/e4d08f7fd6364bcbab7179b472912cbb
Sector index: https://github.com/nbnayak88/learning-township/blob/main/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/financials-origin-stories.md
Google Doc, slide and sheet links are recorded in the sector index after completed saves and readback. Slides are facilitator companions; the Sheet is the build-card workspace. No automatic synchronization, public student access, successful copying, executed tests or realized operational benefits are implied.
