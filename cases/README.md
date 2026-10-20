# Test case catalog

20 cases per site, one branch per case in each site repo (branched from `baseline-v1`). Full details, old/new values and the
expected flow result are in `cases/<site>/case-NN.json`. To use a case: run **Deploy case** in the site repo with `case_branch = <branch>`;
run it again with `main` to return to the baseline. Verify any branch with `py tools/verify_case.py <site repo path> <branch>` (add `--allow-docs` for 15-16, `--allow-delete` for 1).

## Easy - Baptist Community Ministries (`test-site-easy-bcm`)

| # | Test case | Branch | Field |
|---|---|---|---|
| 1 | Opportunity Grants - Page Removed (404) | `case-01-page-removed` | 1.1 Opportunity page removed (404) |
| 2 | Strategic Grants - Soft 404 Page | `case-02-soft-404` | 1.2 Opportunity page replaced by a 'not found' page (200) |
| 3 | Discretionary Donations - Eligibility Criteria changed | `case-03-eligibility-changed` | 2.1 Eligibility criteria |
| 4 | Transom Grants - How to Apply changed | `case-04-how-to-apply-changed` | 2.2 How to apply |
| 5 | Strategic Grants - Focus Areas changed | `case-05-focus-areas-changed` | 2.3 Focus/impact areas |
| 6 | Strategic Grants - Population Served changed | `case-06-population-changed` | 2.4 Population served |
| 7 | Transom Grants - Funding Amount increased | `case-07-funding-increased` | 2.5 Funding amount (increase) |
| 8 | Discretionary Donations - Funding Amount decreased | `case-08-funding-decreased` | 2.5 Funding amount (decrease) |
| 9 | Open Invitation Grants - Opening Date changed | `case-09-opening-date-changed` | 2.6.1 Opening date |
| 10 | Transom Grants - Registration Date changed | `case-10-registration-date-changed` | 2.6.2 Registration date |
| 11 | Transom Grants - LOI Date changed | `case-11-loi-date-changed` | 2.6.3 LOI submission date |
| 12 | Transom Grants - Application Date changed | `case-12-application-date-changed` | 6.4 Key deadline dates - Application submission date |
| 13 | Strategic Grants - Board Meeting Date changed | `case-13-board-meeting-date-changed` | 2.6.5 Board meeting date |
| 14 | Transom Grants - Award Notification Date changed | `case-14-award-notification-changed` | 2.6.6 Award notification date |
| 15 | Transom Grants - RFP Document replaced | `case-15-rfp-replaced` | 2.7.1 RFP |
| 16 | Transom Grants - Template Document replaced | `case-16-template-replaced` | 2.7.2 Template |
| 17 | Discretionary Donations - Contact Information changed | `case-17-contact-changed` | 2.8 Contact information |
| 18 | Transom Grants - Closed Before Deadline | `case-18-closed-before-deadline` | 3.1 Not accepting applications before the deadline |
| 19 | Core Funding Grants - Funder No Longer Available | `case-19-funder-unavailable` | 3.2 Funder not available anymore |
| 20 | Discretionary Donations - Rolling Grant Closed | `case-20-rolling-closed` | 3.3 Rolling opportunity closed |

## Medium - Community Foundation for Muskegon County (`medium-muskegon`)

| # | Test case | Branch | Field |
|---|---|---|---|
| 1 | Faith Partner Grants - Page Removed (404) | `case-01-page-removed` | Page removed (404) |
| 2 | Community Empowerment Grants - Soft 404 Page | `case-02-soft-404` | Soft 404 (page returns 200 but content gone) |
| 3 | Watch Us Vote Grants - Eligibility Criteria changed | `case-03-eligibility-changed` | 2.1 Eligibility criteria |
| 4 | Muskegon LEAD Grants - How to Apply changed | `case-04-how-to-apply-changed` | 2.2 How to apply |
| 5 | Building an Inclusive Community Mini-Grants - Focus Areas changed | `case-05-focus-areas-changed` | 2.3 Focus/impact areas |
| 6 | Muskegon LEAD Grants - Population Served changed | `case-06-population-changed` | 2.4 Population served |
| 7 | Watch Us Vote Grants - Funding Amount increased | `case-07-funding-increased` | 2.5 Funding amount |
| 8 | Muskegon LEAD Grants - Funding Amount decreased | `case-08-funding-decreased` | 2.5 Funding amount |
| 9 | Muskegon LEAD Grants - Opening Date changed | `case-09-opening-date-changed` | 2.6.1 Opening date |
| 10 | Watch Us Vote Grants - Registration Date changed | `case-10-registration-date-changed` | 2.6.2 Registration date |
| 11 | Community Empowerment Grants - LOI Date changed | `case-11-loi-date-changed` | 2.6.3 LOI submission date |
| 12 | Watch Us Vote Grants - Application Date changed | `case-12-application-date-changed` | 2.6.4 Application submission date |
| 13 | Committee Grants - Board Meeting Date changed | `case-13-board-meeting-date-changed` | 2.6.5 Board meeting date |
| 14 | Muskegon LEAD Grants - Award Notification Date changed | `case-14-award-notification-changed` | 2.6.6 Award notification date |
| 15 | Online eGrant Instructions 2016 - RFP Document replaced | `case-15-rfp-replaced` | 2.7.1 RFP |
| 16 | Grant Application Budget - Template Document replaced | `case-16-template-replaced` | 2.7.2 Template |
| 17 | Watch Us Vote Grants - Contact Information changed | `case-17-contact-changed` | 2.8 Contact information |
| 18 | Watch Us Vote Grants - Closed Before Deadline | `case-18-closed-before-deadline` | 3. Closed before deadline (funds depleted) |
| 19 | Committee Grants - Funder No Longer Available | `case-19-funder-unavailable` | 3. Funder no longer available |
| 20 | Community Empowerment Grants - Rolling Grant Closed | `case-20-rolling-closed` | 3. Rolling grant closed |

## Hard - Community Foundation for the Fox Valley Region (`-test-site-hard-cffoxvalley`)

| # | Test case | Branch | Field |
|---|---|---|---|
| 1 | Appleton Rotary Club - Page Removed (404) | `case-01-page-removed` | 1.1 Opportunity page removed (404) |
| 2 | SECURA Insurance Companies Charitable Fund - Soft 404 Page | `case-02-soft-404` | 1.2 Opportunity page replaced by a 'not found' page (200) |
| 3 | Prospera Foundation - Eligibility Criteria changed | `case-03-eligibility-changed` | 2.1 Eligibility criteria |
| 4 | Water-Right Charitable Fund - How to Apply changed | `case-04-how-to-apply-changed` | 2.2 How to apply |
| 5 | Environmental Stewardship Fund - Focus Areas changed | `case-05-focus-areas-changed` | 2.3 Focus/impact areas |
| 6 | John & Sally Mielke Early Years Fund - Population Served changed | `case-06-population-changed` | 2.4 Population served |
| 7 | Chilton Area Community Foundation - Funding Amount increased | `case-07-funding-increased` | 2.5 Funding amount (increase) |
| 8 | Mielke Family Foundation - Funding Amount decreased | `case-08-funding-decreased` | 2.5 Funding amount (decrease) |
| 9 | Community Vision Fund - Opening Date changed | `case-09-opening-date-changed` | 2.6.1 Opening date |
| 10 | Grant Portal - Registration Date changed | `case-10-registration-date-changed` | 2.6.2 Registration date |
| 11 | Brillion Area Family of Funds Endowment Fund - LOI Date changed | `case-11-loi-date-changed` | 2.6.3 LOI submission date |
| 12 | Jewelers Mutual Impact Fund - Application Date changed | `case-12-application-date-changed` | 2.6.4 Application submission date |
| 13 | Clintonville Area Foundation Community Fund - Board Meeting Date changed | `case-13-board-meeting-date-changed` | 2.6.5 Board meeting date |
| 14 | Grant Portal - Award Notification Date changed | `case-14-award-notification-changed` | 2.6.6 Award notification date |
| 15 | Community Vision Fund - RFP Document replaced | `case-15-rfp-replaced` | 2.7.1 RFP |
| 16 | Grant Budget Template - Template Document replaced | `case-16-template-replaced` | 2.7.2 Template |
| 17 | Fox Cares Foundation Fund - Contact Information changed | `case-17-contact-changed` | 2.8 Contact information |
| 18 | Waupaca Area Community Foundation Fund - Closed Before Deadline | `case-18-closed-before-deadline` | 3.1 Not accepting applications before the deadline |
| 19 | Shawano Area Fund - Funder No Longer Available | `case-19-funder-unavailable` | 3.2 Funder not available anymore |
| 20 | Community Vision Fund - Rolling Grant Closed | `case-20-rolling-closed` | 3.3 Rolling opportunity closed |
