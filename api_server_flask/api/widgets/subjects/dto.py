from api_server_flask.util.widget.dto import (
    WidgetSchema,
    PaginationSchema,
)
from api_server_flask.util.covert_model import get_model_from_schema
from marshmallow import fields


class SubjectSchema(WidgetSchema):
    count_hours = fields.Int()


class PaginationSubjectSchema(PaginationSchema):
    items = fields.List(fields.Nested(SubjectSchema))


subject_model = get_model_from_schema(SubjectSchema, "SubjectSchema")
pagination_subject_model = get_model_from_schema(
    PaginationSubjectSchema, "PaginationSubjectSchema"
)
