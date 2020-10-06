from flask import Flask

from routes.migu import blue_migu
from routes.qq import blue_qq


def init_api(app: Flask):
    app.register_blueprint(blue_migu)
    app.register_blueprint(blue_qq)