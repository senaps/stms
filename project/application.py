from flask import Flask


def create_app():
    app = Flask(__name__)

    register_blueprints(app=app)

    return app


def register_blueprints(app):
    from .apps import cms

    app.register_blueprint(cms)