# SAP SuccessFactors Learning – Connector Configuration Guide (Beginner Edition)

| Field | Value |
|---|---|
| Product | SAP SuccessFactors Learning (LMS) |
| Module | Connectors (Talent Management System data import) |
| Country / Region | Global (timezone default America/New_York, USD, English) |
| Industry | Industry-agnostic |
| Version | 1.0 |
| Last updated | 2026-11-23 |
| Owner | To be completed |
| Review date | To be completed |

---

## 1. Solution overview

### What is a "connector"?
Think of a connector as a **conveyor belt for data**. Your HR system (or any source) drops a text file on a server. The LMS picks the file up, reads it line by line, and creates or updates records in Learning (users, courses, enrollments, and so on). Afterwards it sends you a **report** saying what worked and what failed.

### What is this file?
It is the connector **properties file** (key=value lines). It tells the LMS:
1. **Where** to find input files and where to put reports (Common settings).
2. **What the columns in each file mean** (Field mappings).
3. **What to fill in when a column is blank** (Default values).
4. **How to translate values** (Transforms, e.g. `active` becomes `N` for NOTACTIVE).

### How to read any line
```
user.connector.defaultValue.domainID=PUBLIC
 ^       ^           ^          ^        ^
 |       |           |          |        value
 |       |           |          setting name
 |       |           "default value" type
 |       "connector" setting
 which connector (user)
```

| Prefix pattern | Plain meaning |
|---|---|
| `xxx.connector.defaultValue.*` | Value used when the input file leaves it blank |
| `xxx.field.mapping.data.TARGET=SOURCE` | LMS field (left) = column name in your file (right) |
| `xxx.field.transform.data.FIELD.NEWVALUE=a,b,c` | If the file says a, b or c, store NEWVALUE |
| `xxx.connector.inactiveRule.*` | What to do when a record is made inactive |
| `xxx.connector.update.*` | Whether existing records get overwritten |

### Connectors in this file
Organization, User, Federal User, Item (plus Content Module, Item Module, Localization, Competency), Schedule Offering, Position, Domain, Learning History, Enrollment, Job Code, SF User, Person Sync, Competency, Curriculum, Organization Owner, Alternate Job Position, Admin, Skillsoft, Account Code.

### Out of scope
Real passwords and keys (blank or masked here), file-naming conventions per connector, and the scheduling of connector runs (done in System Admin).

---

## 2. Technical environment

| Environment | URL / Instance | Version | Last Patched | Owner |
|---|---|---|---|---|
| Development | To be completed | | | |
| Test | To be completed | | | |
| Production | To be completed | | | |

SFTP server in the file: `fileupload.plateau.com` (port 22, protocol `sftp`).

---

## 3. Configuration reference – by area

### 3.1 Common settings (apply to ALL connectors)

#### Input file format
| Setting | Value | Beginner explanation |
|---|---|---|
| `connector.input.file.escapeChar` | `"` | Character that protects special characters. A value like `"Smith, John"` stays one value. |
| `connector.input.file.columnDelimiter` | `\|` | Columns are separated by a pipe. So `John\|Smith\|HR`, not commas. |
| `connector.input.file.eolSymbols` | `!##!` | Marks the end of a row (instead of a line break). Every row in your file must end with `!##!`. |

> Common beginner mistake: the file is saved with commas or normal line breaks. The connector then reads the whole file as one giant column.

#### Where input files come from
| Setting | Value | Explanation |
|---|---|---|
| `connector.input.file.location` | `FTP` | Choices: `FTP`, `local`, `MDI`. Here files are picked up from an SFTP server. |
| `connector.input.file.fetch.retry.enable` | `false` | If a file is not there, do not retry automatically. |
| `connector.ftp.input.remoteDirectory` | `/home/connector/InputFiles` | Folder on the server where you drop files. |
| `connector.local.input.localDirectory` | `c:\\connectors\\input` | Only used if location = `local`. Ignored today. |
| `connector.input.archive.directory` | blank | Deprecated. Archiving is now in System Admin > Configuration > Connector Settings. |
| `connector.input.file.name.tenant.suffix.enable` | `true` | SaaS only. File names carry your tenant ID, e.g. `user_data_ACME.txt`. |
| `connector.input.file.name.tenant.suffix.override` | blank | Use only if the suffix must differ from the tenant ID. |
| `connector.input.file.curriculum.htmlDescription.enabled` | `false` | Only for HTML descriptions. Copies curriculum description into the HTML description. |

#### Output reports
| Setting | Value | Explanation |
|---|---|---|
| `connector.ftp.output.report.enable` | `true` | Put the run report on the SFTP server. |
| `connector.ftp.output.report.remoteDirectory` | `/home/connector/Output` | Where reports land. |
| `connector.report.email.enable` | `true` | Also email the report. |
| `connector.report.email.toAddresses` | `John.Smith@company.com` | Recipients. Looks like a placeholder; replace with a real shared mailbox. |
| `connector.report.email.CCAddresses` | blank | Optional CC. |
| `connector.report.email.mailSubject` | `$interfaceId$ - Connector Results` | `$interfaceId$` is replaced by the connector name. |
| `connector.report.email.enableDetailReportAttachments` | `false` | Detailed report is not attached to the email. |
| `connector.report.detail.displayMessageTypes` | `Exception,Warning,FATAL` | Which messages appear. `info` is left out to keep reports short. |
| `connector.report.detail.numberOfExceptionsDisplayed` | `5000` | Maximum errors shown per report. |

#### SFTP connection
| Setting | Value | Explanation |
|---|---|---|
| `connector.ftp.protocol` | `sftp` | Secure file transfer (not plain `ftp`). |
| `connector.ftp.server` | `fileupload.plateau.com` | Server address. |
| `connector.ftp.port` | `22` | Standard SFTP port. |
| `connector.ftp.userID` / `password` | blank | Must be filled in before the connector can log in. Do not store real credentials in documents. |

#### PGP encryption (optional)
| Setting | Value | Explanation |
|---|---|---|
| `connector.pgp.enabled` | `false` | Files are not encrypted. If `true`, you send files encrypted with the **public key** and the LMS decrypts them with the **secret key**. |
| `connector.pgp.public.keyring` | long base64 text | The public key to give to whoever creates the encrypted files. Safe to share. |
| `connector.pgp.secret.keyring` / `passphrase` | `*****` | Masked. Keep private. |
| `connector.pgp.file.extension` | `.pgp` | Encrypted files end in `.pgp`. |

---

### 3.2 Organisational structures

#### Organization connector (departments / org units)
Defaults: `domainID=PUBLIC`, `finAcctDomainID=PUBLIC`, `orgTypeID` blank.
**Domain** = a security and data partition in the LMS. `PUBLIC` is the standard shared one.
Mappings are one-to-one (ORG_ID=ORG_ID). Notable fields: ORG_ID_PARENT (builds the hierarchy), billing/shipping address blocks, COL_NUM1..5 (custom columns).

#### Domain connector
Only mappings: DMN_ID, DMN_DESC, DMN_ID_PARENT (parent domain).

#### Position connector
Defaults: `domainID=PUBLIC`, `fteFactor=1.0` (a full-time position), `jobSharingEnabled=N`. Fields cover position number, job code, reports-to, salary range, max headcount and FTE.

#### Job Code connector (`jobposition`)
Maps JP_ID, JP_DESC, auto-assign/remove of qualifications and profiles, job location, grade and salary range.

#### Account Code connector
Defaults: `domainID=PUBLIC`, `acctTypeID=Cost Center`. Used to load cost centers. `REMOVE_ACCT` removes one.

#### Alternate Job Position connector
`removeAlternateJobPositionSameAsJobPosition=N`: if the "alternate" job equals the main job, keep it anyway.

---

### 3.3 User configuration

#### User connector (use when users come from a non-SuccessFactors source)
| Setting | Value | Explanation |
|---|---|---|
| `deletedUser.reincarnate` | `N` | If a deleted user returns, do not revive the old record. |
| `defaultValue.domainID` / `orgDomainID` / `finAcctDomainID` | `PUBLIC` | Default domain. |
| `defaultValue.studentRoleID` | `DEFAULT USER` | Learner role given to new users. |
| `defaultValue.licenseUserType` | `ACTIVE` | `ACTIVE` = full license, `FUNCTIONAL` = limited. |
| `defaultValue.lms-origin` | blank | **Important.** `Y` = user logs in via the LMS page (Learning-only). `N` = user logs in through the SuccessFactors platform. Once set it cannot be changed through the connector; use "Correct User Source System" in Import Data tool. If blank, the system default applies. |
| `jpAutoAssignQuals` / `jpAutoRemoveQuals` | `Y` | Changing a user's job code automatically adds/removes curricula linked to that job. |
| `jpAutoAssignPPRF` / `jpAutoRemovePPRF` | `Y` | Same idea for competency profiles. |
| `preferenceTimeZone` / `Locale` / `Currency` | `America/New_York`, `English`, `USD` | Defaults for new users. |
| `update.updatePreferences` | `N` | Does **not** overwrite preferences of existing users. |
| `supervisorReRoute…` (6 settings) | `N` | Approvals are NOT redirected to the supervisor's boss when the supervisor is absent. |
| `accessToOrgFinAcct` | `N` | New users cannot use org finance accounts. |
| `fullTime` | `Y` | New users are full-time unless stated. |
| `includeInGovtReporting` | `N` | Not part of government reporting by default. |
| `deafultValue.nativeDeepLinkUser` | `N` | Note the spelling `deafult`; it is a known quirk of the template. Keep it as-is unless SAP confirms otherwise. |
| `inactiveRule.cleanDevPlan` | `Y` | When a user is inactivated, clean their development plan. |

**Field mapping.** Left side = LMS field, right side = your file's column name. Examples:
- `STUD_ID` = the unique user ID
- `SUPER` = supervisor's ID
- `NOTACTIVE` = `Y` means the user is inactive
- `COL_NUM1_VAL...15` = custom columns
- `LMS_ORIGIN=USER_SOURCE_SYSTEM`, `LICENSE_USER_TYPE=` (blank, so the column is not read).

**Transforms.** `LICENSE_USER_TYPE.ACTIVE=Active,active` and `LMS_ORIGIN.Y=Y,Yes,LEARNING,...` translate friendly words to system codes.

**User Manager mapping.** `ALT_SUPER=MANAGER` and so on, for alternate supervisors (matrix managers).

#### Federal User connector (US federal customers only)
Copy of the User connector with `federaluser.` prefix plus EHRI fields (SSN, DOB, salary, RNO). **Leave unused unless you are a US federal customer.** Contains sensitive data fields, so restrict file access.

#### SF User connector (the key one for integrated SuccessFactors customers)
Use when users come from **Employee Central / SF core**. Left side = LMS field, right side = **SF export column**.

| LMS field | SF column | Meaning |
|---|---|---|
| NOTACTIVE | STATUS | Active/inactive |
| STUD_ID | USERID | Login ID |
| FNAME / LNAME | FIRSTNAME / LASTNAME | Names |
| JP_ID | JOBCODE | Job code |
| JOB_TITLE | TITLE | Title |
| JL_ID | LOCATION | Job location |
| ORG_ID | DEPARTMENT | Org unit (could be DIVISION instead) |
| REGION_ID | DIVISION | Region |
| EMP_TYP_ID / EMP_STAT_ID | EMPLOYEE-CLASS / EMPLSTATUS | Employee type and status |
| HIRE_DTE / TERM_DTE | HIREDATE / EXIT_DATE | Hire and termination dates |
| SUPER | MANAGER | Supervisor |
| COL_NUM1..15_VAL | CUSTOM01..15 | Custom fields |
| LOCALE | DEFAULT_LOCALE | Language |
| LMS_ORIGIN | USER_SOURCE_SYSTEM | See lms-origin above |
| GENERAL_DISPLAY_NAME | DISPLAYNAME | Display name |
| REGULAR_TEMP_ID / FULLTIME | REGULAR-TEMP / IS-FULLTIME-EMPLOYEE | Employment flags |
| PERSON_GUID / PERSON_ID_EXTERNAL | same | Link to the SF person |

Blank mappings (e.g. `ROLE_ID=`, `ACCT_ID=`) mean "not loaded from this feed".

Helper rules in this connector:
- `@ADDR1`, `@ADDR2` are temporary fields. `add.field.mappings=ADDR=@ADDR1+@ADDR2` joins both lines into the address.
- `copy.field.mappings=JP_DESC=JP_ID, JL_DESC=JL_ID, ORG_DESC=ORG_ID`: since SF gives no description, reuse the ID as the description.
- `additional.field.mappings=PHON_NUM1_DESC, PHON_NUM2_DESC` with defaults "Business Phone" / "Business Fax".
- `transform.data.NOTACTIVE.N=active,active_external,...` and `.Y=inactive,...`: translates status words into the Y/N flag.
- `TIMEZONE.America/New_York=EST` etc.: translates SF short codes to full timezone names.
- `SUPER.@NULLIFY@=NO_MANAGER`: if the file says `NO_MANAGER`, clear the supervisor.
- `SHOPPING_ACCT_TYPE` set from active/inactive: marks internal vs external users.
- `actionOnInvalid.NOTACTIVE=reject`: a row with an unknown status is rejected instead of guessed.
- `date.format.HIRE_DTE.MMM-dd-yyyy HH:mm:ss=MM/dd/yyyy`: converts the date format.
- `sfuser.field.transform.trim.data.enable=false`: names are not truncated.
- `defaultValue.studentRoleID=LEARNING_USER`: note this differs from the User connector (`DEFAULT USER`). Make sure that role really exists.
- `processingRule.requiredFiles` blank: no file is mandatory for a run.
- Extended user mapping brings extra fields (birth date, full-time flag, GUID).

#### Person Sync connector
For integrated customers who do not use the standard employee export. It syncs **PERSON_GUID** and **PERSON_ID_EXTERNAL** by matching SF user ID to LMS user ID. File must be named `PERSON_GUID.csv` (case-sensitive). Mappings are preset; do not change them.

#### Admin connector
Creates LMS administrators. Defaults: `domainID=PUBLIC`, `locked=N`, timezone/locale/currency defaults, `updatePreferences=N`. Fields add or remove up to three roles each (ADD_ROLE_ID1-3, REMOVE_ROLE_ID1-3).

#### Organization Owner connector
Defaults to `N` for including sub-orgs and for succession planning / talent search. Has four sub-files: dashboard, initiatives, training manager, succession.

---

### 3.4 Learning content and delivery

#### Item connector (courses / items)
| Setting | Value | Explanation |
|---|---|---|
| `defaultValue.domainID` | `PUBLIC` | Default domain |
| `item.autoCompetency` | `N` | Do not auto-assign competencies on completion |
| `AICCMaxNormal` | `99` | Default maximum "normal" score for AICC content |
| `scheduleCanOverrideCancelPolicy` | `Y` | A scheduled session may change the cancellation policy |
| `skipContentStructurePage` | `N` | Show the content structure page on launch |
| `cancellationPolicy` | blank | Use the global policy |
| `inactiveRule.updateNotActive` | `true` | Updating NOTACTIVE in the file really changes the item |
| `userRequestsEnabled`, `supervisor/selfRecordLearningEvent`, `approvalRequired` | blank | Blank means "follow System Admin > Configuration > User Settings". |
| `withdrawApprovalRequired` | `N` | No approval needed to withdraw |
| `priorRevisions.updateNotActive` | `N` | Old revisions are not touched. |
| `defaultRevDate.currentTimestamp` | `N` | **Revision date must be in the file**; it is not auto-filled. |
| `itemModule.forceOrder` | `N` | Modules can be taken in any order |
| `userCanWaitlist` | `Y` | Waiting lists allowed |
| `revision.inactivatePriorRevisions` | `Y` | New revision retires the old one |
| `revision.updateLearningPlans / ScheduleOfferings / Curricula` | `Y` | New revision flows into learning plans, schedules and curricula |
| `revision.productionReady` | `Y` | New revision is production ready |
| `revision.retainCurriculaSettingsOnItemRevision` | `N` | Curriculum requirements follow the revised item values (set `Y` to keep existing ones) |

Sub-connectors: Content Module (launch settings and AICC wrapper), Item Module (order, mastery score), Item Localization (translated titles/descriptions), Item Competency (links skills).
- `overwriteItemSkills=N`: add skills but keep existing ones. `Y` means the file becomes the only truth.
- `removeAllItemSkills=Remove_Skills`: the keyword used in CPTY_ID to wipe all skills of an item (works only when overwrite = `Y`).

#### Schedule Offering connector (classroom / virtual sessions)
Defaults: timezone `America/New_York`, publish in all catalogs `N`, all email notifications `N`, waitlist `Y`, super enrollment `N`, approval `N`, inherit 2483 (government training) fields from item `Y`, online access `inherit`.

#### Curriculum connector
| Setting | Value | Explanation |
|---|---|---|
| `forceIncomplete` | `Y` | Changing a curriculum forces learners to redo it |
| `autoAssign/RemoveCompetencyProfile`, `autoAssign/RemoveQuals` | `Y` | Automatic assignment follows rules |
| `propageToStudent` | `N` | (sic) Changes are not pushed to learners' records |
| `inactiveRule.*` (all `N`) | | Inactivating a curriculum does **not** unassign users or remove it from catalogs, parent curricula, prerequisites, job codes or assignment profiles |

Sub-files: curriculum items, parent curricula, requirements, localization.

#### Competency connector
Reads SF competencies from `sf_competency_data.zip`. Defaults: category `Base Category`, type `SF Competency`, prefix `LMS_` for renamed rating scales and competencies, `enableCategorySync=Y`, `useDefaultRatingScale.enable=false`, assessment history processing `false`.

#### Skillsoft connector
Brings in the Skillsoft course catalogue through the OLSA web service.
- `skillsoftconnectors.input.file.location=SkillsoftWebservice`
- `endpoint`, `customer_id`, `shared_secret` are blank: fill with the vendor-provided values.
- Defaults: item source `Skillsoft`, delivery method `WBT` (web-based training), catalog `PUBLIC`, chargeback method `2` (buyer-authorized account), revisions not allowed (`N`).
- Mobile: `mobilestatus=Phone` sets mobile access `Y`; `Tablet` sets `N`.
- Subject area connector is switched off (`process.subjectareaconnector=N`).

---

### 3.5 Transactions (learning records)

#### Learning History connector
Loads completed training. Key fields: STUD_ID, CPNT_TYP_ID, CPNT_ID, REV_DTE, CMPL_STAT_ID (status), COMPL_DTE, GRADE, hours (credit, CPE, contact). Defaults for training funding and completion timezone are blank. Includes e-signature and government-reporting (2483) fields.

#### Enrollment connector
Loads enrollments for scheduled offerings. `rule.scheduleConflicts=ignore`: an overlapping session is still enrolled (no warning). Options: `ignore`, `warn`, `error` (reject).

---

### 3.6 Security / role configuration
- Learner role: `DEFAULT USER` (User connector) and `LEARNING_USER` (SF User connector).
- Admin roles added/removed via ADD_ROLE_ID1-3 / REMOVE_ROLE_ID1-3.
- Domain-based access: all defaults use `PUBLIC`.
- SFTP and PGP credentials: see Section 3.1.

### 3.7 Integration configuration
- Source of user data: SFTP files, with Employee Central via the SF User connector.
- Master Data Integration (MDI) is a permitted input location.
- Skillsoft: OLSA web service.
- Identity: `lms-origin` setting (Learning vs SuccessFactors platform authentication).

### 3.8 Analytics / reporting configuration
Run report: email + SFTP, showing Exceptions, Warnings and FATAL, up to 5000 lines.

### 3.9 Country-specific settings
Defaults point to US: `America/New_York`, USD, English, with US timezone abbreviations (EST, CST, MST, PST, AST). Change them for other countries. Government-reporting (2483) and Federal fields are US-oriented.

### 3.10 Industry-specific settings
None configured.

---

## 4. Known issues and workarounds / things to double-check

| Issue | Impact | Workaround | Permanent Fix ETA | Owner |
|---|---|---|---|---|
| Report recipient looks like a placeholder (`John.Smith@company.com`) | Results go to the wrong person | Replace with a shared mailbox | TBC | TBC |
| SFTP user ID and password are blank | Connector cannot log in | Set via secure process | TBC | TBC |
| `lms-origin` default is blank | New users get the system default, which may be wrong | Decide Y or N before the first load | TBC | TBC |
| Spelling quirks: `deafultValue` (User, Federal, SF User), `HOURLY_RATE_CURRENY` | Setting may be silently ignored | Confirm in SAP documentation before "fixing" | TBC | TBC |
| `USER connector LICENSE_USER_TYPE=` is blank | License type column in file is not read; default `ACTIVE` always applies | Map to a column if functional users are needed | TBC | TBC |
| Learner role differs (`DEFAULT USER` vs `LEARNING_USER`) | Inconsistent roles | Align with the role list in System Admin | TBC | TBC |
| `requiredFiles` blank | A run can pass with a missing user file | Set e.g. `user_data` | TBC | TBC |
| Federal user connector includes SSN fields | Sensitive data exposure | Do not enable unless required | TBC | TBC |

---

## 5. Beginner tips
1. **Only change what you need.** Most lines are factory defaults.
2. **Always test in a non-production tenant first.**
3. **The right side of a mapping must match your file's column header exactly** (case-sensitive).
4. **Blank value does not mean "off"**; it often means "use the global System Admin setting".
5. **Read the run report** after every load; zero errors is the goal.
6. **Keep a copy of the file before each change** and record it in the change history below.

---

## 6. Change history

| Version | Date | Change Description | Changed By | Approved By |
|---|---|---|---|---|
| 1.0 | 2026-11-23 | Initial beginner-friendly guide created from properties file | SuccessLabs Academy | TBC |

## 7. Contacts and support

| Role | Name | Email | Scope |
|---|---|---|---|
| Connector report recipient | John Smith (as per file) | John.Smith@company.com | Run reports |
| LMS administrator | TBC | TBC | Configuration |
| SAP support | TBC | TBC | Product issues |

---
v1.0 | document-solution-config-guide | SuccessLabs Academy
