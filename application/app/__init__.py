from flask import Flask
from .routes import auth, base
from app.config import FlaskConfig

def flask_app():
    
    app = Flask(__name__)

    app.config.from_object(FlaskConfig)

    app.register_blueprint(auth.auth_blueprint)
    app.register_blueprint(base.base_blueprint)

    return app
