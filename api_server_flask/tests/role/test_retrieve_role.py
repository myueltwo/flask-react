"""Test cases for GET request sent to api.role API endpoint"""
from api_server_flask.tests.widget.util import TestWidget

role_widget = TestWidget(url="api.role", url_list="api.role_list", name="role")


def test_retrieve_widget_non_admin_user(client, db, admin, user):
    role_widget.retrieve_widget_non_admin_user(client)


def test_retrieve_widget_does_not_exist(client, db, user):
    role_widget.retrieve_widget_does_not_exist(client)
