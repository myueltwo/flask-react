from flask import request
from marshmallow import ValidationError
from http import HTTPStatus


def parser_schema_load(schema):
    json_data = request.get_json() if request.is_json else request.form
    if not json_data:
        return {"message": "Validation error."}, HTTPStatus.BAD_REQUEST
    try:
        return schema.load(json_data)
    except ValidationError as err:
        return err.messages, HTTPStatus.UNPROCESSABLE_ENTITY
