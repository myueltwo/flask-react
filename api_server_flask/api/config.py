from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restx import Api
from flask import Blueprint
import os
from pathlib import Path
from sqlalchemy import MetaData


HERE = Path(__file__).parent
SQLITE_DEV = "sqlite:///" + str(HERE / "site_dev.db")
SQLITE_TEST = "sqlite:///" + str(HERE / "site_test.db")

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
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
    from api_server_flask.api.widgets.roles.routes import role_ns
    from api_server_flask.api.widgets.groups.routes import group_ns
    from api_server_flask.api.widgets.subjects.routes import subject_ns
    from api_server_flask.api.widgets.type_grade.routes import type_grade_ns
    from api_server_flask.api.widgets.grades.routes import grade_ns
    from api_server_flask.api.widgets.grade_users.routes import grade_users_ns

    rest_api.add_namespace(auth_ns, path="/auth")
    rest_api.add_namespace(role_ns, path="/widgets/roles")
    rest_api.add_namespace(group_ns, path="/widgets/groups")
    rest_api.add_namespace(subject_ns, path="/widgets/subjects")
    rest_api.add_namespace(type_grade_ns, path="/widgets/type_grades")
    rest_api.add_namespace(grade_ns, path="/widgets/grades")
    rest_api.add_namespace(grade_users_ns, path="/widgets/grade_users")
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
