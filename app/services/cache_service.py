import time

_cache: dict = {}


class CacheService:
    """Simple in-memory TTL cache for product lookups."""

    @staticmethod
    def get(key: str):
        entry = _cache.get(key)
        if entry and time.time() < entry['expires']:
            return entry['value']
        _cache.pop(key, None)
        return None

    @staticmethod
    def set(key: str, value, ttl: int = 3600):
        _cache[key] = {'value': value, 'expires': time.time() + ttl}

    @staticmethod
    def delete(key: str):
        _cache.pop(key, None)

    @staticmethod
    def clear():
        _cache.clear()
