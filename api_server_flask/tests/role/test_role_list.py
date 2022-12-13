"""Unit test for POST request sent to api.role_list API endoint"""

import pytest
from api_server_flask.tests.widget.util import TestWidget
from api_server_flask.tests.util import (
    STUDENT_ROLE_NAME,
    TUTOR_ROLE_NAME,
    ADMIN_ROLE_NAME,
)

widget = TestWidget(url="api.role", url_list="api.role_list", name="role")


@pytest.mark.parametrize("name", ["abc123", "role-name", "new_role1"])
def test_create_role_valid_name(client, db, admin, name):
    widget.create_valid_name(client=client, widget_name=name)


def test_create_role_no_admin_token(client, db, user):
    widget.create_no_admin_token(client=client)


def test_retrieve_paginated_role_list(client, db, admin):
    widget.retrieve_paginated_list(
        client, default_names=[STUDENT_ROLE_NAME, TUTOR_ROLE_NAME, ADMIN_ROLE_NAME]
    )
