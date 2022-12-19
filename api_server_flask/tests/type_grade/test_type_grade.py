"""Test cases for DELETE requests sent to the api.type_grade API endpoint """
from api_server_flask.tests.widget.util import TestWidget

widget = TestWidget(
    url="api.type_grade", url_list="api.type_grade_list", name="type's grade"
)


def test_update_type_grade(client, db, admin):
    widget.update(client)


def test_update_type_grade_not_admin(client, db, admin, user):
    widget.update_not_admin(client)


def test_update_type_grade_not_exist(client, db, admin):
    widget.update_not_exist(client)


def test_retrieve_type_grade_non_admin_user(client, db, admin, user):
    widget.retrieve_non_admin_user(client)


def test_retrieve_type_grade_does_not_exist(client, db, user):
    widget.retrieve_does_not_exist(client)


def test_delete_type_grade(client, db, admin):
    widget.delete(client)


def test_delete_type_grade_no_admin_token(client, db, admin, user):
    widget.delete_no_admin_token(client)
