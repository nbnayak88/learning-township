# OmniDaily — Enterprise Architecture, SAP Signavio, SAP LeanIX and Clean Core

## Demo 02 of the BTM11 Consumer Staples Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Consumer Staples (CS) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omnidaily-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 03 AI/GenAI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Energy version of this demo](../../../01-BTM11-ENE-energy/05-Ultimate/bootcamp/02-enterprise-architecture-signavio-leanix-clean-core.md)

> **Evidence boundary:** OmniDaily is a **fictional educational case**. This file is an architecture design and teaching demonstration. It is **not** a record of a client implementation. No executed Signavio model, LeanIX inventory, sync run, Clean Core check or realized benefit is asserted. The case source contains little or no SAP landscape detail, so application names, fact sheets, process codes and requirements below are **synthetic placeholders** (prefix `CS-SYN`) and are labelled as new design. Product names are learning examples, not confirmed OmniDaily implementations.

---

## 1. The question this file answers

> *Enterprise architecture experience across SAP Signavio, SAP LeanIX and Clean Core.*

**What this file shows:** how the architect turns this sector's board-level case into (1) a capability and value-stream model, (2) a governed application and technology inventory, (3) a process model linked to that inventory, and (4) a Clean Core rule that decides how every requirement may extend SAP. It ends with a detailed action plan.

**What it does not show:** a delivered engagement. Real project experience is described separately by the presenter and should not be inferred from this file.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 51B staples group; 84,000 employees; 57 countries; 420M households served |
| Business mix | Foods 30%; beverages 23%; home care 19%; personal care 18%; wellness 10% |
| Burning platform | Demand, promotion, planning, product and ingredient data, quality and route-to-market execution fragmented across 160+ applications |

**Decision under discussion (source):** Fund a bounded demand-to-shelf and quality-evidence pilot before approving enterprise scale.

**Illustrative trigger (source):** A promotion creates a shelf gap while a quality-held batch appears available in a delayed distributor feed (invented; no real safety event is claimed).

**Sector constraint carried from the source:** L4 does not imply permission for unsupervised safety decisions; quality-release authority and partner responsibilities are explicit (source M09, M11).

**What the source gives for this demo (Theme C):**

| Source ID | Content (source) | Source deliverable |
|---|---|---|
| ODG-M09 Business capability architecture | Source L2→L4:demand planning, trade promotion, manufacturing/quality, distribution/execution; L1→L4:sustainability/traceability. Maturity scales require definitions; L4 does not imply permission for unsupervised safety decisions. |  |
| ODG-M10 Value streams and process architecture | Source chain:Sense Demand→Source→Make→Assure Quality→Distribute→Sell→Serve→Recover. Illustrative streams:Signal-to-Available-Shelf, Batch-to-Trusted-Release, Promotion-to-Profitable-Growth and Packaging-to-Recovery. Model decisions and exceptions, not just arrows. |  |
| ODG-M11 Target operating model | Source connected planning rhythm, commercial dashboards and cross-functional teams linking brands, sales, factories, supply and technology. Central standards with local ownership; explicit quality-release authority and partner responsibilities are essential. |  |
| ODG-M12 Enterprise architecture and digital enablement | Source Product/Ingredient/Customer/Outlet/Supplier360; ERP, planning, TPM, MES, LIMS, DMS, CRM, e-commerce; API/B2B/event integration; lakehouse/MDM/PIM/ESG; edge/private cloud for factory workloads. Vendor names are proposals, not verified procurement choices. |  |

**Source fictional stakeholder challenge (each M-section):** *What evidence is missing, which persona can authorize the decision, what constraints apply, and how will value be measured?*

**Resolution categories (series vocabulary, not from this case):** Configuration; Enhancement (BAdI / Key User Extensibility); Side-by-Side Extension (BTP); Custom Development (Private Edition only); Process Change; Third-Party Solution; Deferred. These seven categories come from the OmniVerse Energy source register (written in a SuccessFactors Employee Central gap-capture context). They were searched for in this case's source on 2026-11-10 and are **not present there**. This demo reuses them as a shared teaching vocabulary across the series and says so.

## 3. Source versus new design

| Element | Status |
|---|---|
| Capabilities, value-stream names, operating-model statements, M12 perspectives, personas | **Source** |
| Capability-to-owner register, process taxonomy codes, synthetic applications and fact sheets, LeanIX and Signavio data model, Clean Core admission rule, synthetic requirements, tests, action plan | **New design (illustrative)** |
| Any SAP product behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What minimum common architecture model and extension rule does OmniDaily need so that value-stream teams can deliver independently without creating disconnected pilots and brittle interfaces?

**Scope of this demo:** two source value streams, chosen because the source trigger points at them: **Batch-to-Trusted-Release** and **Signal-to-Available-Shelf**. The other streams reuse the same method.

**Accountable decision owner (proposed):** ODG-P05 Sofia Alvarez, with architecture assurance from ODG-P13 Priya Nair. The sponsor (ODG-P01 Anika Mehra) will test every artefact against customer, employee or operational outcomes, not technology.

## 5. Personas and proposed decision rights

IDs, names and roles come from the case persona cards. Decision rights are **proposed** and need discovery validation.

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| ODG-P05 | Sofia Alvarez, Chief Digital and Data Officer | Owns the minimum common platform decision; challenges disconnected pilots |
| ODG-P13 | Priya Nair, Director Enterprise Architecture | Owns standards, the Clean Core admission rule and architecture review |
| ODG-P12 | Omar Haddad, CISO and Privacy Lead | Security and trust-boundary approval for any extension or integration |
| ODG-P08 | Mei Lin, Head of Product and Ingredient Stewardship | Owns data object definitions and stewardship in the inventory |
| ODG-P07 | David Okoro, Global Quality and Product Safety Director | Business owner for Batch-to-Trusted-Release |
| ODG-P10 | Rohan Shah, Distributor and Field Execution Director | Business owner for Signal-to-Available-Shelf |
| ODG-P09 | Elena Petrović, Plant Operations Director | Operational or frontline authority; reality check on process models; veto where operations or safety are at risk |
| ODG-P01 | Anika Mehra, Group CEO | Sponsor; outcome test for every decision |
| ODG-P14 | Diego Costa, Head of Planning Analytics and AI | Planning analytics and AI |

Shared first names across cases do not establish shared identity. Source: [OmniDaily persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md).

## 6. How the toolchain divides the work

Tool roles are described from SAP's public documentation (reviewed 2026-11-10).

| Tool | Role in this design | Source of truth for |
|---|---|---|
| SAP LeanIX | Enterprise architecture inventory: business capabilities, applications, IT components, data objects, organizations, lifecycle, ownership | Applications, business capabilities, organizations, data objects (SAP documentation recommends LeanIX as source of truth for these) |
| SAP Signavio | Process modelling and process navigation; value chains, process diagrams, dictionary/glossary | Process models and diagrams |
| SAP Cloud ALM | Implementation project, scope, requirements, tests, deployment tracking | Delivery records and requirement trace |
| Clean Core guardrail (this design) | Admission rule for every extension | The extension decision record |

**Documented LeanIX to Signavio integration behaviour (verify before relying on it):** processes sync from Signavio to LeanIX only (process diagrams, navigation maps and value chains become business-context fact sheets, with diagram links on the fact sheet). Applications, business capabilities and organizations sync **in both directions** against Signavio dictionary items, and you choose the source and target per mapping. The process hierarchy can be mapped top-down, bottom-up or by a list of Signavio directories. Fact sheets with matching names are linked; otherwise new ones are created. The setup needs a dedicated Signavio user with read and write permission (an API edition licence is recommended), the tenant ID, and a manual or scheduled sync run.

**Consequence for design:** agree one owner per object type **before** the first sync, otherwise two teams can rename the same capability in two tools (tabletop test T2).

## 7. Capability architecture

Capability names come from the source; owners and evidence needs are proposed. The evidence column is the work to do, not a finding.

| Capability (source) | Source maturity statement | Proposed business owner | Evidence needed before scoring | Stream touched |
|---|---|---|---|---|
| Demand planning | L2 to L4 | To be confirmed | Forecast ownership and data sample | Signal-to-Available-Shelf |
| Trade promotion | L2 to L4 | ODG-P10 Rohan Shah | Promotion calendar ownership | Signal-to-Available-Shelf |
| Manufacturing and quality | L2 to L4 | ODG-P07 David Okoro | Hold and release record sample | Batch-to-Trusted-Release |
| Distribution and execution | L2 to L4 | ODG-P10 Rohan Shah | Feed timeliness sample | Signal-to-Available-Shelf |
| Sustainability and traceability | L1 to L4 | ODG-P08 Mei Lin | Ingredient and packaging lineage | Packaging-to-Recovery |

**Rule:** a maturity level is not scored until the scale is written down and an evidence sample exists.

## 8. Value streams and process taxonomy (new design)

Synthetic taxonomy for the two scoped streams. Codes are placeholders, not SAP Scope Item IDs, and must not be presented as such. The stream names are from the source; stages and processes are illustrative.

| Level | Batch-to-Trusted-Release (`CS-SYN-B2R`) | Signal-to-Available-Shelf (`CS-SYN-S2S`) |
|---|---|---|
| L1 value stream | Batch-to-Trusted-Release | Signal-to-Available-Shelf |
| L2 stages | Make, Test, Hold or release, Distribute, Recall check | Sense demand, Plan, Replenish, Execute in store, Review |
| L3 processes (examples) | Record quality hold; Release batch; Notify distributors; Reconcile status with distributor feed; Close hold | Capture demand signal; Plan promotion volume; Replenish outlet; Confirm shelf availability; Handle exception |
| Control points | Quality-release authority; hold status takes precedence over any feed | Promotion plans checked against hold status; as-of time shown on availability |
| Systems of record | ERP, MES, LIMS and distributor management sources (to be mapped) | Planning, trade promotion and distributor sources (to be mapped) |
| Business owner (proposed) | ODG-P07 David Okoro | ODG-P10 Rohan Shah |

**Deliverable pattern:** one Signavio value chain per stream; process diagrams to L3 for the first two or three processes only; each diagram linked to a capability and an owner.

## 9. Application and technology portfolio (synthetic)

Rows are **roles**, not products, so nobody mistakes them for a real inventory.

| Fact sheet (synthetic) | Type | Supports capability | Owner (proposed) | Lifecycle | Disposition (proposed) | Evidence needed |
|---|---|---|---|---|---|---|
| CS-SYN-APP-01 Enterprise resource planning application | Application | Manufacturing and quality; Demand planning | ODG-P07 David Okoro | Unknown | To be decided | Version and extensions |
| CS-SYN-APP-02 Planning and trade promotion applications | Application | Demand planning; Trade promotion | ODG-P10 Rohan Shah | Unknown | To be decided | Calendar interfaces |
| CS-SYN-APP-03 Manufacturing execution and laboratory applications | Application | Manufacturing and quality | ODG-P07 David Okoro | Unknown | To be decided | Plant interfaces and hold workflow |
| CS-SYN-APP-04 Distributor management application | Application | Distribution and execution | ODG-P10 Rohan Shah | Unknown | To be decided | Feed frequency and partner access |
| CS-SYN-APP-05 Product and ingredient master application | Application | Sustainability and traceability | ODG-P08 Mei Lin | Unknown | To be decided | Data owner and quality |
| CS-SYN-APP-06 Integration and event layer | IT component | All | ODG-P05 Sofia Alvarez | Unknown | To be decided | Existing integration catalogue |

**Disposition values stay "to be decided"** until lifecycle, cost and fit evidence exists. Do not present a disposition as a finding.

**Fact sheet minimum attributes (new design):** name; type; description; business owner; technical owner; lifecycle phase and dates; data classification; hosting; interfaces in and out; supported capabilities; supported processes; criticality; last review date; source of record. A fact sheet without an owner and a review date is not counted as governed.

**Relations to model:** capability to application; application to process (via Signavio link); application to data object; application to IT component; application to interface; organization to capability.

## 10. Clean Core admission rule (new design on a verified SAP concept)

**Verified concept (SAP News, August 2025; reviewed 2026-11-10):** SAP describes a Clean Core level concept that sorts extensions into four levels by architectural integrity and upgrade safety.

| Level | SAP description (summarised) | Design use |
|---|---|---|
| A | Fully compliant: only publicly released, stable SAP interfaces, backed by stability contracts. Side-by-side on SAP BTP; on-stack through the ABAP Cloud model with released APIs | Default admission |
| B | Compliant: may use classic APIs that are documented and generally upgrade-stable | Allowed with owner approval |
| C | Partially compliant: accesses SAP internal objects; higher upgrade risk | Exception only, with expiry and named owner |
| D | Not recommended: modifications, writes to SAP tables, implicit enhancements; highest risk and technical debt | Rejected by default; needs an architecture exception at decision-owner level |

**Applicability warning:** the level concept is described in the context of SAP S/4HANA. Confirm which levels, tooling and wording apply to the actual product and edition before using it with a real client. This case does not state that OmniDaily runs S/4HANA.

**Mapping the series resolution categories to levels (proposed):**

| Resolution category (series vocabulary) | Typical Clean Core level | Admission question |
|---|---|---|
| Configuration | Not an extension | Is the outcome achievable and documented in standard settings? |
| Enhancement (key-user or released extension point) | Level A if only released mechanisms are used | Is the extension mechanism released for the actual product? |
| Side-by-Side Extension (BTP) | Level A if only released APIs and events are used | Are APIs and events released, security and lifecycle owned, cost compared? |
| Custom Development (Private Edition only) | A, B, C or D depending on what it touches | Which objects does it touch, and is a stricter alternative possible? |
| Process Change | Not an extension | Has the business owner approved adoption and control equivalence? |
| Third-Party Solution | Assessed separately | Support, privacy, integration, commercial and exit implications |
| Deferred | Not applicable | Consequence, review trigger and owner recorded? |

**Admission order (decision tree):** (1) configuration, (2) process change, (3) released in-app extension, (4) side-by-side on released APIs, (5) third-party, (6) classic API use with approval, (7) exception for internal object access, (8) deferred. Anything needing level D is returned to the requester with alternatives.

**Extension Decision Record (one page per requirement):** requirement ID; process and capability; source reference; resolution category; proposed Clean Core level and why; objects and APIs touched; alternatives considered; owner; decision authority and date; exception expiry (levels C and D); test links; evidence status.

## 11. Hands-on exercise: classify eight synthetic requirements

All requirements are synthetic. Participants fill the three blank columns without looking at the key. The key is a teaching answer to be debated, not an SAP certification of any item.

| ID | Synthetic requirement | Participant: category | Participant: level | Participant: decision | Proposed answer (teaching key) |
|---|---|---|---|---|---|
| CS-SYN-RQ-01 | Add a hold-reason field to the batch status screen |  |  |  | Enhancement; Level A if a released key-user mechanism covers it; else side-by-side |
| CS-SYN-RQ-02 | Compute an as-of-time availability indicator across holds and distributor feeds for planners |  |  |  | Side-by-side on BTP; Level A only if released APIs and events suffice |
| CS-SYN-RQ-03 | Read an SAP internal table directly for a legacy promotion report |  |  |  | Level C; reject unless no released alternative exists; exception with expiry |
| CS-SYN-RQ-04 | Write directly to an SAP table to change a batch from held to available |  |  |  | Level D; reject; quality-release authority; route to Quality |
| CS-SYN-RQ-05 | Integrate distributor sell-out through a documented classic interface |  |  |  | Level B; allowed with owner approval; plan migration to a released API |
| CS-SYN-RQ-06 | Route availability exceptions by region with a new rule |  |  |  | Configuration first; extension only if configuration cannot do it |
| CS-SYN-RQ-07 | Replace packaging-recovery tracking with an external tool |  |  |  | Third-party; assess partner data, integration, exit |
| CS-SYN-RQ-08 | Advanced price-pack optimization not needed this year |  |  |  | Deferred with consequence, review date and owner |

**Time:** 25 minutes. **Output:** eight Extension Decision Records, at least two argued as exceptions.

## 12. Three tabletop tests

A tabletop test is a paper walk-through. It is not a technical test of a running tenant.

| Test | Scenario | Expected result | Actual paper result | Correction | Pass or revise |
|---|---|---|---|---|---|
| T1 Level D request on a quality hold | A planner asks for a direct table write to release a held batch for a promotion | Admission rule rejects level D; quality-release authority respected; escalation to Quality |  |  |  |
| T2 Two tools, two names | Product renames a brand group in one tool while the inventory keeps the old name before sync | Owner rule decides direction; conflict reported; register updated |  |  |  |
| T3 Stale feed in the dependency view | A distributor feed link is stale; the impact view hides a live dependency on holds | Freshness rule flags it; view states as-of time; owner re-certifies |  |  |  |

## 13. Detailed action plan

This is a **proposed** plan. Durations are working-day estimates for a first bounded pass on two value streams, not commitments. Owners are proposed personas. Every action has an artefact and an acceptance check so it can be inspected.

### Phase 0: Frame the decision

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-01 | Confirm the decision statement in Section 4 and the two scoped streams | ODG-P05 | Case Theme C; sponsor view | One-page decision brief | ODG-P05 and ODG-P13 sign it; sponsor outcome question answered | 1 |
| A-02 | Name one owner per object type: capability, process, application, data object, organization | ODG-P13 | Section 6 | Object ownership rule | No object type has two owners | 1 |
| A-03 | Write the evidence-gap list: what is missing, who can authorize, constraints, how value is measured (source challenge) | ODG-P13 | Section 2 | Evidence-gap register | Every gap has an owner and a due date | 2 |
| A-04 | Agree the standing rule: nothing is scored or targeted without a baseline | ODG-P05 | Source rule | Governance note | Rule appears in the review checklist | 0.5 |

### Phase 1: Capability and value-stream model

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-05 | Write the capability maturity scale (what each level means, observably) | ODG-P13 with business owners | Source capability statements | Scale definition page | Each level has an observable test | 2 |
| A-06 | Build the capability map and owner register (Section 7) | ODG-P13 | A-02, A-05 | Capability map; owner register | Source capabilities present; owners confirmed or marked TBC | 3 |
| A-07 | Collect evidence samples for the capabilities touched by the two streams only | ODG-P07, ODG-P10, ODG-P08 | A-05 | Evidence samples | Sample method documented; no invented scores | 5 |
| A-08 | Draw the two value streams and stage-capability matrices (Section 8) | ODG-P07, ODG-P10 | Source stream names | Value-stream maps | Each stage maps to a capability and an owner | 3 |
| A-09 | Walk the maps with the operational authority to find what the diagram misses | ODG-P09 | A-08 | Findings log | At least one change or an explicit "no change" recorded | 1 |

### Phase 2: Process model (Signavio)

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-10 | Set the process taxonomy and naming rules (Section 8) | ODG-P13 | A-08 | Naming and level standard | Two reviewers apply it to the same process and get the same code | 1 |
| A-11 | Model two or three L3 processes per stream with owners and control points | Process owners | A-10 | Process diagrams | Owner has read back and accepted each diagram | 5 |
| A-12 | Record glossary or dictionary entries for capabilities, applications, organizations | ODG-P08 | A-06 | Dictionary entries | No duplicates; names match the owner register | 2 |
| A-13 | Mark every process step that touches operational authority, consent or a regulated control | ODG-P09 and ODG-P07 | A-11 | Control-point overlay | Each marked step names its approver | 1 |

### Phase 3: Inventory (LeanIX) and integration

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-14 | Define the fact sheet attributes and data-quality rules (Section 9) | ODG-P13 and ODG-P08 | A-02 | Inventory standard | Rules testable by a script or a checklist | 2 |
| A-15 | Load the scoped applications as fact sheets with owners, lifecycle and interfaces | Technical owners | A-14 | Inventory for scoped streams | Every fact sheet has an owner and a review date | 5 |
| A-16 | Decide sync direction per object type, mapping and schedule | ODG-P13 | A-02, A-12 | Sync design note | Matches the owner rule; one source of truth per type | 1 |
| A-17 | Obtain the dedicated integration user and confirm permissions and licensing | ODG-P12 and ODG-P13 | A-16 | Access record | Least privilege; credentials held in a managed secret store | 2 |
| A-18 | Run a first sync in a non-production or sandbox setting and review conflicts | ODG-P13 | A-16, A-17 | Sync report | Every conflict has a resolution; unexpected changes explained | 2 |
| A-19 | Produce one dependency view: process, application, data, interface | ODG-P13 | A-15, A-18 | Impact view | Freshness statement included; one known dependency verified by hand | 2 |

### Phase 4: Clean Core guardrail and delivery tracking

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-20 | Confirm which Clean Core levels, tools and terms apply to the actual SAP products and editions in scope | ODG-P13 | Current SAP documentation | Applicability note | Wording checked against SAP sources on a stated date | 1 |
| A-21 | Approve the admission rule and exception policy (Section 10) | ODG-P05, ODG-P13, ODG-P12 | A-20 | Admission rule v1 | Level D default rejection and exception expiry written | 1 |
| A-22 | Create the Extension Decision Record template and the decision log | ODG-P13 | A-21 | Template and log | Template fits on one page; log fields match source attributes | 1 |
| A-23 | Run the eight-requirement exercise with real reviewers and refine the rule | ODG-P13 | Section 11 | Revised rule and key | Reviewers agree on at least the A and D cases; disagreements logged | 1 |
| A-24 | Link requirements to processes and resolution categories in the delivery tool (validate tenant features first) | Delivery lead | A-21 | Traceable requirement set | Every approved requirement has category, level, owner, tests | 2 |

### Phase 5: Prove it on paper, then decide

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-25 | Run tabletop tests T1 to T3 and revise | ODG-P13 with ODG-P12 | Section 12 | Test sheet | Each test has actual result and pass or revise | 1 |
| A-26 | Define review cadence: monthly architecture review; quarterly inventory re-certification | ODG-P13 | A-14 | Review calendar | Dates set; owners named | 0.5 |
| A-27 | Select the measures and capture baselines before any target | ODG-P05 | Section 14 | Baseline sheet | Targets blank until baselines exist | 2 |
| A-28 | Present the decision pack to the sponsor and finance: what was built, what is evidence, what is not | ODG-P05 | All | Decision pack | Open questions and evidence gaps are visible, not hidden | 1 |

**Critical path (proposed):** A-02, A-05, A-08, A-10, A-14, A-16, A-18, A-21. Phases 2 and 3 can overlap once A-10 and A-14 are done.

### Presenter action items for the technical discussion

These are for the trainer preparing to show this demo to a corporate audience. They do not appear in the case.

| ID | Action | Why | Done when |
|---|---|---|---|
| P-01 | Decide which parts you will show live and which on paper; label each as sandbox, vendor-provided or paper | Honesty about what was actually exercised | Slide or note states the status of every screen |
| P-02 | Confirm access to a Signavio and a LeanIX environment, or prepare static screenshots from your own training sandbox | The vendor is expected to provide demo systems | Access confirmed in writing, or fallback ready |
| P-03 | Load the synthetic fact sheets from Section 9 and one synthetic process for Batch-to-Trusted-Release | Gives a concrete walkthrough | Records carry the `CS-SYN` prefix |
| P-04 | Rehearse the 25-minute classification exercise with a colleague | Timing and disagreements | Timing and key adjusted |
| P-05 | Prepare the one-page answer to "have you done this for a client?" using your real engagements, kept separate from this file | Do not imply that fictional work is client work | Answer reviewed by you; no client names without permission |
| P-06 | Re-check the SAP sources listed in Section 17 for changes the day before delivery | Product guidance changes | Review date updated |
| P-07 | Record the session run log (Section 16) | Evidence trail | Log completed with what was actually run |

## 14. Acceptance and measures

**The design is acceptable for a bounded first pass only if:** one owner exists per object type; the two scoped streams have capability and process models read back by their owners; scoped applications have owners and review dates; the admission rule and exception policy are approved; tabletop tests are walked through; and the evidence status below is honest.

**Candidate measures (no baseline, no target supplied):**

| Measure | Definition | Baseline status |
|---|---|---|
| Governed fact sheet share | Scoped fact sheets with owner, lifecycle and review date divided by scoped fact sheets | Not measured |
| Requirement traceability | Approved requirements with category, level, owner and tests divided by approved requirements | Not measured |
| Exception count and age | Open level C and D exceptions, with age against expiry | Not measured |
| Sync conflicts | Conflicts found per sync run and time to resolve | Not measured |
| Inventory freshness | Fact sheets reviewed within the review period | Not measured |

**Do not invent a baseline, benefit or target.** Set a target only after measuring a baseline with the accountable owner.

## 15. Fit in a 2 to 3 hour session

| Minutes | Activity | Output |
|---|---|---|
| 0 to 20 | Case briefing; decision and personas (Sections 2 to 5) | Decision statement and owner |
| 20 to 50 | Toolchain roles and ownership rule (Section 6); capability and value-stream view (Sections 7 and 8) | Ownership rule; map sketch |
| 50 to 80 | Portfolio and fact sheet standard (Section 9) | Fact sheet template filled for two rows |
| 80 to 125 | Clean Core levels, admission rule and the eight-requirement exercise (Sections 10 and 11) | Eight decision records |
| 125 to 150 | Three tabletop tests (Section 12) | Pass or revise decisions |
| 150 to 180 | Action plan walk-through (Section 13); recall check; assessment; attendance | Assessment record |

This is a proposed teaching pattern, not a committed schedule.

## 16. Evidence status and limits

| Item | Status |
|---|---|
| Capability, value-stream and portfolio design | Designed, not executed |
| Fact sheets and requirements | Synthetic placeholders |
| Signavio and LeanIX sync | Described from public documentation; not run here |
| Clean Core classification of the eight requirements | Teaching key; not an SAP classification |
| Tabletop tests | Template; paper results filled in session |
| Real client delivery | Not represented by this file |

**Run log (fill only with what was actually run):**

| Date | Environment | Items run | Result | Notes |
|---|---|---|---|---|
|  |  |  |  |  |

## 17. Resources and sources

- SAP News, [Extend SAP S/4HANA Cloud the right way: clean and clear](https://news.sap.com/2025/08/extend-sap-s4hana-cloud-right-way-clean-clear/) (Clean Core level concept; reviewed 2026-11-10)
- SAP LeanIX documentation, [SAP Signavio integration](https://docs-eam.leanix.net/docs/technical-signavio) (reviewed 2026-11-10)
- SAP Learning, [Integrating SAP LeanIX and SAP Signavio](https://learning.sap.com/courses/sap-signavio-process-management/integrating-sap-leanix-and-sap-signavio-3)
- Case: [OmniDaily](https://github.com/nbnayak88/successlabs-case-studies/tree/main/05-consumer-staples/omnidaily-consumer-goods-ltd) · [Theme C architecture (ODG-M09 to M12)](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/master/theme-c-architecture.md) · [source and assumptions](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/references/source-and-assumptions.md) · [persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/05-consumer-staples/omnidaily-consumer-goods-ltd/personas/persona-cards.md)
- Series baseline: [Demo 01](01-omnidaily-case-baseline-sap-nextgen-architecture.md)

**Educational alignment:** TOGAF for architecture views and decisions; BIZBOK for capability and value-stream distinctions; BABOK for needs and acceptance; DAMA for data ownership and quality; COBIT for accountable control. These mappings are educational and are not compliance certification or reproduction of proprietary standards.

**Publication note:** this is a demonstration file in the bootcamp folder. It is not proof that a course is live, purchasable or delivered.
