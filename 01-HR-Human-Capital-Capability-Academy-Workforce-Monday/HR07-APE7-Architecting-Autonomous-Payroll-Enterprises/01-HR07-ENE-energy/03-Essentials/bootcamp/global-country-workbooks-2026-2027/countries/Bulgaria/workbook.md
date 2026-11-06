# Bulgaria Payroll Workbook

[Open the live Bulgaria workbook](https://nbnayak88.github.io/payroll/Bulgaria.html) · [Browse all 62 countries](https://nbnayak88.github.io/payroll/)

**SuccessLabs Academy — Architecting Experiences for a Better World.**

Employee Central Payroll learning edition. Horizon: 2026–2027 onward. Source evidence review: 6 November 2026. Configuration sections: 44.

These are learning and implementation-design materials. Country facts retain the source workbook review date. Proposed configurations and fictional case data need employer-specific validation. Unverified statutory parameters remain pending. The arithmetic practice is not a complete statutory payroll calculation engine. Actual tenant tests, submissions and production approval remain unexecuted.

This edition adapts the six HTML learning tools into editable questions, retrieval cards, a crossword, facilitated Snakes & Ladders, AVG reflection and a notes journal. Use the linked HTML for interactive browser play. Notes in different formats are independent and do not automatically sync.

## Country baseline

| Field | Reference |
| --- | --- |
| Currency | EUR |
| Authorities | National Revenue Agency and National Social Security Institute |
| Employee identifiers | EGN or foreign-person identifier; NRA employer registration; insurance category |
| 2026 focus | Euro adoption took effect on 1 January 2026 at EUR 1 = BGN 1.95583. Historical payroll and retro periods need controlled currency conversion. |
| 2027 onward | 2027 amounts and reporting specifications: refresh the cited authority publications before activating a new version. No unverified 2027 numerical rates are preloaded. |
| Local year | Confirm local tax and contribution year before release |

## Configuration contents

- [01. Cover](#section-01)
- [02. Change Log](#section-02)
- [03. Contents & Learning Path](#section-03)
- [04. Introduction & Scope](#section-04)
- [05. Company Structure](#section-05)
- [06. Personnel Structure](#section-06)
- [07. Lifecycle Actions](#section-07)
- [08. Personal Information](#section-08)
- [09. Address & Locality](#section-09)
- [10. Bank Details](#section-10)
- [11. Date Types](#section-11)
- [12. Replicated Pay Components](#section-12)
- [13. Work Schedules](#section-13)
- [14. Time Types & Leave](#section-14)
- [15. Payroll Control Record](#section-15)
- [16. Payroll Areas & Calendar](#section-16)
- [17. Wage Type Catalogue](#section-17)
- [18. Salary Payment Configuration](#section-18)
- [19. Off-Cycle Payroll](#section-19)
- [20. Garnishment Intake](#section-20)
- [21. Payslip Configuration](#section-21)
- [22. Income Tax & Withholding](#section-22)
- [23. Social Insurance](#section-23)
- [24. Statutory Reporting](#section-24)
- [25. Pensions & Enrolment](#section-25)
- [26. Benefits & Expenses](#section-26)
- [27. Statutory & Absence Pay](#section-27)
- [28. Minimum Pay & Agreements](#section-28)
- [29. Attachment Calculation & Remittance](#section-29)
- [30. Schema & Calculation Sequence](#section-30)
- [31. Retroactive Processing](#section-31)
- [32. Year-End & New-Year Opening](#section-32)
- [33. Authority Updates & Notices](#section-33)
- [34. EC Data Validation](#section-34)
- [35. Payment Exceptions](#section-35)
- [36. Finance Posting](#section-36)
- [37. Replication Triggers & Monitoring](#section-37)
- [38. Integration Suite & Extensions](#section-38)
- [39. Test Scenarios](#section-39)
- [40. Cutover Plan](#section-40)
- [41. Training & Facilitation](#section-41)
- [42. Hypercare & Operations](#section-42)
- [43. End-to-End Integration Map](#section-43)
- [44. Risk Register](#section-44)

<a id="section-01"></a>
## 01. Cover

**Category:** Setup

**What:** Establish the project baseline and its country boundary.

**Why:** A clear baseline prevents a learning example from becoming an unapproved production configuration.

### Approach

1. Record legal employer, payroll population, product release and implementation owner.
2. Identify the controlling statutory sources and their effective dates.
3. Separate legal facts, proposed design choices and completed tenant evidence.
4. Record the approval and evidence needed before production use.

### Workbook identification

| Field | Baseline / decision |
| --- | --- |
| Country | Bulgaria |
| Scope | Employee Central Payroll learning and configuration design |
| Currency | EUR |
| Statutory horizon | 2026 baseline; 2027 onward change control |
| Evidence review date | 6 November 2026 |
| Company | OmniVerse Energy — Bulgaria learning subsidiary (fictional) |
| Scenario employee | Elena Petrova — Sofia (fictional) |
| Release | 1.0 • researched learning edition |
| Production approval | Not assessed; no tenant configuration or statutory submission has been performed |

### Applied experiment

Create a one-page scope statement for a 120-person Bulgaria subsidiary. Explain every assumption you would confirm before configuration.

**Prerequisite:** Country evidence desk and scope baseline

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-02"></a>
## 02. Change Log

**Category:** Setup

**What:** Record legal updates and workbook decisions without erasing prior versions.

**Why:** A new statutory amount may apply prospectively while an earlier result still needs the historical rule.

### Approach

1. Assign a change owner and classify law, design or defect.
2. Record publication date separately from effective date.
3. List impacted wage types, interfaces, reports and tests.
4. Retain approval, transport and regression evidence before activation.

### Version register

| Version | Date | Change | Status / evidence |
| --- | --- | --- | --- |
| 1.0 | 6 November 2026 | Country learning workbook created from the supplied UK reference | Draft implementation decisions; official sources linked |
| Next release | To schedule | 2027 rule pack and reporting specification refresh | Await source validation and business approval |

### Local change register

| Period | Country item | Required decision |
| --- | --- | --- |
| 2026 | Euro adoption took effect on 1 January 2026 at EUR 1 = BGN 1.95583. Historical payroll and retro periods need controlled currency conversion. | Assess impacted calculations and reporting |
| 2027 onward | 2027 amounts and reporting specifications: refresh the cited authority publications before activating a new version. No unverified 2027 numerical rates are preloaded. | Version each effective-dated rule; do not silently copy 2026 |

### Applied experiment

Write a change request for the country item above. Include a valid-from date, affected population, comparison result and rollback condition.

**Prerequisite:** Country evidence desk and scope baseline

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-03"></a>
## 03. Contents & Learning Path

**Category:** Setup

**What:** Navigate the full configuration and learning journey.

**Why:** A dependency-based journey makes it easier to understand why a downstream payroll result is wrong.

### Approach

1. Start with foundation data before calculation rules.
2. Read the country evidence desk before choosing rates.
3. Build one employee path through calculation, reporting, payment and posting.
4. Use the learning tools to explain the decisions in your own words.

### Suggested learning sequence

| Stage | Sections | Exit evidence |
| --- | --- | --- |
| Discover | 01–04 and Evidence desk | Scope and source classification |
| Design | 05–21 | Entity, data, wage-type and calendar decisions |
| Calculate | 22–33 | Country bases, deductions and reporting design |
| Connect | 34–38 and 43 | Replication, payment and Finance reconciliations |
| Validate | 39–44 | Not-run test pack, cutover and support ownership |
| Reflect | Quiz, Crossword, Snakes & Ladders, AVG Wall, Flashcards, Notes | Explanation, self-assessment and next experiment |

### Applied experiment

Choose one missing skill and create a path of five sections that would help you demonstrate it with evidence.

**Prerequisite:** Country evidence desk and scope baseline

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-04"></a>
## 04. Introduction & Scope

**Category:** Setup

**What:** Define what this country implementation must achieve.

**Why:** Country payroll is a chain of legal, employee, payment and accounting decisions; no single rate table describes the entire process.

### Approach

1. Identify employee categories and out-of-scope special regimes.
2. Agree regular and special-pay frequencies.
3. Separate statutory filing from bank payment and GL posting.
4. Confirm standard or partner localization and release compatibility.

### Scope boundary

| Area | Country baseline | Design / acceptance |
| --- | --- | --- |
| Authorities | National Revenue Agency and National Social Security Institute | Confirm registrations and delegated access |
| Identity | EGN or foreign-person identifier; NRA employer registration; insurance category | Validate identity and eligibility evidence |
| Reporting | NRA declarations 1 and 6 | Use current formats and feedback |
| In scope | Standard local employee design and representative edge cases | Define actual workforce before build |
| Special regimes | Cross-border, directors, protected / exceptional categories | Separate legal and product assessment |
| SAP availability | Country / release support must be checked | Use current SAP availability documentation; no schema is guessed |

### Applied experiment

Interview a fictional payroll manager. List three scope assumptions that could change tax, social insurance or filing design.

**Prerequisite:** Country evidence desk and scope baseline

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-05"></a>
## 05. Company Structure

**Category:** Foundation

**What:** Connect legal employers, establishments and accounting ownership.

**Why:** An employee can be paid correctly while a liability is reported under the wrong legal registration.

### Approach

1. Create a legal-entity and establishment inventory.
2. Map EC legal entity to the verified ECP enterprise structure.
3. Assign accounting currency, Finance company and authority registration.
4. Check whether location determines tax or contribution rules.

### Illustrative entity blueprint

| Learning entity | Location | Currency | Design responsibility |
| --- | --- | --- | --- |
| Main employer | Sofia | EUR | Legal registrations and payroll liabilities |
| Operations establishment | Bulgaria regional work location | EUR | Locality / risk / agreement classification |
| Shared-service cost object | Payroll operations | EUR | Cost allocation; not a separate legal employer |

### Registration decisions

| Registration | Required evidence |
| --- | --- |
| Tax authority | Employer registration and delegated filing access |
| Social / pension | Insurance, fund or compensation-office identifiers |
| Bank | Employer account mandate and approved payment format |
| Finance | Company, chart of accounts and cost-object mapping |

### Applied experiment

Draw the legal-employer-to-authority mapping. Decide which registrations cannot be shared between two companies.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-06"></a>
## 06. Personnel Structure

**Category:** Foundation

**What:** Classify payroll populations before deriving eligibility.

**Why:** Worker status, hours and age can change contribution, tax and benefit treatment independently.

### Approach

1. Define salaried, hourly, apprentice and director populations only where relevant.
2. Record agreement, insurance and pension membership separately.
3. Assign an actual payroll area and period parameter in the tenant.
4. Test a transfer that changes legal employer or pay frequency.

### Illustrative population matrix

| Population | Frequency proposal | Country decision | Validation |
| --- | --- | --- | --- |
| Office employee | Monthly | Standard local employment | Tax / insurance category evidenced |
| Hourly operations | Monthly or agreed cycle | Hours and minimum-floor treatment | Roster-to-pay reconciliation |
| Young / apprentice worker | As contracted | Age or category eligibility | Birthday and effective-date boundary |
| Director / special status | Separate assessment | Do not inherit standard assumptions | Legal review and separate test |
| Cross-border employee | Separate assessment | Tax residence and social coverage | Treaty / coverage evidence |

### Applied experiment

Build a population decision tree using employment type, residence, age and agreement. Find a case where two classifications differ.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-07"></a>
## 07. Lifecycle Actions

**Category:** Foundation

**What:** Translate employment events into dated payroll changes.

**Why:** A hire, transfer or termination can affect multiple infotypes, eligibility rules and authority messages.

### Approach

1. Map EC event reasons to approved target actions.
2. Preserve effective dates and prior employment identity.
3. Identify the required country reporting event.
4. Reconcile the first and final pay after replication.

### Action design

| Event | Typical payroll data | Country impact | Acceptance evidence |
| --- | --- | --- | --- |
| Hire | Actions / organisation / pay / bank | Register under NRA declarations 1 and 6 | First result and registration receipt |
| Pay change | Basic / recurring / additional pay | Recalculate taxable and insured bases | Effective-date result comparison |
| Transfer | Employer / location / cost assignment | Review local tax and insurance scope | Before-and-after mapping |
| Termination | Leaving date / final earnings | Final reporting and benefit / leave settlement | Final payslip, filing and payment match |
| Rehire | Employment identity and history | Avoid duplicate registrations / annual bases | Cumulative balance review |
| Leave return | Absence and work schedule | Restore the correct earning and insurance treatment | Absence-to-pay reconciliation |

### Applied experiment

Simulate a termination entered after cutoff. Choose whether to reopen, run an approved off-cycle or adjust the next cycle, and justify the reporting consequences.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-08"></a>
## 08. Personal Information

**Category:** Foundation

**What:** Capture reliable identity and classification data.

**Why:** Format-valid identifiers can still belong to the wrong employee or be incompatible with a filing record.

### Approach

1. Collect the identifiers required by the authority and product localization.
2. Validate identity, birth date, residence and evidence of special status.
3. Use supported country-specific fields; confirm actual target infotypes.
4. Minimise copied personal data in test evidence.

### Personal-data control matrix

| Data | Country requirement | Control |
| --- | --- | --- |
| Identity | EGN or foreign-person identifier; NRA employer registration; insurance category | Authoritative document plus duplicate check |
| Birth date | Age-sensitive eligibility | Boundary test at the applicable date |
| Residence / work location | Tax and contribution scope | Effective-date history |
| Dependants / family status | Supported relief / scheme classification | Declaration and validity dates |
| Tax / insurer decision | Authority-supplied classification | Store receipt, expiry and applied version |
| Test identity | Fictional person only | Never submit an invented identifier to an authority |

### Applied experiment

Create a fictional employee data checklist. Explain why a checksum test alone cannot prove that an identifier is correct.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-09"></a>
## 09. Address & Locality

**Category:** Foundation

**What:** Model residence and work location as separate effective-dated records.

**Why:** Municipality, region or canton may drive tax, contribution or reporting classification.

### Approach

1. Capture residence and work establishment separately.
2. Validate the current postal format and official locality reference.
3. Identify whether a move changes payroll treatment.
4. Preserve the old address for earlier periods and corrections.

### Address design

| Field | Learning example / rule | Evidence |
| --- | --- | --- |
| Country | Bulgaria | Country and locality reference |
| City | Sofia | Fictional scenario location only |
| Postal address | Use a validated local structure | Do not rely on an invented universal regex |
| Residence start | Effective-dated | Employee declaration and supporting document |
| Work establishment | Independent from residence | Contract / organisational assignment |
| Cross-border address | Separate tax / social review | Coverage and residence decisions |

### Applied experiment

Enter a future-dated residence move. Decide whether it changes the next payroll, prior payroll or only reporting, using the country evidence desk.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-10"></a>
## 10. Bank Details

**Category:** Foundation

**What:** Validate employee payment instructions and their approval.

**Why:** A successful payroll calculation does not prove that the salary can be paid to the intended beneficiary.

### Approach

1. Identify supported domestic or international bank rails.
2. Validate account structure through the bank-approved process.
3. Require evidence and independent review for account changes.
4. Use synthetic bank test data and record bank acknowledgement.

### Payment master-data checklist

| Item | Country design | Acceptance |
| --- | --- | --- |
| Currency | EUR | Payment currency matches approved account and contract |
| Account identifier | Bank-approved IBAN / domestic account format | Format and beneficiary checks |
| Routing | Required bank / branch / clearing identifier | Approved reference source |
| Change authority | Employee request and independent approval | Audit record retained |
| Payment method | Actual bank-agreed rail and format | Bank test accepted |
| International transfer | Fees, currency and beneficiary assessment | Treasury approval |

### Applied experiment

Reject a bank change with valid syntax but missing employee authorisation. Describe the evidence needed before releasing it.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-11"></a>
## 11. Date Types

**Category:** Configuration

**What:** Maintain the dates that drive eligibility, calculation and reporting.

**Why:** Employment date, earning period and payment date can have different statutory consequences.

### Approach

1. Inventory legal and contractual dates for the population.
2. Distinguish date storage from a processing trigger.
3. Map each date to a supported field or extension.
4. Test a boundary across December / January and a mid-period change.

### Date register

| Date | Purpose | Verification |
| --- | --- | --- |
| Employment start / end | Eligibility and authority events | Contract and reported employment |
| Payment date | Withholding / reporting period where applicable | Bank value date and declaration |
| Earning period | Proration and contribution attribution | Contract and payroll result |
| Rule valid-from | Statutory version selection | Published effective date |
| Benefit eligibility | Insurance / pension / leave scope | Authority or provider decision |
| Earliest retro date | Historical recalculation boundary | Control record, employee status and migration policy |
| Authority due date | Filing / remittance clock | Official country calendar |

### Applied experiment

Place earning date, payment date and submission date on a timeline. Identify which one controls NRA declarations 1 and 6.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-12"></a>
## 12. Replicated Pay Components

**Category:** Configuration

**What:** Map EC compensation into the appropriate target pay records.

**Why:** A pay component can replicate successfully yet have the wrong tax, insurance or pension characteristics.

### Approach

1. Inventory recurring and one-time components.
2. Assign a supported replication route and target infotype.
3. Map business meaning before choosing a local wage-type template.
4. Trace each component into payroll result, filing, payslip and posting.

### Illustrative mapping decisions

| EC component | Typical target | Country classification | Acceptance |
| --- | --- | --- | --- |
| Base salary | Basic Pay (0008) | Tax / insured / pension treatment validated | One standard month |
| Recurring allowance | Recurring Payments / Deductions (0014) where supported | Assess each base independently | Retro and eligibility test |
| One-time bonus | Additional Payments (0015) where supported | Special-pay rules may differ | Bonus and year-end test |
| Employer benefit | Supported benefit / payroll input route | Cash vs non-cash distinction | Payslip and taxable-net trace |
| Reimbursement | Approved payroll / expense interface | Evidence-dependent exemption | Duplicate-payment check |

### Applied experiment

Trace one bonus from EC to the country filing. Explain why copying the base-salary wage type could be wrong.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-13"></a>
## 13. Work Schedules

**Category:** Configuration

**What:** Translate contractual hours, rosters and holidays into payroll inputs.

**Why:** Proration, overtime and minimum-pay checks depend on the actual working-time model.

### Approach

1. Record contractual weekly hours and the applicable agreement.
2. Assign work and holiday calendars by location.
3. Distinguish planned hours, recorded hours and payable hours.
4. Validate mid-period hire, part-time and rotating-roster cases.

### Illustrative schedule design

| Schedule | Proposed pattern | Country decision | Test |
| --- | --- | --- | --- |
| Office full-time | Five-day pattern; contractual hours to confirm | Agreement and local holiday calendar | One public-holiday month |
| Part-time | Employee-specific working days | Proration basis and minimum floor | Mid-month change |
| Operations roster | Approved shift cycle | Overtime / premium eligibility | Month crossing roster boundary |
| On-call | Availability and call-out recorded separately | Tax and earning classification | No double counting |
| Unpaid absence | Reduce agreed payable units | Minimum insured base may still apply | Low-earnings scenario |

### Applied experiment

Create a part-time schedule and explain which units reduce salary, which count for minimum pay and which count for insured days.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-14"></a>
## 14. Time Types & Leave

**Category:** Configuration

**What:** Distinguish absence records from the payment rules they trigger.

**Why:** The same absence can involve employee entitlement, employer liability and insurer reimbursement on different timelines.

### Approach

1. Define absence categories without assuming all are paid.
2. Capture eligibility and supporting documents.
3. Map employer-funded, insurer-funded and unpaid segments.
4. Reconcile absence dates to payroll and reporting events.

### Country leave design

| Category | Country assessment | Evidence / test |
| --- | --- | --- |
| Country baseline | Track employer sickness responsibilities and NSSI benefit claims as separate flows; do not treat all absence days as normal earnings. | Current law, agreement and payer decision |
| Annual leave | Entitlement, pay basis and carryover | Part-time and termination settlement |
| Sickness | Employer vs insurer responsibility | Continuous / linked absence test |
| Maternity / parental | Eligibility and benefit payer | Change of payer and return date |
| Unpaid leave | Pay reduction and insurance consequences | Minimum-base and reporting test |
| Public holiday | Location and roster treatment | Holiday on a non-working day |

### Applied experiment

Build one sickness case from first day to insurer responsibility. Explain each base and any reimbursement without treating the reimbursement as employee earnings.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-15"></a>
## 15. Payroll Control Record

**Category:** Configuration

**What:** Control the payroll-area run state and correction cycle.

**Why:** Run state protects calculation consistency; it must be coordinated with replication and historical changes.

### Approach

1. Use the actual payroll-area control record and period.
2. Distinguish PA03 area control from employee Payroll Status (0003).
3. Review what changes are allowed in the current release and state.
4. Test lock behaviour, correction, rerun and exit before handover.

### Run-state design

| Control | Purpose | Acceptance evidence |
| --- | --- | --- |
| PA03 | Payroll-area period and process state | State transitions documented |
| Employee Payroll Status (0003) | Employee processing / retro information | Employee record checked separately |
| Released for payroll | Protect current and past payroll-relevant changes | Replication lock test |
| Correction cycle | Correct and recalculate exceptions | Release-specific permitted-change test |
| Exit payroll | Close approved processing cycle | Result, reporting, bank and GL reconciliations |
| Retro boundary | Define earliest permissible recalculation | Migration and statutory correction assessment |

### Applied experiment

Attempt a payroll-relevant historical change while the area is locked in a sandbox. Capture the observed behaviour and the correct recovery path.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Supported Countries/Regions | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-s4hana/supported-countries-regions); [Payroll Control Record | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/payroll-control-record); [Setting Up the Point-to-Point Integration | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/setting-up-point-to-point-integration); [Set Up Connection Between an Employee Central Payroll System and Employee Central | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-point-to-point-time-data-replication/set-up-connection-between-employee-central-payroll-system-and-employee-central)

<a id="section-16"></a>
## 16. Payroll Areas & Calendar

**Category:** Configuration

**What:** Build an operational calendar for regular and special runs.

**Why:** The bank cutoff, statutory deadline and calculation cutoff are independent dates.

### Approach

1. Select payroll frequency and period definition.
2. Agree pay-date rules with Treasury and employee contracts.
3. Load official holidays before shifting dates.
4. Create separate calculation, filing, remittance and posting milestones.

### Calendar control points

| Milestone | Planning rule | Owner |
| --- | --- | --- |
| Input cutoff | Agreed business date before calculation | HR / Payroll |
| Replication closure | All critical data accepted before freeze | Integration |
| Calculation and variance review | Allow time for correction and approval | Payroll |
| Payment date | Contractual rule; bank holiday validation | Treasury |
| Filing | Standard employer declaration 1 is due by the 25th of the next month; additional-pay and correction rules differ. | Statutory reporting |
| Remittance | Independent tax / insurer schedule | Treasury / Payroll |
| 2027 opening | Rule pack, calendar and interface versions reviewed | Payroll lead |

### Country reporting note

| Item | Country requirement |
| --- | --- |
| Return | NRA declarations 1 and 6 |
| Timing caution | Preserve employee-level insurance data and aggregate liabilities. Match the declaration version, currency and period before submission. |

### Applied experiment

Build the November 2026 and January 2027 run calendars. Validate actual holiday dates before proposing any final bank or statutory deadline.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-17"></a>
## 17. Wage Type Catalogue

**Category:** Configuration

**What:** Design earning and deduction behaviour across all downstream outputs.

**Why:** Taxable, insurable, pensionable, cash and posting treatment are separate decisions.

### Approach

1. Select delivered local templates only after tenant verification.
2. Document each base and cumulation independently.
3. Assign payslip, authority and GL treatment.
4. Test changes and retro before releasing a customer wage type.

### Illustrative wage-type design — labels are not SAP technical codes

| Business wage type | Cash flow | Tax / social decision | Reconciliation |
| --- | --- | --- | --- |
| Base salary | Cash earning | Standard employee treatment | Gross to payslip / return |
| Bonus | Cash earning | Special vs ordinary payment rule | Tax version and cumulations |
| Taxable benefit | Non-cash earning | Tax and insurance inclusion | Net taxable vs cash net |
| Expense reimbursement | Cash reimbursement | Exemption requires evidence | Expense system duplicate check |
| Employee tax | Employee deduction | Authority withholding result | Tax payable and return |
| Employee social / pension | Employee deduction | Scheme-specific result | Provider and authority liability |
| Employer contribution | Employer cost | Separate from employee net | Expense and liability |
| Attachment | Post-tax / legal-order process | Protected-pay rules | Order balance and remittance |

### Applied experiment

Create a wage-type specification for a company car. List every base and output that must be tested.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-18"></a>
## 18. Salary Payment Configuration

**Category:** Configuration

**What:** Configure the approved bank instruction and release process.

**Why:** A generated payment file is only an instruction; acceptance and settlement need separate evidence.

### Approach

1. Obtain the bank-approved file / API specification.
2. Map debtor, beneficiary, value date and payment reference.
3. Reconcile file control totals to approved cash net.
4. Enforce independent Treasury release and reconcile settlement.

### Bank interface contract

| Control | Proposed acceptance | Evidence |
| --- | --- | --- |
| Format | Actual bank-approved version | Bank specification and sandbox test |
| Currency | EUR | Approved debtor account and settlement currency |
| Count / amount | Matches approved employee payment list | Control-total report |
| Duplicate prevention | Stable run and payment identifiers | Repeated-send test |
| Release | Independent approver | Approval trail |
| Acceptance | Bank acknowledges valid instruction | Bank message / response |
| Settlement | Cash movement matches released totals | Bank statement reconciliation |

### Applied experiment

Generate a fictional three-employee payment control sheet. Design the duplicate prevention test and the acceptance evidence.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-19"></a>
## 19. Off-Cycle Payroll

**Category:** Configuration

**What:** Handle urgent or exceptional payments without breaking cumulative balances.

**Why:** An off-cycle payment can create an extra tax, reporting and remittance event even when the earning belongs to an earlier month.

### Approach

1. Classify the reason: advance, correction, bonus or leaver payment.
2. Select the supported country off-cycle process.
3. Determine payment-date and earning-period consequences.
4. Reconcile regular and off-cycle balances and filing corrections.

### Off-cycle decision matrix

| Reason | Core decision | Country consequence | Approval evidence |
| --- | --- | --- | --- |
| Urgent underpayment | Supplemental pay vs rerun | NRA declarations 1 and 6 and payment-date assessment | Calculation comparison and release |
| Bonus | Regular or separate supported run | Special-pay treatment | Tax / social / reporting trace |
| Leaver settlement | Final pay / post-termination pay | Employment status and return handling | Final result and authority event |
| Advance | Loan / advance vs earnings | Recovery and taxable timing | Signed policy and recovery schedule |
| Reversal | Void instruction or corrective run | Avoid duplicate / orphan reporting | Bank, return and GL reconciliation |

### Applied experiment

Pay a correction after a return has been accepted. Explain which balances and acknowledgements must change.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-20"></a>
## 20. Garnishment Intake

**Category:** Configuration

**What:** Register legal attachment instructions and establish their scope.

**Why:** A deduction order needs legal validity, priority, protected pay and a traceable balance.

### Approach

1. Validate the issuing authority and employee match.
2. Capture order type, priority, valid-from date and balance.
3. Identify the current protected-pay rule and dependant evidence.
4. Route uncertain orders to the legal / payroll owner before deduction.

### Order intake register

| Field | Required record | Acceptance |
| --- | --- | --- |
| Authority | Verified issuer and order reference | Authenticity confirmed |
| Employee | Identity and employment match | No fuzzy-name-only matching |
| Scope | Income categories and effective date | Legal review |
| Priority | Relationship to existing orders | Priority decision recorded |
| Protected amount | Current local schedule and family data | Boundary test |
| Recipient | Verified legal recipient and reference | Bank / authority confirmation |
| Balance | Opening, withheld, remitted, remaining | Period reconciliation |

### Applied experiment

Receive two competing orders. Build an intake record and identify the missing information before either is applied.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-21"></a>
## 21. Payslip Configuration

**Category:** Configuration

**What:** Make gross-to-net and employer information understandable and reconcilable.

**Why:** The employee, authority and Finance may view different bases; a payslip should expose the distinction clearly.

### Approach

1. Confirm legally required fields and delivery language.
2. Separate cash earnings from taxable benefits.
3. Show employee deductions, net pay and relevant cumulative amounts.
4. Test access, correction, accessibility and confidentiality.

### Payslip content decisions

| Element | Country design | Acceptance |
| --- | --- | --- |
| Employer / employee | Legal employer and verified identity | Matches payroll result |
| Pay period / payment date | Show both when distinct | Employee can identify timing |
| Gross earnings | Itemised ordinary and special pay | Wage-type trace |
| Tax | Local withholding labels and basis | Reconciles with NRA declarations 1 and 6 |
| Employee social / pension | Separate components where required | Provider / authority match |
| Non-cash benefits | Visible without inflating bank net | Cash vs taxable-net test |
| Net payment | EUR amount and payment details | Matches released instruction |
| Employer costs | Show where required / chosen | Never deducted twice from employee |

### Applied experiment

Annotate a fictional payslip with gross, tax base, social base and cash net. Explain every difference.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-22"></a>
## 22. Income Tax & Withholding

**Category:** Payroll Rules

**What:** Configure country withholding from its correct taxable basis.

**Why:** A final annual tariff, a tax card and a payroll withholding table are different calculation mechanisms.

### Approach

1. Confirm residency, income type and withholding mechanism.
2. Load the official 2026 version and its valid-from date.
3. Apply allowances, credits, rounding and cumulative rules in statutory order.
4. Test boundaries and compare against the authoritative method.

### 2026 country tax reference — amounts in EUR

| Basis / slice | Rate / setting | Scope |
| --- | --- | --- |
| Employment income tax | 10% | Applicable taxable employment base |
| Employee mandatory contributions | Deduct as permitted | Derive taxable base before income tax |
| Tax relief | Evidence-based | Apply eligibility and annual adjustment |

### Tax configuration decisions

| Decision | Country instruction |
| --- | --- |
| Calculation caution | Classify taxable earnings and employee contributions before applying income tax; separately assess resident and non-resident treatment. |
| Authority | National Revenue Agency and National Social Security Institute |
| 2027 treatment | 2027 amounts and reporting specifications: refresh the cited authority publications before activating a new version. No unverified 2027 numerical rates are preloaded. |
| Production mapping | Confirm delivered country implementation and approved parameters; no guessed schema or tax-table identifiers |

### Applied experiment

Use a supported local reference calculator or official worked example, then reconcile its taxable base, deductions and rounding to a sandbox payroll result.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-23"></a>
## 23. Social Insurance

**Category:** Payroll Rules

**What:** Derive employee and employer contributions independently.

**Why:** Each contribution may have a different base, ceiling, insured category and funding party.

### Approach

1. Classify the employee and actual insurer / scheme.
2. Load the applicable 2026 rate, base and ceiling by component.
3. Calculate employee deductions and employer costs separately.
4. Test threshold, low-pay, special-status and retro cases.

### 2026 component reference

| Component | Employee | Employer / combined figure | Scope |
| --- | --- | --- | --- |
| Pension / supplementary pension | Birth-cohort dependent | Category-dependent | Use the employed-person schedule |
| Health insurance | Official employee share | Official employer share | Do not use self-employed percentages |
| Sickness and unemployment | Insured-category schedule | Insured-category schedule | Apply contribution ceiling |
| Occupational risk | — | Risk-category rate | Employer-only component |

### Contribution controls

| Control | Country decision |
| --- | --- |
| Local caution | NSSI publishes a 2026 ceiling split: EUR 2,111.64 January–July and EUR 2,300 August–December. Confirm the employee category; the self-employed minimum is not an employee wage floor. |
| Pension relationship | Resolve pension cohort and supplementary-fund membership before deriving contributions; keep fund identifiers effective-dated. |
| Ceiling design | Document component, period, currency, proration and excess treatment |
| Exemptions | Retain valid evidence; never assume a reduction based on a job title alone |
| Reconciliation | Payroll result → individual declaration → aggregate liability → remittance |

### Applied experiment

Construct a gross-to-base worksheet for each component. Find one reason the social base could differ from the tax base.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-24"></a>
## 24. Statutory Reporting

**Category:** Payroll Rules

**What:** Convert approved results into accepted country declarations.

**Why:** A transmitted file can still be rejected, incomplete or mismatched to the payment liability.

### Approach

1. Inventory every employee, employer and event return.
2. Select the correct period-specific format and legal registration.
3. Validate counts, bases, liabilities and identifiers before sending.
4. Retain acknowledgement and reconcile corrections and remittances.

### Country reporting design

| Item | Requirement |
| --- | --- |
| Reporting route | NRA declarations 1 and 6 |
| Timing | Standard employer declaration 1 is due by the 25th of the next month; additional-pay and correction rules differ. |
| Important distinction | Preserve employee-level insurance data and aggregate liabilities. Match the declaration version, currency and period before submission. |
| Employee identity | EGN or foreign-person identifier; NRA employer registration; insurance category |
| Success evidence | Accepted processing feedback, not merely upload completion |
| Correction | Versioned replacement / correction linked to the original receipt |
| Outage | Document failed attempts, escalation and approved recovery |

### Submission runbook

| Step | Control | Owner |
| --- | --- | --- |
| Prepare | Match approved payroll and declaration population | Reporting analyst |
| Validate | Authority format / schema and control totals | Payroll reviewer |
| Authorise | Independent release decision | Payroll lead |
| Submit | Use authorised secure channel | Delegated filer |
| Close | Receipt, liability and payment reconciled | Payroll / Treasury |

### Applied experiment

Create a fictional rejected-return incident. Trace it back to one employee input, correct it and describe the accepted closure evidence.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-25"></a>
## 25. Pensions & Enrolment

**Category:** Payroll Rules

**What:** Resolve pension coverage, contribution bases and provider movements.

**Why:** Statutory social insurance, occupational pensions and voluntary savings may coexist without sharing a base.

### Approach

1. Identify mandatory coverage and any enrolment / opt-out rules.
2. Capture provider, plan, membership and effective dates.
3. Document pensionable earnings and employee / employer shares.
4. Reconcile contributions, joiners, leavers and provider acknowledgements.

### Country pension design

| Area | Decision / control |
| --- | --- |
| Local treatment | Resolve pension cohort and supplementary-fund membership before deriving contributions; keep fund identifiers effective-dated. |
| Membership | Evidence of eligibility, election and provider acceptance |
| Earnings base | List included and excluded wage types; test special pay |
| Contribution | Use statutory / actual plan rules rather than a national average |
| Changes | Handle joiner, leaver, unpaid leave and backdated enrolment |
| Provider interface | Secure file / API, control totals and rejection recovery |
| Reconciliation | Employee deduction + employer cost = provider liability, adjusted for timing |

### Applied experiment

Design a pension enrolment test that crosses an eligibility date and includes a bonus. Explain the base and provider evidence.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-26"></a>
## 26. Benefits & Expenses

**Category:** Payroll Rules

**What:** Classify non-cash benefits and reimbursed expenses correctly.

**Why:** Tax, social insurance, pension and cash-net treatment can differ for the same benefit.

### Approach

1. Inventory each benefit and reimbursement type.
2. Obtain the current valuation and exemption conditions.
3. Record employee contributions and private / business use.
4. Reconcile payroll, expense system and authority reporting.

### Benefit assessment

| Type | Country / design assessment | Evidence |
| --- | --- | --- |
| Country baseline | Separate taxable allowances from documented reimbursed business expenditure; validate any vouchers or social-expense treatment. | Current authority rule and effective date |
| Company car | Value, private use and employee payment | Contract and valuation sheet |
| Meal / voucher | Cash vs non-cash; exemption conditions | Provider and employee eligibility |
| Housing / phone | Tax and contribution treatment | Usage and market / statutory valuation |
| Business expense | Reimbursement vs taxable allowance | Receipt and business purpose |
| Salary exchange | Legal, contractual and base consequences | Employee agreement and floor test |

### Applied experiment

Create a benefit decision record with four independent outcomes: tax, social, pension and bank net. Find a case where they differ.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-27"></a>
## 27. Statutory & Absence Pay

**Category:** Payroll Rules

**What:** Model pay entitlements, benefit responsibility and recoveries.

**Why:** Leave entitlement does not automatically mean the employer pays full salary for the entire absence.

### Approach

1. Identify legal entitlement and the contractual supplement.
2. Determine qualifying period, reference earnings and payer.
3. Define payroll payment and insurer-recovery flows separately.
4. Test the transition between funding parties and return to work.

### Country payment design

| Layer | Assessment | Evidence |
| --- | --- | --- |
| Country baseline | Track employer sickness responsibilities and NSSI benefit claims as separate flows; do not treat all absence days as normal earnings. | Legislation, agreement and insurer decision |
| Eligibility | Service, insurance and supporting-document conditions | Eligibility worksheet |
| Reference earnings | Official period and included earnings | Calculation record |
| Employer payment | Salary continuation or supplement | Contract and payroll result |
| Insurer benefit | Direct payment vs reimbursement / subrogation | Claim and receipt |
| Reporting | Absence / benefit / employment event | Accepted declaration |
| Recovery | Offset only a proven recoverable amount | Claims-to-ledger reconciliation |

### Applied experiment

Build a sickness case with partial employer pay and an insurer benefit. Explain how you prevent duplicate employee payment.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-28"></a>
## 28. Minimum Pay & Agreements

**Category:** Payroll Rules

**What:** Test remuneration against the correct legal or contractual floor.

**Why:** An hourly floor, a monthly floor and a collective-agreement minimum cannot be substituted for one another.

### Approach

1. Identify the applicable legal, regional and collective-agreement floor.
2. Record units, eligible earnings, hours and effective dates.
3. Prorate only according to the governing rule.
4. Test young workers, part-time, unpaid absence and salary exchange.

### Country minimum-pay assessment

| Item | Country / design decision |
| --- | --- |
| Current floor guidance | Load the enacted employee minimum-wage decree in EUR and the occupational insurance minima; neither equals the self-employed minimum. |
| Unit | Hourly / monthly / annual / agreement classification must be explicit |
| Covered earnings | Determine which allowances, bonuses and benefits count |
| Hours | Distinguish paid, contracted and actually worked units |
| Effective date | Allow in-year and 2027 changes without overwriting history |
| Exceptions | Require legal basis and employee-category evidence |
| Acceptance | At-boundary and one-unit-below tests using the current authority rule |

### Applied experiment

Calculate the floor test for a part-time employee with an allowance. Explain whether the allowance counts and what evidence supports that choice.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-29"></a>
## 29. Attachment Calculation & Remittance

**Category:** Payroll Rules

**What:** Apply valid orders while protecting the legally reserved amount.

**Why:** Deduction priority, protected earnings and remaining balances must be recalculated consistently.

### Approach

1. Determine the legally attachable earning base.
2. Apply current protected-pay and dependant rules.
3. Resolve competing orders and any permitted fees.
4. Reconcile withholding, recipient remittance and remaining order balance.

### Attachment control sequence

| Step | Decision | Test |
| --- | --- | --- |
| Base | Which earnings can legally be attached? | Bonus / benefit / final-pay case |
| Protection | Current Bulgaria schedule and household evidence | Below / at / above protected pay |
| Priority | Order precedence and parallel deductions | Two competing orders |
| Limit | Maximum deduction and residual balance | Low-net and final-instalment case |
| Remittance | Recipient, reference and due date | Payment and order balance match |
| Change / stop | Effective notice and release | No deduction after valid stop |
| Privacy | Restrict order access | Role and audit-log review |

### Applied experiment

Model a low-net month with two orders. Record the legal assumptions instead of forcing the planned instalment through.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-30"></a>
## 30. Schema & Calculation Sequence

**Category:** Payroll Rules

**What:** Trace the delivered local payroll process before changing it.

**Why:** Guessed schema names or copied technical wage types can make a plausible design impossible to implement.

### Approach

1. Confirm the licensed local version and support package.
2. Inspect the actual delivered schema and calculation log.
3. Trace inputs, valuation, bases, tax, social and net processing.
4. Use supported customer extensions with regression evidence.

### Conceptual calculation path — verify actual delivered order

| Stage | Input / result | Control |
| --- | --- | --- |
| Input | Employment, pay, time and benefit data | Effective dates and completeness |
| Valuation | Payable units and earning amounts | Agreement and proration |
| Bases | Taxable, insurable and pensionable values | Independent classification |
| Statutory calculations | Tax / employee and employer components | Country rule version |
| Net and balances | Cash net and cumulative results | No duplicate non-cash or deduction |
| Outputs | Payslip, declaration, bank and Finance | Cross-output reconciliation |
| Technical mapping | Tenant-confirmed schema / PCR / wage types | No production identifier is asserted by this workbook |

### Applied experiment

Annotate one actual sandbox calculation log. Identify where a wrong base first appears, before looking at the final net amount.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Supported Countries/Regions | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-s4hana/supported-countries-regions); [Payroll Control Record | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/payroll-control-record); [Setting Up the Point-to-Point Integration | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/setting-up-point-to-point-integration); [Set Up Connection Between an Employee Central Payroll System and Employee Central | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-point-to-point-time-data-replication/set-up-connection-between-employee-central-payroll-system-and-employee-central)

<a id="section-31"></a>
## 31. Retroactive Processing

**Category:** Payroll Rules

**What:** Recalculate history without losing the original result or reporting lineage.

**Why:** Historical earning rules and current payment-date obligations may both matter in a single correction.

### Approach

1. Identify the effective period and earliest permissible retro date.
2. Preserve original results and applied legal versions.
3. Determine statutory correction and current-payment consequences.
4. Reconcile delta pay, declarations, provider movements and Finance.

### Retro decision matrix

| Scenario | Country assessment | Evidence |
| --- | --- | --- |
| Backdated salary change | Earning-period bases and tax method | Original vs recalculated result |
| Historical classification correction | Insurer / locality / tax status validity | Authority or employee evidence |
| Prior-year payment | Year boundary and reporting correction | Year-specific legal assessment |
| Pre-migration adjustment | Opening balances and legacy ownership | Signed migration reconciliation |
| Benefit correction | Tax, social and cash effects may differ | Valuation and payslip comparison |
| Payment already settled | Delta instruction; avoid duplicate gross payment | Bank and GL reconciliation |

### Applied experiment

Backdate a salary change into 2026 and pay the difference in 2027. List every rule version and reporting period you must assess.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-32"></a>
## 32. Year-End & New-Year Opening

**Category:** Payroll Rules

**What:** Close annual obligations and prepare a controlled 2027 opening.

**Why:** A correct December net does not prove annual certificates, ceilings or January parameters are correct.

### Approach

1. Reconcile year-to-date balances to filings, remittances and GL.
2. Prepare country certificates and employee summaries.
3. Identify current-year and prior-year correction routes.
4. Load only validated new-year rules and retest boundaries.

### Country year-end assessment

| Area | Instruction |
| --- | --- |
| Local obligations | Reconcile annual employment income and tax adjustments, including balances converted from lev; retain the fixed-rate conversion evidence. |
| 2027 onward | 2027 amounts and reporting specifications: refresh the cited authority publications before activating a new version. No unverified 2027 numerical rates are preloaded. |
| Balance closure | Gross, tax, employee social, employer costs, pension and net |
| Certificate / summary | Required employee and authority versions and due dates |
| Open items | Unsettled bank returns, authority rejections and provider differences |
| New-year opening | Calendar, age cohorts, limits, tax cards / tables and interface versions |
| Sign-off | Payroll, Finance, statutory reporting and provider owners |

### Applied experiment

Create a December-to-January checklist and identify three differences that a cumulative year-end reconciliation could reveal.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-33"></a>
## 33. Authority Updates & Notices

**Category:** Payroll Rules

**What:** Turn an authority notification into a controlled payroll decision.

**Why:** A notice may change one employee, one employer registration or an entire statutory rule pack.

### Approach

1. Verify the issuer, scope and validity of the update.
2. Classify employee instruction, rate change or format change.
3. Assess effective date and any historical impact.
4. Capture application, review and reconciliation evidence.

### Notification handling

| Notice type | Required action | Acceptance |
| --- | --- | --- |
| Tax instruction | Apply the valid employee / employer instruction | Receipt version and affected run |
| Insurance decision | Update coverage and contribution classification | Insurer evidence and valid-from date |
| Statutory publication | Euro adoption took effect on 1 January 2026 at EUR 1 = BGN 1.95583. Historical payroll and retro periods need controlled currency conversion. | Impact analysis and regression |
| 2027 publication | 2027 amounts and reporting specifications: refresh the cited authority publications before activating a new version. No unverified 2027 numerical rates are preloaded. | No activation from an unverified proposal |
| Rejected declaration | Resolve error against original submission | Accepted correction and reconciled liability |
| Bank / provider update | Validate new format or account mandate | Approved compatibility test |

### Applied experiment

Receive a notice after input cutoff with an earlier effective date. Decide the payroll and correction path and record the reasoning.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll configuration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-34"></a>
## 34. EC Data Validation

**Category:** Integration

**What:** Prevent incomplete or inconsistent data from entering payroll.

**Why:** Replication success is a technical result; statutory data validity requires additional business checks.

### Approach

1. Define mandatory fields by employee population and country.
2. Validate combinations and effective dates, not only syntax.
3. Route errors to an accountable business owner.
4. Reconcile EC population to accepted ECP records before calculation.

### Validation matrix

| Field / combination | Rule | Disposition |
| --- | --- | --- |
| Identity | EGN or foreign-person identifier; NRA employer registration; insurance category | Hold critical missing or conflicting data |
| Employer / country / currency | Supported combination and valid registration | Resolve before replication release |
| Tax / insurance classification | Authority evidence valid for period | Escalate unsupported category |
| Pay and hours | Contract, unit and minimum-pay consistency | Payroll / HR review |
| Bank change | Verified request plus approval | Block payment release until complete |
| Dependants / special relief | Declaration and valid dates | Apply only supported treatment |
| Termination / payment | Final date and post-termination handling | Review reporting and final pay |

### Applied experiment

Create a record that passes format validation but fails a business combination check. Explain which owner resolves it.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Integration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Supported Countries/Regions | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-s4hana/supported-countries-regions); [Payroll Control Record | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/payroll-control-record); [Setting Up the Point-to-Point Integration | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/setting-up-point-to-point-integration); [Set Up Connection Between an Employee Central Payroll System and Employee Central | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-point-to-point-time-data-replication/set-up-connection-between-employee-central-payroll-system-and-employee-central)

<a id="section-35"></a>
## 35. Payment Exceptions

**Category:** Integration

**What:** Recover failed instructions without paying twice.

**Why:** Rejection, accepted-but-unsettled and returned-after-settlement states require different responses.

### Approach

1. Read the actual bank response and identify the failed stage.
2. Separate master-data correction from payment reissue.
3. Check original settlement before a replacement instruction.
4. Reconcile payroll, bank, GL and employee communication records.

### Exception runbook

| Observed state | Investigation | Recovery evidence |
| --- | --- | --- |
| Format rejected | Bank specification and control totals | Corrected file; original rejected |
| Beneficiary rejected | Verified account and employee authorisation | Approved master-data correction |
| Acknowledged; settlement unknown | Bank tracking / Treasury enquiry | No duplicate instruction until status resolved |
| Returned after payment | Statement and original reference | Return posted and approved reissue |
| Duplicate detected | Run / payment identity comparison | Blocked duplicate and audit record |
| Partial acceptance | Accepted vs rejected employee list | Reissue only proven unpaid items |

### Applied experiment

A bank accepts a file but one employee says payment is missing. Explain the investigation before authorising another transfer.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Integration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-36"></a>
## 36. Finance Posting

**Category:** Integration

**What:** Map payroll expenses and liabilities into reconciled Finance documents.

**Why:** Technical wage types and GL accounts must be verified in the tenant; business labels alone do not establish posting correctness.

### Approach

1. Agree the chart of accounts and cost-object ownership.
2. Map business wage types through the supported symbolic-account design.
3. Separate employee liabilities, employer costs and clearing.
4. Reconcile posting, remittance and bank settlement by currency and period.

### Illustrative accounting design — business labels only

| Event | Debit concept | Credit concept | Reconciliation |
| --- | --- | --- | --- |
| Gross cash earnings | Salary expense | Payroll clearing | Earning result |
| Employee tax withheld | Payroll clearing | Tax payable | Declaration and tax payment |
| Employee social / pension | Payroll clearing | Insurer / pension payable | Individual and aggregate totals |
| Employer contribution | Employer contribution expense | Insurer / pension payable | Employer liability |
| Net salary paid | Payroll clearing | Bank clearing / bank | Released instruction and settlement |
| Taxable non-cash benefit | Benefit / offset accounts per design | Approved offset concept | No fictitious cash payment |
| Cost allocation | Expense by approved cost object | Counterpart per posting design | Cost-centre totals and split dates |

### Applied experiment

Prepare a balanced fictional journal and prove that employee deductions are liabilities while employer contributions are additional cost.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Integration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-37"></a>
## 37. Replication Triggers & Monitoring

**Category:** Integration

**What:** Move effective-dated employee changes into payroll and prove they arrived.

**Why:** A missing or delayed change may be invisible until an employee is paid incorrectly.

### Approach

1. Use the supported replication scope and schedule.
2. Identify changes to employee, compensation, time and bank data.
3. Monitor confirmation status and investigate rejects.
4. Replay only with idempotency and a population reconciliation.

### Trigger / control matrix

| Change | Payroll impact | Monitoring evidence |
| --- | --- | --- |
| Hire / rehire | Create valid employment and pay records | Target identity and confirmation |
| Compensation | Correct effective-dated wage input | Source / target amount and date |
| Bank | Approved payment instruction | Change approval and target match |
| Residence / dependants | Tax / insurance / relief assessment | Classification decision |
| Absence / time | Payable units and benefit processing | Time-replication confirmation |
| Termination | Final pay and employment reporting | Target date and final-result review |
| Correction during lock | Release-specific queue / retry behaviour | No lost change or silent overwrite |

### Applied experiment

Simulate a failed compensation replication and demonstrate how the next accepted replay avoids a duplicate payment.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Integration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Supported Countries/Regions | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-s4hana/supported-countries-regions); [Payroll Control Record | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/payroll-control-record); [Setting Up the Point-to-Point Integration | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/setting-up-point-to-point-integration); [Set Up Connection Between an Employee Central Payroll System and Employee Central | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-point-to-point-time-data-replication/set-up-connection-between-employee-central-payroll-system-and-employee-central)

<a id="section-38"></a>
## 38. Integration Suite & Extensions

**Category:** Integration

**What:** Use middleware where the chosen interface architecture requires it.

**Why:** Standard EC-to-ECP point-to-point master-data replication should not be replaced by an invented mandatory middleware flow.

### Approach

1. Confirm standard point-to-point scope and release prerequisites.
2. Inventory external bank, benefit, time and Finance integrations.
3. Use approved Integration Suite packages or extensions only where needed.
4. Define authentication, data minimisation, retry and reconciliation controls.

### Architecture decisions

| Flow | Supported design assessment | Evidence |
| --- | --- | --- |
| EC master data → ECP | Assess delivered point-to-point integration | Current SAP guide and tenant configuration |
| EC time → ECP | Assess delivered time replication | Supported mapping and confirmation |
| External benefits / time | Optional middleware based on actual source | Interface contract and reconciliation |
| Bank / authority / provider | Actual supported file, API or delegated service | Recipient specification and acceptance |
| Finance | Supported posting / integration pattern | Document and cost-object reconciliation |
| Security | Release-supported credentials and scoped roles | No secrets stored in the HTML workbook |
| Operations | Explicit retry, duplicate prevention and alert owner | Failed-message recovery test |

### Applied experiment

Compare a standard master-data flow with an external benefits interface. Explain which needs middleware and why.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Integration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Supported Countries/Regions | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-s4hana/supported-countries-regions); [Payroll Control Record | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/payroll-control-record); [Setting Up the Point-to-Point Integration | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/setting-up-point-to-point-integration); [Set Up Connection Between an Employee Central Payroll System and Employee Central | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-point-to-point-time-data-replication/set-up-connection-between-employee-central-payroll-system-and-employee-central)

<a id="section-39"></a>
## 39. Test Scenarios

**Category:** Governance

**What:** Validate calculation and every downstream output with owned evidence.

**Why:** A green status without actual execution evidence makes the workbook unreliable as an implementation record.

### Approach

1. Define expected results independently of the implementation.
2. Use synthetic data and current authority examples.
3. Capture result, declaration, payment and posting evidence.
4. Leave status Not run until the actual environment has been tested.

### Country test pack — all scenarios initially not run

| Scenario | Expected control | Status |
| --- | --- | --- |
| Standard local employee | Gross-to-net, return, bank and GL reconcile | Not run |
| Tax threshold / card / table boundary | Correct method and effective version | Not run |
| Social base / ceiling / special category | Correct component allocation | Not run |
| Country experiment | Recalculate a pre-euro retro adjustment paid in 2026; preserve the original currency result and the conversion audit trail. | Not run |
| New hire / mid-period change | Proration and registration accurate | Not run |
| Termination / post-termination pay | Final earnings and reporting accurate | Not run |
| Sickness / parental absence | Correct payer and reference earnings | Not run |
| Pension entry / exit | Correct membership and liability | Not run |
| Taxable benefit | Correct tax, social and cash treatment | Not run |
| Attachment / low net | Protected pay and priority observed | Not run |
| Bank rejection / replay | Only unpaid items reissued | Not run |
| Replication while locked | No lost or unintended data change | Not run |
| Prior-year retro | Historical result and reporting lineage retained | Not run |
| 2027 opening | Only approved new-year settings active | Not run |
| Authority rejection / correction | Accepted feedback reconciles to liability | Not run |
| Finance / bank settlement | Posting and actual cash reconcile | Not run |

### Applied experiment

Select one scenario and write an independently calculated expected result. Identify the exact evidence needed to change Not run to Passed.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll delivery lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

<a id="section-40"></a>
## 40. Cutover Plan

**Category:** Governance

**What:** Sequence migration, validation and first live processing by dependency.

**Why:** A fixed date is meaningless if employee balances, registrations or payment approvals are not ready.

### Approach

1. Choose a go-live period and assign entry criteria.
2. Freeze and reconcile legacy master data and balances.
3. Complete representative parallel processing and recipient testing.
4. Approve first live payroll, then monitor settlement and accepted filings.

### Relative cutover milestones — planning proposals

| Milestone | Activity | Gate / owner |
| --- | --- | --- |
| Before final migration | Registration, product and interface readiness | Payroll / integration / Treasury |
| Legacy freeze | Approved input cutoff and change log | HR / Payroll |
| Migration | Employee data, year-to-date and open liabilities | Data lead; signed reconciliations |
| Parallel comparison | Gross, tax, social, net and downstream outputs | Payroll; explained differences |
| Go / no-go | No unresolved critical employee or statutory issue | Business accountable owner |
| First live calculation | Full variance and exception review | Payroll approver |
| Release | Authorised declarations and bank instructions | Statutory / Treasury |
| Closure | Accepted feedback, settled cash and balanced posting | Payroll / Finance |
| Hypercare exit | Stable owned operations and resolved critical issues | Service owner |

### Applied experiment

Set a proposed go-live month and work backwards from the country filing and bank dates. Replace relative dates only after checking the real calendar.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll delivery lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-41"></a>
## 41. Training & Facilitation

**Category:** Governance

**What:** Turn configuration knowledge into demonstrated operating capability.

**Why:** Learners should explain a decision and recover an exception, not merely recognise a screen.

### Approach

1. Assign one practical outcome per role.
2. Use the country scenario and synthetic employee evidence.
3. Ask learners to predict, test, explain and improve.
4. Assess the complete flow rather than attendance alone.

### Suggested 21-hour experiential arc — learning design

| Session | Practice outcome | Duration |
| --- | --- | --- |
| Discover and source | Scope, authority evidence and employee classification | 3 hours |
| Design foundations | Employment, time, bank and wage-type decisions | 3 hours |
| Calculate locally | Tax, social, pension and benefit bases | 3 hours |
| Report and pay | Accepted declaration, remittance and bank design | 3 hours |
| Connect and reconcile | EC replication and Finance posting | 3 hours |
| Test and recover | Boundary, rejection and retro scenarios | 3 hours |
| Operate and explain | Cutover simulation, teach-back and reflection | 3 hours |

### Facilitator prompts

| Prompt | Evidence |
| --- | --- |
| What do you predict? | Written expected result before sandbox execution |
| What surprised you? | Difference traced to one data or rule choice |
| What would you change? | Revised decision with a new test |
| Can you teach it? | Three-minute explanation with a reconciled artifact |

### Applied experiment

Facilitate a 20-minute teach-back using Recalculate a pre-euro retro adjustment paid in 2026; preserve the original currency result and the conversion audit trail. Ask for one prediction and one revised explanation.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll delivery lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-42"></a>
## 42. Hypercare & Operations

**Category:** Governance

**What:** Establish an owned service for payroll, reporting and payment exceptions.

**Why:** The first live runs need fast triage and complete reconciliation across systems and authorities.

### Approach

1. Define severity by employee impact and statutory / cash deadline.
2. Assign business, technical and recipient escalation owners.
3. Set service targets as contract proposals, not legal deadlines.
4. Exit hypercare only after stable cycles and knowledge transfer.

### Proposed service targets — confirm with the organisation

| Priority | Trigger | Response proposal | Closure evidence |
| --- | --- | --- | --- |
| Critical | Widespread unpaid salary or imminent statutory failure | Immediate triage; named incident lead | Paid / accepted / reconciled with approved recovery |
| High | Individual material error or rejected return | Within agreed payroll support window | Corrected employee and downstream outputs |
| Medium | Statement / posting discrepancy without missed pay | Next agreed support window | Reconciled explanation and correction |
| Low | Enhancement or usability request | Prioritised backlog | Reviewed change and regression evidence |

### Operational checks

| Control | Owner |
| --- | --- |
| Replications accepted and exceptions owned | Integration / HR |
| Country obligations monitored: NRA declarations 1 and 6 | Payroll reporting |
| Bank and tax / insurer cash settled | Treasury |
| GL and provider balances reconciled | Finance / Benefits |
| 2027 changes reviewed before activation | Payroll legal / configuration owners |

### Applied experiment

Run a desk simulation of a statutory rejection on payday. Identify incident owner, recovery, employee impact and closure evidence.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll delivery lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** 

<a id="section-43"></a>
## 43. End-to-End Integration Map

**Category:** Integration

**What:** Trace an employee change through all systems and reconciliations.

**Why:** Interface-level success does not guarantee a correct employee, statutory or accounting outcome.

### Approach

1. Map source, target, business object and confirmation.
2. Separate master data, time, calculation and outputs.
3. Identify where an owner accepts each handoff.
4. Demonstrate recovery after one intentionally failed handoff.

### Country integration contract

| Source → target | Business object | Acceptance evidence |
| --- | --- | --- |
| Employee Central → ECP | Employment, personal and compensation data | Supported replication confirmation and target comparison |
| Time source → ECP | Payable time and absence | Accepted input and date / unit reconciliation |
| ECP → employee | Payslip and approved net pay | Employee document matches result |
| ECP → National Revenue Agency and National Social Security Institute | NRA declarations 1 and 6 | Accepted processing feedback and liability reconciliation |
| ECP → bank | Salary payment instruction | Acceptance plus settlement |
| ECP → pension / insurer | Membership and contribution data | Provider acceptance and liability match |
| ECP → Finance | Expenses, liabilities and cost allocation | Balanced document and clearing reconciliation |
| Authority / provider → payroll | Notices and error feedback | Owned decision, correction and closure |

### Applied experiment

Trace Elena Petrova from a pay change in EC through reporting, payment and GL. Mark every acknowledgement and reconciliation.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Integration lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Supported Countries/Regions | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-s4hana/supported-countries-regions); [Payroll Control Record | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/payroll-control-record); [Setting Up the Point-to-Point Integration | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/setting-up-point-to-point-integration); [Set Up Connection Between an Employee Central Payroll System and Employee Central | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-point-to-point-time-data-replication/set-up-connection-between-employee-central-payroll-system-and-employee-central)

<a id="section-44"></a>
## 44. Risk Register

**Category:** Governance

**What:** Make uncertain statutory, data and delivery decisions visible and owned.

**Why:** A useful risk register links each risk to a preventive control, evidence and decision owner.

### Approach

1. Identify the failure and affected employee / obligation.
2. Assign impact, likelihood and accountable owner.
3. Define prevention, detection and recovery evidence.
4. Review residual risk at each release and go-live gate.

### Initial risk register — ratings are workshop proposals

| Risk | Impact | Mitigation / evidence | Owner |
| --- | --- | --- | --- |
| Wrong 2026 or 2027 legal version | Critical | Source, valid-from date and boundary tests | Payroll legal owner |
| Country-specific change missed | High | Euro adoption took effect on 1 January 2026 at EUR 1 = BGN 1.95583. Historical payroll and retro periods need controlled currency conversion. | Country payroll lead |
| Unverified identity / classification | High | Document validation and source-target checks | HR / Payroll |
| Wrong tax or social base | Critical | Independent expected results and component trace | Configuration lead |
| Reporting version / date mismatch | Critical | Current NRA declarations 1 and 6 specification and calendar | Reporting lead |
| Unconfirmed product localization | High | Release / license / country support gate | Solution architect |
| Lost replication during lock | High | Supported queue / retry and population reconciliation | Integration lead |
| Duplicate or unpaid salary | Critical | Idempotency, independent release and settlement | Treasury |
| Wrong pension coverage | High | Membership and provider reconciliation | Benefits lead |
| Unreconciled year-to-date balances | High | Signed migration and annual reconciliation | Data / Finance |
| Unsupported special regime | High | Separate legal and product assessment | Payroll lead |
| Sensitive data in training | High | Synthetic employees and scoped access | Security / facilitator |
| Unresolved authority guidance conflict | High | Document conflicting pages and obtain governing decision | Statutory owner |
| Local progress assumed to be shared evidence | Medium | Export and controlled team evidence repository | Facilitator |
| New-year copy-forward without review | High | 2027 activation gate and regression pack | Payroll lead |

### Applied experiment

Choose the two highest country risks and define a measurable control that proves they are reduced before go-live.

**Prerequisite:** Foundation data and the relevant country rule decision

**Suggested owner:** Payroll delivery lead

### Evidence to capture

- Decision and effective date recorded
- Country / employee scope stated
- Expected result or acceptance criterion written
- Sandbox / authority / bank evidence linked when actually executed
- Open questions assigned to a named owner

Explain your decision, record the unresolved assumption and choose the next validation experiment.

**Learner review:** Not started. **Implementation tests:** Not run.

**Decision / notes:** _Add your decision, effective date, evidence link, owner and next experiment._

**Reference trail:** [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827); [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6); [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/); [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga); [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)

## Learning tool 1 — Knowledge quiz

Record A, B, C or D before consulting the answer key.

### Question 1: Which authority set is relevant to this Bulgaria workbook?

A. National Revenue Agency and National Social Security Institute
B. A single worldwide payroll authority
C. The employee’s bank alone
D. Only the software vendor

**Your answer / reasoning:** __________________

### Question 2: Which employee-data set should be established before Bulgaria payroll?

A. An email address alone
B. EGN or foreign-person identifier; NRA employer registration; insurance category
C. A job title without identity records
D. A training nickname

**Your answer / reasoning:** __________________

### Question 3: Which reporting route belongs in the Bulgaria design?

A. A generic bank transfer receipt
B. A personal expense claim
C. NRA declarations 1 and 6
D. A learning-completion badge

**Your answer / reasoning:** __________________

### Question 4: Which minimum-pay statement fits this country?

A. Every country uses the same monthly floor
B. A Eurostat comparison figure is always a payroll floor
C. Any company allowance automatically counts
D. Load the enacted employee minimum-wage decree in EUR and the occupational insurance minima; neither equals the self-employed minimum.

**Your answer / reasoning:** __________________

### Question 5: What is the correct first step for the highlighted country experiment?

A. Recalculate a pre-euro retro adjustment paid in 2026; preserve the original currency result and the conversion audit trail.
B. Apply a copied rate without checking the base
C. Mark the scenario passed before execution
D. Ignore all effective dates

**Your answer / reasoning:** __________________

### Question 6: How should a 2027 rate not yet verified in this workbook be handled?

A. Assume it equals 2026
B. Keep it pending until authoritative confirmation
C. Use an average from neighbouring countries
D. Delete the historical 2026 version

**Your answer / reasoning:** __________________

### Question 7: What proves that a statutory declaration is complete?

A. The file exists
B. The upload button was clicked
C. Accepted processing feedback plus reconciled liability
D. The employee downloaded a payslip

**Your answer / reasoning:** __________________

### Question 8: Which item is the payroll-area run control?

A. An employee bank record
B. A payslip template
C. A tax declaration receipt
D. PA03 control record

**Your answer / reasoning:** __________________

### Question 9: How should employer contributions affect the standard gross-to-net bridge?

A. They are additional employer cost, unless a specific legal arrangement says otherwise
B. They are always deducted again from employee cash net
C. They replace the employee income tax
D. They can be omitted from Finance

**Your answer / reasoning:** __________________

### Question 10: Which approach is supported for EC-to-ECP master-data design?

A. Invent a mandatory middleware flow ID
B. Assess delivered point-to-point replication and actual release requirements
C. Assume no confirmation is needed
D. Copy a country schema name from a different country

**Your answer / reasoning:** __________________

### Question 11: A bank instruction is acknowledged but settlement is unknown. What comes next?

A. Pay the full file again
B. Delete the original payment ID
C. Investigate settlement before authorising a replacement
D. Mark the employee paid without checking

**Your answer / reasoning:** __________________

### Question 12: What is the strongest evidence that a learner can operate the process?

A. Attendance alone
B. Reading every page
C. Selecting every completion checkbox
D. Explaining and reconciling a country case with tested evidence

**Your answer / reasoning:** __________________

### Quiz answer key

| Question | Answer | Explanation |
| --- | --- | --- |
| 1 | A | The evidence desk identifies the relevant national authorities; employer registrations and scope still need confirmation. |
| 2 | B | Use the required identifiers and valid classification evidence; format checks alone are insufficient. |
| 3 | C | Preserve employee-level insurance data and aggregate liabilities. Match the declaration version, currency and period before submission. |
| 4 | D | Confirm units, effective dates, covered earnings and employee category before testing the floor. |
| 5 | A | Build a prediction and trace its country-specific basis before sandbox execution. |
| 6 | B | A prospective parameter needs a source, effective date, scope and approval before activation. |
| 7 | C | Transmission, acceptance, payment and reconciliation are separate states. |
| 8 | D | The payroll-area control record is distinct from employee Payroll Status (0003). |
| 9 | A | Separate employee deductions, employer costs and recipient liabilities to avoid double deduction. |
| 10 | B | Use the current SAP guide and the actual tenant; external extensions may use middleware where required. |
| 11 | C | A duplicate payment is prevented by proving the status of the original instruction. |
| 12 | D | Learning progress is self-recorded; implementation validation requires real, independently assessed evidence. |

## Learning tool 2 — Flashcards

Cover the answer column, explain the prompt and compare.

| Card | Prompt | Retrieval answer |
| --- | --- | --- |
| 1 | Authorities | National Revenue Agency and National Social Security Institute |
| 2 | Employee identifiers | EGN or foreign-person identifier; NRA employer registration; insurance category |
| 3 | Payroll currency | EUR |
| 4 | Country reporting | NRA declarations 1 and 6 |
| 5 | Reporting timing | Standard employer declaration 1 is due by the 25th of the next month; additional-pay and correction rules differ. |
| 6 | Reporting distinction | Preserve employee-level insurance data and aggregate liabilities. Match the declaration version, currency and period before submission. |
| 7 | 2026 change | Euro adoption took effect on 1 January 2026 at EUR 1 = BGN 1.95583. Historical payroll and retro periods need controlled currency conversion. |
| 8 | 2027 onward | 2027 amounts and reporting specifications: refresh the cited authority publications before activating a new version. No unverified 2027 numerical rates are preloaded. |
| 9 | Tax caution | Classify taxable earnings and employee contributions before applying income tax; separately assess resident and non-resident treatment. |
| 10 | Social caution | NSSI publishes a 2026 ceiling split: EUR 2,111.64 January–July and EUR 2,300 August–December. Confirm the employee category; the self-employed minimum is not an employee wage floor. |
| 11 | Pension decision | Resolve pension cohort and supplementary-fund membership before deriving contributions; keep fund identifiers effective-dated. |
| 12 | Benefit decision | Separate taxable allowances from documented reimbursed business expenditure; validate any vouchers or social-expense treatment. |
| 13 | Absence-pay decision | Track employer sickness responsibilities and NSSI benefit claims as separate flows; do not treat all absence days as normal earnings. |
| 14 | Minimum-pay decision | Load the enacted employee minimum-wage decree in EUR and the occupational insurance minima; neither equals the self-employed minimum. |
| 15 | Year-end decision | Reconcile annual employment income and tax adjustments, including balances converted from lev; retain the fixed-rate conversion evidence. |
| 16 | Replicated Pay Components | Map EC compensation into the appropriate target pay records. A pay component can replicate successfully yet have the wrong tax, insurance or pension characteristics. |
| 17 | Payroll Control Record | Control the payroll-area run state and correction cycle. Run state protects calculation consistency; it must be coordinated with replication and historical changes. |
| 18 | Wage Type Catalogue | Design earning and deduction behaviour across all downstream outputs. Taxable, insurable, pensionable, cash and posting treatment are separate decisions. |
| 19 | Salary Payment Configuration | Configure the approved bank instruction and release process. A generated payment file is only an instruction; acceptance and settlement need separate evidence. |
| 20 | Payslip Configuration | Make gross-to-net and employer information understandable and reconcilable. The employee, authority and Finance may view different bases; a payslip should expose the distinction clearly. |
| 21 | Statutory Reporting | Convert approved results into accepted country declarations. A transmitted file can still be rejected, incomplete or mismatched to the payment liability. |
| 22 | Schema & Calculation Sequence | Trace the delivered local payroll process before changing it. Guessed schema names or copied technical wage types can make a plausible design impossible to implement. |
| 23 | Retroactive Processing | Recalculate history without losing the original result or reporting lineage. Historical earning rules and current payment-date obligations may both matter in a single correction. |
| 24 | Finance Posting | Map payroll expenses and liabilities into reconciled Finance documents. Technical wage types and GL accounts must be verified in the tenant; business labels alone do not establish posting correctness. |
| 25 | End-to-End Integration Map | Trace an employee change through all systems and reconciliations. Interface-level success does not guarantee a correct employee, statutory or accounting outcome. |

## Learning tool 3 — Payroll crossword

Complete the original intersecting crossword in the HTML edition or use the Crossword sheet. The grid and clue list follow in the converted editions.

| ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | 1 | ■ | ■ | ■ | ■ | ■ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ■ | ■ | ■ | ■ | ■ | 2 | □ | □ | □ | □ | □ | □ | ■ | ■ |
| ■ | ■ | ■ | ■ | ■ | ■ | ■ | ■ | □ | ■ | ■ | ■ | ■ | ■ |
| ■ | ■ | ■ | ■ | ■ | 3 | 4 | □ | □ | □ | □ | 5 | ■ | ■ |
| ■ | ■ | ■ | ■ | 6 | ■ | □ | ■ | □ | ■ | ■ | □ | ■ | ■ |
| 7 | □ | □ | □ | □ | □ | □ | □ | ■ | 8 | □ | □ | □ | □ |
| ■ | ■ | ■ | ■ | □ | ■ | □ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |
| ■ | ■ | ■ | ■ | ■ | ■ | □ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |
| ■ | ■ | ■ | ■ | ■ | ■ | □ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |
| ■ | ■ | ■ | ■ | ■ | ■ | □ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |
| ■ | ■ | ■ | ■ | ■ | ■ | □ | ■ | ■ | ■ | ■ | ■ | ■ | ■ |

| No. | Direction | Clue |
| --- | --- | --- |
| 1 | down | Earnings before employee deductions. (5) |
| 2 | across | The complete employee pay calculation process. (7) |
| 3 | across | Coverage and contributions studied in section 25. (7) |
| 4 | down | What supports an implementation decision or a passed test. (8) |
| 5 | down | Cash amount after employee deductions. (3) |
| 6 | down | Country withholding category studied in section 22. (3) |
| 7 | across | Country of this workbook (ignore spaces). (8) |
| 8 | across | Short name for historical payroll recalculation. (5) |

### Crossword answer key

| No. | Answer |
| --- | --- |
| 1 | GROSS |
| 2 | PAYROLL |
| 3 | PENSION |
| 4 | EVIDENCE |
| 5 | NET |
| 6 | TAX |
| 7 | BULGARIA |
| 8 | RETRO |

## Learning tool 4 — Snakes & Ladders

Two learners start at 1. Roll a die and answer one country quiz question. Both correct and wrong answers permit the roll. A correct answer permits a ladder and avoids a snake. A wrong answer activates a snake when present and does not permit a ladder. Reach 100 or beyond to finish. Ladders: 3 to 22, 12 to 34, 28 to 49, 46 to 66, 60 to 82. Snakes: 31 to 9, 55 to 35, 73 to 52, 89 to 68, 97 to 77. Use physical tokens and a die in facilitated editions.

| 100 | 99 | 98 | 97 | 96 | 95 | 94 | 93 | 92 | 91 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 |
| 80 | 79 | 78 | 77 | 76 | 75 | 74 | 73 | 72 | 71 |
| 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 |
| 60 | 59 | 58 | 57 | 56 | 55 | 54 | 53 | 52 | 51 |
| 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
| 40 | 39 | 38 | 37 | 36 | 35 | 34 | 33 | 32 | 31 |
| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
| 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 | 12 | 11 |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

| Round | Learner | Start | Die | Question / answer | Move / explanation |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Learning tool 5 — AVG reflection

| Reflection | Your entry |
| --- | --- |
| Affirmation | What capability am I strengthening through this country case? |
| Visualisation | What would a reconciled, evidence-backed payroll operation look like? |
| Gratitude | What person, insight or experiment helped me learn? |
| Intention | What is my next specific experiment and when will I review it? |

## Learning tool 6 — Notes journal

| Date | Section / topic | Assumption, decision or question | Evidence / next experiment |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Gross-to-net practice

| Practice field | Value / calculation |
| --- | --- |
| Gross cash earnings | Enter independently verified example |
| Employee social deduction | Enter |
| Taxable non-cash benefit | Enter |
| Other permitted taxable-base deduction | Enter |
| Employee withholding | Enter |
| Post-tax deduction | Enter |
| Additional employer contribution | Enter |
| Illustrative taxable base | Gross + benefit − social − other permitted base deduction |
| Cash net | Gross − employee social − withholding − post-tax deduction |
| Employer cash cost bridge | Gross + additional employer contribution |

Country law may permit only part of a contribution to reduce taxable pay. Employer cost here excludes non-cash benefit cost and other expenses. The Excel / Google Sheets edition contains editable inputs and formulas.

## Source register

- [Personal Income Taxes :: Ministry of Finance](https://www.minfin.bg/en/827)
- [Official authority guidance](https://nra.bg/wps/wcm/connect/nra.bg25863/agency/site/uslugi/deklarirane-na-osiguritelni-vnoski-ob1-ob6)
- [НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица - НОИ](https://www.nssi.bg/dohod01082026/)
- [Bulgaria and the euro](https://economy-finance.ec.europa.eu/euro/eu-countries-and-euro/bulgaria-and-euro_en?prefLang=ga)
- [New Local Version for Bulgaria | SAP Help Portal](https://help.sap.com/docs/successfactors-release-information/8e0d540f96474717bbf18df51e54e522/401b460f4dc546dba07a7fcaded81216.html?locale=en-US)
- [Supported Countries/Regions | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-s4hana/supported-countries-regions)
- [Payroll Control Record | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/payroll-control-record)
- [Setting Up the Point-to-Point Integration | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-employee-central-payroll-based-on-sap-human-capital-management-for-sap-erp-hcm/setting-up-point-to-point-integration)
- [Set Up Connection Between an Employee Central Payroll System and Employee Central | SAP Help Portal](https://help.sap.com/docs/successfactors-employee-central-payroll/implementing-point-to-point-time-data-replication/set-up-connection-between-employee-central-payroll-system-and-employee-central)

## Format and maintenance notes

These are independent editions of the same reviewed learning baseline. Updating one edition does not automatically update the others. Revisit the governing source and effective date before changing statutory content. Browser-local notes require an exported HTML backup to move between browser contexts.
