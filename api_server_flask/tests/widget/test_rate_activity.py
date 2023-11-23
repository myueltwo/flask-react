"""Unit test for requests sent to api.rate_activity and api.rate_activity_list
API endpoint"""

import pytest
from api_server_flask.tests.widget.util import (
    Widget,
    DEFAULT_NAME,
    NAMES,
)
from api_server_flask.api.models.rate_activity import RateActivity
from api_server_flask.api.models.activity_type import ActivityType
from api_server_flask.api.models.activity_sub_type import ActivitySubType


def add_context(db, types_names):
    types = []
    for i in types_names:
        types.append(
            ActivityType(
                name=i,
            )
        )
    db.session.add_all(types)
    db.session.commit()
    subtype = ActivitySubType(name=DEFAULT_NAME)
    db.session.add(subtype)
    db.session.commit()
    return [
        {"activity_type_id": v.id, "activity_sub_type_id": subtype.id, "value": 1 if i < 2 else 2}
        for i, (v) in enumerate(types)
    ]


class TestWidget(Widget):
    url = "api.rate_activity"
    url_list = "api.rate_activity_list"
    name = "rate_activity"

    @pytest.fixture
    def widget_dict(self, db):
        return add_context(db, types_names=[DEFAULT_NAME])[0]

    @pytest.fixture
    def widget_dict_updated(self, db):
        data = add_context(db, types_names=[DEFAULT_NAME])[0]
        data["value"] = 3
        return data

    @pytest.fixture
    def widget_dict_list(self, db):
        return add_context(db, NAMES)

    @pytest.fixture
    def widget_dict_create(self, db):
        return add_context(
            db, ["first subject", "second subj", "test_subj"]
        )

    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        for i in widget_dict_create:
            super().test_create_valid_name(client, db, admin, widget_dict_create=i)
