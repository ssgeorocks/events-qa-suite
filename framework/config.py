import os


class Settings:
    """Single source for API Client configuration"""

    def __init__(self):
        self.base_url = os.environ.get("BASE_URL", "http://localhost:8080")
        self.timeout = float(os.environ.get("TIMEOUT", "10"))