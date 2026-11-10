# The line reported full output; the product was on hold
## SCM04 — Architecting Smart Manufacturing

**SuccessLabs Academy · OmniConnect Media Networks Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-SCM04-COM-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one production flow that separates produced, released and held quantities.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

A production line for a network component at a regional network reports full output, and the shift report shows green.

**Supply chain lead:** Amelia Jones — Subscriber and Enterprise Client Representative (OCN-P15).  
**Counterpart:** Daniel Weber — Director Enterprise Architecture (OCN-P12).  
**Operations or data owner:** Mei Lin — Subscriber Data and Consent Lead (OCN-P09).

Amelia Jones asks what must be true before the team decides. Daniel Weber asks which evidence and owner support the decision. Mei Lin asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic record, units were counted at the line but a quality hold blocked their release, and a sensor reading was stale.

**Pause:** What must be true for this decision to stand? Which evidence is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniConnect Media Networks Ltd. is an aspirational case study (USD 37B communications group; 62,000 employees; 28 countries; 210M subscriptions). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniConnect Media Networks Ltd. history.

- **1970s–1980s:** Output is counted by hand at the line.
- **1980s–1990s:** Plant systems record production; quality is separate.
- **2000s–2010s:** MES and sensors connect lines; data is trusted without checks.
- **2020s–2026:** Assisted monitoring flags anomalies; release and stale-data rules still need owners.

**Mindset shift:** start with the service promise, the evidence and who carries the risk, then choose the model or automation. Automating an unclear step can move the same error faster.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to draft scenarios and flag exceptions; retain the evidence gate, a named decision owner and a challenge route.

**2040 question:** if partners share signals directly, can each node's evidence be visible without exposing commercial detail?

**2050 scene:** Imagine a network that adjusts itself within agreed promises. Providers may react faster, but people must own the promise, the trade-offs and the right to stop.

**Competing future:** A simpler network with buffers, clear fallbacks and trained planners may beat an adaptive one on resilience and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OCN-SCM04-OS-CAP01:** trusted production and release. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OCN-SCM04-OS-VS01:** Plan run → produce → measure → inspect → release or hold → report.

**Objects to distinguish:** line, batch, sensor reading, hold and release.

**Proposed responsibility:** Manufacturing owns the run; quality owns release; the data owner owns sensor sources. SCM04 owns the production flow, not the plant system.

**Protected boundary:** Counted output is not released output, and a sensor reading is not current without a timestamp.

Planning, manufacturing and logistics applications are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole chain. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OCN-SCM04-OS-SYN001**. Synthetic line COM-LN300, batch COM-BT300 on hold, sensor COM-SN300 stale. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare reporting line output with reporting released output.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OCN-SCM04-OS-REQ01:** link one production-release experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OCN-SCM04-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — Output is counted before release

**Expected:** Show produced, released and held quantities separately.

### T02 — A sensor reading is stale

**Expected:** Mark the reading stale; do not act on it as current.

### T03 — A recipe or setting changes mid-run

**Expected:** Record the change with an approver and apply it from that point.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OCN-SCM04-OS-T01/T02/T03, supporting OCN-SCM04-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OCN-SCM04-OS-KPI01:** Share of produced units released without hold, with defined window and exclusions. Assign Amelia Jones as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

**Acceptance:** the card identifies source and owner, preserves the protected boundary, handles all three tests after documented revisions and explains the decision in 60 seconds. Missing evidence remains visible. Record what is still unverified.

## 7. Use your 120 minutes

- **0–20:** read the origin timeline; explain what changed and what did not.
- **20–45:** role-play the story; ask the lead, counterpart and voice one useful question each.
- **45–65:** draw responsibilities and consult one resource selectively.
- **65–100:** complete the single Decision Card and compare the alternative.
- **100–115:** run the three tests; revise from observed paper behavior.
- **115–120:** explain the decision in 60 seconds and choose the next experiment.

All reading fits within these blocks. Do not complete an entire product course during the sprint.

## 8. Read with a question

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): which evidence, owner and monitoring would bound an assisted decision here?
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework/privacy-framework): who owns permitted information use for this card?
- [W3C WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/): can everyone affected perceive, operate and understand the journey?

Official reference pages checked 10 November 2026; access and versions can vary. The historical periods and future stories are educational synthesis, not claims established by these pages.

## 9. Reflect and continue

Whose risk did your option move? Which evidence was missing? What would make you reject your design?

**Next Pre-Foundation experiment:** write one falsifiable supply-chain hypothesis and the observation that would test it.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniConnect Media Networks Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/09-communication-services/omniconnect-media-networks-ltd/personas/persona-cards.md): existing names, designations and OCN-P identifiers.
- **New material:** OCN-SCM04-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OCN-SCM04-OS-CAP01 → OCN-SCM04-OS-VS01 → OCN-SCM04-OS-REQ01 → OCN-SCM04-OS-ADR01 → OCN-SCM04-OS-EXP01 (this tabletop experiment) → OCN-SCM04-OS-T01/T02/T03 → OCN-SCM04-OS-KPI01. OCN-SCM04-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
