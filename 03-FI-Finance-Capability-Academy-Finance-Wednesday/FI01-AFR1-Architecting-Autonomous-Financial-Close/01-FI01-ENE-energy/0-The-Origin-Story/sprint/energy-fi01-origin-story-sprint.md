# The close was green; the accounts still disagreed
## FI01 — Architecting Autonomous Financial Close

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-FI01-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published educational content, not an enrolled course or certification.

> **Your promise:** In two hours, design one evidence-backed close decision that keeps unresolved differences visible.

**One story · One Decision Card · Three tabletop tests**

## 1. The decision behind the numbers

A refinery ledger and its subledger differ at month-end. A dashboard turns green when every task is marked complete, even though an intercompany mismatch and a late accrual remain unexplained.

**Workshop lead:** Aditi Sen — Group Financial Controller (OVE-FI-OS-P01, new fictional learning persona).  
**Counterpart:** Michael Reed — Group Chief Financial Officer (OVE-P03).

Michael asks whether the accounts are ready to rely on. Aditi asks which balances were reconciled, who reviewed the difference and what a green task actually proves.

They separate task completion, journal approval, reconciliation and reporting release. The next action is an owned investigation and policy-based adjustment proposal, not an unsupported balancing entry.

**Pause:** Which fact would change your decision? Ask the counterpart one question before proposing a product.

OmniVerse is a fictional energy enterprise with 68,000 employees in 42 countries. Existing OVE-P identities come from the enterprise register. Aditi, Rohan and Amira are explicitly new fictional operational personas with OVE-FI-OS-P identifiers. All new dialogue and incidents are learning designs. Country, entity, accounting basis and approved policy must be established rather than assumed.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Before OmniVerse's fictional 1978 founding, examples describe the wider domain.

- **1970–1989:** Paper journals and periodic ledgers make review depend on document trails.
- **1990–1999:** Spreadsheets and finance databases speed schedules; versions can diverge.
- **2000–2009:** ERP links transactions and ledgers; interfaces and intercompany balances still require reconciliation.
- **2010–2019:** Close orchestration exposes dependencies; completing a task does not establish accounting accuracy.
- **2020–2025:** Analytics and exception detection prioritize review; late evidence and estimates still need judgment.

**Mindset:** faster processing is useful when the evidence and decision remain trustworthy. Who bears the cost of an incorrect result: a supplier, worker, customer, investor or community?

## 3. AI-driven horizon, 2026–2050

**2026 starting experiment:** let assistance prepare a low-risk draft, match suggestion or evidence summary. Test its limits before permitting consequential actions.

**2030 checkpoint:** compare the assisted process with a human-led baseline. Require source evidence, approved authority and a usable challenge route.

**2035–2050 scenario:** By 2035, an assistant might assemble reconciliations and explain differences. In an imagined 2050 close, reviewers still need current evidence, approved estimates and a decision on unresolved items.

**Alternative:** If source systems are delayed or unavailable, a controlled manual reconciliation with visible limitations remains preferable to fabricated completeness.

These are possibilities and test questions, not forecasts, accounting interpretations or product commitments. Autonomy means bounded assistance under approved authority.

## 4. Smallest useful architecture

**Capability — OVE-FI01-OS-CAP01:** evidence-based financial close.

**Value stages — OVE-FI01-OS-VS01:** Record → reconcile → investigate → propose adjustment → approve → release report.

**Objects:** entity, ledger, period, journal version, reconciliation difference and approval evidence.

**Application responsibility:** Ledger/subledger services own recorded balances; close orchestration owns tasks; controllers own reconciliation and policy decisions. FI01 owns close readiness, while FI12 owns exchange/recovery.

**Boundary:** A balanced journal or completed checklist does not prove a true and fair result or authorize unsupported corrections.

The twelve FI themes are a curriculum axis, separate from the twelve architecture streams. SAP Finance is an optional demonstration context; edition, licensing and local requirements remain to validate. Live configuration, posting and payment execution are outside this paper sprint.

## 5. One Decision Card

Use synthetic case **OVE-FI01-OS-SYN001**. Keep the response to one card or screen.

1. **Need:** one business decision, affected population and missing fact.
2. **Evidence:** source IDs, entity, period/effective date, currency or other relevant unit, and approved policy owner.
3. **Ownership:** source application, accountable decision maker and receiving owner.
4. **Gate:** prerequisite, authorized next state and failure/hold condition.
5. **Alternative:** Compare forcing all indicators green with releasing only against agreed reconciliation and exception criteria.
6. **Recovery:** exception owner, escalation and safe correction/retry.
7. **Proof:** the three actual paper results, measure and stop/revise/proceed decision.

**Requirement — OVE-FI01-OS-REQ01:** retain source balances, owned differences and authorized adjustment evidence before reporting release.

**Decision — OVE-FI01-OS-ADR01:** record your choice, trade-off and the evidence that would make you change it.

## 6. Three tabletop tests

### T01 — Unexplained intercompany difference

**Expected:** Keep the difference open, assign counterpart owners and reconcile currency/period/source evidence.

### T02 — Late accrual after an approved schedule

**Expected:** Apply the agreed period/change process and reviewer gate; preserve the prior version.

### T03 — Assistant proposes a plug journal

**Expected:** Reject unsupported balancing, request evidence and retain a human accounting decision.

Record **input → expected → actual paper result → evidence note → revision → retest**. Tests OVE-FI01-OS-T01/T02/T03 support REQ01; expected results are not observed tenant evidence.

**Measure — OVE-FI01-OS-KPI01:** reconciliations meeting defined evidence/reviewer criteria / reconciliations due; disclose unresolved items separately. Name the accountable operational owner, baseline, exclusions and as-of date before setting a target.

**Acceptance:** your card preserves the boundary, names accountable owners, handles all three tests after revisions and supports a 60-second explanation. Unresolved facts remain visible; no achieved financial benefit is claimed.

## 7. Your 120 minutes

- **0–20:** explore the history and explain the enduring problem.
- **20–45:** role-play the lead and counterpart; ask for evidence.
- **45–65:** map responsibilities and consult one resource selectively.
- **65–100:** complete the card and compare the alternative.
- **100–115:** run the three tests and revise.
- **115–120:** explain the decision and choose the next experiment.

## 8. Resources and reflection

[SAP Discovering Finance](https://learning.sap.com/learning-journeys/discovering-finance) and [Financial Accounting Overview](https://learning.sap.com/learning-journeys/outlining-the-financial-accounting-overview): select the part relevant to record-to-report and controlled close. Ask which application owns the fact and which person approves its interpretation. Read selectively within the sprint.

Official resource pages checked 31 October 2026. Resources orient learning; current local authority guidance and qualified policy interpretation are still needed before production design, particularly for tax and reporting.

**Reflect:** What became clearer? Who could your design disadvantage? What evidence would overturn your choice?

**Next Pre-Foundation experiment:** define one close gate and its source-to-ledger reconciliation test.

**Mission:** Architecting Experiences for a Better World.

## Traceability and scope

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Finance blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/03-finance.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Finance academy source](https://app.notion.com/p/0c0a85eaefe145d3bed6c2ea143b6009).

Inherited blueprint anchors: OVE-M02, OVE-M08, OVE-M14, OVE-M20. New namespace OVE-FI01-OS denotes this learning expansion, not previously approved enterprise requirements.

**Trace:** source → OVE-FI01-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 (this experiment) → T01/T02/T03 → KPI01. All shortened IDs carry the same OVE-FI01-OS prefix. EV01 remains an empty evidence slot until a learner records results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA ownership/quality; COBIT control accountability; ISO/IEC 27001 information protection. This is not a compliance certification.

**Publication:** matching manually published learning editions. Original enterprise research and financial hypotheses remain preserved. No unattended synchronization is asserted.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/03-FI-Finance-Capability-Academy-Finance-Wednesday/FI01-AFR1-Architecting-Autonomous-Financial-Close/01-FI01-ENE-energy/0-The-Origin-Story/sprint/energy-fi01-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1YOEZVMc5GaknCiaJTh1MSpAE2HGsWZRiyD1m6Hoji8A/edit?usp=drivesdk)

[Notion edition](https://app.notion.com/p/40ace6de6089818d8534ef04d58f896d?pvs=204)
