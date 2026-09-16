import uuid
import pytest
from framework.api_client import ApiClient
from framework.config import Settings


@pytest.fixture(scope="session")
def settings():
    return Settings()


@pytest.fixture
def client(settings):
    c = ApiClient(settings)
    yield c
    c.close()

@pytest.fixture
def user_data():
    """Datos únicos por test: el email es llave única en el schema."""
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
    assert r.status_code in (200, 201), f"registro falló: {r.status_code} — {r.text}"
    return user_data

@pytest.fixture
def logged_in_client(client, registered_user):
    r = client.login(registered_user["email"], registered_user["password"])
    assert r.status_code == 200, f"login falló: {r.status_code} — {r.text}"
    assert client.auth_cookie, "no se emitió la cookie cookietoken"
    return client
