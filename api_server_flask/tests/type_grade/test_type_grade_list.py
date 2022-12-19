"""Unit test for POST request sent to api.type_grade_list API endoint"""

import pytest
from api_server_flask.tests.widget.util import TestWidget

widget = TestWidget(
    url="api.type_grade", url_list="api.type_grade_list", name="type's grade"
)


@pytest.mark.parametrize("name", ["abc123", "type_grade-name", "new_type_grade1"])
def test_create_type_grade_valid_name(client, db, admin, name):
    widget.create_valid_name(client=client, widget_dict={"name": name})


def test_create_type_grade_no_admin_token(client, db, user):
    widget.create_no_admin_token(client=client)


def test_retrieve_paginated_type_grade_list(client, db, admin):
    widget.retrieve_paginated_list(client)
