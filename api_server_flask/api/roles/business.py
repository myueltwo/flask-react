from http import HTTPStatus
from api_server_flask.api.models.role import Role
from flask_restx import abort
from api_server_flask.api import db
from flask import jsonify, url_for


def create_role(role_dict):
    name = role_dict.get("name")
    if Role.find_by_name(name):
        error = f"Role name: {name} already exists, must be unique."
        abort(HTTPStatus.CONFLICT, error, status="fail")
    role = Role(**role_dict)
    db.session.add(role)
    db.session.commit()
    response = jsonify(status="success", message=f"New role added: {name}.")
    response.status_code = HTTPStatus.CREATED
    response.headers["Location"] = url_for("api.role", id=role.id)
    return response
