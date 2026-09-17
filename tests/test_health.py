import pytest


@pytest.mark.api
def test_health_responds_ok(client):
    res = client.health()
    assert res.status_code == 200, f"Expected 200, but returned {res.status_code} — {res.text}"
