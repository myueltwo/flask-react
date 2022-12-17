# """Test cases for DELETE requests sent to the api.subject API endpoint """
# from api_server_flask.tests.widget.util import TestWidget
#
# widget = TestWidget(url="api.subject", url_list="api.subject_list", name="subject")
#
#
# def test_update_subject(client, db, admin):
#     widget.update(client)
#
#
# def test_update_subject_not_admin(client, db, admin, user):
#     widget.update_not_admin(client)
#
#
# def test_update_subject_not_exist(client, db, admin):
#     widget.update_not_exist(client)
#
#
# def test_retrieve_subject_non_admin_user(client, db, admin, user):
#     widget.retrieve_non_admin_user(client)
#
#
# def test_retrieve_subject_does_not_exist(client, db, user):
#     widget.retrieve_does_not_exist(client)
#
#
# def test_delete_subject(client, db, admin):
#     widget.delete(client)
#
#
# def test_delete_subject_no_admin_token(client, db, admin, user):
#     widget.delete_no_admin_token(client)
