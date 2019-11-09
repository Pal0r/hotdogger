# New Hire Example Test Project
This project is designed to test potential hires for structure and Django understanding. It has several flaws the candidate should identify and fix.

## Getting Started
1. Install Requirements
2. Create a database called `hotdogger`
3. Install fixtures `python manage.py loaddata vendors/fixtures/data.json`
4. (optional) create a super user `python manage.py createsuperuser`
5. Start the instance `python manage.py runserver`
6. Visit http://localhost:8000/accounts/signup/

## Testing
Hotdogger uses the standard testing library for both DRF and Django.
Coverage reports can be generated by running `coverage run manage.py test`. To view the coverage report `coverage report -m`.

## Ticket 1
QA witnessed a regression in test coverage. Please confirm regress and update and/or create unit tests where necessary.

## Ticket 2
The CEO of Hotdogger Inc was browsing the site while not logged in. He was able to view the vendor list without being authenticated. Needless to say, this is a major problem. Investigate all endpoints and implement security measures. Then prove with unit tests that this is no longer a problem.

## Ticket 3
It appears vendors are able to see their competitor's product offering. Often, this is a major competitive advantage for a vendor. This represents a breach of trust. Ensure vendors can only see their own offerings.

## Ticket 4
Hot dog options not yet available are showing up in the vendor items list view. Make sure that only available products are displayed.

## Ticket 5
Our clients are starting to notice a lag in response times in the vendor item listing. Investigate. If possible improve page queries WITHOUT the aid of caching.

## Ticket 6
Some clients have 100s of product offerings. Limit the number of offerings on a page.