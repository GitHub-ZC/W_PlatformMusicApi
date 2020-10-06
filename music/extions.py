from flask_caching import Cache


cache = Cache()


def init_app(app):
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})