# events-qa-suite

API and E2E test suite for the events app's auth service (JWT + cookieParser). It's kept as its own repo on purpose: no imports from the app's code, its own dependencies, configuration through environment variables only.

## Requirements
1. Python 3.12+
2. Google Chrome (only needed for the e2e tests)
3. The app under test running

## Setup
```
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration
Set these as environment variables before running the tests:

1. `BASE_URL`: defaults to `http://localhost:8080`. URL of the app under test.
2. `TIMEOUT`: defaults to `10`. HTTP timeout in seconds.

## Running the tests
```
pytest                     # everything
pytest -m api               # API tests only
pytest -m e2e               # browser tests (needs Chrome and driver)
pytest -m "not e2e"         # skip the browser tests
```

## Project structure
```
framework/
  api_client.py     wraps the HTTP client (httpx); one method per API action
  config.py         reads BASE_URL / TIMEOUT from the environment
  pages/             page objects used by the e2e tests (login page, profile page)
  schemas/           JSON schemas used by the contract tests

tests/
  test_health.py     is the service up?
  test_auth.py        login issues a valid session cookie, protected routes are reachable with it
  test_contract.py    response shape of /datosuser matches the schema
  test_login.py       e2e: log in from a browser

conftest.py          fixtures shared across tests (client, registered user, logged in client, etc.)
```

## Fixtures worth knowing about
1. `client`: a plain HTTP client, not logged in, fresh for every test.
2. `user_data`: a throwaway user with a unique email (via uuid) so tests don't collide with each other.
3. `registered_user`: registers that user against the running app and returns its data.
4. `logged_in_client`: the same client, but already logged in with `registered_user`'s credentials.

Each test asks for whichever fixture it actually needs; they build on top of each other, so a test that just needs an authenticated session doesn't have to know how registration or login work underneath.

## Markers
Defined in `pytest.ini`:
1. `api`: HTTP level tests, no browser involved.
2. `e2e`: needs a real browser (Selenium + Chrome).

`e2e` is left out of the regular PR gate on purpose. It's slower and needs a browser, so it runs on its own workflow instead.
