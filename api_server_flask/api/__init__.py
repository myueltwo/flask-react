from flask import Flask
from api_server_flask.api.config import db, bcrypt, create_api_bp, get_config
from flask_migrate import Migrate

migrate = Migrate(render_as_batch=True)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    api_bp = create_api_bp()
    app.register_blueprint(api_bp)
    return app
