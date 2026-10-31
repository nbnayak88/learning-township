# The customer paid; the receivable was still overdue
## FI03 — Architecting Intelligent Revenue Operations

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-FI03-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published educational content, not an enrolled course or certification.

> **Your promise:** In two hours, design one receivables decision that separates billing, recognized revenue, cash receipt and clearing.

**One story · One Decision Card · Three tabletop tests**

## 1. The decision behind the numbers

An industrial customer pays several energy invoices together, deducting a disputed amount. The bank receipt lacks clear references, yet an automated collection message calls the whole account overdue.

**Workshop lead:** Aditi Sen — Group Financial Controller (OVE-FI-OS-P01, new fictional learning persona).  
**Counterpart:** Grace Okafor — Chief Customer and Retail Officer (OVE-P10).

Grace asks how the customer can correct the dispute. Aditi asks which invoice is valid, what the payment actually covers and whether the accounting policy permits the proposed treatment.

The team preserves the receipt, proposes evidence-backed allocation and leaves the disputed balance visible. It separates collection action from cash application and from the accounting assessment of revenue.

**Pause:** Which fact would change your decision? Ask the counterpart one question before proposing a product.

OmniVerse is a fictional energy enterprise with 68,000 employees in 42 countries. Existing OVE-P identities come from the enterprise register. Aditi, Rohan and Amira are explicitly new fictional operational personas with OVE-FI-OS-P identifiers. All new dialogue and incidents are learning designs. Country, entity, accounting basis and approved policy must be established rather than assumed.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Before OmniVerse's fictional 1978 founding, examples describe the wider domain.

- **1970–1989:** Sales ledgers and receipts track debts manually; allocation depends on references.
- **1990–1999:** Receivables databases organize due dates; separate customer and bank records still disagree.
- **2000–2009:** ERP billing and AR connect documents; invoice creation does not itself settle every accounting question.
- **2010–2019:** Credit, collections and dispute workflows expose responsibility; disputed and overdue are not identical states.
- **2020–2025:** Assisted cash matching suggests allocations; partial payments and ambiguous evidence still require review.

**Mindset:** faster processing is useful when the evidence and decision remain trustworthy. Who bears the cost of an incorrect result: a supplier, worker, customer, investor or community?

## 3. AI-driven horizon, 2026–2050

**2026 starting experiment:** let assistance prepare a low-risk draft, match suggestion or evidence summary. Test its limits before permitting consequential actions.

**2030 checkpoint:** compare the assisted process with a human-led baseline. Require source evidence, approved authority and a usable challenge route.

**2035–2050 scenario:** A possible 2050 customer agent might send machine-readable remittance and dispute evidence. The receiving provider must still validate allocation, policy and consequential collection decisions.

**Alternative:** If remittance is incomplete or a bank feed is delayed, preserve unapplied cash and a human resolution route rather than invent a match.

These are possibilities and test questions, not forecasts, accounting interpretations or product commitments. Autonomy means bounded assistance under approved authority.

## 4. Smallest useful architecture

**Capability — OVE-FI03-OS-CAP01:** evidence-backed receivables and cash application.

**Value stages — OVE-FI03-OS-VS01:** Validate billing → establish receivable → receive cash → propose allocation → resolve dispute → clear or retain balance.

**Objects:** contract evidence, invoice, receivable, remittance, bank receipt, allocation and dispute.

**Application responsibility:** Billing owns source invoices; accounting policy owners decide recognition; AR owns open items and clearing; treasury/bank feeds provide receipt evidence; service/business teams resolve commercial disputes.

**Boundary:** Invoice, revenue, cash receipt and clearing are distinct. A forecast or matched reference cannot replace approved accounting judgment.

The twelve FI themes are a curriculum axis, separate from the twelve architecture streams. SAP Finance is an optional demonstration context; edition, licensing and local requirements remain to validate. Live configuration, posting and payment execution are outside this paper sprint.

## 5. One Decision Card

Use synthetic case **OVE-FI03-OS-SYN001**. Keep the response to one card or screen.

1. **Need:** one business decision, affected population and missing fact.
2. **Evidence:** source IDs, entity, period/effective date, currency or other relevant unit, and approved policy owner.
3. **Ownership:** source application, accountable decision maker and receiving owner.
4. **Gate:** prerequisite, authorized next state and failure/hold condition.
5. **Alternative:** Compare automatic full clearing with evidence-backed partial allocation and an owned dispute.
6. **Recovery:** exception owner, escalation and safe correction/retry.
7. **Proof:** the three actual paper results, measure and stop/revise/proceed decision.

**Requirement — OVE-FI03-OS-REQ01:** retain traceable allocation and dispute status before clearing or issuing consequential collection action.

**Decision — OVE-FI03-OS-ADR01:** record your choice, trade-off and the evidence that would make you change it.

## 6. Three tabletop tests

### T01 — Payment covers multiple invoices with unclear references

**Expected:** Hold uncertain allocation, seek remittance and preserve unapplied cash status.

### T02 — Customer deducts a disputed amount

**Expected:** Separate disputed and undisputed balances; route the dispute under approved policy.

### T03 — Bank receipt is reversed

**Expected:** Reverse or reopen the affected status through approved controls; do not keep a false paid state.

Record **input → expected → actual paper result → evidence note → revision → retest**. Tests OVE-FI03-OS-T01/T02/T03 support REQ01; expected results are not observed tenant evidence.

**Measure — OVE-FI03-OS-KPI01:** cash allocations supported by verified receipt/remittance evidence / allocations reviewed, with unresolved balance aging. Name the accountable operational owner, baseline, exclusions and as-of date before setting a target.

**Acceptance:** your card preserves the boundary, names accountable owners, handles all three tests after revisions and supports a 60-second explanation. Unresolved facts remain visible; no achieved financial benefit is claimed.

## 7. Your 120 minutes

- **0–20:** explore the history and explain the enduring problem.
- **20–45:** role-play the lead and counterpart; ask for evidence.
- **45–65:** map responsibilities and consult one resource selectively.
- **65–100:** complete the card and compare the alternative.
- **100–115:** run the three tests and revise.
- **115–120:** explain the decision and choose the next experiment.

## 8. Resources and reflection

[SAP Discovering Finance](https://learning.sap.com/learning-journeys/discovering-finance) and [Financial Accounting Overview](https://learning.sap.com/learning-journeys/outlining-the-financial-accounting-overview): select the part relevant to receivables and cash application. Ask which application owns the fact and which person approves its interpretation. Read selectively within the sprint.

Official resource pages checked 31 October 2026. Resources orient learning; current local authority guidance and qualified policy interpretation are still needed before production design, particularly for tax and reporting.

**Reflect:** What became clearer? Who could your design disadvantage? What evidence would overturn your choice?

**Next Pre-Foundation experiment:** define one partial-payment allocation rule and a disputed-balance test.

**Mission:** Architecting Experiences for a Better World.

## Traceability and scope

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Finance blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/03-finance.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Finance academy source](https://app.notion.com/p/0c0a85eaefe145d3bed6c2ea143b6009).

Inherited blueprint anchors: OVE-M02, OVE-M08, OVE-M14, OVE-M20. New namespace OVE-FI03-OS denotes this learning expansion, not previously approved enterprise requirements.

**Trace:** source → OVE-FI03-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 (this experiment) → T01/T02/T03 → KPI01. All shortened IDs carry the same OVE-FI03-OS prefix. EV01 remains an empty evidence slot until a learner records results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA ownership/quality; COBIT control accountability; ISO/IEC 27001 information protection. This is not a compliance certification.

**Publication:** matching manually published learning editions. Original enterprise research and financial hypotheses remain preserved. No unattended synchronization is asserted.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/03-FI-Finance-Capability-Academy-Finance-Wednesday/FI03-AOT3-Architecting-Intelligent-Revenue-Operations/01-FI03-ENE-energy/0-The-Origin-Story/sprint/energy-fi03-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1aNulRgIAUiB7xdzUNdjGPZv1q6UXKCnIm4sfvTAOOFc/edit?usp=drivesdk)

[Notion edition](https://app.notion.com/p/40ace6de60898194b81bdcec9bbd1216?pvs=204)
