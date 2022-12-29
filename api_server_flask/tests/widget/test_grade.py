"""Unit test for requests sent to api.grade and api.grade_list API endpoint"""

import pytest
from api_server_flask.tests.widget.util import (
    Widget,
    DEFAULT_NAME,
    NAMES,
    UPDATED_DEFAULT_NAME,
)
from api_server_flask.api.models.subject import Subject
from api_server_flask.api.models.type_grade import TypeGrade


class TestWidget(Widget):
    url = "api.grade"
    url_list = "api.grade_list"
    name = "grade"

    @pytest.fixture
    def type_grades(self, db):
        type_grades = []
        for i in ["exam", "offset"]:
            type_grades.append(TypeGrade(name=i))
        db.session.add_all(type_grades)
        db.session.commit()
        return type_grades

    @pytest.fixture
    def widget_dict(self, db, type_grades):
        subject = Subject(name=DEFAULT_NAME, count_hours=5)
        db.session.add(subject)
        db.session.commit()
        return {
            "subject_id": subject.id,
            "type_id": type_grades[0].id,
        }

    @pytest.fixture
    def widget_dict_updated(self, db, type_grades):
        subject = Subject(name=UPDATED_DEFAULT_NAME, count_hours=6)
        db.session.add(subject)
        db.session.commit()
        return {
            "subject_id": subject.id,
            "type_id": type_grades[1].id,
        }

    @pytest.fixture
    def widget_dict_list(self, db, type_grades):
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
                "type_id": type_grades[0].id if i < 2 else type_grades[1].id,
            }
            for i, (v) in enumerate(subjects)
        ]

    @pytest.fixture
    def widget_dict_create(self, db, type_grades):
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
                "type_id": type_grades[0].id if i < 2 else type_grades[1].id,
            }
            for i, (v) in enumerate(subjects)
        ]

    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        for i in widget_dict_create:
            super().test_create_valid_name(client, db, admin, widget_dict_create=i)
