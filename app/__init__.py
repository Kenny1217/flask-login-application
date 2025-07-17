from flask import Flask
from .routes import auth, base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def flask_app():
    app = Flask(__name__)

    app.config.from_object('config.datbaseConfig')

    db.init_app(app)

    app.register_blueprint(auth.auth_blueprint)
    app.register_blueprint(base.base_blueprint)

    return app