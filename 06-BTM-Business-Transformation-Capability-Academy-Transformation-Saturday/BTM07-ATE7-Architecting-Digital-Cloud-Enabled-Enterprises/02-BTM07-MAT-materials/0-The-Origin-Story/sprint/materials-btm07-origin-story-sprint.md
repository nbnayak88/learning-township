# The workload moved to the cloud; the control did not move with it
## BTM07 — Architecting Digital and Cloud-Enabled Enterprises

**SuccessLabs Academy · OmniForge Materials Ltd. · Level 0 → Pre-Foundation**  
**IIL — Industry Immersion Lab · Version 1.0 · 10 November 2026**  
**Planning reference:** HUB-ORIGIN-BTM07-MAT-sprint (not an LMS ID)  
**Format:** Origin Story Sprint · 120 minutes · Free — Community/Citizen Edition  
**Status:** Published learning content; not an enrolled course or certification.

> **Your promise:** In two hours, design one cutover decision that proves controls and dependencies moved with the workload.

**One story · One build card · Three tabletop tests**

## 1. Start with the story

A workload for a plant modernization at a materials business unit migrates to the cloud on schedule, and cost and speed improve.

**Transformation lead:** Sofia de Vries — Chief Digital and Sustainability Officer (OMF-P04).  
**Counterpart:** Priya Nair — Director Enterprise Architecture (OMF-P13).  
**Business or data owner:** Hassan Al-Farsi — CISO and OT Security Lead (OMF-P12).

Sofia de Vries asks what must be true before the team decides. Priya Nair asks which evidence and owner support the decision. Hassan Al-Farsi asks for the outcome that matters to the people affected.

**Evidence reveal:** In the synthetic record, an access control was not migrated, and a dependency was undocumented.

**Pause:** What must be true for this decision to stand? Which evidence is missing, and who can confirm it? Ask the counterpart one discovery question before choosing a solution.

**Case boundary:** OmniForge Materials Ltd. is an aspirational case study (USD 42B materials group; 46,000 employees; 31 countries). These incidents, services and dialogue are proposed learning scenarios, not corporate history, confirmed deployments or achieved results. Preserve the enterprise persona IDs above. Country-specific permissions, contracts and operating rules require validation; this sprint does not invent them.

## 2. Trace the origin: 1970–2026

These overlapping periods are teaching lenses, not invention dates or a universal adoption sequence. Earlier practices can coexist with newer ones. Pre-1978 scenes describe the wider domain, not OmniForge Materials Ltd. history.

- **1970s–1980s:** Applications run on in-house machines.
- **1980s–1990s:** Client-server and outsourcing shift hosting.
- **2000s–2010s:** Virtualization and early cloud spread; controls are rebuilt unevenly.
- **2020s–2026:** Cloud-native and assisted migration speed moves; evidence of controls still needs people.

**Mindset shift:** start with the decision, its evidence and its owner, then choose the tool or programme. Digitizing an unclear decision can accelerate the same mistake.

**Pause:** Which old problem survives in a newer interface? Who bears its cost?

## 3. Explore possible futures: 2030–2050

**2030 experiment:** allow assistance to draft options and flag gaps; retain the evidence gate, a named decision owner and a challenge route.

**2040 question:** if the enterprise and its partners share more signals, can each decision carry its evidence and owner without losing trust or choice?

**2050 scene:** Imagine an enterprise that adjusts within agreed boundaries. Providers may act faster, but people must own the purpose, the trade-offs and the right to stop.

**Competing future:** A simpler, well-owned way of working with trained people may beat a larger transformation on reliability, cost and trust.

All future passages are design hypotheses, not forecasts or product roadmaps. Test a useful part today rather than assume the future will arrive as described.

## 4. Draw the smallest useful architecture

**Capability — OMF-BTM07-OS-CAP01:** controlled cloud cutover. A capability is an ability; it is not an application or a sequence of steps.

**Value stages — OMF-BTM07-OS-VS01:** Assess workload → map controls and dependencies → migrate → test → cut over → run.

**Objects to distinguish:** workload, control, dependency, cutover and running cost.

**Proposed responsibility:** The workload owner owns the move; security owns controls; operations owns running cost. BTM07 owns the cutover decision, not the cloud platform.

**Protected boundary:** A workload that runs in the cloud is not controlled unless its controls and dependencies moved with it.

Transformation, architecture and platform applications are optional demonstration candidates, chosen after requirements. No product is assumed installed, licensed or able to cover the whole programme. This sprint focuses on application responsibility while referencing data, integration and security owners.

## 5. Build one Decision Card

Use synthetic case **OMF-BTM07-OS-SYN001**. Synthetic workload MAT-WL300, control MAT-CT300 not migrated, dependency MAT-DP300 undocumented. Keep everything on one card or screen.

1. **Need:** the outcome, affected people and one missing fact.
2. **Evidence:** relevant object IDs, source, validity or effective time, data purpose and permitted access.
3. **Ownership:** business decision owner, authoritative application and receiving owner.
4. **Gate:** prerequisite, allowed next state, authorized actor and the message anyone affected will see.
5. **Alternative:** Compare cutting over on schedule with requiring evidenced controls and dependencies.
6. **Exception:** one failure state, escalation owner and a safe recovery or assisted route.
7. **Proof:** the three results below, one measure and a stop, revise or proceed decision.

**Requirement — OMF-BTM07-OS-REQ01:** link one cloud-cutover experiment hypothesis to an owned intervention and observed follow-up, including negative evidence.

**Decision — OMF-BTM07-OS-ADR01:** record your chosen option and the alternative from item 5, one trade-off, and the evidence that would change your choice.

## 6. Run three tabletop tests

### T01 — A control is not migrated with the workload

**Expected:** Block cutover until the control is evidenced.

### T02 — A dependency is undocumented

**Expected:** Record and test it before cutover.

### T03 — A cost saving ignores a new running cost

**Expected:** Report total cost before claiming a saving.

For each, record **input → expected → actual paper result → evidence note → revision → retest**. These are sprint-local tests OMF-BTM07-OS-T01/T02/T03, supporting OMF-BTM07-OS-REQ01. A completed lesson is not an executed tenant test.

**Measure — OMF-BTM07-OS-KPI01:** Share of cutovers with evidenced controls and dependencies; define window and exclusions. Assign Sofia de Vries as proposed measure owner, establish the baseline and exclusions, and review after the experiment. No numeric improvement is asserted.

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

Who carries the risk of your option? Which evidence was missing? What would make you reject your design?

**Next Pre-Foundation experiment:** write one falsifiable transformation hypothesis and the observation that would test it.

**SuccessLabs mission:** Architecting Experiences for a Better World.

## Source traceability

- [OmniForge Materials Ltd. executive case](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/executive-one-pager.md): aspirational enterprise baseline. Existing targets remain targets.
- [Enterprise persona register](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md): existing names, designations and OMF-P identifiers.
- **New material:** OMF-BTM07-OS is a new sprint-local namespace. The scenario, requirement, alternative, tests and measure are proposed learning designs, not an approved enterprise implementation.

**Trace:** source case → OMF-BTM07-OS-CAP01 → OMF-BTM07-OS-VS01 → OMF-BTM07-OS-REQ01 → OMF-BTM07-OS-ADR01 → OMF-BTM07-OS-EXP01 (this tabletop experiment) → OMF-BTM07-OS-T01/T02/T03 → OMF-BTM07-OS-KPI01. OMF-BTM07-OS-EV01 is an empty evidence slot until a learner records actual results.

**Educational alignment:** TOGAF responsibility and options; BIZBOK capability and value; BABOK need-to-acceptance trace; DAMA ownership and quality; COBIT decision accountability; ISO/IEC 27001 information-protection principles. This mapping does not establish compliance or certification.

**Publication:** Published learning content. No live implementation or achieved outcome is claimed.
