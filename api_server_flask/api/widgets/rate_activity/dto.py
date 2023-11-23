from api_server_flask.util.widget.dto import (
    PaginationSchema, WidgetSchema
)
from api_server_flask.util.covert_model import get_model_from_schema
from marshmallow import fields, Schema


class RateActivitySchema(Schema):
    activity_type_id = fields.Str(required=True)
    activity_type = fields.Nested(WidgetSchema, dump_only=True)
    activity_sub_type_id = fields.Str(required=True)
    activity_sub_type = fields.Nested(WidgetSchema, dump_only=True)
    value = fields.Int(required=False, default=0)


class PaginationRateActivitySchema(PaginationSchema):
    items = fields.List(fields.Nested(RateActivitySchema))


rate_activity_model = get_model_from_schema(RateActivitySchema, "RateActivitySchema")
pagination_rate_activity_model = get_model_from_schema(
    PaginationRateActivitySchema, "PaginationRateActivitySchema"
)
