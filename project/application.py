from flask import Flask

from .config import get_conf

def create_app(conf_name):
    app = Flask(__name__, template_folder="media/templates",
                static_folder="/media/statics")

    config_application(app=app, conf_name=conf_name)
    register_extenstions(app=app)
    register_blueprints(app=app)

    return app


def config_application(app, conf_name):
    conf = get_conf(conf_name)
    app.config.from_object(conf)


def register_extenstions(app):
    from .extentions import db

    db.init_app(app=app)


def register_blueprints(app):
    from .apps import cms

    app.register_blueprint(cms)