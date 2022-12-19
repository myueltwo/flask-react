"""Unit test for POST request sent to api.subject_list API endoint"""

import pytest
from api_server_flask.tests.widget.util import TestWidget, DEFAULT_NAME, NAMES


widget = TestWidget(
    url="api.subject",
    url_list="api.subject_list",
    name="subject",
    widget_dict={"name": DEFAULT_NAME, "count_hours": 5},
    widget_dict_list=[{"name": v, "count_hours": i} for i, (v) in enumerate(NAMES)],
)


@pytest.mark.parametrize(
    "name,count_hours", [("abc123", 5), ("subject-name", 6), ("new_subject1", 10)]
)
def test_create_subject_valid_name(client, db, admin, name, count_hours):
    widget.create_valid_name(
        client=client, widget_dict={"name": name, "count_hours": count_hours}
    )


def test_create_subject_no_admin_token(client, db, user):
    widget.create_no_admin_token(client=client)


def test_retrieve_paginated_subject_list(client, db, admin):
    widget.retrieve_paginated_list(client)
