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
