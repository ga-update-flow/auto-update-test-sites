# Live test report - all 60 test cases

Each case branch was published to its real GitHub Pages URL, then opened on the live site two ways (plain HTTP and a real headless Chrome). Checks: the changed file is live byte-for-byte; the new text is visible; the old text is gone; new links are present and old links gone; the removed page returns 404; home and grants pages stay identical to the baseline.

**Final result: 60 of 60 PASS.**  5 cases failed on the first run because GitHub Pages kept serving a stale copy for 10+ minutes after publishing; all of them passed on a re-run (same content, nothing changed).

## Easy - bcm.org - 20/20 PASS

| # | Test case | Result | Checks | Live page now says (examples) |
|---|---|---|---|---|
| 1 | Opportunity Grants - Page Removed (404) | PASS | 3/3 | page returns 404 |
| 2 | Strategic Grants - Soft 404 Page | PASS | 9/9 | Page not found - Baptist Community Ministries // Page not found // Sorry, the page you requested could not be found. |
| 3 | Discretionary Donations - Eligibility Criteria changed | PASS | 9/9 | The organization must be based in, and primarily serve residents of, Orleans, Jefferson or St. Bernard Parish and must have been operating f // The organization must be a registered 501(c)(3) public charity with a current IRS dete |
| 4 | Transom Grants - How to Apply changed | PASS | 9/9 | LOIs are now submitted by email to grants@bcm.org using the LOI Overview format; the online application portal is no longer used for Letters // Only organizations that are invited to do so are allowed to submit a full transom gran |
| 5 | Strategic Grants - Focus Areas changed | PASS | 9/9 | Strategic Grants and investments go to support projects and organizations related to BCM strategic priorities. Current areas of investment i // Housing Stability & Homelessness Prevention // In the Housing focus area, BCM engages  |
| 6 | Strategic Grants - Population Served changed | PASS | 9/9 | Quality seats for children with disabilities and for families experiencing homelessness, with particular focus on rural parishes |
| 7 | Transom Grants - Funding Amount increased | PASS | 9/9 | All requests must be at least $75,000 per year to be considered. // A – BCM Transom requests must include a minimum request of $75,000 per year up to three years (including indirect costs up to 12%). While no |
| 8 | Discretionary Donations - Funding Amount decreased | PASS | 9/9 | BCM awards Discretionary Donations in amounts of $1,000 or $2,500 to support community events. If your organization seeks funding for an eve // Grants are awarded in the amounts of $1,000 and $2,500. |
| 9 | Open Invitation Grants - Opening Date changed | PASS | 9/9 | BCM is proud to support the growth of our community by providing funding for programs that promote the well-being of those living in it. We  |
| 10 | Transom Grants - Registration Date changed | PASS | 8/8 | Registration for the Spring 2027 Transom Info Session closes January 8, 2027. |
| 11 | Transom Grants - LOI Date changed | PASS | 9/9 | Upcoming Spring 2027 Cycle // January 12, 2027: Transom Info Session 10:00-11:00AM / // Spring 2027 Info Session Recording |
| 12 | Transom Grants - Application Date changed | PASS* | 9/9 | March 1, 2027: Full application deadline at 5:00 PM // May 17, 2027: Grant decision notifications sent |
| 13 | Strategic Grants - Board Meeting Date changed | PASS | 9/9 | Strategic Grants and investments go to support projects and organizations related to BCM strategic priorities. Current areas of investment i |
| 14 | Transom Grants - Award Notification Date changed | PASS | 9/9 | April 12, 2027: Grant decision notifications sent |
| 15 | Transom Grants - RFP Document replaced | PASS* | 13/13 | (document replaced; link updated) |
| 16 | Transom Grants - Template Document replaced | PASS | 13/13 | (document replaced; link updated) |
| 17 | Discretionary Donations - Contact Information changed | PASS | 13/13 | grantsteam@bcm.org |
| 18 | Transom Grants - Closed Before Deadline | PASS* | 9/9 | March 1, 2027: Full application deadline at 5:00 PM // May 17, 2027: Grant decision notifications sent // Update: BCM has reached its funding capacity for this cycle and is no longer accepting applications, ahead of the March 1, 2 |
| 19 | Core Funding Grants - Funder No Longer Available | PASS | 9/9 | Core funding grants provide unrestricted general operating funds to support an organization’s general infrastructure over an extended period |
| 20 | Discretionary Donations - Rolling Grant Closed | PASS | 9/9 | BCM awards Discretionary Donations in amounts of $2,500 or $5,000 to support community events. If your organization seeks funding for an eve // . Applications are no longer being accepted. The Discretionary Donations program is cl |

## Medium - muskegonfoundation.org - 20/20 PASS

| # | Test case | Result | Checks | Live page now says (examples) |
|---|---|---|---|---|
| 1 | Faith Partner Grants - Page Removed (404) | PASS | 3/3 | page returns 404 |
| 2 | Community Empowerment Grants - Soft 404 Page | PASS | 9/9 | Page not found // Page not found // Sorry, the page you are looking for could not be found or may no longer exist. |
| 3 | Watch Us Vote Grants - Eligibility Criteria changed | PASS | 9/9 | Nonprofit organizations headquartered in Muskegon County with an annual operating budget under $250,000 // Neighborhood associations and volunteer-led community groups applying through a nonprofit fiscal sponsor // Youth-serving o |
| 4 | Muskegon LEAD Grants - How to Apply changed | PASS | 9/9 | Organizations seeking grant dollars must apply online. Create a login in the Grant Portal and submit a complete nomination package that incl // A completed online nomination form with your mission and vision and a three-page narra |
| 5 | Building an Inclusive Community Mini-Grants - Focus Areas changed | PASS* | 9/9 | we’re looking for ideas that create projects, programs, or events that advance youth literacy, healthy food access, and neighborhood beautif // within the community. We will be awarding five (5) grants to projects that support rea |
| 6 | Muskegon LEAD Grants - Population Served changed | PASS | 9/9 | (Leading Efforts Against Discrimination) Giving Circle was organized to collectively fund initiatives in Muskegon County, specifically and i |
| 7 | Watch Us Vote Grants - Funding Amount increased | PASS* | 9/9 | The Community Foundation invites all Muskegon County Nonprofits to apply for Watch Us Vote Mini‑Grants, providing up to $2,500 to support no |
| 8 | Muskegon LEAD Grants - Funding Amount decreased | PASS | 9/9 | Future plans and dreams for work that will create a just, diverse, inclusive, and equitable community, including how a grant of $2,500 – $3, |
| 9 | Muskegon LEAD Grants - Opening Date changed | PASS | 9/9 | Muskegon LEAD Grant nominations are now closed and will reopen February 2027. |
| 10 | Watch Us Vote Grants - Registration Date changed | PASS | 9/9 | Fill out the super-simple application linked below. Applications will be reviewed bi-weekly and awarded on a first-come, first-served basis. |
| 11 | Community Empowerment Grants - LOI Date changed | PASS | 9/9 | The beginning of each month grants are reviewed by a staff committee. Requests over $2,000 require a letter of intent, due February 19, 2027 |
| 12 | Watch Us Vote Grants - Application Date changed | PASS | 9/9 | Grants will be available until funds are depleted or until March 1, 2027. |
| 13 | Committee Grants - Board Meeting Date changed | PASS | 9/9 | There are two rounds of Committee Grants in 2026. The spring round (December 2025 – February 2026) is closed. The fall round (July 2026 – Se |
| 14 | Muskegon LEAD Grants - Award Notification Date changed | PASS | 9/9 | Decisions announced by the end of January 2027 |
| 15 | Online eGrant Instructions 2016 - RFP Document replaced | PASS | 13/13 | (document replaced; link updated) |
| 16 | Grant Application Budget - Template Document replaced | PASS | 13/13 | (document replaced; link updated) |
| 17 | Watch Us Vote Grants - Contact Information changed | PASS | 13/13 | Questions? Contact Dana Whitfield, Grants Manager, at // dwhitfield@muskegonfoundation.org // or call 231-722-4538 ext. 214 |
| 18 | Watch Us Vote Grants - Closed Before Deadline | PASS | 9/9 | All funds for this program were awarded before the March 1, 2027 deadline, and the Community Foundation is no longer accepting Watch Us Vote // Thank you for your interest and support. |
| 19 | Committee Grants - Funder No Longer Available | PASS | 9/9 | The Committee Grants program has been discontinued. The Community Foundation is no longer accepting letters of intent or applications for co |
| 20 | Community Empowerment Grants - Rolling Grant Closed | PASS | 9/9 | Grants are reviewed and awarded each month – this is a “rolling timeline” until funds are depleted. This rolling grant is now closed and is  // Previously, at the beginning of each month, grants were reviewed by a staff committee  |

## Hard - cffoxvalley.org - 20/20 PASS

| # | Test case | Result | Checks | Live page now says (examples) |
|---|---|---|---|---|
| 1 | Appleton Rotary Club - Page Removed (404) | PASS | 3/3 | page returns 404 |
| 2 | SECURA Insurance Companies Charitable Fund - Soft 404 Page | PASS | 9/9 | Page not found - Community Foundation for the Fox Valley Region // Page not found // Sorry, the page you requested could not be found. |
| 3 | Prospera Foundation - Eligibility Criteria changed | PASS | 9/9 | Be a 501(c)(3) public charity with at least three years of audited financial statements. // Located or provide services in the counties in which Prospera Credit Union branches serve: Outagamie and Winnebago only; organizations ser |
| 4 | Water-Right Charitable Fund - How to Apply changed | PASS | 9/9 | Based on the general grant policies and grant guidelines stated above, if you believe you qualify, follow the email instructions below. The  // Applications for this fund are now accepted by email only: send a one-page request and |
| 5 | Environmental Stewardship Fund - Focus Areas changed | PASS | 9/9 | Priority 1: Water & Watersheds // — Support clean-water and watershed restoration projects in the Fox River basin. // Priority 2: Climate & Energy |
| 6 | John & Sally Mielke Early Years Fund - Population Served changed | PASS | 9/9 | To support programs that serve children from prenatal to five years of age and their families, with priority given to rural and migrant farm // Remove barriers to access for children from rural and migrant farmworker families |
| 7 | Chilton Area Community Foundation - Funding Amount increased | PASS | 9/9 | up to $15,000. |
| 8 | Mielke Family Foundation - Funding Amount decreased | PASS | 9/9 | Responsive grants will be for one year, up to $30,000. |
| 9 | Community Vision Fund - Opening Date changed | PASS | 9/9 | Opens March 8, 2027; Closes October 31; // Event sponsorship applications will open on March 8th. While we routinely ask for 60-day advance notice, we recognize that the timing of our // Opens March 8, 2027; Closes October 31; |
| 10 | Grant Portal - Registration Date changed | PASS | 9/9 | Once you register in the new Grant Portal, you don’t have to wait for approval to begin applying for grants as you would in our old Grant Po |
| 11 | Brillion Area Family of Funds Endowment Fund - LOI Date changed | PASS | 9/9 | Grant application will open February 1st with a deadline of April 1st at 11:59 p.m. Letters of intent are due January 15, 2027. |
| 12 | Jewelers Mutual Impact Fund - Application Date changed | PASS | 9/9 | March 15, 2027, June 15, 2027, September 15, 2027 and December 15, 2027 by 11:59 p.m. Central Time. |
| 13 | Clintonville Area Foundation Community Fund - Board Meeting Date changed | PASS | 8/8 | Board Meeting: // The Clintonville Area Foundation board reviews recommendations on January 14, 2027. |
| 14 | Grant Portal - Award Notification Date changed | PASS | 9/9 | Please do your best to be concise and remember that sometimes staff and grants committee members may be reviewing twenty or more grant appli |
| 15 | Community Vision Fund - RFP Document replaced | PASS | 13/13 | (document replaced; link updated) |
| 16 | Grant Budget Template - Template Document replaced | PASS | 13/13 | (document replaced; link updated) |
| 17 | Fox Cares Foundation Fund - Contact Information changed | PASS | 13/13 | 920.555.0142 // lindsay.fenlon@cffoxvalley.org // 920.555.0142 |
| 18 | Waupaca Area Community Foundation Fund - Closed Before Deadline | PASS | 9/9 | June 10 by 11:59 p.m. Update: all available funds for this cycle have been awarded and the fund is no longer accepting applications, ahead o |
| 19 | Shawano Area Fund - Funder No Longer Available | PASS | 9/9 | come from fundraising activities and unrestricted funds that donors established intending that the boards of the SACF and the Community Foun // The Foundation previously accepted requests with greater flexibility as to the type of |
| 20 | Community Vision Fund - Rolling Grant Closed | PASS | 9/9 | Rolling applications are now closed; requests were previously reviewed and responded to by // Event sponsorship applications opened on February 23rd and are now closed. While we routinely ask for 60-day advance notice, we recogniz |

\* failed the first live run because of stale Pages cache, passed on re-run.

Details per case (every check with evidence) are in `results/<case>.md` on the `qa-report` branch of each site repo.
