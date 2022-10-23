from flask_restx import Namespace, Resource, fields
from api_server_flask.api.auth.dto import UserSchema
from http import HTTPStatus
from flask import request
from marshmallow import ValidationError

auth_ns = Namespace('auth', description='Authentication of users')


@auth_ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {
                   "success": True,
                   "msg": "Hello world"
               }, 200


login_model = auth_ns.model(
    'SignUpModel', {
        "login": fields.String(required=True, min_length=4, max_length=64),
        "password": fields.String(required=True, min_length=4, max_length=16)
    }
)


@auth_ns.route('/login', methods=["POST"])
class LoginUser(Resource):

    @auth_ns.expect(login_model)
    @auth_ns.response(int(HTTPStatus.OK), "Login succeeded.")
    @auth_ns.response(int(HTTPStatus.UNAUTHORIZED), "login or password does not match")
    @auth_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @auth_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "Validation error."}, HTTPStatus.BAD_REQUEST
        # Validate and deserialize input
        try:
            user_schema = UserSchema()
            data = user_schema.load(json_data)
        except ValidationError as err:
            return err.messages, HTTPStatus.UNPROCESSABLE_ENTITY
        login = data.get('login')
        password = data.get("password")
        from api_server_flask.api.auth.business import process_login_request

        return process_login_request(login, password)
