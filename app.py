from flask_script import Manager

from music import create_app

app = create_app()

# 初始化命令行模式
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
