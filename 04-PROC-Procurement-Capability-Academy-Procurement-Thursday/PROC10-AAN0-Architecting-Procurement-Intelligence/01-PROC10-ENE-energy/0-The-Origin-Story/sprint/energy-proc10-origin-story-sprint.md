# The spend dashboard counted the same purchase three times
## PROC10 — Architecting Procurement Intelligence

**SuccessLabs Academy · OmniVerse Energy Ltd. · IIL — Industry Immersion Lab**  
**Version:** 1.0 · 31 October 2026 · **Level:** Origin Story → Pre-Foundation  
**Planning reference:** HUB-ORIGIN-PROC10-ENE-sprint (not an LMS ID)  
**Format:** 120-minute sprint · Free — Community/Citizen Edition  
**Status:** Published learning content, not an enrolled course or certification.

> **Your promise:** In two hours, design one procurement measure with clear transaction grain, reconciled sources and an accountable owner.

**One story · One Decision Card · Three tests**

## 1. The purchase behind the process

A dashboard combines purchase orders, receipts and invoices into one spend number. Supplier aliases and inconsistent currencies distort category concentration, and an assistant invents a confident explanation.

**Lead:** Dr. Leila Haddad — Head of Data Governance and AI (OVE-P16).  
**Counterpart:** Wei Zhang — Chief Supply Chain & Procurement Officer (OVE-P11).

Wei asks what decision the measure supports. Leila asks whether each row represents commitment, receipt or invoice and which sources reconcile.

The team selects a grain and period, preserves source references and reconciles a small synthetic sample. It labels missing data and separates descriptive insight from causal recommendations.

**Pause:** What business need and evidence must be clear before the next commitment? Ask both people one useful question.

OmniVerse is a fictional integrated energy group with 68,000 employees in 42 countries. Existing OVE-P personas retain their source identities. Dialogue, incidents, supplier records and proposed outcomes here are new learning fiction. No real supplier, award, transaction or implementation result is represented.

## 2. Origins and evolution, 1970–2025

These closed, non-overlapping periods are teaching lenses, not invention dates or universal adoption deadlines. Practices coexist. Pre-1978 examples describe the wider domain rather than OmniVerse corporate history.

- **1970–1989:** Purchase summaries total local ledger entries.
- **1990–1999:** Spreadsheets consolidate reports with inconsistent classifications.
- **2000–2009:** Warehouses combine procurement sources but require common definitions.
- **2010–2019:** Self-service analytics and spend tools increase access.
- **2020–2025:** Generated insights accelerate explanation; lineage and meaningful denominators remain essential.

**Mindset:** optimize the business outcome and relationship, with evidence for each consequential decision. A faster purchase can still create a larger downstream problem.

**Social impact question:** whose safety, livelihood, access to opportunity or environment could this choice affect?

## 3. AI-driven horizon, 2026–2050

**2026 experiment:** use assistance for a narrow evidence summary, draft or exception suggestion. Test what it misses before delegating any action.

**2030 checkpoint:** compare assisted work with a human-led baseline, including contrary evidence and a challenge route.

**2035–2050 scenario:** Imagine a 2050 procurement intelligence service tracing every conclusion to governed evidence. It should disclose coverage gaps rather than produce an apparently complete answer.

**Competing future:** When integration is incomplete, a limited reconciled view can support a better decision than an inflated total.

These are design hypotheses, not forecasts, legal interpretations or vendor roadmaps. Autonomy remains bounded by approved authority.

## 4. Smallest useful architecture

**Capability — OVE-PROC10-OS-CAP01:** procurement intelligence.

**Value stages — OVE-PROC10-OS-VS01:** Frame question → define grain → reconcile → calculate → validate sample → explain limitations.

**Objects to distinguish:** transaction grain, source document, category, supplier mapping, period, currency and definition.

**Application responsibility:** Source applications own documents; supplier/category stewards own mappings; analytics owns definitions and lineage; procurement approves business actions. PROC10 supplies insight, while PROC08 owns spend initiatives.

**Protected boundary:** Order, receipt and invoice are lifecycle records, not automatically additive spend. A predictive score is not established causation.

Start with the business need before choosing SAP Ariba, SAP Business Network, ERP or another platform. Product scope, editions, local obligations and licensing require validation. The twelve PROC themes and twelve architecture streams are separate axes.

## 5. One Decision Card

Use synthetic case **OVE-PROC10-OS-SYN001**. The Google workbook supplies editable fields; the deck supports discussion. Together they decode this same sprint rather than adding separate required deliverables.

1. **Need:** one decision, affected population and missing fact.
2. **Evidence:** source/business IDs, specification or scope, validity, unit/currency where relevant.
3. **Owner:** accountable business decision maker, source application and receiving owner.
4. **Gate:** prerequisite, allowed next state and exception condition.
5. **Alternative:** Compare a multi-source sum with a grain-specific reconciled view and explicit coverage.
6. **Recovery:** escalation owner and safe correction/assisted route.
7. **Proof:** three actual paper results, a measure and stop/revise/proceed decision.

**Requirement — OVE-PROC10-OS-REQ01:** publish one measure with defined grain, sources, units, scope, exclusions and reconciliation.

**Decision — OVE-PROC10-OS-ADR01:** record the chosen option, alternative, trade-off and evidence that would change your choice.

## 6. Three tabletop tests

### T01 — PO, receipt and invoice refer to one purchase

**Expected:** Select the intended grain and avoid counting the same economic activity repeatedly.

### T02 — Currency or date basis differs

**Expected:** Reconcile conversion/as-of rules and period scope before comparison.

### T03 — Supplier alias mapping is uncertain

**Expected:** Expose the gap and seek steward review before concentration conclusions.

Record **input → expected → actual paper result → evidence → reviewer decision → revision/retest**. Sprint-local tests OVE-PROC10-OS-T01/T02/T03 support REQ01. Publishing expected results does not prove execution.

**Measure — OVE-PROC10-OS-KPI01:** in-scope measures with approved grain/lineage/reconciliation / measures reviewed. Confirm the owner, baseline, period and exclusions before setting targets.

**Acceptance:** the card names owners and sources, preserves the protected boundary, handles all three tests after documented revisions and explains the decision in 60 seconds. Keep unverified facts visible.

## 7. Your 120 minutes

- **0–20:** read the evolution; explain the problem that persists.
- **20–45:** role-play the lead and counterpart; request evidence.
- **45–65:** map application responsibilities and inspect one resource.
- **65–100:** complete the card and compare the alternative.
- **100–115:** run the three tests and revise from observed paper behavior.
- **115–120:** explain your decision and choose the next experiment.

## 8. Resources and reflection

[SAP Procurement Process Overview](https://learning.sap.com/courses/procurement-process-overview) and [Sourcing and Contract Management learning journey](https://learning.sap.com/learning-journeys/discovering-procurement-sourcing-and-contract-management-in-sap-ariba-and-sap-cloud-erp): read the relevant portion selectively. Which product owns the record, and what must the receiving application acknowledge?

[ISO 20400 sustainable procurement guidance](https://www.iso.org/standard/63026.html): consider stakeholder impact and accountable sustainable purchasing. This educational mapping does not claim certification.

Official reference pages checked 31 October 2026. Historical periodization and future scenarios are teaching synthesis, not facts established by these product pages.

**Reflect:** What changed for the buyer and supplier? Who could be excluded? Which evidence would overturn your preferred option?

**Next Pre-Foundation experiment:** define one spend measure and reconcile three synthetic lifecycle records.

**Mission:** Architecting Experiences for a Better World.

## Sources and traceability

[Executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/executive-one-pager.md) · [Procurement blueprint](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/derived-streams/04-procurement.md) · [Enterprise personas](https://github.com/nbnayak88/successlabs-case-studies/blob/main/01-energy/omniverse-energy-ltd/personas/persona-cards.md) · [Current academy mapping](https://app.notion.com/p/54da2cdc13204086bb4f7fb2387b591a).

Inherited anchors: OVE-M03, OVE-M09, OVE-M10, OVE-M17. New OVE-PROC10-OS IDs belong to this proposed learning expansion.

**Trace:** source → OVE-PROC10-OS-CAP01 → VS01 → REQ01 → ADR01 → EXP01 → T01/T02/T03 → KPI01. Shortened IDs retain the OVE-PROC10-OS prefix. EV01 stays empty until observed evidence is recorded.

**Source reconciliation:** legacy Drive prompt filenames use PROC01 for Ariba Sourcing. They remain preserved. This edition follows the current catalog: PROC01 strategy, PROC02 sourcing, and unchanged APR1–AIG2 course-code sequence.

**Educational alignment:** TOGAF responsibility/options; BIZBOK capability/value; BABOK requirements/acceptance; DAMA data quality; COBIT accountability; ISO/IEC 27001 information protection; ISO 20400 sustainability guidance. No compliance certification is claimed.

[GitHub sprint](https://github.com/nbnayak88/learning-township/blob/main/04-PROC-Procurement-Capability-Academy-Procurement-Thursday/PROC10-AAN0-Architecting-Procurement-Intelligence/01-PROC10-ENE-energy/0-The-Origin-Story/sprint/energy-proc10-origin-story-sprint.md) · [Google Doc](https://docs.google.com/document/d/1-mSwttrTDnMr7Gizp1GgMpVPeZVlS0gLUW0wnBXxI6U/edit?usp=drivesdk)


[Google Slides](https://docs.google.com/presentation/d/1HatcQh0gor6-KiFQDr0zmPTRNOsZQDK50YRr0KYLsIs/edit?usp=drivesdk) · [Google Sheets Decision Card](https://docs.google.com/spreadsheets/d/1zoG-exhyKscmB96doGCQsFz5Zr2fDOR9TpoSi1BH-Yo/edit?usp=drivesdk) · [Notion](https://app.notion.com/p/40ace6de60898150a505dd2d9697e50a?pvs=204) · [All twelve Energy Procurement stories](https://github.com/nbnayak88/learning-township/blob/main/04-PROC-Procurement-Capability-Academy-Procurement-Thursday/energy-origin-stories.md)
