from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_api():
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
    return api_bp


class BaseConfig():
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
