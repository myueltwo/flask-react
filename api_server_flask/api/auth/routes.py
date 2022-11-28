from flask_restx import Namespace, Resource
from api_server_flask.api.auth.dto import user_schema, login_model, user_model
from http import HTTPStatus
from api_server_flask.api.auth.business import (
    process_login_request,
    process_logout_request,
    get_logged_in_user,
)

auth_ns = Namespace("auth", description="Authentication of users")
auth_ns.models[login_model.name] = login_model
auth_ns.models[user_model.name] = user_model


@auth_ns.route("/login", endpoint="auth_login")
class LoginUser(Resource):
    """Handles HTTP requests to URL: /api/v1/auth/login."""

    @auth_ns.doc(security=None)
    @auth_ns.expect(login_model)
    @auth_ns.response(int(HTTPStatus.OK), "Login succeeded.")
    @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), "login or password does not match")
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @auth_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        """Authenticate an existing user and return an access token."""
        from api_server_flask.util.schema_load import parser_schema_load

        data = parser_schema_load(user_schema)
        login = data.get("login")
        password = data.get("password")
        return process_login_request(login, password)


@auth_ns.route("/logout", endpoint="auth_logout")
class LogoutUser(Resource):
    """Handles HTTP requests to URL: /auth/logout."""

    @auth_ns.doc(security="Bearer")
    @auth_ns.response(int(HTTPStatus.OK), "Log out succeeded, token is no longer valid.")
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    @auth_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        """Add token to blacklist, deauthenticating the current user."""
        return process_logout_request()


@auth_ns.route("/user", endpoint="auth_user")
class GetUser(Resource):
    """Handles HTTP requests to URL: /auth/user."""

    @auth_ns.doc(security="Bearer")
    @auth_ns.response(int(HTTPStatus.OK), "Token is currently valid.", user_model)
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), "Token is invalid or expired.")
    def get(self):
        """Validate access token and return user info."""
        user = get_logged_in_user()
        return user_schema.dump(user)
