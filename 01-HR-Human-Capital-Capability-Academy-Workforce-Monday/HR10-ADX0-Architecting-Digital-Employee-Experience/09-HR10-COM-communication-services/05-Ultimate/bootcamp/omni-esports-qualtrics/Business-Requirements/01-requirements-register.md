# Requirements Register

25 requirements derived from the client's workbook (7 surveys, 157 questions, plus the notes on the overview and inventory tabs). Each row links to its **what / why / how** in [`02-what-why-how.md`](02-what-why-how.md).

**Verdict:** ✅ Standard · 🟡 Standard + config · 🟠 Workaround · 🔴 Not possible as stated (none)
**Effort (relative, my estimate):** S small · M medium · L large

---

## Register

| ID | Survey | Requirement | Verdict | Effort | Depends on |
|---|---|---|---|---|---|
| [BR-01](02-what-why-how.md#br-01) | S01 | Annual company-wide engagement survey: 54 rated items on a 5-point agreement scale | ✅ | S | none |
| [BR-02](02-what-why-how.md#br-02) | S01 | Results by reporting factor and by team, followed by action planning | 🟡 | M | BR-07 |
| [BR-03](02-what-why-how.md#br-03) | S01 | Confidentiality model "to be agreed" | 🟡 | S | Client decision, data protection officer |
| [BR-04](02-what-why-how.md#br-04) | S01 | Optional comment on every rated item | 🟠 | M to L | Client decision |
| [BR-05](02-what-why-how.md#br-05) | S01 | Three open-text questions and comment analysis | ✅ | S | Licence for AI summaries (optional) |
| [BR-06](02-what-why-how.md#br-06) | S01 | 13 demographic questions, 11 voluntary with "Prefer not to say" | 🟡 | M | Data protection officer |
| [BR-07](02-what-why-how.md#br-07) | S01 to S04 | Employee attributes and org hierarchy from SuccessFactors into Qualtrics | 🟡 | M | SuccessFactors admin, SFTP |
| [BR-08](02-what-why-how.md#br-08) | S02 | New hire check-in sent automatically 30 days after SuccessFactors hire date | 🟡 | M | BR-07 |
| [BR-09](02-what-why-how.md#br-09) | S03 | Exit survey triggered when a termination is entered in SuccessFactors | 🟡 | M | BR-07, SuccessFactors Intelligent Services |
| [BR-10](02-what-why-how.md#br-10) | S03 | Leaver details pre-filled from SuccessFactors, not asked | 🟡 | M | A "regretted leaver" field in SuccessFactors |
| [BR-11](02-what-why-how.md#br-11) | S03 | Select up to 3 reasons, then pick the main one from those chosen | ✅ | S | none |
| [BR-12](02-what-why-how.md#br-12) | S03 | Conditional follow-up question and optional open text | ✅ | S | none |
| [BR-13](02-what-why-how.md#br-13) | S03 | Optional follow-up conversation request routed to the People team, regretted leavers first | 🟡 | S | BR-10 |
| [BR-14](02-what-why-how.md#br-14) | S03 | Exit trends by team, tenure, regretted versus non-regretted | 🟡 | M | BR-07, BR-10 |
| [BR-15](02-what-why-how.md#br-15) | S02, S03 | Exit and new-hire results comparable with engagement results | 🟡 | M | Client decision on wording |
| [BR-16](02-what-why-how.md#br-16) | S04 | Ad hoc survey to a group filtered from SuccessFactors data | 🟡 | S | A "remote" attribute in SuccessFactors |
| [BR-17](02-what-why-how.md#br-17) | S04 | Negatively worded item scored correctly | ✅ | S | none |
| [BR-18](02-what-why-how.md#br-18) | S02 | New hire survey in English, Bahasa Indonesia and Filipino (Tagalog) | ✅ | S (review M) | Translations beyond question text |
| [BR-19](02-what-why-how.md#br-19) | S02 | Each new hire receives the survey in their own language | 🟡 | S to M | BR-18, to be tested |
| [BR-20](02-what-why-how.md#br-20) | S05 to S07 | Recruitment survey content: single, multi-select, yes/no, open text | ✅ | S | none |
| [BR-21](02-what-why-how.md#br-21) | S05 to S07 | Automatic triggers from SmartRecruiters (end of process, offer accepted, role filled) | 🟠 | L | Platform decision |
| [BR-22](02-what-why-how.md#br-22) | S05, S06 | Surveys to external candidates of every outcome | 🟡 | M | BR-21, data protection officer |
| [BR-23](02-what-why-how.md#br-23) | S07 | Hiring manager identified and surveyed when a role is filled | 🟠 | M | BR-21 |
| [BR-24](02-what-why-how.md#br-24) | S01 to S04 | A results dashboard for every Qualtrics survey, with segments | ✅ | M | none |
| [BR-25](02-what-why-how.md#br-25) | All | Data protection, sensitive data and data residency across the workforce | 🟡 | M | Data protection officer, legal |

---

## Count check

| Verdict | Requirements | Count |
|---|---|---|
| ✅ Standard | BR-01, 05, 11, 12, 17, 18, 20, 24 | 8 |
| 🟡 Standard + config | BR-02, 03, 06, 07, 08, 09, 10, 11, 13, 14, 15, 16, 19, 22, 25 | 15 |
| 🟠 Workaround | BR-04, 21, 23 | 3 |
| 🔴 Not possible as stated | none | 0 |
| **Total** | | **25** |

## Sequencing suggestion (our judgement)

1. **Decide first:** BR-03 (confidentiality), BR-04 (per-item comments), BR-21 (recruitment platform), BR-06 and BR-25 (privacy).
2. **Foundation:** BR-07 (SuccessFactors data and hierarchy). Almost everything else waits on it.
3. **Build in parallel after BR-07:** S02 new hire (BR-08, 18, 19), S03 exit (BR-09 to 15), S01 engagement (BR-01, 02, 05, 06).
4. **Then:** S04 ad hoc (BR-16, 17), dashboards (BR-24).
5. **Last, platform permitting:** recruitment (BR-20 to 23).
