# OmniForge Materials — Enterprise Architecture, SAP Signavio, SAP LeanIX and Clean Core

## Demo 02 of the BTM11 Materials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Materials (MAT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniforge-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 03 AI/GenAI on SAP BTP](03-ai-genai-rag-agents-sap-btp.md) · [Energy version of this demo](../../../01-BTM11-ENE-energy/05-Ultimate/bootcamp/02-enterprise-architecture-signavio-leanix-clean-core.md)

> **Evidence boundary:** OmniForge Materials is a **fictional educational case**. This file is an architecture design and teaching demonstration. It is **not** a record of a client implementation. No executed Signavio model, LeanIX inventory, sync run, Clean Core check or realized benefit is asserted. The case source contains little or no SAP landscape detail, so application names, fact sheets, process codes and requirements below are **synthetic placeholders** (prefix `MAT-SYN`) and are labelled as new design. Product names are learning examples, not confirmed OmniForge implementations.

---

## 1. The question this file answers

> *Enterprise architecture experience across SAP Signavio, SAP LeanIX and Clean Core.*

**What this file shows:** how the architect turns this sector's board-level case into (1) a capability and value-stream model, (2) a governed application and technology inventory, (3) a process model linked to that inventory, and (4) a Clean Core rule that decides how every requirement may extend SAP. It ends with a detailed action plan.

**What it does not show:** a delivered engagement. Real project experience is described separately by the presenter and should not be inferred from this file.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 42B materials group; 46,000 employees; 31 countries |
| Business mix | Steel and alloys 30%; cement and aggregates 22%; chemicals 20%; mining and minerals 16%; advanced materials 12% |
| Burning platform | Disconnected mining, production, logistics, quality, sales and recycling; 180+ applications; weak material genealogy; manual ESG reconciliation |

**Decision under discussion (source):** Select a bounded materials-traceability and reliability pilot before committing an enterprise rollout.

**Illustrative trigger (source):** A customer queries a shipped batch's certificate after a laboratory correction, while a kiln reliability alert and uncertain recycled-feedstock records expose the same trust gap (illustrative hero trigger in the case).

**Sector constraint carried from the source:** L4 does not authorize autonomous safety-critical control (source). Plant stop authority and commercial accountability stay local (source M11).

**What the source gives for this demo (Theme C):**

| Source ID | Content (source) | Source deliverable |
|---|---|---|
| OMF-M09 Business capability architecture | Source maturity: asset management L2→L4, production optimization L2→L4, quality L2→L4, supply-chain planning L2→L4, sustainability reporting L1→L4. Scale definitions and evidence must be created; L4 does not authorize autonomous safety-critical control. |  |
| OMF-M10 Value streams and process architecture | Source chain Explore→Extract→Process→Manufacture→Distribute→Recover→Reuse. Illustrative cross-enterprise streams: Feedstock-to-Qualified-Material, Asset-to-Reliability, Order-to-Trusted-Delivery, Recover-to-Reuse and Evidence-to-Carbon-Claim. |  |
| OMF-M11 Target operating model | Source calls for a Chief Digital and Sustainability Officer, cross-functional steering and plant product teams. Central definitions and assurance coexist with local process ownership, plant stop authority and commercial accountability. |  |
| OMF-M12 Enterprise architecture and digital enablement | Source architecture: Asset/Material/Product/Supplier/Customer 360, ERP/MES/EAM/LIMS/mine planning, APIs/events/B2 B and governed data products; edge for plant controls and hybrid cloud for enterprise workloads. Vendor names are source architecture proposals, not validated selections. Carbon and quality evidence require lineage. |  |

**Source fictional stakeholder challenge (each M-section):** *What evidence is missing, which persona can authorize the decision, what constraints apply, and how will value be measured?*

**Resolution categories (series vocabulary, not from this case):** Configuration; Enhancement (BAdI / Key User Extensibility); Side-by-Side Extension (BTP); Custom Development (Private Edition only); Process Change; Third-Party Solution; Deferred. These seven categories come from the OmniVerse Energy source register (written in a SuccessFactors Employee Central gap-capture context). They were searched for in this case's source on 2026-11-10 and are **not present there**. This demo reuses them as a shared teaching vocabulary across the series and says so.

## 3. Source versus new design

| Element | Status |
|---|---|
| Capabilities, value-stream names, operating-model statements, M12 perspectives, personas | **Source** |
| Capability-to-owner register, process taxonomy codes, synthetic applications and fact sheets, LeanIX and Signavio data model, Clean Core admission rule, synthetic requirements, tests, action plan | **New design (illustrative)** |
| Any SAP product behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** What minimum common architecture model and extension rule does OmniForge need so that value-stream teams can deliver independently without creating disconnected pilots and brittle interfaces?

**Scope of this demo:** two source value streams, chosen because the source trigger points at them: **Order-to-Trusted-Delivery** and **Asset-to-Reliability**. The other streams reuse the same method.

**Accountable decision owner (proposed):** OMF-P04 Sofia de Vries, with architecture assurance from OMF-P13 Priya Nair. The sponsor (OMF-P01 Ananya Deshpande) will test every artefact against customer, employee or operational outcomes, not technology.

## 5. Personas and proposed decision rights

IDs, names and roles come from the case persona cards. Decision rights are **proposed** and need discovery validation.

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OMF-P04 | Sofia de Vries, Chief Digital and Sustainability Officer | Owns the minimum common platform decision; challenges disconnected pilots |
| OMF-P13 | Priya Nair, Director Enterprise Architecture | Owns standards, the Clean Core admission rule and architecture review |
| OMF-P12 | Hassan Al-Farsi, CISO and OT Security Lead | Security and trust-boundary approval for any extension or integration |
| OMF-P14 | Diego Alvarez, Head of Data Governance and AI | Owns data object definitions and stewardship in the inventory |
| OMF-P08 | Rohan Kulkarni, Head of Quality and Laboratories | Business owner for Order-to-Trusted-Delivery |
| OMF-P07 | Elena Petrova, Cement Plant Director | Business owner for Asset-to-Reliability |
| OMF-P16 | Nikhil Sen, Shift Supervisor and Workforce Representative | Operational or frontline authority; reality check on process models; veto where operations or safety are at risk |
| OMF-P01 | Ananya Deshpande, Group CEO | Sponsor; outcome test for every decision |
| OMF-P10 | Li Wei, Chief Commercial and Customer Officer | Customer communication impact of certificate decisions |

Shared first names across cases do not establish shared identity. Source: [OmniForge Materials persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md).

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
| Asset management | L2 to L4 | OMF-P07 Elena Petrova | Plant condition data quality sample | Asset-to-Reliability |
| Production optimization | L2 to L4 | OMF-P07 Elena Petrova | Definition of L2 and L4 on one page | Asset-to-Reliability |
| Quality | L2 to L4 | OMF-P08 Rohan Kulkarni | Certificate revision and correction record sample | Order-to-Trusted-Delivery |
| Supply-chain planning | L2 to L4 | To be confirmed | Supplier and material master ownership | Feedstock-to-Qualified-Material |
| Sustainability reporting | L1 to L4 | To be confirmed | Carbon and quality evidence lineage | Evidence-to-Carbon-Claim |

**Rule:** a maturity level is not scored until the scale is written down and an evidence sample exists.

## 8. Value streams and process taxonomy (new design)

Synthetic taxonomy for the two scoped streams. Codes are placeholders, not SAP Scope Item IDs, and must not be presented as such. The stream names are from the source; stages and processes are illustrative.

| Level | Order-to-Trusted-Delivery (`MAT-SYN-O2D`) | Asset-to-Reliability (`MAT-SYN-A2R`) |
|---|---|---|
| L1 value stream | Order-to-Trusted-Delivery | Asset-to-Reliability |
| L2 stages | Order, Make, Test and certify, Ship, Support claim | Detect condition, Assess risk, Plan work, Execute work, Verify and learn |
| L3 processes (examples) | Issue batch certificate; Record laboratory correction; Notify affected customers; Reconcile certificate with batch genealogy; Close customer query | Raise kiln condition alert; Review alert with plant; Plan maintenance window; Issue and close work order; Record failure cause |
| Control points | Quality releases certificates; no compliance statement while a correction is open | Plant stop authority; OT write access stays within plant safety boundaries |
| Systems of record | ERP, LIMS and certificate records (to be mapped) | EAM, MES and condition sources (to be mapped) |
| Business owner (proposed) | OMF-P08 Rohan Kulkarni | OMF-P07 Elena Petrova |

**Deliverable pattern:** one Signavio value chain per stream; process diagrams to L3 for the first two or three processes only; each diagram linked to a capability and an owner.

## 9. Application and technology portfolio (synthetic)

Rows are **roles**, not products, so nobody mistakes them for a real inventory.

| Fact sheet (synthetic) | Type | Supports capability | Owner (proposed) | Lifecycle | Disposition (proposed) | Evidence needed |
|---|---|---|---|---|---|---|
| MAT-SYN-APP-01 Enterprise resource planning application | Application | Quality; Supply-chain planning | OMF-P08 Rohan Kulkarni | Unknown | To be decided | Version, interfaces, certificate objects |
| MAT-SYN-APP-02 Laboratory information management application | Application | Quality | OMF-P08 Rohan Kulkarni | Unknown | To be decided | Correction workflow and data owner |
| MAT-SYN-APP-03 Plant maintenance and asset application | Application | Asset management | OMF-P07 Elena Petrova | Unknown | To be decided | OT boundary and data flow |
| MAT-SYN-APP-04 Manufacturing execution application | Application | Production optimization | OMF-P07 Elena Petrova | Unknown | To be decided | Plant interfaces and criticality |
| MAT-SYN-APP-05 Customer portal and certificate delivery | Application | Quality | OMF-P08 Rohan Kulkarni | Unknown | To be decided | Channels and access model |
| MAT-SYN-APP-06 Integration and event layer | IT component | All | OMF-P04 Sofia de Vries | Unknown | To be decided | Existing integration catalogue |

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

**Applicability warning:** the level concept is described in the context of SAP S/4HANA. Confirm which levels, tooling and wording apply to the actual product and edition before using it with a real client. This case does not state that OmniForge runs S/4HANA.

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
| MAT-SYN-RQ-01 | Add a laboratory-correction reason field to the batch certificate screen |  |  |  | Enhancement; Level A if a released key-user mechanism covers it; else side-by-side |
| MAT-SYN-RQ-02 | Compute a certificate-status indicator from correction and genealogy records and show it to customer service |  |  |  | Side-by-side on BTP; Level A only if released APIs and events suffice |
| MAT-SYN-RQ-03 | Read an SAP internal table directly for a legacy batch report |  |  |  | Level C; reject unless no released alternative exists; exception with expiry |
| MAT-SYN-RQ-04 | Write directly to an SAP table to mark a certificate as re-issued |  |  |  | Level D; reject; ask for the business outcome and offer a released API or process change |
| MAT-SYN-RQ-05 | Integrate laboratory results through a documented classic interface |  |  |  | Level B; allowed with owner approval; plan migration to a released API |
| MAT-SYN-RQ-06 | Route customer certificate queries to the right quality desk by product family |  |  |  | Configuration first; extension only if configuration cannot do it |
| MAT-SYN-RQ-07 | Replace carbon-claim evidence tracking with an external tool |  |  |  | Third-party; assess support, lineage, integration, exit |
| MAT-SYN-RQ-08 | Advanced yield analytics not needed this year |  |  |  | Deferred with consequence, review date and owner |

**Time:** 25 minutes. **Output:** eight Extension Decision Records, at least two argued as exceptions.

## 12. Three tabletop tests

A tabletop test is a paper walk-through. It is not a technical test of a running tenant.

| Test | Scenario | Expected result | Actual paper result | Correction | Pass or revise |
|---|---|---|---|---|---|
| T1 Level D request during a certificate dispute | A user asks for a direct table write to re-issue a certificate after a lab correction | Admission rule rejects level D; alternatives listed; Quality (OMF-P08) informed; decision record kept |  |  |  |
| T2 Two tools, two names | Quality renames a capability in the process tool while the architecture tool keeps the old name before a scheduled sync | Object owner rule decides direction first; conflict reported, not overwritten; owner register updated |  |  |  |
| T3 Stale inventory hides a dependency | A retired certificate portal is still linked to three processes; an impact report omits a live dependency | Review-date rule flags the fact sheet; report states freshness; owner re-certifies |  |  |  |

## 13. Detailed action plan

This is a **proposed** plan. Durations are working-day estimates for a first bounded pass on two value streams, not commitments. Owners are proposed personas. Every action has an artefact and an acceptance check so it can be inspected.

### Phase 0: Frame the decision

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-01 | Confirm the decision statement in Section 4 and the two scoped streams | OMF-P04 | Case Theme C; sponsor view | One-page decision brief | OMF-P04 and OMF-P13 sign it; sponsor outcome question answered | 1 |
| A-02 | Name one owner per object type: capability, process, application, data object, organization | OMF-P13 | Section 6 | Object ownership rule | No object type has two owners | 1 |
| A-03 | Write the evidence-gap list: what is missing, who can authorize, constraints, how value is measured (source challenge) | OMF-P13 | Section 2 | Evidence-gap register | Every gap has an owner and a due date | 2 |
| A-04 | Agree the standing rule: nothing is scored or targeted without a baseline | OMF-P04 | Source rule | Governance note | Rule appears in the review checklist | 0.5 |

### Phase 1: Capability and value-stream model

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-05 | Write the capability maturity scale (what each level means, observably) | OMF-P13 with business owners | Source capability statements | Scale definition page | Each level has an observable test | 2 |
| A-06 | Build the capability map and owner register (Section 7) | OMF-P13 | A-02, A-05 | Capability map; owner register | Source capabilities present; owners confirmed or marked TBC | 3 |
| A-07 | Collect evidence samples for the capabilities touched by the two streams only | OMF-P08, OMF-P07, OMF-P14 | A-05 | Evidence samples | Sample method documented; no invented scores | 5 |
| A-08 | Draw the two value streams and stage-capability matrices (Section 8) | OMF-P08, OMF-P07 | Source stream names | Value-stream maps | Each stage maps to a capability and an owner | 3 |
| A-09 | Walk the maps with the operational authority to find what the diagram misses | OMF-P16 | A-08 | Findings log | At least one change or an explicit "no change" recorded | 1 |

### Phase 2: Process model (Signavio)

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-10 | Set the process taxonomy and naming rules (Section 8) | OMF-P13 | A-08 | Naming and level standard | Two reviewers apply it to the same process and get the same code | 1 |
| A-11 | Model two or three L3 processes per stream with owners and control points | Process owners | A-10 | Process diagrams | Owner has read back and accepted each diagram | 5 |
| A-12 | Record glossary or dictionary entries for capabilities, applications, organizations | OMF-P14 | A-06 | Dictionary entries | No duplicates; names match the owner register | 2 |
| A-13 | Mark every process step that touches operational authority, consent or a regulated control | OMF-P16 and OMF-P08 | A-11 | Control-point overlay | Each marked step names its approver | 1 |

### Phase 3: Inventory (LeanIX) and integration

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-14 | Define the fact sheet attributes and data-quality rules (Section 9) | OMF-P13 and OMF-P14 | A-02 | Inventory standard | Rules testable by a script or a checklist | 2 |
| A-15 | Load the scoped applications as fact sheets with owners, lifecycle and interfaces | Technical owners | A-14 | Inventory for scoped streams | Every fact sheet has an owner and a review date | 5 |
| A-16 | Decide sync direction per object type, mapping and schedule | OMF-P13 | A-02, A-12 | Sync design note | Matches the owner rule; one source of truth per type | 1 |
| A-17 | Obtain the dedicated integration user and confirm permissions and licensing | OMF-P12 and OMF-P13 | A-16 | Access record | Least privilege; credentials held in a managed secret store | 2 |
| A-18 | Run a first sync in a non-production or sandbox setting and review conflicts | OMF-P13 | A-16, A-17 | Sync report | Every conflict has a resolution; unexpected changes explained | 2 |
| A-19 | Produce one dependency view: process, application, data, interface | OMF-P13 | A-15, A-18 | Impact view | Freshness statement included; one known dependency verified by hand | 2 |

### Phase 4: Clean Core guardrail and delivery tracking

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-20 | Confirm which Clean Core levels, tools and terms apply to the actual SAP products and editions in scope | OMF-P13 | Current SAP documentation | Applicability note | Wording checked against SAP sources on a stated date | 1 |
| A-21 | Approve the admission rule and exception policy (Section 10) | OMF-P04, OMF-P13, OMF-P12 | A-20 | Admission rule v1 | Level D default rejection and exception expiry written | 1 |
| A-22 | Create the Extension Decision Record template and the decision log | OMF-P13 | A-21 | Template and log | Template fits on one page; log fields match source attributes | 1 |
| A-23 | Run the eight-requirement exercise with real reviewers and refine the rule | OMF-P13 | Section 11 | Revised rule and key | Reviewers agree on at least the A and D cases; disagreements logged | 1 |
| A-24 | Link requirements to processes and resolution categories in the delivery tool (validate tenant features first) | Delivery lead | A-21 | Traceable requirement set | Every approved requirement has category, level, owner, tests | 2 |

### Phase 5: Prove it on paper, then decide

| ID | Action | Proposed owner | Input | Output artefact | Acceptance check | Est. days |
|---|---|---|---|---|---|---|
| A-25 | Run tabletop tests T1 to T3 and revise | OMF-P13 with OMF-P12 | Section 12 | Test sheet | Each test has actual result and pass or revise | 1 |
| A-26 | Define review cadence: monthly architecture review; quarterly inventory re-certification | OMF-P13 | A-14 | Review calendar | Dates set; owners named | 0.5 |
| A-27 | Select the measures and capture baselines before any target | OMF-P04 | Section 14 | Baseline sheet | Targets blank until baselines exist | 2 |
| A-28 | Present the decision pack to the sponsor and finance: what was built, what is evidence, what is not | OMF-P04 | All | Decision pack | Open questions and evidence gaps are visible, not hidden | 1 |

**Critical path (proposed):** A-02, A-05, A-08, A-10, A-14, A-16, A-18, A-21. Phases 2 and 3 can overlap once A-10 and A-14 are done.

### Presenter action items for the technical discussion

These are for the trainer preparing to show this demo to a corporate audience. They do not appear in the case.

| ID | Action | Why | Done when |
|---|---|---|---|
| P-01 | Decide which parts you will show live and which on paper; label each as sandbox, vendor-provided or paper | Honesty about what was actually exercised | Slide or note states the status of every screen |
| P-02 | Confirm access to a Signavio and a LeanIX environment, or prepare static screenshots from your own training sandbox | The vendor is expected to provide demo systems | Access confirmed in writing, or fallback ready |
| P-03 | Load the synthetic fact sheets from Section 9 and one synthetic process for Order-to-Trusted-Delivery | Gives a concrete walkthrough | Records carry the `MAT-SYN` prefix |
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
- Case: [OmniForge Materials](https://github.com/nbnayak88/successlabs-case-studies/tree/main/02-materials/omniforge-materials-ltd) · [Theme C architecture (OMF-M09 to M12)](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/master/theme-c-architecture.md) · [source and assumptions](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/references/source-and-assumptions.md) · [persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md)
- Series baseline: [Demo 01](01-omniforge-case-baseline-sap-nextgen-architecture.md)

**Educational alignment:** TOGAF for architecture views and decisions; BIZBOK for capability and value-stream distinctions; BABOK for needs and acceptance; DAMA for data ownership and quality; COBIT for accountable control. These mappings are educational and are not compliance certification or reproduction of proprietary standards.

**Publication note:** this is a demonstration file in the bootcamp folder. It is not proof that a course is live, purchasable or delivered.
