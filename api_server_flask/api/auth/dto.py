from marshmallow import Schema, fields, ValidationError, pre_load


class UserSchema(Schema):
    login = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    username = fields.Str()
    surname = fields.Str()
    patronymic = fields.Str()
    formatted_name = fields.Method("format_name", dump_only=True)

    def format_name(self, user):
        return f"{user.username}, {user.surname}"
