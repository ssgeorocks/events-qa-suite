import httpx

from framework.config import Settings


class ApiClient:
    """Centraliza base URL, sesión y cookies.
    Los tests llaman acciones, no URLs."""

    def __init__(self, settings=None):
        self.settings = settings or Settings()
        self._client = httpx.Client(
            base_url=self.settings.base_url,
            timeout=self.settings.timeout,
            follow_redirects=False,
        )

    def close(self):
        self._client.close()

    # --- acciones ---

    def health(self):
        return self._client.get("/health")

    def register(self, first_name, last_name, email, password, role="user"):
        return self._client.post(
            "/api/sessions/register",
            json={
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "password": password,
                "role": role,
            },
        )

    def login(self, email, password):
        return self._client.post(
            "/api/sessions/login",
            json={"email": email, "password": password},
        )

    def logout(self):
        return self._client.get("/api/sessions/logout")

    def datos_user(self):
        return self._client.get("/api/sessions/datosuser")

    def datos_admin(self):
        return self._client.get("/api/sessions/datosadmin")

    # --- estado, para pruebas negativas ---

    @property
    def auth_cookie(self):
        return self._client.cookies.get("cookietoken")

    def set_raw_cookie(self, value):
        self._client.cookies.set("cookietoken", value)

    def clear_cookies(self):
        self._client.cookies.clear()