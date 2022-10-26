from flask_restx import Namespace, Resource
from api_server_flask.api.auth.dto import UserSchema, login_model
from http import HTTPStatus
from flask import request
from marshmallow import ValidationError

auth_ns = Namespace('auth', description='Authentication of users')
auth_ns.models[login_model.name] = login_model


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
        try:
            data = UserSchema().load(json_data)
        except ValidationError as err:
            return err.messages, HTTPStatus.UNPROCESSABLE_ENTITY
        login = data.get('login')
        password = data.get("password")
        from api_server_flask.api.auth.business import process_login_request

        return process_login_request(login, password)
