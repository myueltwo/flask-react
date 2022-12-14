from flask import url_for
from http import HTTPStatus
from api_server_flask.tests.util import (
    LOGIN,
    ADMIN_LOGIN,
    ADMIN_PASSWORD,
    FORBIDDEN,
    login_user,
)
import pytest

DEFAULT_NAME = "some name"
UPDATED_DEFAULT_NAME = "update some name2"

NAMES = [
    "widget1",
    "second_widget",
    "widget-thrice",
    "tetraWIDGET",
    "PENTA-widget-GON-et",
    "hexa_widget",
]


def create(test_client, access_token, url, widget_dict):
    return test_client.post(
        url_for(url),
        headers={"Authorization": f"Bearer {access_token}"},
        data="&".join([f"{k}={v}" for k, v in widget_dict.items()]),
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


def update(test_client, access_token, url, widget_id, widget_dict):
    return test_client.put(
        url_for(url, widget_id=widget_id),
        headers={"Authorization": f"Bearer {access_token}"},
        data="&".join([f"{k}={v}" for k, v in widget_dict.items()]),
        content_type="application/x-www-form-urlencoded",
    )


def delete(test_client, access_token, url, widget_id):
    return test_client.delete(
        url_for(url, widget_id=widget_id),
        headers={"Authorization": f"Bearer {access_token}"},
    )


class Widget:
    """Class for test cases by simple widgets"""

    url = None
    url_list = None
    name = None
    default_names = []

    @pytest.fixture
    def widget_dict(self):
        return {"name": DEFAULT_NAME}

    @pytest.fixture
    def widget_dict_updated(self):
        return {
            "name": UPDATED_DEFAULT_NAME,
        }

    @pytest.fixture
    def widget_dict_list(self):
        dict_list = []
        for i in NAMES:
            dict_list.append({"name": i})
        return dict_list

    def __str__(self):
        """Informal string representation of a widget."""
        return self.name

    def __repr__(self):
        """Official string representation of a widget."""
        return f"<Widget name={self.name}>"

    @pytest.mark.parametrize(
        "widget_dict_create",
        [{"name": "abc123"}, {"name": "widget-name"}, {"name": "new_widget1"}],
    )
    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(
            client, access_token, url=self.url_list, widget_dict=widget_dict_create
        )
        assert response.status_code == HTTPStatus.CREATED
        assert "widget_id" in response.json and response.json["widget_id"]
        widget_id = response.json["widget_id"]
        assert "status" in response.json and response.json["status"] == "success"
        success = f"New {self.name} added: {widget_id}."
        assert "message" in response.json and response.json["message"] == success

        location = url_for(self.url, widget_id=widget_id)
        assert (
            "Location" in response.headers and response.headers["Location"] == location
        )

    def test_create_no_admin_token(self, client, db, user, widget_dict):
        response = login_user(client, login=LOGIN)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(
            client, access_token, url=self.url_list, widget_dict=widget_dict
        )
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert "message" in response.json and response.json["message"] == FORBIDDEN

    def test_delete(self, client, db, admin, widget_dict):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(
            client, access_token, url=self.url_list, widget_dict=widget_dict
        )
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

    def test_delete_no_admin_token(self, client, db, admin, user, widget_dict):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(
            client, access_token, url=self.url_list, widget_dict=widget_dict
        )
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

    def test_retrieve_non_admin_user(self, client, db, admin, user, widget_dict):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(
            client, access_token, url=self.url_list, widget_dict=widget_dict
        )
        assert response.status_code == HTTPStatus.CREATED
        widget_id = response.json["widget_id"]
        assert widget_id

        response = login_user(client, login=LOGIN)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = retrieve(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.OK

        for k, v in widget_dict.items():
            assert k in response.json and response.json[k] == v

    def test_retrieve_does_not_exist(self, client, db, user):
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

    def test_update(self, client, db, admin, widget_dict, widget_dict_updated):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(
            client, access_token, url=self.url_list, widget_dict=widget_dict
        )
        assert response.status_code == HTTPStatus.CREATED
        widget_id = response.json["widget_id"]
        assert widget_id

        response = update(
            client,
            access_token,
            url=self.url,
            widget_id=widget_id,
            widget_dict=widget_dict_updated,
        )
        assert response.status_code == HTTPStatus.OK
        assert "message" in response.json
        assert response.json["message"] == f"'{widget_id}' was successfully updated"
        response = retrieve(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.OK

        for k, v in widget_dict_updated.items():
            assert k in response.json and response.json[k] == v

    def test_update_not_admin(
        self, client, db, admin, user, widget_dict, widget_dict_updated
    ):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]
        response = create(
            client, access_token, url=self.url_list, widget_dict=widget_dict
        )
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
            widget_dict=widget_dict_updated,
        )
        assert response.status_code == HTTPStatus.FORBIDDEN
        assert "message" in response.json and response.json["message"] == FORBIDDEN

    def test_update_not_exist(self, client, db, admin, widget_dict_updated):
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
            widget_dict=widget_dict_updated,
        )
        assert response.status_code == HTTPStatus.CREATED
        assert "status" in response.json and response.json["status"] == "success"
        assert "widget_id" in response.json
        widget_id = response.json["widget_id"]
        success = f"New {self.name} added: {widget_id}."
        assert "message" in response.json and response.json["message"] == success

        response = retrieve(client, access_token, url=self.url, widget_id=widget_id)
        assert response.status_code == HTTPStatus.OK

        for k, v in widget_dict_updated.items():
            assert k in response.json and response.json[k] == v

    def test_retrieve_paginated_list(self, client, db, admin, widget_dict_list):
        response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
        assert "access_token" in response.json
        access_token = response.json["access_token"]

        # Maximum of default_names can be 3
        assert len(self.default_names) <= 3

        # ADD SIX ROLE INSTANCES TO DATABASE
        for i in range(0, len(widget_dict_list)):
            response = create(
                client,
                access_token,
                url=self.url_list,
                widget_dict=widget_dict_list[i],
            )
            assert response.status_code == HTTPStatus.CREATED

        names_with_default = self.default_names.copy()
        names_with_default.extend(widget_dict_list)
        total_count_roles = len(names_with_default)

        # REQUEST PAGINATED LIST OF ROLES: 5 PER PAGE, PAGE #1
        response = retrieve_list(
            client, access_token, url=self.url_list, page=1, per_page=5
        )
        assert response.status_code == HTTPStatus.OK

        # VERIFY PAGINATION ATTRIBUTES FOR PAGE #1
        assert "has_prev" in response.json and not response.json["has_prev"]
        assert "has_next" in response.json and response.json["has_next"]
        assert "page" in response.json and response.json["page"] == 1
        assert "total_pages" in response.json and response.json["total_pages"] == 2
        assert "items_per_page" in response.json and response.json["items_per_page"] == 5
        assert (
            "total_items" in response.json
            and response.json["total_items"] == total_count_roles
        )
        assert "items" in response.json and len(response.json["items"]) == 5

        # VERIFY ATTRIBUTES OF ROLES #1-5
        for i in range(0, len(response.json["items"])):
            item = response.json["items"][i]
            for k, v in names_with_default[i].items():
                assert k in item and item[k] == v

        # REQUEST PAGINATED LIST OF WIDGETS: 5 PER PAGE, PAGE #2
        response = retrieve_list(
            client, access_token, url=self.url_list, page=2, per_page=5
        )
        assert response.status_code == HTTPStatus.OK

        # VERIFY PAGINATION ATTRIBUTES FOR PAGE #2
        assert "has_prev" in response.json and response.json["has_prev"]
        assert "has_next" in response.json and not response.json["has_next"]
        assert "page" in response.json and response.json["page"] == 2
        assert "total_pages" in response.json and response.json["total_pages"] == 2
        assert "items_per_page" in response.json and response.json["items_per_page"] == 5
        assert (
            "total_items" in response.json
            and response.json["total_items"] == total_count_roles
        )
        assert (
            "items" in response.json
            and len(response.json["items"]) == total_count_roles - 5
        )

        # VERIFY ATTRIBUTES OF ROLES #6-9
        for i in range(5, response.json["total_items"]):
            item = response.json["items"][i - 5]
            for k, v in names_with_default[i].items():
                assert k in item and item[k] == v

        # REQUEST PAGINATED LIST OF WIDGETS: 10 PER PAGE, PAGE #1
        response = retrieve_list(
            client, access_token, url=self.url_list, page=1, per_page=10
        )
        assert response.status_code == HTTPStatus.OK

        # VERIFY PAGINATION ATTRIBUTES FOR PAGE #1
        assert "has_prev" in response.json and not response.json["has_prev"]
        assert "has_next" in response.json and not response.json["has_next"]
        assert "page" in response.json and response.json["page"] == 1
        assert "total_pages" in response.json and response.json["total_pages"] == 1
        assert (
            "items_per_page" in response.json and response.json["items_per_page"] == 10
        )
        assert (
            "total_items" in response.json
            and response.json["total_items"] == total_count_roles
        )
        assert (
            "items" in response.json and len(response.json["items"]) == total_count_roles
        )

        # VERIFY ATTRIBUTES OF ROLES #1-9
        for i in range(0, len(response.json["items"])):
            item = response.json["items"][i]
            for k, v in names_with_default[i].items():
                assert k in item and item[k] == v

        # REQUEST PAGINATED LIST OF ROLES: DEFAULT PARAMETERS
        response = retrieve_list(client, access_token, url=self.url_list)
        assert response.status_code == HTTPStatus.OK

        # VERIFY PAGINATION ATTRIBUTES FOR PAGE #1
        assert "has_prev" in response.json and not response.json["has_prev"]
        assert "has_next" in response.json and not response.json["has_next"]
        assert "page" in response.json and response.json["page"] == 1
        assert "total_pages" in response.json and response.json["total_pages"] == 1
        assert (
            "items_per_page" in response.json and response.json["items_per_page"] == 10
        )
        assert (
            "total_items" in response.json
            and response.json["total_items"] == total_count_roles
        )
        assert (
            "items" in response.json and len(response.json["items"]) == total_count_roles
        )

        # VERIFY ATTRIBUTES OF WIDGETS #1-9
        for i in range(0, len(response.json["items"])):
            item = response.json["items"][i]
            for k, v in names_with_default[i].items():
                assert k in item and item[k] == v
