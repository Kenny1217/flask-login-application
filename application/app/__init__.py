from flask import Flask
from .routes import auth, base

def flask_app():
    
    app = Flask(__name__)

    app.register_blueprint(auth.auth_blueprint)
    app.register_blueprint(base.base_blueprint)

    return app
