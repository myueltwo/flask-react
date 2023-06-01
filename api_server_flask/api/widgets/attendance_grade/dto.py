from api_server_flask.util.widget.dto import (
    PaginationSchema,
)
from api_server_flask.util.covert_model import get_model_from_schema
from api_server_flask.api.widgets.attendance.dto import AttendanceSchema
from api_server_flask.api.auth.dto import UserSchema
from marshmallow import fields, Schema


class AttendanceGradeSchema(Schema):
    attendance_id = fields.Str(required=True)
    attendance = fields.Nested(AttendanceSchema, dump_only=True)
    user_id = fields.Str(required=True)
    user = fields.Nested(UserSchema, dump_only=True)
    active = fields.Int(required=False, default=0)


class PaginationAttendanceGradeSchema(PaginationSchema):
    items = fields.List(fields.Nested(AttendanceGradeSchema))


attendance_grade_model = get_model_from_schema(AttendanceGradeSchema, "AttendanceGradeSchema")
pagination_attendance_grade_model = get_model_from_schema(
    PaginationAttendanceGradeSchema, "PaginationAttendanceGradeSchema"
)
