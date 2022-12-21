"""Unit test for requests sent to api.subject and api.subject_list API endpoint"""

import pytest
from api_server_flask.tests.widget.util import (
    Widget,
    DEFAULT_NAME,
    NAMES,
    UPDATED_DEFAULT_NAME,
)


class TestWidget(Widget):
    url = "api.subject"
    url_list = "api.subject_list"
    name = "subject"
    widget_dict = {"name": DEFAULT_NAME, "count_hours": 5}
    widget_dict_list = [{"name": v, "count_hours": i} for i, (v) in enumerate(NAMES)]
    widget_dict_updated = {"name": UPDATED_DEFAULT_NAME, "count_hours": 6}

    @pytest.mark.parametrize(
        "widget_dict_create",
        [
            {"name": "abc123", "count_hours": 5},
            {"name": "subject-name", "count_hours": 6},
            {"name": "new_subject1", "count_hours": 10},
        ],
    )
    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        super().test_create_valid_name(client, db, admin, widget_dict_create)
