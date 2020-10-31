from flask_restful import request

from music.extions import cache


def before_request():
    path = request.url

    data = cache.get(path)
    if data:
        return data