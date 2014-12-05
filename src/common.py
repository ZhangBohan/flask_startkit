from functools import wraps
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request
from werkzeug.contrib.cache import SimpleCache

__author__ = 'bohan'

app = Flask(__name__)
app.debug = True

if not app.debug:
    formatter = logging.Formatter(
            "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('/tmp/foo.log', maxBytes=100000, backupCount=10)
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)

cache = SimpleCache()


def cached(timeout=5 * 60):
    def cache_request(func):

        def decorator(*args, **kwargs):
            response = cache.get(request.path)
            if response is None:
                response = func(*args, **kwargs)
                cache.set(request.path, response, timeout)
            return response
        return decorator
    return cache_request

import routes