import os


API_URL = os.getenv("INTEGRATION_TEST_URL", "http://localhost:8000")

KNOWN_ENVS = {
    "http://localhost:8000": "LOCAL",
    "https://api.fauxpenverse.engineering": "PRODUCTION",
    "https://api-dev.fauxpenverse.engineering": "TESTING",
}
