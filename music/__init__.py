from flask import Flask
from flask_script import Manager

from routes import init_api
from . import setting
from .extions import init_app


def create_app():
    # 创建并且导入Flask相关配置(邮箱，数据库，。。。)
    app = Flask(__name__)
    app.config.from_object(setting)

    # 初始化路由
    init_api(app)

    # 初始化第三方插件
    init_app(app)

    # 初始化命令行模式
    manager = Manager(app)

    # 最终上线需要 return app
    return manager