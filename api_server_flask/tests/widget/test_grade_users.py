"""Unit test for requests sent to api.grade_users and api.grade_users_list
API endpoint"""

import pytest
from api_server_flask.tests.widget.util import (
    Widget,
    DEFAULT_NAME,
    NAMES,
)
from api_server_flask.api.models.subject import Subject
from api_server_flask.api.models.type_grade import TypeGrade
from api_server_flask.api.models.grade import Grade


def add_grades(db, type_grades, user, subjects_names):
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
    grades = []
    for i in subjects:
        grades.append(
            Grade(
                subject_id=i.id,
                type_id=type_grades[0].id,
            )
        )
    db.session.add_all(grades)
    db.session.commit()
    return [
        {"grade_id": v.id, "user_id": user.id, "value": 4 if i < 2 else 3}
        for i, (v) in enumerate(grades)
    ]


class TestWidget(Widget):
    url = "api.grade_users"
    url_list = "api.grade_users_list"
    name = "grade_users"

    @pytest.fixture
    def type_grades(self, db):
        type_grades = []
        for i in ["exam", "offset"]:
            type_grades.append(TypeGrade(name=i))
        db.session.add_all(type_grades)
        db.session.commit()
        return type_grades

    @pytest.fixture
    def grade(self, db, type_grades):
        subject = Subject(name=DEFAULT_NAME, count_hours=5)
        db.session.add(subject)
        db.session.commit()
        grade = Grade(
            subject_id=subject.id,
            type_id=type_grades[0].id,
        )
        db.session.add(grade)
        db.session.commit()
        return grade

    @pytest.fixture
    def widget_dict(self, db, grade, user):
        return {"grade_id": grade.id, "user_id": user.id, "value": 4}

    @pytest.fixture
    def widget_dict_updated(self, db, grade, user):
        return {"grade_id": grade.id, "user_id": user.id, "value": 5}

    @pytest.fixture
    def widget_dict_list(self, db, type_grades, user):
        return add_grades(db, type_grades, user, NAMES)

    @pytest.fixture
    def widget_dict_create(self, db, type_grades, user):
        return add_grades(
            db, type_grades, user, ["first subject", "second subj", "test_subj"]
        )

    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        for i in widget_dict_create:
            super().test_create_valid_name(client, db, admin, widget_dict_create=i)
