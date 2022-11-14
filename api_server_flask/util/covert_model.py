from flask_restx import SchemaModel
from marshmallow_jsonschema import JSONSchema


def get_model_from_schema(scheme, name_model):
    """Method helps to convert scheme from MARSHMALLOW lib to flask_restx's model"""
    load_schema = scheme()
    name = type(load_schema).__name__
    scheme_model_json = JSONSchema().dump(load_schema)["definitions"][name]
    print(scheme_model_json)
    return SchemaModel(name_model, scheme_model_json)
