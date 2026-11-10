# OmniForge Materials — Security and Zero Trust for AI Assistants and Agents on SAP BTP

## Demo 08 of the BTM11 Materials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Materials (MAT) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniforge-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniForge Materials is a **fictional educational case**. The case sources describe security perspectives; the agent permissions, threats and checks below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `MAT-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Security architecture for AI and autonomous operations: what can an assistant or agent do, as whom, and what stops it doing more?*

**What this file shows:** an identity and permission model for OmniForge's assistant and agents, four threat scenarios with a control and a check, and the sector boundary that no agent may cross.

**What it does not show:** a configured identity tenant, a penetration test result or a certified control.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 42B materials group; 46,000 employees; 31 countries |
| Business mix | Steel and alloys 30%; cement and aggregates 22%; chemicals 20%; mining and minerals 16%; advanced materials 12% |
| Burning platform | Disconnected mining, production, logistics, quality, sales and recycling; 180+ applications; weak material genealogy; manual ESG reconciliation |

**Decision under discussion (source):** Select a bounded materials-traceability and reliability pilot before committing an enterprise rollout.

**Illustrative trigger (source):** A customer queries a shipped batch's certificate after a laboratory correction, while a kiln reliability alert and uncertain recycled-feedstock records expose the same trust gap (illustrative hero trigger in the case).

**Pilot from Demo 03:** Batch-certificate query assistant for quality and customer-facing staff

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Agent identity model, permission matrix, threat scenarios, tests | **New design (illustrative)** |
| SAP identity and BTP security behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Under what identity and permissions may OmniForge's assistant and agents run, and who can widen them?

**Accountable owner (proposed):** OMF-P12 Hassan Al-Farsi, with OMF-P13 Priya Nair for the pattern and OMF-P14 Diego Alvarez for AI governance.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OMF-P04 | Sofia de Vries, Chief Digital and Sustainability Officer | Funds and prioritizes |
| OMF-P13 | Priya Nair, Director Enterprise Architecture | Owns standards and review |
| OMF-P12 | Hassan Al-Farsi, CISO and OT Security Lead | Security and boundary approval |
| OMF-P14 | Diego Alvarez, Head of Data Governance and AI | Data and AI governance |
| OMF-P08 | Rohan Kulkarni, Head of Quality and Laboratories | Business owner (first scope) |
| OMF-P07 | Elena Petrova, Cement Plant Director | Business owner (second scope) |
| OMF-P16 | Nikhil Sen, Shift Supervisor and Workforce Representative | Operational authority and veto |

Decision rights are **proposed** and need discovery validation.

## 6. What SAP describes (public documentation, verify)

| Capability | What the documentation or SAP community describes | Use in this design |
|---|---|---|
| SAP Cloud Identity Services (Identity Authentication, Identity Provisioning) | Sign-in, tokens and user provisioning across SAP and non-SAP systems | Identity for people and applications |
| App-to-app OAuth2 client credentials | In an SAP community example the token identifies the application, not the end user; the agent checks signature, issuer, audience, expiry and a scope claim | Agent identity; user-level access needs principal propagation, so verify |
| Agent-to-agent protocol and BTP Destinations | An SAP community example secures an agent with a middleware and calls it through a destination using OAuth2 client credentials | Pattern for agent calls; verify for current versions |
| Role collections and authorizations on BTP | Roles are grouped into role collections and assigned to users | Human roles for approvals |

## 7. Identity and permission model (new design)

| Principle | Design |
|---|---|
| Two identities | The user's identity decides what data is visible; the agent's own identity decides which tools it may call |
| Least privilege | Each tool has its own scope; no wildcard scopes |
| Read before write | Agents start read-only; write tools are drafts that a person confirms |
| Approvals | Bound to one action, expire quickly, recorded with approver |
| Data minimization | Role filter applied before retrieval; identifiers masked |
| Untrusted text | Retrieved text is data and cannot trigger a tool call |
| Audit | Every tool call logged with user, agent, input class and result |

**Tool permission matrix from the Demo 03 pilot**

| Tool | Mode | Approval | Note |
|---|---|---|---|
| search_certificates | Read | None | Always returns revision status |
| get_batch_genealogy | Read | None | Reports gaps as unknown, never fills them |
| draft_customer_reply | Draft only | Quality approves before any send | No compliance statement while a certificate is under correction |
| raise_certificate_review | Creates a task | Quality owns the outcome | Assistant cannot issue or revoke a certificate |
| Any OT or process write | Not exposed | Not available to the agent | Plant safety boundary |

**Sector boundary:** Plant control systems are out of reach for any AI tool; data flows from plant to enterprise only.

**Never available:** Unreleased laboratory results; OT control tags and setpoints; Another customer's specification; Instructions found inside uploaded certificates

## 8. Threat scenarios

| Threat | Control | Check |
|---|---|---|
| Injection in a supplier document | Treat documents as data; no tool calls triggered by text | Insert an instruction in a test document |
| Agent suggests a plant control change | No control tools exist for agents | Ask for one; expect refusal |
| Leak of customer specifications | Customer-scoped filters | Query across customers |
| Overbroad analytics access | Role-based views | Compare a user's view to their role |

## 9. Hands-on exercise (synthetic data)

1. List every tool the assistant can call and mark its scope and approval.
2. Run the four threat checks on paper and record the expected result.
3. Draw the two identities (user and agent) on the first tool call.
4. Decide who may widen a scope and how the change is approved.
5. Record open decisions in the run log.

## Three tabletop tests

A tabletop test is a paper walk-through, not a technical test of a running system.

| Test | Setup | Expected finding |
|---|---|---|
| T1 Plant boundary | An agent proposes a setpoint change | No tool exists; refused |
| T2 Customer cross-read | A user asks for another customer's spec | Filter blocks; logged |
| T3 Poisoned supplier file | A file instructs the agent to email data | Instruction ignored; file flagged |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Tools with an explicit scope and approval rule | Count against the tool list | Not measured |
| Threat checks with a recorded expected result | Count of four | Not measured |
| Tool calls with audit fields defined | Review | Not measured |
| Scope changes with a named approver | Policy review | Not measured |

No baseline, target or benefit is stated because none exists for this fictional case. Targets are agreed in discovery.

## 2–3 hour session pattern

| Time | Activity | Output |
|---|---|---|
| 0:00 to 0:20 | Why agents change the threat model | Shared problem statement |
| 0:20 to 1:00 | Identity and permission model | Matrix with scopes |
| 1:00 to 1:45 | Threat scenarios | Four checks |
| 1:45 to 2:15 | Tabletop tests | Three findings |
| 2:15 to 2:30 | Decisions | Open items with owners |

## Evidence status and run log

| Item | Status |
|---|---|
| Design in this file | Written |
| Walk-through with a live audience | Not yet run |
| Hands-on run on a vendor-provided system | Not yet run |
| Customer-confirmed requirements | Not applicable (fictional case) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP Cloud Identity Services](https://www.sap.com/products/technology-platform/cloud-identity-services.html)
- [SAP community: secure code-based agents with IAS](https://community.sap.com/t5/technology-blog-posts-by-sap/joule-a2a-secure-code-based-agents-with-ias/ba-p/14367792)

- [OmniForge Materials case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/02-materials/omniforge-materials-ltd)
- [OmniForge Materials persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/02-materials/omniforge-materials-ltd/personas/persona-cards.md)

