from api_server_flask.util.widget.dto import (
    PaginationSchema,
)
from api_server_flask.api.widgets.grades.dto import GradeSchema
from api_server_flask.api.auth.dto import UserSchema
from api_server_flask.util.covert_model import get_model_from_schema
from marshmallow import fields, Schema


class GradeUsersSchema(Schema):
    grade_id = fields.Str(required=True)
    grade = fields.Nested(GradeSchema, dump_only=True)
    user_id = fields.Str(required=True)
    user = fields.Nested(UserSchema, dump_only=True)
    value = fields.Int(default=0)


class PaginationGradeUsersSchema(PaginationSchema):
    items = fields.List(fields.Nested(GradeUsersSchema))


grade_users_model = get_model_from_schema(GradeUsersSchema, "GradeUsersSchema")
pagination_grade_users_model = get_model_from_schema(
    PaginationGradeUsersSchema, "PaginationGradeUsersSchema"
)
