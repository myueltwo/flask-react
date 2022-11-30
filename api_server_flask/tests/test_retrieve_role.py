"""Test cases for GET request sent to api.role API endpoint"""

from http import HTTPStatus

from api_server_flask.tests.util import (
    ADMIN_LOGIN,
    ADMIN_PASSWORD,
    LOGIN,
    DEFAULT_ROLE_NAME,
    login_user,
    create_role,
    retrieve_role,
)


def test_retrieve_widget_non_admin_user(client, db, admin, user):
    response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = create_role(client, access_token)
    assert response.status_code == HTTPStatus.CREATED
    role_id = response.json["role_id"]
    assert role_id

    response = login_user(client, login=LOGIN)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    response = retrieve_role(client, access_token, role_id=role_id)
    assert response.status_code == HTTPStatus.OK

    assert "name" in response.json and response.json["name"] == DEFAULT_ROLE_NAME


def test_retrieve_widget_does_not_exist(client, db, user):
    response = login_user(client, login=LOGIN)
    assert "access_token" in response.json
    access_token = response.json["access_token"]
    from api_server_flask.api.models.util import create_id

    not_exist_role_id = create_id()
    response = retrieve_role(client, access_token, role_id=not_exist_role_id)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert (
        "message" in response.json
        and f"{not_exist_role_id} not found in database" in response.json["message"]
    )
