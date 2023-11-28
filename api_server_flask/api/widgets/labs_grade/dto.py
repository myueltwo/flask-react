from api_server_flask.util.widget.dto import (
    PaginationSchema,
)
from api_server_flask.util.covert_model import get_model_from_schema
from api_server_flask.api.widgets.labs.dto import LabSchema
from api_server_flask.api.auth.dto import UserSchema
from marshmallow import fields, Schema


class LabGradeSchema(Schema):
    lab_id = fields.Str(required=True)
    lab = fields.Nested(LabSchema, dump_only=True)
    user_id = fields.Str(required=True)
    user = fields.Nested(UserSchema, dump_only=True)
    date = fields.DateTime(required=False)


class PaginationLabGradeSchema(PaginationSchema):
    items = fields.List(fields.Nested(LabGradeSchema))


lab_grade_model = get_model_from_schema(LabGradeSchema, "LabGradeSchema")
pagination_lab_grade_model = get_model_from_schema(
    PaginationLabGradeSchema, "PaginationLabGradeSchema"
)
