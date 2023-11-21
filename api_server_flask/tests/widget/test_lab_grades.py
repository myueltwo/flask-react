"""Unit test for requests sent to api.labs_grade and api.labs_grade_list API endpoint"""

import pytest
from datetime import datetime
from api_server_flask.tests.widget.util import (
    Widget,
    DEFAULT_NAME,
    NAMES,
)
from api_server_flask.api.models.lab import Lab
from api_server_flask.api.models.subject import Subject


def add_context(db, user, subjects_names):
    subjects = []
    for i in subjects_names:
        subjects.append(
            Subject(
                name=i,
                count_hours=5,
            )
        )
    db.session.add_all(subjects)
    db.session.commit()
    labs = [
        Lab(
            subject_id=v.id,
            name=DEFAULT_NAME,
            datetime=datetime.now(),
            deadline=datetime.now(),
        )
        for i, (v) in enumerate(subjects)
    ]
    db.session.add_all(labs)
    db.session.commit()
    return [
        {"lab_id": v.id, "user_id": user.id, "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")}
        for i, (v) in enumerate(labs)
    ]


class TestWidget(Widget):
    url = "api.labs_grade"
    url_list = "api.labs_grade_list"
    name = "labs_grade"

    @pytest.fixture
    def widget_dict(self, db, user):
        return add_context(db, user, subjects_names=[DEFAULT_NAME])[0]

    @pytest.fixture
    def widget_dict_updated(self, db, user):
        data = add_context(db, user, subjects_names=[DEFAULT_NAME])[0]
        data["date"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        return data

    @pytest.fixture
    def widget_dict_list(self, db, user):
        return add_context(db, user, NAMES)

    @pytest.fixture
    def widget_dict_create(self, db, user):
        return add_context(
            db, user, ["first subject", "second subj", "test_subj"]
        )

    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        for i in widget_dict_create:
            super().test_create_valid_name(client, db, admin, widget_dict_create=i)
