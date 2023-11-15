from api_server_flask.util.widget.dto import (
    PaginationSchema,
)
from api_server_flask.util.covert_model import get_model_from_schema
from api_server_flask.api.widgets.grades.dto import GradeSubjectSchema
from marshmallow import fields, Schema


class AttendanceTypeSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)


class GroupSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)


class AttendanceSchema(Schema):
    subject_id = fields.Str(required=True)
    subject = fields.Nested(GradeSubjectSchema, dump_only=True)
    type_id = fields.Str(required=True)
    type = fields.Nested(AttendanceTypeSchema, dump_only=True)
    group_id = fields.Str(required=True)
    group = fields.Nested(GroupSchema, dump_only=True)
    date = fields.DateTime(required=False)


class PaginationAttendanceSchema(PaginationSchema):
    items = fields.List(fields.Nested(AttendanceSchema))


attendance_group_model = get_model_from_schema(GroupSchema, "GroupSchema")
attendance_type_model = get_model_from_schema(
    AttendanceTypeSchema, "AttendanceTypeSchema"
)
attendance_model = get_model_from_schema(AttendanceSchema, "AttendanceSchema")
pagination_attendance_model = get_model_from_schema(
    PaginationAttendanceSchema, "PaginationAttendanceSchema"
)
