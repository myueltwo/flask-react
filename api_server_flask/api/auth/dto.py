from marshmallow import Schema, fields
from flask_restx import Model, fields as fields_fl, SchemaModel
from marshmallow_jsonschema import JSONSchema
from api_server_flask.util.widget.dto import WidgetSchema
from api_server_flask.util.covert_model import get_model_from_schema


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    login = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    name = fields.Str()
    surname = fields.Str()
    patronymic = fields.Str()
    token_expires_in = fields.Str()
    group = fields.Nested(WidgetSchema, dump_only=True)
    role = fields.Nested(WidgetSchema, dump_only=True)


class ResetSchema(Schema):
    new_password = fields.Str(required=True, load_only=True)
    repeat_password = fields.Str(required=True, load_only=True)


login_model = Model(
    "LoginModel",
    {
        "login": fields_fl.String(required=True, min_length=4, max_length=64),
        "password": fields_fl.String(required=True, min_length=4, max_length=16),
    },
)

user_schema = UserSchema()
user_model_schema = JSONSchema().dump(user_schema)["definitions"]["UserSchema"]
user_model = SchemaModel("UserSchema", user_model_schema)
reset_model = get_model_from_schema(ResetSchema, "ResetSchema")
