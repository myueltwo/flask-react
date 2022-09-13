from flask import Flask
from .config import db, bcrypt, login_manager
from .routes import rest_api

login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.BaseConfig')
    db.init_app(app)
    bcrypt.init_app(app)
    rest_api.init_app(app)
    login_manager.init_app(app)
    return app
