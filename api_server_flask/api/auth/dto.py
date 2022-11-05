from marshmallow import Schema, fields
from flask_restx import Model, fields as fields_fl


class UserSchema(Schema):
    login = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    username = fields.Str()
    surname = fields.Str()
    patronymic = fields.Str()
    formatted_name = fields.Method("format_name", dump_only=True)

    def format_name(self, user):
        return f"{user.username}, {user.surname}"


login_model = Model(
    "LoginModel",
    {
        "login": fields_fl.String(required=True, min_length=4, max_length=64),
        "password": fields_fl.String(required=True, min_length=4, max_length=16),
    },
)
