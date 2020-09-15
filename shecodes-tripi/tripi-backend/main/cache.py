from flask_caching import Cache


default_timeout = 180

cache = Cache(config={
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": default_timeout
})
