from flask import Flask
from .routes import base

def flask_app():
    app = Flask(__name__)

    app.register_blueprint(base.base_blueprint)

    return app