from api_server_flask.util.widget.dto import (
    PaginationSchema,
)
from api_server_flask.util.covert_model import get_model_from_schema
from api_server_flask.api.widgets.grades.dto import GradeSubjectSchema
from marshmallow import fields, Schema


class LabSchema(Schema):
    name = fields.Str(required=True)
    subject_id = fields.Str(required=True)
    subject = fields.Nested(GradeSubjectSchema, dump_only=True)
    datetime = fields.DateTime(required=False)
    deadline = fields.DateTime(required=False)


class PaginationLabSchema(PaginationSchema):
    items = fields.List(fields.Nested(LabSchema))


lab_model = get_model_from_schema(LabSchema, "LabSchema")
pagination_lab_model = get_model_from_schema(PaginationLabSchema, "PaginationLabSchema")
