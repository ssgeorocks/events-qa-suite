import os


class Settings:
    """Un solo lugar para la configuración. Nada hardcodeado en los tests."""

    def __init__(self):
        self.base_url = os.environ.get("BASE_URL", "http://localhost:8080")
        self.timeout = float(os.environ.get("TIMEOUT", "10"))