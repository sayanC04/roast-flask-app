from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache

# Explicit memory storage to avoid 'no storage specified' warning
limiter = Limiter(key_func=get_remote_address, storage_uri="memory://")
cache = Cache()
