import os
from app_citationNet import create_app
from flask_script import Manager, Server, Shell
from config import config

conf = config[os.getenv('FLASK_CONFIG') or 'default']
app = create_app(os.getenv('FLASK_CONFIG') or 'default')


def _make_context():
    return dict(app=app)


manager = Manager(app)
manager.add_command('runserver', Server(host=conf.host, port=conf.port))
manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
