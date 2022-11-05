from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restx import Api
from flask import Blueprint
import os
from pathlib import Path


HERE = Path(__file__).parent
SQLITE_DEV = "sqlite:///" + str(HERE / "site_dev.db")
SQLITE_TEST = "sqlite:///" + str(HERE / "site_test.db")

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_api_bp():
    api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
    authorizations = {
        "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
    }
    rest_api = Api(
        api_bp,
        version="1.0",
        title="Flask API with JWT-Based Authentication",
        description="Welcome to the Swagger UI documentation site!",
        doc="/ui",
        authorizations=authorizations,
        security="Bearer",
    )
    from .auth.routes import auth_ns

    rest_api.add_namespace(auth_ns, path="/auth")
    return api_bp


class BaseConfig:
    """Base configuration."""

    SECRET_KEY = os.getenv("SECRET_KEY", "open sesame")
    SQLALCHEMY_DATABASE_URI = SQLITE_DEV
    TOKEN_EXPIRE_HOURS = 0
    TOKEN_EXPIRE_MINUTES = 0


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = SQLITE_TEST


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
