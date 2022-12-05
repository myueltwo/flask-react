from marshmallow import Schema, fields, validate
from api_server_flask.util.covert_model import get_model_from_schema


class WidgetSchema(Schema):
    name = fields.Str(required=True)
    link = fields.URL(schemes=["http", "https"], dump_only=True)


class PaginationLoadScheme(Schema):
    page = fields.Int(load_default=1)
    per_page = fields.Int(validate=validate.OneOf([5, 10, 25, 50, 100]), load_default=10)


class PaginationLinksSchema(Schema):
    self = fields.Str()
    prev = fields.Str()
    next = fields.Str()
    first = fields.Str()
    last = fields.Str()


class PaginationSchema(Schema):
    links = fields.Nested(PaginationLinksSchema)
    has_prev = fields.Bool()
    has_next = fields.Bool()
    page = fields.Int()
    total_pages = fields.Int(attribute="pages")
    items_per_page = fields.Int(attribute="per_page")
    total_items = fields.Int(attribute="total")
    items = fields.List(fields.Nested(WidgetSchema))


widget_model = get_model_from_schema(WidgetSchema, "WidgetSchema")
pagination_load_model = get_model_from_schema(
    PaginationLoadScheme, "PaginationLoadScheme"
)
pagination_links_model = get_model_from_schema(
    PaginationLinksSchema, "PaginationLinksSchema"
)
pagination_model = get_model_from_schema(PaginationSchema, "PaginationSchema")
