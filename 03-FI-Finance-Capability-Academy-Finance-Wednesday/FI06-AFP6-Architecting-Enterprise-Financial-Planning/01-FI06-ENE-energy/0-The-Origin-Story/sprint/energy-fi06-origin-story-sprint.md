# The forecast improved when someone hid the assumptions
## FI06 — Architecting Enterprise Financial Planning

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-FI06-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published educational content, not an enrolled course or certification.

> **Your promise:** In two hours, design one financial scenario that makes energy-transition assumptions, uncertainty and cash timing visible.

**One story · One Decision Card · Three tabletop tests**

## 1. The decision behind the numbers

A renewable investment forecast shows a strong return, but electricity prices, utilization, construction timing and maintenance costs come from different versions. The downside case has disappeared from the slide.

**Workshop lead:** Aditi Sen — Group Financial Controller (OVE-FI-OS-P01, new fictional learning persona).  
**Counterpart:** Leena Fernandes — Chief Sustainability and Transition Officer (OVE-P06).

Leena asks which transition assumptions are credible. Aditi asks when cash moves, who owns each driver and whether savings overlap another initiative.

They choose one project decision, align assumptions to a version/date and compare base and downside cases. Approval of a plan is kept separate from forecast updates and actual outcomes.

**Pause:** Which fact would change your decision? Ask the counterpart one question before proposing a product.

OmniVerse is a fictional energy enterprise with 68,000 employees in 42 countries. Existing OVE-P identities come from the enterprise register. Aditi, Rohan and Amira are explicitly new fictional operational personas with OVE-FI-OS-P identifiers. All new dialogue and incidents are learning designs. Country, entity, accounting basis and approved policy must be established rather than assumed.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Before OmniVerse's fictional 1978 founding, examples describe the wider domain.

- **1970–1989:** Annual budgets and paper schedules allocate resources using limited scenario detail.
- **1990–1999:** Spreadsheets make sensitivity analysis accessible; copied formulas and versions can conflict.
- **2000–2009:** ERP actuals and planning tools connect budgets to performance; driver ownership remains important.
- **2010–2019:** Integrated planning links operational and financial assumptions; dependencies complicate attribution.
- **2020–2025:** Predictive forecasts propose ranges; explainability and scenario discipline remain necessary.

**Mindset:** faster processing is useful when the evidence and decision remain trustworthy. Who bears the cost of an incorrect result: a supplier, worker, customer, investor or community?

## 3. AI-driven horizon, 2026–2050

**2026 starting experiment:** let assistance prepare a low-risk draft, match suggestion or evidence summary. Test its limits before permitting consequential actions.

**2030 checkpoint:** compare the assisted process with a human-led baseline. Require source evidence, approved authority and a usable challenge route.

**2035–2050 scenario:** Imagine a 2050 planning assistant continually proposing energy-mix scenarios. It should retain driver provenance, uncertainty and decision authority rather than announce one inevitable future.

**Alternative:** If data or markets change abruptly, a small transparent driver model may be more useful than a complex point forecast.

These are possibilities and test questions, not forecasts, accounting interpretations or product commitments. Autonomy means bounded assistance under approved authority.

## 4. Smallest useful architecture

**Capability — OVE-FI06-OS-CAP01:** driver-based financial planning.

**Value stages — OVE-FI06-OS-VS01:** Frame decision → agree drivers → create scenarios → compare uncertainty → review → record decision → revisit actuals.

**Objects:** scenario version, driver, volume/price basis, cash period, cost assumption and approval.

**Application responsibility:** Business owners own operational drivers; FP&A owns financial-model versioning; treasury owns funding/cash inputs; sustainability owners validate environmental assumptions; sponsors approve investment decisions.

**Boundary:** Budget, forecast, valuation and realized cash are different. Do not inherit the enterprise investment envelope as a project allocation or double-count benefit categories.

The twelve FI themes are a curriculum axis, separate from the twelve architecture streams. SAP Finance is an optional demonstration context; edition, licensing and local requirements remain to validate. Live configuration, posting and payment execution are outside this paper sprint.

## 5. One Decision Card

Use synthetic case **OVE-FI06-OS-SYN001**. Keep the response to one card or screen.

1. **Need:** one business decision, affected population and missing fact.
2. **Evidence:** source IDs, entity, period/effective date, currency or other relevant unit, and approved policy owner.
3. **Ownership:** source application, accountable decision maker and receiving owner.
4. **Gate:** prerequisite, authorized next state and failure/hold condition.
5. **Alternative:** Compare a single optimistic estimate with a transparent base/downside model and explicit decision triggers.
6. **Recovery:** exception owner, escalation and safe correction/retry.
7. **Proof:** the three actual paper results, measure and stop/revise/proceed decision.

**Requirement — OVE-FI06-OS-REQ01:** retain approved driver sources, timing, versions and at least one downside alternative for the chosen decision.

**Decision — OVE-FI06-OS-ADR01:** record your choice, trade-off and the evidence that would make you change it.

## 6. Three tabletop tests

### T01 — Price driver changes without version update

**Expected:** Flag the inconsistency; recalculate affected outputs under an approved new version.

### T02 — Profit improvement is presented as immediate cash

**Expected:** Separate accounting impact, working capital and cash timing assumptions.

### T03 — Two programs claim the same saving

**Expected:** Identify overlap, name the benefit owner and avoid adding unsupported duplicate value.

Record **input → expected → actual paper result → evidence note → revision → retest**. Tests OVE-FI06-OS-T01/T02/T03 support REQ01; expected results are not observed tenant evidence.

**Measure — OVE-FI06-OS-KPI01:** material forecast drivers with current source, owner and version / material drivers reviewed. Name the accountable operational owner, baseline, exclusions and as-of date before setting a target.

**Acceptance:** your card preserves the boundary, names accountable owners, handles all three tests after revisions and supports a 60-second explanation. Unresolved facts remain visible; no achieved financial benefit is claimed.

## 7. Your 120 minutes

- **0–20:** explore the history and explain the enduring problem.
- **20–45:** role-play the lead and counterpart; ask for evidence.
- **45–65:** map responsibilities and consult one resource selectively.
- **65–100:** complete the card and compare the alternative.
- **100–115:** run the three tests and revise.
- **115–120:** explain the decision and choose the next experiment.

## 8. Resources and reflection

[SAP Discovering Finance](https://learning.sap.com/learning-journeys/discovering-finance) and [Financial Accounting Overview](https://learning.sap.com/learning-journeys/outlining-the-financial-accounting-overview): select the part relevant to planning, cost and business-value assumptions. Ask which application owns the fact and which person approves its interpretation. Read selectively within the sprint.

Official resource pages checked 31 October 2026. Resources orient learning; current local authority guidance and qualified policy interpretation are still needed before production design, particularly for tax and reporting.

**Reflect:** What became clearer? Who could your design disadvantage? What evidence would overturn your choice?

**Next Pre-Foundation experiment:** build one base/downside driver pair and record what evidence would change the investment decision.

**Mission:** Architecting Experiences for a Better World.

## Traceability and scope

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Finance blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/03-finance.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Finance academy source](https://app.notion.com/p/0c0a85eaefe145d3bed6c2ea143b6009).

Inherited blueprint anchors: OVE-M02, OVE-M08, OVE-M14, OVE-M20. New namespace OVE-FI06-OS denotes this learning expansion, not previously approved enterprise requirements.

**Trace:** source → OVE-FI06-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 (this experiment) → T01/T02/T03 → KPI01. All shortened IDs carry the same OVE-FI06-OS prefix. EV01 remains an empty evidence slot until a learner records results.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA ownership/quality; COBIT control accountability; ISO/IEC 27001 information protection. This is not a compliance certification.

**Publication:** matching manually published learning editions. Original enterprise research and financial hypotheses remain preserved. No unattended synchronization is asserted.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/03-FI-Finance-Capability-Academy-Finance-Wednesday/FI06-AFP6-Architecting-Enterprise-Financial-Planning/01-FI06-ENE-energy/0-The-Origin-Story/sprint/energy-fi06-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1JFDZzvF_Zt3ELhYrH97kesJyS-QXv6rihQttmaLYFyw/edit?usp=drivesdk)

[Notion edition](https://app.notion.com/p/40ace6de608981f99228ef6efb401def?pvs=204)
