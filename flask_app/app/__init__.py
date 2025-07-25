from flask import Flask
from .config import FlaskConfig
from .routes import base, auth

def flask_app():
    app = Flask(__name__)

    app.config.from_object(FlaskConfig)

    app.register_blueprint(base.base_blueprint)
    app.register_blueprint(auth.auth_blueprint)

    return app