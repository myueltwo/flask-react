from http import HTTPStatus
from api_server_flask.api.models import User
from flask_restx import abort
from flask import current_app, jsonify


def process_login_request(login, password):
    user = User.get_by_login(login)
    if not user or not user.check_password(password):
        abort(HTTPStatus.UNAUTHORIZED, 'login or password does not match', status="fail")
    access_token = user.encode_access_token()
    # return {
    #
    # }, HTTPStatus.OK
    return _create_auth_successful_response(
        access_token,
        HTTPStatus.OK,
        "successfully logged in"
    )


def _create_auth_successful_response(token, status_code, message):
    response = jsonify(
        status="success",
        message=message,
        access_token=token,
        token_type="bearer",
        expires_in=_get_token_expire_time(),
    )
    response.status_code = status_code
    response.headers["Cache-Control"] = "no-store"
    response.headers["Pragma"] = "no-cache"
    return response


def _get_token_expire_time():
    token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
    token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
    expires_in_seconds = token_age_h * 3600 + token_age_m * 60
    return expires_in_seconds if not current_app.config["TESTING"] else 5