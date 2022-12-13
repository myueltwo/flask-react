"""Test cases for DELETE requests sent to the api.group API endpoint """
from api_server_flask.tests.widget.util import TestWidget

widget = TestWidget(url="api.group", url_list="api.group_list", name="group")


def test_update_group(client, db, admin):
    widget.update(client)


def test_update_group_not_admin(client, db, admin, user):
    widget.update_not_admin(client)


def test_update_group_not_exist(client, db, admin):
    widget.update_not_exist(client)


def test_retrieve_group_non_admin_user(client, db, admin, user):
    widget.retrieve_non_admin_user(client)


def test_retrieve_group_does_not_exist(client, db, user):
    widget.retrieve_does_not_exist(client)


def test_delete_group(client, db, admin):
    widget.delete(client)


def test_delete_group_no_admin_token(client, db, admin, user):
    widget.delete_no_admin_token(client)
