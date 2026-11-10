# OmniWorks Industrial Systems Ltd. — Security and Zero Trust for AI Assistants and Agents on SAP BTP

## Demo 08 of the BTM11 Industrials Ultimate Bootcamp demo series

**SuccessLabs Academy · BTM11 · Industrials (IND) · Ultimate (Level 5) · Bootcamp**
**Version:** 2026-11-10 · Demonstration material; not an enrolled course, certification or published pathway.
**Series baseline:** [Demo 01 case baseline](01-omniworks-case-baseline-sap-nextgen-architecture.md) · **Related:** [Demo 02](02-enterprise-architecture-signavio-leanix-clean-core.md) · [Demo 03](03-ai-genai-rag-agents-sap-btp.md) · [Demo 04](04-knowledge-graph-context-engineering-sap.md) · [Demo 05](05-integration-event-driven-advanced-event-mesh-sap.md) · [Demo 06](06-basis-modernization-aiops-autonomous-operations-sap.md) · [Demo 07](07-data-foundation-data-products-sap-business-data-cloud.md) · [Demo 09](09-ai-governance-evaluation-llmops-sap.md) · [Demo 10](10-migration-path-clean-core-readiness-sap.md) · [Demo 11](11-operating-model-finops-intelligent-operations-sap.md) · [Demo 12](12-resilience-failure-drills-sap.md) · [Demo 13](13-sustainability-green-it-sap.md) · [Demo 14](14-low-code-pro-code-vibe-code-citizen-development-sap.md) · [Demo 15](15-industry-regulation-country-anchored-sap.md)

> **Evidence boundary:** OmniWorks Industrial Systems Ltd. is an **aspirational case study**. The case sources describe security perspectives; the agent permissions, threats and checks below are new design. Nothing here is a record of a client implementation, an executed test or a realized benefit. Names marked synthetic carry the prefix `IND-SYN` and are new design. SAP product statements come from public SAP documentation reviewed 2026-11-10 and must be verified before real delivery.

---

## 1. The question this file answers

> *Security architecture for AI and autonomous operations: what can an assistant or agent do, as whom, and what stops it doing more?*

**What this file shows:** an identity and permission model for OmniWorks's assistant and agents, four threat scenarios with a control and a check, and the sector boundary that no agent may cross.

**What it does not show:** a configured identity tenant, a penetration test result or a certified control.

## 2. Case anchor (source facts)

| Attribute | Case baseline |
|---|---|
| Scale | USD 48B revenue; 74,000 employees; 36 countries; 61 plants and facilities; 320 service depots; 7,200 suppliers |
| Business mix | Industrial automation 27%; aerospace and defence 23%; transport and mobility 19%; infrastructure 16%; aftermarket and lifecycle services 15% |
| Burning platform | Recurring transport asset failures cannot be consistently traced across configuration, telemetry, supplier batches and maintenance history |

**Decision under discussion (source):** Turn a USD 575M transformation envelope into credible customer, operational and financial value without disrupting safety-critical operations.

**Illustrative trigger (source):** Repeat customer asset failures expose fragmented engineering-to-service information, and the business wants to sell uptime rather than equipment (hero story).

**Pilot from Demo 03:** Field-service copilot for transport-asset failure triage

## 3. Source versus new design

| Element | Status |
|---|---|
| Case facts, personas | **Source** |
| Agent identity model, permission matrix, threat scenarios, tests | **New design (illustrative)** |
| SAP identity and BTP security behaviour | Public SAP documentation reviewed 2026-11-10; **not exercised here** |

## 4. Decision under discussion

**Decision:** Under what identity and permissions may OmniWorks's assistant and agents run, and who can widen them?

**Accountable owner (proposed):** OW-P06 Marcus Vogel, with OW-P11 Hannah Fischer for the pattern and OW-P15 Dr. Leila Haddad for AI governance.

## 5. Personas and proposed decision rights

| Source ID | Persona | Proposed role in this demo |
|---|---|---|
| OW-P05 | Priya Nair, CIDO | Funds and prioritizes |
| OW-P11 | Hannah Fischer, Director, Enterprise Architecture | Owns standards and review |
| OW-P06 | Marcus Vogel, CISO | Security and boundary approval |
| OW-P15 | Dr. Leila Haddad, Head of Data Governance & AI | Data and AI governance |
| OW-P09 | Isabel Torres, Chief Customer & Service Officer | Business owner (first scope) |
| OW-P10 | Ravi Deshpande, VP Manufacturing, Pune Operations | Business owner (second scope) |
| OW-P12 | Daniel Okafor, Field Service Operations Manager | Operational authority and veto |

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
| search_service_docs | Read | None | Always returns document revision |
| get_asset_history | Read | None | Entitlement-filtered |
| draft_work_order | Draft only | Field Service manager approves | Safety-critical steps require a named human sign-off |
| request_engineering_review | Creates a task | Engineering owns the outcome | Assistant cannot approve a deviation |
| Any OT, safety-setting or parts-release action | Not exposed | Not available to the agent | Human-in-the-loop for safety-critical AI |

**Sector boundary:** OT edge and equipment controls stay outside AI tooling; segmented networks stay segmented.

**Never available:** Engineering IP outside the user's role entitlement; Supplier-confidential data in customer-facing contexts; Live OT commands or setpoints; Instructions found inside retrieved documents

## 8. Threat scenarios

| Threat | Control | Check |
|---|---|---|
| Injection through a service note | Text is data; no tool calls from text | Seed a note with an instruction |
| Agent reading restricted supplier notices | Share-permission filter | Query as a customer role |
| Agent with write access to work orders | Draft only; human creates the order | Check scopes |
| Credential in a payload | Payload validation rejects secrets | Send a payload with a token |

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
| T1 Restricted notice | A customer-role user asks for supplier notices | Blocked; logged |
| T2 Draft versus create | An agent tries to create a work order | Only a draft is made |
| T3 Secret in payload | A payload contains a credential | Rejected; owner notified |

## Acceptance (measures only; no baselines or targets asserted)

| Measure | How it is observed | Value |
|---|---|---|
| Tools with an explicit scope and approval rule | Count against the tool list | Not measured |
| Threat checks with a recorded expected result | Count of four | Not measured |
| Tool calls with audit fields defined | Review | Not measured |
| Scope changes with a named approver | Policy review | Not measured |

No baseline, target or benefit is stated because none exists for this aspirational case study. Targets are agreed in discovery.

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
| Customer-confirmed requirements | Not applicable (aspirational case study) |

| Date | Audience | Exercise run | Observed result | Changes made |
|---|---|---|---|---|
|  |  |  |  |  |

## Resources

- [SAP Cloud Identity Services](https://www.sap.com/products/technology-platform/cloud-identity-services.html)
- [SAP community: secure code-based agents with IAS](https://community.sap.com/t5/technology-blog-posts-by-sap/joule-a2a-secure-code-based-agents-with-ias/ba-p/14367792)

- [OmniWorks Industrial Systems Ltd. case library](https://github.com/nbnayak88/successlabs-case-studies/tree/main/03-industrials/omniworks-industrial-systems)
- [OmniWorks Industrial Systems Ltd. persona cards](https://github.com/nbnayak88/successlabs-case-studies/blob/main/03-industrials/omniworks-industrial-systems/personas/persona-cards.md)

