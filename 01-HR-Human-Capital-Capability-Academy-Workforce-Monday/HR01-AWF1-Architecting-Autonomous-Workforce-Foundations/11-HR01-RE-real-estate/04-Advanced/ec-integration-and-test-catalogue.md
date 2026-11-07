# OmniSpace HR01 — Integration, exceptions and verification
Edition: 2026-11-07 · Contract design; no connector execution claimed.

## Interfaces
| Interface | Authoritative direction | Minimum payload | Completion evidence |
|---|---|---|---|
| OSP-HR01-IF01 | Finance → EC reference staging | Cost center, validity, owner/version | Accepted references and rejected-record reconciliation |
| OSP-HR01-IF02 | Property master → HR reference staging | Property key, status, validity/version | Active-property reference validation |
| OSP-HR01-IF03 | EC → payroll | Approved employment/job/pay data required by payroll | Payroll acceptance and record/control-total reconciliation |
| OSP-HR01-IF04 | EC → IAM/security workflow | Worker/employment keys, property/location, effective interval, approved change reference | Request accepted; access outcome separately confirmed |
| OSP-HR01-IF05 | Learning/assessor → readiness service | Completion/assessment reference, scope and validity | Property authority decides task authorization |

These are logical interfaces, not assertions of packaged connectors. EC does not write physical-access grants directly. Use authenticated least-privilege connections, encrypted transport and protected operational logs.

## Message and recovery rules
Envelope: schema version, event ID, correlation ID, worker/employment reference, source version, effective date/time with timezone, recorded time, operation, approval reference and minimum changed fields.
Use UTC transport timestamps; retain Asia/Kolkata business-date interpretation. Treat extraction time and effective date separately.
Deduplicate by event ID; process by employment/source version; quarantine stale or conflicting changes. Consumers must not apply future changes early. Replaying the same event must not duplicate requests. Corrections and cancellations carry links to superseded versions.
Synthetic service policy: retry transient failures after 1, 5 and 15 minutes, then route to an exception queue with named integration owner; alert within 30 minutes. Business rejection requires correction, not blind retry.
Reconcile daily and before declaring a transfer complete. Compare approved source change, accepted destination version and outcome. A missing acknowledgment leaves access unconfirmed. Security controls access containment; a successful HR commit is not automatically rolled back because IAM is unavailable.
Proposed pilot recovery objectives: reconcile interrupted handoffs within four business hours and re-extract from the last confirmed checkpoint with no lost approved change. Validate feasibility before adoption as an operational SLA.

## Extended tests: separate from Origin Story T01–T03
All observed results/status/evidence initially UNEXECUTED.
| Test | Requirement/interface | Input | Expected result |
|---|---|---|---|
| OSP-HR01-IT01 | REQ06/IF04 | Future-dated A→B move | History intact; no early B access; 99/21 on effective date |
| OSP-HR01-IT02 | REQ06/IF03 | Backdated correction after payroll acceptance | Corrected version reconciled; payroll impact reviewed |
| OSP-HR01-IT03 | REQ06/IF04 | Cancel move after request sent | Cancellation reconciled; security confirms relevant request/access disposition |
| OSP-HR01-IT04 | REQ09 | Different legal employer | Separate approved design required; simple move blocked |
| OSP-HR01-IT05 | REQ10 | Temporary B coverage | Primary A job preserved; bounded permissions |
| OSP-HR01-IT06 | Security | Other-property manager attempts restricted read/edit | Denied and logged according to policy |
| OSP-HR01-IT07 | IF04 | Duplicate and older events after newer version | No duplicate grant/request and no stale overwrite |
| OSP-HR01-IT08 | REQ07/IF04 | Termination with security outage | Removal exception escalated; no false completion |
| OSP-HR01-IT09 | REQ08 | Rehire with matching prior person | Identity matched; employment treatment reviewed |
| OSP-HR01-IT10 | REQ03 | Invalid position/property/date | Validation rejects inconsistent record |
| OSP-HR01-IT11 | IF03 | Payroll rejection | HR/payroll states explicit; corrected record reconciled |
| OSP-HR01-IT12 | Adoption | Field worker without personal device | Assisted accessible journey succeeds with privacy protected |

Evidence record: test ID, dataset version, expected, observed, timestamps, source/destination IDs, reviewer, pass/fail, defect and retest link. Expected results are not pass evidence.
