"""Unit test for requests sent to api.attendance and api.attendance_list
API endpoint"""

import pytest
from api_server_flask.tests.widget.util import (
    Widget,
    DEFAULT_NAME,
    NAMES,
)
from datetime import datetime
from api_server_flask.api.models.attendance_type import AttendanceType
from api_server_flask.api.models.group import Group
from api_server_flask.api.models.subject import Subject


def add_context(db, type_attendance, group_name, subjects_names):
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
    group = Group(name=group_name)
    db.session.add(group)
    db.session.commit()
    return [
        {
            "subject_id": v.id,
            "group_id": group.id,
            "type_id": type_attendance[0].id if i < 2 else type_attendance[1].id,
        }
        for i, (v) in enumerate(subjects)
    ]


class TestWidget(Widget):
    url = "api.attendance"
    url_list = "api.attendance_list"
    name = "attendance"

    @pytest.fixture
    def type_attendance(self, db):
        type_attendance = []
        for i in ["lecture", "practise"]:
            type_attendance.append(AttendanceType(name=i))
        db.session.add_all(type_attendance)
        db.session.commit()
        return type_attendance

    @pytest.fixture
    def widget_dict(self, db, type_attendance):
        return add_context(
            db, type_attendance, group_name="424", subjects_names=DEFAULT_NAME
        )[0]

    @pytest.fixture
    def widget_dict_updated(self, db, type_attendance):
        data = add_context(
            db, type_attendance, group_name="424", subjects_names=DEFAULT_NAME
        )[0]
        data["date"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        return data

    @pytest.fixture
    def widget_dict_list(self, db, type_attendance):
        return add_context(db, type_attendance, group_name="424", subjects_names=NAMES)

    @pytest.fixture
    def widget_dict_create(self, db, type_attendance):
        return add_context(
            db, type_attendance, "424", ["first subject", "second subj", "test_subj"]
        )

    def test_create_valid_name(self, client, db, admin, widget_dict_create):
        for i in widget_dict_create:
            super().test_create_valid_name(client, db, admin, widget_dict_create=i)
