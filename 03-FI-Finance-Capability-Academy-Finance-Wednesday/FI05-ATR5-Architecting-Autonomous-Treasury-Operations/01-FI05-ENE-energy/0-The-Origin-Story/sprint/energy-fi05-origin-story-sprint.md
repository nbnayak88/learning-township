# The cash dashboard looked healthy until the payment cut-off
## FI05 — Architecting Autonomous Treasury Operations

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-FI05-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published educational content, not an enrolled course or certification.

> **Your promise:** In two hours, design one liquidity and payment-release decision using current bank evidence and independent authorization.

**One story · One Decision Card · Three tabletop tests**

## 1. The decision behind the numbers

A renewable-project payment is due. The liquidity view includes a stale bank balance and an expected customer receipt as if it had settled. An urgent instruction requests release before cut-off.

**Workshop lead:** Rohan Mehta — Treasury Operations Lead (OVE-FI-OS-P02, new fictional learning persona).  
**Counterpart:** Michael Reed — Group Chief Financial Officer (OVE-P03).

Michael asks what cash is actually available. Rohan asks which balances are verified, restricted or forecast, and who can authorize the release independently.

They separate actual bank evidence from forecast inflows, surface currency/date restrictions and build a release proposal with explicit approval. A bank submission is tracked through its confirmed outcome.

**Pause:** Which fact would change your decision? Ask the counterpart one question before proposing a product.

OmniVerse is a fictional energy enterprise with 68,000 employees in 42 countries. Existing OVE-P identities come from the enterprise register. Aditi, Rohan and Amira are explicitly new fictional operational personas with OVE-FI-OS-P identifiers. All new dialogue and incidents are learning designs. Country, entity, accounting basis and approved policy must be established rather than assumed.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Before OmniVerse's fictional 1978 founding, examples describe the wider domain.

- **1970–1989:** Cash books, cheques and bank calls provide periodic visibility.
- **1990–1999:** Treasury spreadsheets and bank files centralize positions but introduce timing gaps.
- **2000–2009:** Treasury/ERP connectivity coordinates cash and accounting; bank evidence still needs reconciliation.
- **2010–2019:** Multi-bank platforms improve visibility and control; currency, cut-offs and restrictions remain relevant.
- **2020–2025:** Predictive liquidity tools suggest actions; uncertain receipts cannot become settled funds.

**Mindset:** faster processing is useful when the evidence and decision remain trustworthy. Who bears the cost of an incorrect result: a supplier, worker, customer, investor or community?

## 3. AI-driven horizon, 2026–2050

**2026 starting experiment:** let assistance prepare a low-risk draft, match suggestion or evidence summary. Test its limits before permitting consequential actions.

**2030 checkpoint:** compare the assisted process with a human-led baseline. Require source evidence, approved authority and a usable challenge route.

**2035–2050 scenario:** In an imagined 2050 treasury, agents propose funding and payment options against uncertain conditions. Delegated limits, independently approved releases and confirmed bank outcomes remain explicit.

**Alternative:** If connectivity fails near cut-off, an approved continuity process and controlled status check must prevent uncontrolled re-sending.

These are possibilities and test questions, not forecasts, accounting interpretations or product commitments. Autonomy means bounded assistance under approved authority.

## 4. Smallest useful architecture

**Capability — OVE-FI05-OS-CAP01:** controlled cash visibility and payment release.

**Value stages — OVE-FI05-OS-VS01:** Verify position → separate forecast → assess liquidity → approve release → submit → confirm → reconcile.

**Objects:** bank account, balance timestamp, restriction, currency, forecast item, payment instruction and bank status.

**Application responsibility:** Banks provide external status; treasury owns cash-position assumptions and release process; AP/payroll supply approved obligations; accounting owns ledger reconciliation; risk owners approve exposures.

**Boundary:** This is a synthetic control exercise, not a funding or trading recommendation. Proposal, authorization, bank acceptance and settlement are separate states.

The twelve FI themes are a curriculum axis, separate from the twelve architecture streams. SAP Finance is an optional demonstration context; edition, licensing and local requirements remain to validate. Live configuration, posting and payment execution are outside this paper sprint.

## 5. One Decision Card

Use synthetic case **OVE-FI05-OS-SYN001**. Keep the response to one card or screen.

1. **Need:** one business decision, affected population and missing fact.
2. **Evidence:** source IDs, entity, period/effective date, currency or other relevant unit, and approved policy owner.
3. **Ownership:** source application, accountable decision maker and receiving owner.
4. **Gate:** prerequisite, authorized next state and failure/hold condition.
5. **Alternative:** Compare an aggregated headline cash figure with a timestamped, currency-specific position and approved contingency.
6. **Recovery:** exception owner, escalation and safe correction/retry.
7. **Proof:** the three actual paper results, measure and stop/revise/proceed decision.

**Requirement — OVE-FI05-OS-REQ01:** base release on verified available-position evidence, approved authority and a confirmed bank outcome.

**Decision — OVE-FI05-OS-ADR01:** record your choice, trade-off and the evidence that would make you change it.

## 6. Three tabletop tests

### T01 — Balance is stale and expected receipt is uncertain

**Expected:** Show freshness/forecast distinctions and hold unsupported availability assumptions.

### T02 — Same operator changes payee and releases payment

**Expected:** Apply segregation/independent approval requirements or an explicitly approved compensating control.

### T03 — Submission times out near cut-off

**Expected:** Check bank outcome using the instruction reference before retry; prevent duplicate release.

Record **input → expected → actual paper result → evidence note → revision → retest**. Tests OVE-FI05-OS-T01/T02/T03 support REQ01; expected results are not observed tenant evidence.

**Measure — OVE-FI05-OS-KPI01:** in-scope payment instructions reconciled to confirmed bank and ledger outcomes / instructions due. Name the accountable operational owner, baseline, exclusions and as-of date before setting a target.

**Acceptance:** your card preserves the boundary, names accountable owners, handles all three tests after revisions and supports a 60-second explanation. Unresolved facts remain visible; no achieved financial benefit is claimed.

## 7. Your 120 minutes

- **0–20:** explore the history and explain the enduring problem.
- **20–45:** role-play the lead and counterpart; ask for evidence.
- **45–65:** map responsibilities and consult one resource selectively.
- **65–100:** complete the card and compare the alternative.
- **100–115:** run the three tests and revise.
- **115–120:** explain the decision and choose the next experiment.

## 8. Resources and reflection

[SAP Discovering Finance](https://learning.sap.com/learning-journeys/discovering-finance) and [Financial Accounting Overview](https://learning.sap.com/learning-journeys/outlining-the-financial-accounting-overview): select the part relevant to treasury and bank connectivity. Ask which application owns the fact and which person approves its interpretation. Read selectively within the sprint.

[SAP Treasury Management](https://learning.sap.com/courses/discovering-treasury-management): inspect cash position and bank handoffs; distinguish forecast, instruction and confirmed outcome.

Official resource pages checked 31 October 2026. Resources orient learning; current local authority guidance and qualified policy interpretation are still needed before production design, particularly for tax and reporting.

**Reflect:** What became clearer? Who could your design disadvantage? What evidence would overturn your choice?

**Next Pre-Foundation experiment:** define one payment state transition and a safe timeout/retry test.

**Mission:** Architecting Experiences for a Better World.

## Traceability and scope

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Finance blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/03-finance.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Finance academy source](https://app.notion.com/p/0c0a85eaefe145d3bed6c2ea143b6009).

Inherited blueprint anchors: OVE-M02, OVE-M08, OVE-M14, OVE-M20. New namespace OVE-FI05-OS denotes this learning expansion, not previously approved enterprise requirements.

**Trace:** source → OVE-FI05-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 (this experiment) → T01/T02/T03 → KPI01. All shortened IDs carry the same OVE-FI05-OS prefix. EV01 remains an empty evidence slot until a learner records results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA ownership/quality; COBIT control accountability; ISO/IEC 27001 information protection. This is not a compliance certification.

**Publication:** matching manually published learning editions. Original enterprise research and financial hypotheses remain preserved. No unattended synchronization is asserted.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/03-FI-Finance-Capability-Academy-Finance-Wednesday/FI05-ATR5-Architecting-Autonomous-Treasury-Operations/01-FI05-ENE-energy/0-The-Origin-Story/sprint/energy-fi05-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1y0YIYZBEI5RK-9Z4An9PfNEzbmvzfgQVNRUx-EQYrIM/edit?usp=drivesdk)

[Notion edition](https://app.notion.com/p/40ace6de60898116914ac62ae09138cf?pvs=204)
