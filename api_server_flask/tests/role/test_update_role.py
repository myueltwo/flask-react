"""Test cases for PUT requests sent to the api.role API endpoint"""
from api_server_flask.tests.widget.util import TestWidget

role_widget = TestWidget(url="api.role", url_list="api.role_list", name="role")


def test_update_role(client, db, admin):
    role_widget.update_role(client)


def test_update_role_not_admin(client, db, admin, user):
    role_widget.update_role_not_admin(client)


def test_update_role_not_exist(client, db, admin):
    role_widget.update_role_not_exist(client)
