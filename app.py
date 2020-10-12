from flask import render_template
from flask_script import Manager

from music import create_app

app = create_app()

def index():
    return render_template('index.html')

app.add_url_rule('/', view_func=index)

# 初始化命令行模式
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
