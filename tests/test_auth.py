import pytest


@pytest.mark.api
def test_login_issues_cookie_token(client, registered_user):
    res = client.login(registered_user["email"], registered_user["password"])
    assert res.status_code == 200, f"{res.status_code}: {res.text}"

    set_cookie = res.headers.get("set-cookie", "")
    assert "cookietoken=" in set_cookie, f"Incorrect cookie token issued: {set_cookie}"

@pytest.mark.api
def test_authenticated_user_can_access_protected_route(logged_in_client):
    res = logged_in_client.datos_user()
    assert res.status_code == 200, f"{res.status_code}: {res.text}"