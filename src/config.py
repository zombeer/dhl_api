import os

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL", "https://api-eu.dhl.com/track")
SELF_URL = os.getenv("SELF_URL", "http://localhost/")
ENABLE_CORS = os.getenv("ENABLE_CORS", True)
REDIS_URL = os.getenv("REDIS_URL", "redis://172.17.0.2:6379")
