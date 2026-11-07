# OmniSpace HR01 — Process, configuration and controls
Edition: 2026-11-07 · Specification authored; configuration unexecuted.
Dependencies: baseline → structure/references → positions → employee data → permissions/workflows → rules → integrations → tests.

## Lifecycle catalogue and acceptance
| Requirement | Trigger and controlled behavior | Acceptance evidence |
|---|---|---|
| OSP-HR01-REQ03 Hire | Approved identity, employer and available position; HR validates required fields and start date | One unique person/employment relationship, approved record and correct start-date view |
| OSP-HR01-REQ04 Personal change | Employee requests own permitted fields; sensitive changes reviewed by HR | Field permissions, approved/denied cases, correction audit |
| OSP-HR01-REQ05 Promotion | Manager requests new role/pay; HR approves, compensation owner approves pay impact | Position/job consistency, effective-date views, payroll handoff |
| OSP-HR01-REQ06 Same-employer transfer | Receiving manager confirms role; HR approves dated assignment | RE-P100 remains linked to RE-E100; A/B counts become 99/21; access and task states remain independent |
| OSP-HR01-REQ07 Termination | Authorized separation request with date and reason | Correct employment state; security removal confirmed separately; unresolved failures escalated |
| OSP-HR01-REQ08 Rehire | HR matches prior identity and reviews employment treatment | No duplicate person; employment decision and downstream identity handling documented |
| OSP-HR01-REQ09 Cross-employer/international move | Different employer or country detected | Route to separate design review; no reuse of same-employer automation without validation |
| OSP-HR01-REQ10 Temporary coverage | Operations requests bounded coverage interval | Primary job unchanged; property authority and security separately approve relevant scopes |

## Proposed workflow policy
Manager initiates permanent job change → receiving manager confirms capacity → HR approves employment/organization change → payroll owner reviews changes with payroll impact. Security approves access independently; property authority approves restricted tasks independently. Requesters cannot approve their own requests; self-requests and missing approvers route to a designated independent HR approver. Unresolved routing remains pending and escalates after one business day (synthetic pilot policy). Delegation must be time bounded and audited.

Event reasons, workflow rules, field derivation, position synchronization and country rules require tenant-specific design confirmation. Do not label all changes as a generic transfer. Correction of bad history differs from a new business event.

## Permission design
| Role | Target population | Permitted scope | Explicit restriction |
|---|---|---|---|
| Employee | Self | View own permitted records; request allowed personal changes | No approval of own consequential change |
| Property manager | Authorized reporting population/property responsibility | Required job/assignment visibility; initiate changes | No unrestricted pay, bank or national-ID visibility |
| HR administrator | Assigned employer population | Maintain authorized HR records | No uncontrolled security-access grant |
| HR approver | Delegated employer population | Review employment changes | Independent approval where requester conflicts |
| Payroll service user | Approved payroll population/fields | Minimum payroll feed | No building authorization |
| IAM service user | Approved identity population/fields | Identity and access-request handoff only | No pay or bank data |
| Auditor | Authorized audit scope | Read evidence | No operational modification |

Validate target populations on transfers, future dates and manager changes. Record read/create/edit/insert/correct/delete permissions separately as supported; test both allowed and denied actions.

## Implementation journal
For each change record requirement ID, object/field, rule/workflow reference, source documentation/release, alternatives, configurator, reviewer, test IDs, evidence URL and rollback action. Values are unfilled until actual implementation. BABOK: trace needs to acceptance; COBIT: named accountability; ISO/IEC principles: least privilege and controlled change.
