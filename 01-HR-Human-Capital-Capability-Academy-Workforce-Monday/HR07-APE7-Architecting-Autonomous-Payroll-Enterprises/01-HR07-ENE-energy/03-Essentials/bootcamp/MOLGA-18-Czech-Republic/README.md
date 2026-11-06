# OmniVerse Energy Ltd — Czech Republic Payroll Bootcamp

[Open the live Czech Republic workbook](https://nbnayak88.github.io/payroll/Czech_Republic.html) · [Browse all 62 countries](https://nbnayak88.github.io/payroll/)

**SuccessLabs Academy | HR07 APE7 | GICS01 Energy | Essentials | Applied case study**  
**MOLGA:** `18` · **ISO:** `CZ` · **Case ID:** `OV-ENE-HR07-18`  
**Case status:** Fictional training scenario · statutory and SAP localization verification required

## Executive scenario
OmniVerse Energy Ltd is a **fictional** multi-country energy enterprise operating generation, distribution, field maintenance, operations centres and corporate services. The transformation office is designing a controlled, auditable payroll operating model for its **Czech Republic** workforce. Learners act as payroll solution architects responsible for compliant design, integration, testing, controls and hypercare. No headcount, pay rates or live financial data are asserted.

## Country-specific investigation
Research the country's current income-tax withholding, employer/employee social contributions, mandatory benefits, labour agreements, statutory files, and record-retention requirements. Do not assume statutory rules or SAP standard support.

**SAP fit check:** Native SAP Payroll support not asserted; validate the installed release, localization, and licensing. Check `T500L` and `T500L-PYSOL` in the actual target SAP HCM/ECP system, the supported release and SAP country localization documentation; assess partner payroll or external engine when needed. MOLGA is not evidence of a delivered payroll engine.

## Business problem and personas
- **CHRO:** accountable for employee trust, accuracy and employee experience.
- **Country payroll lead:** owns local compliance sign-off and calendars.
- **Plant operations manager:** submits shifts, overtime, standby and emergency-callout events.
- **HR service lead:** manages employee master data, life events and exceptions.
- **Finance controller:** signs off posting, cost centres and reconciliation.
- **Security/audit officer:** tests access segregation, personal-data protection and payroll evidence.

## Architecture and delivery lab
1. **Discover:** identify employee groups (union/non-union, shift, contractor boundaries), jurisdiction, collective agreements, time/pay events and regulatory stakeholders.
2. **Flow:** map hire-to-retire, time-to-pay, gross-to-net, pay-to-bank and payroll-to-general-ledger value streams.
3. **Design:** model personnel structure, pay components, country grouping, payroll calendar, infotypes/EC data mapping, integrations, security and exception queues.
4. **Build:** prepare illustrative rule/configuration decisions and interfaces for SAP SuccessFactors EC → ECP/SAP HCM → banking/finance/reporting; adapt to actual SAP support evidence.
5. **Validate:** test positive/negative cases, retroactive adjustment, off-cycle pay, unpaid leave, termination, emergency overtime and reconciliation.
6. **Operate:** prepare controls for segregation of duties, statutory cutoff, audit logs, data retention, employee inquiries and cutover.

## Applied exercise: energy outage payroll
A grid outage requires technicians to work a night shift across a payroll cutoff. Design the event capture, approval chain, wage-type determination (jurisdiction dependent), retroactivity decision, finance posting and employee communication. Explicitly distinguish confirmed local legal requirements from assumptions.

## Required learner artifacts
- One-page country payroll business case and stakeholder/RACI matrix.
- Country statutory research register (source URL, publication date, owner, effective date, confidence).
- Capabilities, value stream and process swimlane diagram.
- Source-to-target data mapping and integration inventory (EC/HCM, time, payroll, finance, banking).
- Payroll controls matrix and 12+ scenario-based test cases with expected results.
- Exception dashboard specification, cutover checklist and executive demonstration.

## Suggested evaluation
**100 points:** business understanding 15; legal/source traceability 20; architecture 20; controls and security 15; testing 20; executive communication 10. Passing threshold: 75 with no unresolved critical statutory or privacy issue.

## Learner simulation prompts
- Country payroll lead challenges your treatment of a new statutory rule.
- Operations director demands late overtime pay after cutoff.
- CFO disputes the payroll-to-GL reconciliation.
- Auditor requests evidence of access governance and retroactive changes.

## Delivery modes
- **Fast Track (3 h):** country discovery, core flow, architecture and case demo.
- **Guided Track (up to 21 h):** evidence collection, build simulations, validation and executive defense.

## Publication controls
Educational case only. Country-specific statutory rates, schemas, payroll drivers, wage types and legal entitlements **must not be invented**. Confirm against authoritative jurisdiction sources and the deployed SAP release before presenting any production recommendations. A published README does not mean the course is available for enrolment.
