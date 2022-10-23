from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

from flask_restx import Api
from flask import Blueprint
from .auth.routes import auth_ns

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
authorizations = {
    "Bearer": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}
rest_api = Api(
    api_bp,
    version="1.0",
    title="Flask API with JWT-Based Authentication",
    description="Welcome to the Swagger UI documentation site!",
    doc="/ui",
    authorizations=authorizations,
)
rest_api.add_namespace(auth_ns, path='/auth')


class BaseConfig():
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    TOKEN_EXPIRE_MINUTES = 15


class ProductionConfig(BaseConfig):
    """Production configuration."""

    TOKEN_EXPIRE_HOURS = 1


ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)
