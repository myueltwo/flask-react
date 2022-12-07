"""Test cases for DELETE requests sent to the api.role API endpoint """
from http import HTTPStatus

from api_server_flask.tests.util import (
    ADMIN_LOGIN,
    ADMIN_PASSWORD,
    LOGIN,
    FORBIDDEN,
    login_user,
    create_role,
    retrieve_role,
    delete_role,
)


def test_delete_widget(client, db, admin):
    response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = create_role(client, access_token)
    assert response.status_code == HTTPStatus.CREATED
    assert "widget_id" in response.json
    role_id = response.json["widget_id"]
    assert role_id
    response = delete_role(client, access_token, role_id=role_id)
    assert response.status_code == HTTPStatus.NO_CONTENT
    response = retrieve_role(client, access_token, role_id=role_id)
    assert response.status_code == HTTPStatus.NOT_FOUND

    # delete not found role
    from api_server_flask.api.models.util import create_id

    role_id = create_id()
    response = delete_role(client, access_token, role_id=role_id)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_widget_no_admin_token(client, db, admin, user):
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
    access_token = response.json["access_token"]
    response = delete_role(client, access_token, role_id=role_id)
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert "message" in response.json and response.json["message"] == FORBIDDEN
