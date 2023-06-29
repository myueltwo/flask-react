"""Unit test for requests sent to api.attendance_grade and api.attendance_grade_list
API endpoint"""

import pytest
from api_server_flask.tests.widget.util import (
    Widget,
    DEFAULT_NAME,
    NAMES,
)
from api_server_flask.api.models.attendance_type import AttendanceType
from api_server_flask.api.models.group import Group
from api_server_flask.api.models.subject import Subject
from api_server_flask.api.models.attendance import Attendance


def add_context(db, type_attendance, user, subjects_names):
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
    group = Group(name=DEFAULT_NAME)
    db.session.add(group)
    db.session.commit()
    attendance = [
        Attendance(
            subject_id=v.id,
            group_id=group.id,
            type_id=type_attendance[0].id if i < 2 else type_attendance[1].id
        )
        for i, (v) in enumerate(subjects)
    ]
    db.session.add_all(attendance)
    db.session.commit()
    return [
        {"attendance_id": v.id, "user_id": user.id, "active": 1}
        for i, (v) in enumerate(attendance)
    ]


class TestWidget(Widget):
    url = "api.attendance_grade"
    url_list = "api.attendance_grade_list"
    name = "attendance_grade"

    @pytest.fixture
    def type_attendance(self, db):
        type_attendance = []
        for i in ["lecture", "practise"]:
            type_attendance.append(AttendanceType(name=i))
        db.session.add_all(type_attendance)
        db.session.commit()
        return type_attendance

    @pytest.fixture
    def widget_dict(self, db, type_attendance, user):
        return add_context(db, type_attendance, user, subjects_names=[DEFAULT_NAME])[0]

    @pytest.fixture
    def widget_dict_updated(self, db, type_attendance, user):
        data = add_context(db, type_attendance, user, subjects_names=[DEFAULT_NAME])[0]
        data["active"] = 2
        return data

    @pytest.fixture
    def widget_dict_list(self, db, type_attendance, user):
        return add_context(db, type_attendance, user, NAMES)

    @pytest.fixture
    def widget_dict_create(self, db, type_attendance, user):
        return add_context(db, type_attendance, user, ["first subject", "second subj", "test_subj"])

    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        for i in widget_dict_create:
            super().test_create_valid_name(client, db, admin, widget_dict_create=i)
