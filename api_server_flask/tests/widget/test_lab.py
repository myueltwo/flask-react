"""Unit test for requests sent to api.lab and api.lab_list API endpoint"""

import pytest
from datetime import datetime
from api_server_flask.tests.widget.util import (
    Widget,
    DEFAULT_NAME,
    NAMES,
    UPDATED_DEFAULT_NAME,
)
from api_server_flask.api.models.subject import Subject


class TestWidget(Widget):
    url = "api.lab"
    url_list = "api.lab_list"
    name = "lab"

    @pytest.fixture
    def widget_dict(self, db):
        subject = Subject(name=DEFAULT_NAME, count_hours=5)
        db.session.add(subject)
        db.session.commit()
        return {
            "subject_id": subject.id,
            "name": DEFAULT_NAME,
            "datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "deadline": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
        }

    @pytest.fixture
    def widget_dict_updated(self, db):
        subject = Subject(name=UPDATED_DEFAULT_NAME, count_hours=6)
        db.session.add(subject)
        db.session.commit()
        return {
            "subject_id": subject.id,
            "name": UPDATED_DEFAULT_NAME,
            "datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
            "deadline": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
        }

    @pytest.fixture
    def widget_dict_list(self, db):
        subjects = []
        for i in NAMES:
            subjects.append(
                Subject(
                    name=i,
                    count_hours=5,
                )
            )
        db.session.add_all(subjects)
        db.session.commit()
        return [
            {
                "subject_id": v.id,
                "name": NAMES[i],
                "datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "deadline": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
            }
            for i, (v) in enumerate(subjects)
        ]

    @pytest.fixture
    def widget_dict_create(self, db):
        subjects = []
        for i in ["first subject", "second subj", "test_subj"]:
            subjects.append(
                Subject(
                    name=i,
                    count_hours=5,
                )
            )
        db.session.add_all(subjects)
        db.session.commit()
        return [
            {
                "subject_id": v.id,
                "name": DEFAULT_NAME,
                "datetime": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "deadline": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
            }
            for i, (v) in enumerate(subjects)
        ]

    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        for i in widget_dict_create:
            super().test_create_valid_name(client, db, admin, widget_dict_create=i)
