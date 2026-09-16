import pytest


@pytest.mark.smoke
def test_login_emite_cookie_httponly(client, registered_user):
    r = client.login(registered_user["email"], registered_user["password"])
    assert r.status_code == 200, f"{r.status_code} — {r.text}"

    set_cookie = r.headers.get("set-cookie", "")
    assert "cookietoken=" in set_cookie, f"no se emitió cookietoken — {set_cookie}"
    assert "HttpOnly" in set_cookie, "la cookie debe ser HttpOnly, no accesible por JS"


@pytest.mark.smoke
def test_ruta_protegida_accesible_con_sesion(logged_in_client):
    r = logged_in_client.datos_user()
    assert r.status_code == 200, f"{r.status_code} — {r.text}"