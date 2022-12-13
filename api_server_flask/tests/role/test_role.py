"""Test cases for DELETE requests sent to the api.role API endpoint """
from api_server_flask.tests.widget.util import TestWidget

role_widget = TestWidget(url="api.role", url_list="api.role_list", name="role")


def test_update_role(client, db, admin):
    role_widget.update(client)


def test_update_role_not_admin(client, db, admin, user):
    role_widget.update_not_admin(client)


def test_update_role_not_exist(client, db, admin):
    role_widget.update_not_exist(client)


def test_retrieve_role_non_admin_user(client, db, admin, user):
    role_widget.retrieve_non_admin_user(client)


def test_retrieve_role_does_not_exist(client, db, user):
    role_widget.retrieve_does_not_exist(client)


def test_delete_role(client, db, admin):
    role_widget.delete(client)


def test_delete_role_no_admin_token(client, db, admin, user):
    role_widget.delete_no_admin_token(client)
