from flask import Flask
from api_server_flask.api.config import db, bcrypt, api_bp, get_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    db.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(api_bp)
    return app
