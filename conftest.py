import os
import uuid
import pytest
from framework.api_client import ApiClient
from framework.config import Settings
from selenium import webdriver


@pytest.fixture(scope="session")
def settings():
    return Settings()

@pytest.fixture
def driver():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--headless=new")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-dev-shm-usage")
    opt.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(0)
    yield driver
    driver.quit()

@pytest.fixture
def client(settings):
    c = ApiClient(settings)
    yield c
    c.close()

@pytest.fixture
def user_data():
    """User data. This all the information required from the user at the moment.
    Email will be unique for each test."""
    suffix = uuid.uuid4().hex[:8]
    return {
        "first_name": "Test",
        "last_name": "User",
        "email": f"qa_{suffix}@example.com",
        "password": "Passw0rd!123",
    }

@pytest.fixture
def registered_user(client, user_data):
    r = client.register(**user_data)
    assert r.status_code in (200, 201), f"User registration failed: {r.status_code} — {r.text}"
    return user_data

@pytest.fixture
def logged_in_client(client, registered_user):
    r = client.login(registered_user["email"], registered_user["password"])
    assert r.status_code == 200, f"Login failed: {r.status_code} — {r.text}"
    assert client.auth_cookie, "Cookie token not issued"
    return client
