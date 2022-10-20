from flask import Flask
from .config import db, bcrypt, create_api


def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.BaseConfig')
    db.init_app(app)
    bcrypt.init_app(app)

    api_bp = create_api()
    app.register_blueprint(api_bp)
    return app
