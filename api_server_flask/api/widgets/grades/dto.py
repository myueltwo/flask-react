from api_server_flask.util.widget.dto import (
    PaginationSchema,
)
from api_server_flask.util.covert_model import get_model_from_schema
from marshmallow import fields, Schema


class GradeSubjectSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)


class GradeTypeSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)


class GradeSchema(Schema):
    subject_id = fields.Str(required=True, load_only=True)
    subject = fields.Nested(GradeSubjectSchema, dump_only=True)
    type_id = fields.Str(required=True, load_only=True)
    type = fields.Nested(GradeTypeSchema, dump_only=True)


class PaginationGradeSchema(PaginationSchema):
    items = fields.List(fields.Nested(GradeSchema))


grade_subject_model = get_model_from_schema(GradeSubjectSchema, "GradeSubjectSchema")
grade_type_model = get_model_from_schema(GradeTypeSchema, "GradeTypeSchema")
grade_model = get_model_from_schema(GradeSchema, "GradeSchema")
pagination_grade_model = get_model_from_schema(
    PaginationGradeSchema, "PaginationGradeSchema"
)

