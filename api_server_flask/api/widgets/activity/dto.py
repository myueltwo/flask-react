from api_server_flask.util.widget.dto import (
    PaginationSchema, WidgetSchema
)
from api_server_flask.util.covert_model import get_model_from_schema
from api_server_flask.api.auth.dto import UserSchema
from api_server_flask.api.widgets.rate_activity.dto import RateActivitySchema
from marshmallow import fields, Schema


class ActivitySchema(Schema):
    name = fields.Str(required=True)
    type_id = fields.Str(required=True)
    type = fields.Nested(WidgetSchema, dump_only=True)
    user_id = fields.Str(required=True)
    user = fields.Nested(UserSchema, dump_only=True)
    file = fields.Str(required=True)
    status = fields.Bool(required=False)
    comment = fields.Str(required=False)
    rate_id = fields.Str(required=False)
    rate = fields.Nested(RateActivitySchema, dump_only=True)


class PaginationActivitySchema(PaginationSchema):
    items = fields.List(fields.Nested(ActivitySchema))


activity_model = get_model_from_schema(ActivitySchema, "ActivitySchema")
pagination_activity_model = get_model_from_schema(
    PaginationActivitySchema, "PaginationActivitySchema"
)
