"""Unit tests for api.auth_user API endpoint."""
import time
from http import HTTPStatus

from flask import url_for
from .util import LOGIN, WWW_AUTH_NO_TOKEN, login_user, get_user

TOKEN_EXPIRED = "Access token expired. Please log in again."
WWW_AUTH_EXPIRED_TOKEN = (
    f"{WWW_AUTH_NO_TOKEN}, "
    'error="invalid_token", '
    f'error_description="{TOKEN_EXPIRED}"'
)


def test_auth_user(client, db, user):
    response = login_user(client)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = get_user(client, access_token)
    assert response.status_code == HTTPStatus.OK
    assert "login" in response.json and response.json["login"] == LOGIN
    # assert "admin" in response.json and not response.json["admin"]


def test_auth_user_no_token(client, db):
    response = client.get(url_for("api.auth_user"))
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "message" in response.json and response.json["message"] == "Unauthorized"
    assert "WWW-Authenticate" in response.headers
    assert response.headers["WWW-Authenticate"] == WWW_AUTH_NO_TOKEN


def test_auth_user_expired_token(client, db, user):
    response = login_user(client)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    time.sleep(6)
    response = get_user(client, access_token)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert "message" in response.json and response.json["message"] == TOKEN_EXPIRED
    assert "WWW-Authenticate" in response.headers
    assert response.headers["WWW-Authenticate"] == WWW_AUTH_EXPIRED_TOKEN
