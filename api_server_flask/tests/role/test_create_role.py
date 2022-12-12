"""Unit test for POST request sent to api.role_list API endoint"""

import pytest
from api_server_flask.tests.widget.util import TestWidget

role_widget = TestWidget(url="api.role", url_list="api.role_list", name="role")


@pytest.mark.parametrize("role_name", ["abc123", "role-name", "new_role1"])
def test_create_role_valid_name(client, db, admin, role_name):
    role_widget.create_valid_name(client=client, widget_name=role_name)


def test_create_role_no_admin_token(client, db, user):
    role_widget.create_no_admin_token(client=client)
