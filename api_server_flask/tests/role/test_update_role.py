"""Test cases for PUT requests sent to the api.role API endpoint"""
from http import HTTPStatus

from api_server_flask.tests.util import (
    ADMIN_LOGIN,
    ADMIN_PASSWORD,
    LOGIN,
    login_user,
    create_role,
    retrieve_role,
    update_role,
    FORBIDDEN,
)

UPDATED_DEFAULT_ROLE_NAME = "update some role2"


def test_update_role(client, db, admin):
    response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = create_role(client, access_token)
    assert response.status_code == HTTPStatus.CREATED
    role_id = response.json["widget_id"]
    assert role_id

    response = update_role(
        client,
        access_token,
        role_id=role_id,
        role_name=UPDATED_DEFAULT_ROLE_NAME,
    )
    assert response.status_code == HTTPStatus.OK
    assert "message" in response.json
    assert response.json["message"] == f"'{role_id}' was successfully updated"
    response = retrieve_role(client, access_token, role_id=role_id)
    assert response.status_code == HTTPStatus.OK

    assert "name" in response.json and response.json["name"] == UPDATED_DEFAULT_ROLE_NAME


def test_update_role_not_admin(client, db, admin, user):
    response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = create_role(client, access_token)
    assert response.status_code == HTTPStatus.CREATED
    assert "widget_id" in response.json
    role_id = response.json["widget_id"]
    assert role_id

    response = login_user(client, login=LOGIN)
    assert "access_token" in response.json
    access_token_user = response.json["access_token"]
    response = update_role(
        client,
        access_token_user,
        role_id=role_id,
        role_name=UPDATED_DEFAULT_ROLE_NAME,
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert "message" in response.json and response.json["message"] == FORBIDDEN


def test_update_role_not_exist(client, db, admin):
    response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    from api_server_flask.api.models.util import create_id

    role_id = create_id()

    response = update_role(
        client,
        access_token,
        role_id=role_id,
        role_name=UPDATED_DEFAULT_ROLE_NAME,
    )
    assert response.status_code == HTTPStatus.CREATED
    assert "status" in response.json and response.json["status"] == "success"
    success = f"New role added: {UPDATED_DEFAULT_ROLE_NAME}."
    assert "message" in response.json and response.json["message"] == success
    assert "widget_id" in response.json
    role_id = response.json["widget_id"]
    response = retrieve_role(client, access_token, role_id=role_id)
    assert response.status_code == HTTPStatus.OK

    assert "name" in response.json and response.json["name"] == UPDATED_DEFAULT_ROLE_NAME
