import os

class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(24))
    DEBUG = False
    TESTING = False

    RATELIMIT_DEFAULT = "30 per minute"

    CACHE_TYPE = os.getenv("CACHE_TYPE", "SimpleCache")
    CACHE_DEFAULT_TIMEOUT = 60

    CONTENT_SECURITY_POLICY = "default-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://fonts.gstatic.com;"

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True
    RATELIMIT_ENABLED = False

class ProductionConfig(BaseConfig):
    pass

def get_config(env: str | None):
    env = (env or "production").lower()
    if env.startswith("dev"):
        return DevelopmentConfig
    if env.startswith("test"):
        return TestingConfig
    return ProductionConfig
