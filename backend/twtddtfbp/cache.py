__cache = {}

def has_key(key):
    return key in __cache

def set(key, value):
    __cache[key] = value

def get(key):
    return __cache.get(key)
