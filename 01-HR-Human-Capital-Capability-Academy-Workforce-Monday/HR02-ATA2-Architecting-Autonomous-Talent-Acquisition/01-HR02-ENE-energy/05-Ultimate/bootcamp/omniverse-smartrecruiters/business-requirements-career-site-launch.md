# Business Requirements — OmniVerse Energy Career Site Launch

**Program:** HR02 — Architecting Autonomous Talent Acquisition  
**Sector:** Energy | Ultimate Bootcamp  
**Platform:** SmartRecruiters for SAP SuccessFactors  
**Status:** Proposed requirements. Acceptance testing and sign-off pending.

## Business objective

Give external candidates a clear path to discover energy-sector vacancies, assess their fit, apply on mobile or desktop, and receive confirmation. Give Recruiting a reliable process to publish and close vacancies and measure completed applications.

## Scope and implementation

Scope covers the public career page, job search, vacancy detail, the SmartRecruiters application handoff, confirmation, analytics, and launch ownership. Use the native Career Page Builder header, hero, additional sections, and job list where available. Verify tenant support for prefiltered career-stage links, custom domains, and analytics before committing to those implementation choices. [SAP career site options](https://learning.sap.com/courses/smartrecruiters-for-sap-successfactors-project-team-orientation/exploring-career-site-options-in-smartrecruiters_baeebfa0-4b47-460b-9f70-dd3a491a2fec)

## Requirements and acceptance criteria

Award one point per requirement after the pass criteria have been verified in the launch environment. Record the tester, date, test URL, evidence, and result for each requirement. The 10/10 target measures launch readiness. Post-launch conversion uses funnel data.

| ID | Business requirement | Acceptance criteria |
|---|---|---|
| HR02-ENE-CS-01 | **Brand and first screen.** Use the rectangular and square OmniVerse logos in their intended placements, the energy-sector hero image, a live headline, and a prominent **Search jobs** action. | On mobile and desktop, candidates can identify OmniVerse, understand the type of work, and reach job search from the first screen. Both logos preview cleanly in their intended placements. |
| HR02-ENE-CS-02 | **Job discovery.** Provide keyword search and location and job-family discovery. Give experienced professionals, graduates and interns, and technicians and field teams relevant entry points where supported by inventory. Handle empty results. | Candidates can find a vacancy by job title or location. Career-stage links show relevant roles or a useful next step. Use prefiltered destinations where the setup supports them. |
| HR02-ENE-CS-03 | **Location and vacancy data.** Use consistent public city, region, country, and worksite values. Verify the stored address and public display for predefined locations. Exclude test, duplicate, placeholder, and expired vacancies. | The same correct location appears in results, job details, and the application handoff. Sample an office role and a field role when both are in scope. |
| HR02-ENE-CS-04 | **Energy-sector vacancy details.** Present title, employer, location, employment type, and **Apply** near the top. Separate essential and preferred qualifications. Publish relevant shift, rotation, travel, on-site, and certification requirements. | A candidate can determine the worksite, responsibilities, and minimum qualifications before opening the application form. |
| HR02-ENE-CS-05 | **SmartRecruiters application.** Validate the published vacancy's apply link, résumé upload, manual entry, screening questions, validation errors, retry, and confirmation. | A test candidate submits on phone and desktop. Recruiting verifies the corresponding application under the correct SmartRecruiters job. A confirmation-page view alone is insufficient evidence. |
| HR02-ENE-CS-06 | **Candidate trust and support.** Publish hiring steps, an applicant privacy notice, a recruitment-fraud notice, and an accommodations or support contact. Explain and route any enabled **Get in Touch** or general application flow. | Candidates can find support and know what happens after applying. The mailbox is monitored and a general application reaches its designated owner when enabled. |
| HR02-ENE-CS-07 | **Job SEO.** Verify a canonical crawlable URL per vacancy and validate single-job `JobPosting` markup against visible content. Verify closure behavior. | A representative live vacancy passes Google's Rich Results Test. A closed test vacancy follows Google's expiration guidance on the actual hosted setup. |
| HR02-ENE-CS-08 | **Accessibility and mobile performance.** Check keyboard navigation, screen reader use, zoom, contrast, focus, image descriptions, and form errors against WCAG 2.2 AA. Test mobile performance on the homepage and an individual job. | Candidates complete the tested journey with assistive technology. Resolve issues that block discovery or submission. Record prelaunch performance and review field Core Web Vitals when available. |
| HR02-ENE-CS-09 | **Conversion measurement.** Measure visits, vacancy views, apply starts, and confirmed submissions where supported. Verify the ATS handoff and keep personal data out of analytics. | A test submission reconciles to one ATS application. Refreshing confirmation creates no duplicate conversion. Use ATS submission counts and document any measurement gap when browser events are unavailable. |
| HR02-ENE-CS-10 | **Go-live ownership.** Assign owners for careers content, job data, candidate support, and reporting. Rehearse publishing, updating, and closing a vacancy. | Recruiting and the site owner can publish and close a vacancy, verify the public outcome, and handle a candidate issue. All ten requirements have documented evidence and named sign-off. |

## Release rehearsal

1. Give one participant the public careers URL and ask them to find a field operations role by worksite.
2. Give a second participant the same URL and ask them to find an early-career role on mobile.
3. Have both participants assess the job requirements and submit controlled test applications without coaching. Verify both submissions in SmartRecruiters.
4. After launch, review job-view, apply-start, and completed-application rates by device, career stage, and job family where the data supports it.

## References

- [SAP SmartRecruiters — Building Career Pages](https://learning.sap.com/courses/smartrecruiters-for-sap-successfactors-academy/building-career-pages_f0d1706c-6524-49de-84c6-ed9f3d2fc7a9)
- [SAP SmartRecruiters — Navigating the Candidate Experience](https://learning.sap.com/courses/smartrecruiters-for-sap-successfactors-project-team-orientation/navigating-the-candidate-experience_a041dba6-dbd1-4c11-b823-6524d5206db2)
- [Google Search Central — Job posting structured data](https://developers.google.com/search/docs/appearance/structured-data/job-posting)
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [web.dev — Core Web Vitals thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds)
