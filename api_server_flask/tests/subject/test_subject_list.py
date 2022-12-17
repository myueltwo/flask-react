# """Unit test for POST request sent to api.subject_list API endoint"""
#
# import pytest
# from api_server_flask.tests.widget.util import TestWidget
#
#
# widget = TestWidget(url="api.subject", url_list="api.subject_list", name="subject")
#
#
# @pytest.mark.parametrize("name", ["abc123", "subject-name", "new_subject1"])
# def test_create_subject_valid_name(client, db, admin, name):
#     widget.create_valid_name(client=client, widget_name=name)
#
#
# def test_create_subject_no_admin_token(client, db, user):
#     widget.create_no_admin_token(client=client)
#
#
# def test_retrieve_paginated_subject_list(client, db, admin):
#     widget.retrieve_paginated_list(client)
