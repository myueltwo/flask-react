"""Unit test for POST request sent to api.role_list API endoiint"""

from http import HTTPStatus
from flask import url_for
import pytest
from api_server_flask.tests.util import (
    LOGIN,
    ADMIN_LOGIN,
    ADMIN_PASSWORD,
    BAD_REQUEST,
    FORBIDDEN,
    DEFAULT_ROLE_NAME,
    login_user,
    create_role,
)


@pytest.mark.parametrize("role_name", ["abc123", "role-name", "new_role1"])
def test_create_widget_valid_name(client, db, admin, role_name):
    response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = create_role(client, access_token, role_name=role_name)
    assert response.status_code == HTTPStatus.CREATED
    assert "status" in response.json and response.json["status"] == "success"
    success = f"New role added: {role_name}."
    assert "message" in response.json and response.json["message"] == success
    assert "role_id" in response.json and response.json["role_id"]
    role_id = response.json["role_id"]
    location = url_for("api.role", role_id=role_id)
    assert "Location" in response.headers and response.headers["Location"] == location
