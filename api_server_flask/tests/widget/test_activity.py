"""Unit test for requests sent to api.activity and api.activity_list
API endpoint"""

import pytest
from api_server_flask.tests.widget.util import (
    Widget,
    DEFAULT_NAME,
    NAMES,
)
from api_server_flask.api.models.activity_type import ActivityType
from api_server_flask.api.models.rate_activity import RateActivity
from api_server_flask.api.models.activity_sub_type import ActivitySubType


def add_context(db, user, types_names):
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
    rates = [
        RateActivity(
            activity_type_id=v.id,
            activity_sub_type_id=subtype.id,
            value=1 if i < 2 else 2,
        )
        for i, (v) in enumerate(types)
    ]
    db.session.add_all(rates)
    db.session.commit()
    return [
        {
            "name": DEFAULT_NAME,
            "type_id": v.activity_type_id,
            "user_id": user.id,
            "file": DEFAULT_NAME,
            "status": False,
            "comment": DEFAULT_NAME,
            "rate_id": v.id,
        }
        for i, (v) in enumerate(rates)
    ]


class TestWidget(Widget):
    url = "api.activity"
    url_list = "api.activity_list"
    name = "activity"

    @pytest.fixture
    def widget_dict(self, db, user):
        return add_context(db,  user, [DEFAULT_NAME])[0]

    @pytest.fixture
    def widget_dict_updated(self, db, user):
        data = add_context(db, user, [DEFAULT_NAME])[0]
        data["status"] = True
        return data

    @pytest.fixture
    def widget_dict_list(self, db,  user):
        return add_context(db, user, NAMES)

    @pytest.fixture
    def widget_dict_create(self, db, user):
        return add_context(
            db, user, ["first subject", "second subj", "test_subj"]
        )

    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        for i in widget_dict_create:
            super().test_create_valid_name(client, db, admin, widget_dict_create=i)
