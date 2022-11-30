"""Unit tests for api.auth_login API endpoint."""
from http import HTTPStatus

from api_server_flask.api.models.user import User
from api_server_flask.tests.util import login_user, LOGIN

SUCCESS = "successfully logged in"
UNAUTHORIZED = "login or password does not match"


def test_login(client, db, user):
    response = login_user(client)
    assert response.status_code == HTTPStatus.OK
    assert "status" in response.json and response.json["status"] == "success"
    assert "message" in response.json and response.json["message"] == SUCCESS
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    result = User.verify_reset_token(access_token)
    assert result.success
    token_payload = result.value
    # assert not token_payload["admin"]
    user_login = User.find_by_id(token_payload["user_id"])
    assert user_login and user_login.login == LOGIN


def test_login_does_not_exist(client, db, user):
    response = login_user(client, login="intruder")
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "message" in response.json and response.json["message"] == UNAUTHORIZED
    assert "access_token" not in response.json
