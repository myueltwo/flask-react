"""Unit tests for api.auth_reset_password API endpoint."""
from http import HTTPStatus
from flask import url_for
from api_server_flask.tests.util import (
    ADMIN_PASSWORD,
    login_user,
    PASSWORD,
)

SUCCESS = "Password was changed."


def _reset_token(test_client, access_token, widget_dict):
    return test_client.post(
        url_for("api.auth_reset_password"),
        headers={"Authorization": f"Bearer {access_token}"},
        data="&".join([f"{k}={v}" for k, v in widget_dict.items()]),
        content_type="application/x-www-form-urlencoded",
    )


def test_reset_token(client, db, user):
    response = login_user(client)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = _reset_token(
        client,
        access_token,
        {"new_password": ADMIN_PASSWORD, "repeat_password": ADMIN_PASSWORD},
    )
    assert response.status_code == HTTPStatus.OK


def test_reset_not_equal_passwords(client, db, user):
    response = login_user(client)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = _reset_token(
        client,
        access_token,
        {"new_password": ADMIN_PASSWORD, "repeat_password": PASSWORD},
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert "status" in response.json and response.json["status"] == "error"
    assert (
        "status" in response.json
        and response.json["message"] == "passwords are not equal"
    )


def test_reset_password_no_token(client, db, user):
    response = _reset_token(
        client,
        "",
        {"new_password": ADMIN_PASSWORD, "repeat_password": ADMIN_PASSWORD},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert (
        "message" in response.json
        and response.json["message"] == "Invalid token. Please log in again"
    )
