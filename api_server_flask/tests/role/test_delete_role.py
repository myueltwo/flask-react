"""Test cases for DELETE requests sent to the api.role API endpoint """
from api_server_flask.tests.widget.util import TestWidget

role_widget = TestWidget(url="api.role", url_list="api.role_list", name="role")


def test_delete_widget(client, db, admin):
    role_widget.delete(client)


def test_delete_widget_no_admin_token(client, db, admin, user):
    role_widget.delete_no_admin_token(client)
