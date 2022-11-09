from http import HTTPStatus
from api_server_flask.api.models.user import User
from api_server_flask.api.models.black_listed_token import BlacklistedToken
from flask_restx import abort
from flask import current_app, jsonify
from api_server_flask.api.auth.decorators import token_required
from api_server_flask.util.datetime_util import (
    remaining_fromtimestamp,
    format_timespan_digits,
)


def process_login_request(login, password):
    user = User.get_by_login(login)
    if not user or not user.check_password(password):
        abort(HTTPStatus.UNAUTHORIZED, "login or password does not match", status="fail")
    access_token = user.encode_access_token()
    return _create_auth_successful_response(
        access_token, HTTPStatus.OK, "successfully logged in"
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


@token_required
def process_logout_request():
    access_token = process_logout_request.token
    expires_at = process_logout_request.expires_at
    blacklisted_token = BlacklistedToken(access_token, expires_at)
    from api_server_flask.api import db

    db.session.add(blacklisted_token)
    db.session.commit()
    response_dict = dict(status="success", message="successfully logged out")
    return response_dict, HTTPStatus.OK


@token_required
def get_logged_in_user():
    user_id = get_logged_in_user.user_id
    user = User.find_by_id(user_id)
    expires_at = get_logged_in_user.expires_at
    user.token_expires_in = format_timespan_digits(remaining_fromtimestamp(expires_at))
    return user
