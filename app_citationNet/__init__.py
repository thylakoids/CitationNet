from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
