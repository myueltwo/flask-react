from flask import request
from marshmallow import ValidationError
from http import HTTPStatus


def parser_schema_load(schema):
    json_data = None
    if request.is_json:
        json_data = request.get_json()
    elif request.form:
        json_data = request.form
    elif request.args:
        json_data = request.args

    if not json_data:
        json_data = {}
    try:
        return schema.load(json_data)
    except ValidationError as err:
        return err.messages, HTTPStatus.UNPROCESSABLE_ENTITY
