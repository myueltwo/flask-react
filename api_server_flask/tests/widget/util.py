from flask import url_for
from http import HTTPStatus
from api_server_flask.tests.util import (
    LOGIN,
    ADMIN_LOGIN,
    ADMIN_PASSWORD,
    FORBIDDEN,
    login_user,
)

DEFAULT_NAME = "some name"
UPDATED_DEFAULT_NAME = "update some name2"


def create(test_client, access_token, url, name=DEFAULT_NAME):
    return test_client.post(
        url_for(url),
        headers={"Authorization": f"Bearer {access_token}"},
        data=f"name={name}",
        content_type="application/x-www-form-urlencoded",
    )


def retrieve_list(test_client, access_token, url, page=None, per_page=None):
    return test_client.get(
        url_for(url, page=page, per_page=per_page),
        headers={"Authorization": f"Bearer {access_token}"},
    )


def retrieve(test_client, access_token, url, widget_id):
    return test_client.get(
        url_for(url, widget_id=widget_id),
        headers={"Authorization": f"Bearer {access_token}"},
    )


def update(test_client, access_token, url, widget_id, name):
    return test_client.put(
        url_for(url, widget_id=widget_id),
        headers={"Authorization": f"Bearer {access_token}"},
        data=f"name={name}",
        content_type="application/x-www-form-urlencoded",
    )


def delete(test_client, access_token, url, widget_id):
    return test_client.delete(
        url_for(url, widget_id=widget_id),
        headers={"Authorization": f"Bearer {access_token}"},
    )


class TestWidget:
    """Class for test cases by simple widgets"""

    # Prevent pytest from trying to collect webtest's TestWidget as tests:
    __test__ = False

    def __init__(self, url, url_list, name):
        self.url = url
        self.url_list = url_list
        self.name = name

    def __str__(self):
        """Informal string representation of a widget."""
        return self.name

    def __repr__(self):
        """Official string representation of a widget."""
        return f"<Widget name={self.name} >"

    def create_valid_name(self, client, widget_name):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(client, access_token, url=self.url_list, name=widget_name)
        assert response.status_code == HTTPStatus.CREATED
        assert "status" in response.json and response.json["status"] == "success"
        success = f"New {self.name} added: {widget_name}."
        assert "message" in response.json and response.json["message"] == success
        assert "widget_id" in response.json and response.json["widget_id"]
        role_id = response.json["widget_id"]
        location = url_for(self.url, widget_id=role_id)
        assert (
            "Location" in response.headers and response.headers["Location"] == location
        )

    def create_no_admin_token(self, client):
        response = login_user(client, login=LOGIN)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(client, access_token, url=self.url_list)
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert "message" in response.json and response.json["message"] == FORBIDDEN

    def delete(self, client):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(client, access_token, url=self.url_list)
        assert response.status_code == HTTPStatus.CREATED
        assert "widget_id" in response.json
        widget_id = response.json["widget_id"]
        assert widget_id
        response = delete(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.NO_CONTENT
        response = retrieve(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.NOT_FOUND

        # delete not found role
        from api_server_flask.api.models.util import create_id

        widget_id = create_id()
        response = delete(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.NOT_FOUND

    def delete_no_admin_token(self, client):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(client, access_token, url=self.url_list)
        assert response.status_code == HTTPStatus.CREATED
        assert "widget_id" in response.json
        widget_id = response.json["widget_id"]
        assert widget_id

        response = login_user(client, login=LOGIN)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = delete(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert "message" in response.json and response.json["message"] == FORBIDDEN

    def retrieve_widget_non_admin_user(self, client):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(client, access_token, url=self.url_list)
        assert response.status_code == HTTPStatus.CREATED
        widget_id = response.json["widget_id"]
        assert widget_id

        response = login_user(client, login=LOGIN)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = retrieve(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.OK

        assert "name" in response.json and response.json["name"] == DEFAULT_NAME

    def retrieve_widget_does_not_exist(self, client):
        response = login_user(client, login=LOGIN)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        from api_server_flask.api.models.util import create_id

        not_exist_role_id = create_id()
        response = retrieve(
            client, access_token, url=self.url, widget_id=not_exist_role_id
        )
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert (
            "message" in response.json
            and f"{not_exist_role_id} not found in database" in response.json["message"]
        )

    def update_role(self, client):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(client, access_token, url=self.url_list)
        assert response.status_code == HTTPStatus.CREATED
        widget_id = response.json["widget_id"]
        assert widget_id

        response = update(
            client,
            access_token,
            url=self.url,
            widget_id=widget_id,
            name=UPDATED_DEFAULT_NAME,
        )
        assert response.status_code == HTTPStatus.OK
        assert "message" in response.json
        assert response.json["message"] == f"'{widget_id}' was successfully updated"
        response = retrieve(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.OK

        assert "name" in response.json and response.json["name"] == UPDATED_DEFAULT_NAME

    def update_role_not_admin(self, client):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(client, access_token, url=self.url_list)
        assert response.status_code == HTTPStatus.CREATED
        assert "widget_id" in response.json
        widget_id = response.json["widget_id"]
        assert widget_id

        response = login_user(client, login=LOGIN)
        assert "access_token" in response.json
        access_token_user = response.json["access_token"]
        response = update(
            client,
            access_token_user,
            url=self.url,
            widget_id=widget_id,
            name=UPDATED_DEFAULT_NAME,
        )
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert "message" in response.json and response.json["message"] == FORBIDDEN

    def update_role_not_exist(self, client):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        from api_server_flask.api.models.util import create_id

        widget_id = create_id()

        response = update(
            client,
            access_token,
            url=self.url,
            widget_id=widget_id,
            name=UPDATED_DEFAULT_NAME,
        )
        assert response.status_code == HTTPStatus.CREATED
        assert "status" in response.json and response.json["status"] == "success"
        success = f"New {self.name} added: {UPDATED_DEFAULT_NAME}."
        assert "message" in response.json and response.json["message"] == success
        assert "widget_id" in response.json
        widget_id = response.json["widget_id"]
        response = retrieve(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.OK

        assert "name" in response.json and response.json["name"] == UPDATED_DEFAULT_NAME
