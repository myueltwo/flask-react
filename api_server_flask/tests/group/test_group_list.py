"""Unit test for POST request sent to api.group_list API endoint"""

import pytest
from api_server_flask.tests.widget.util import TestWidget

widget = TestWidget(url="api.group", url_list="api.group_list", name="group")


@pytest.mark.parametrize("name", ["abc123", "group-name", "new_group1"])
def test_create_group_valid_name(client, db, admin, name):
    widget.create_valid_name(client=client, widget_dict={"name": name})


def test_create_group_no_admin_token(client, db, user):
    widget.create_no_admin_token(client=client)


def test_retrieve_paginated_group_list(client, db, admin):
    widget.retrieve_paginated_list(client)
