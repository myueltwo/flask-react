"""API endpoint definitions for /role namespace."""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.api.roles.dto import (
    role_model,
    pagination_load_model,
    pagination_links_model,
    pagination_model,
    RoleSchema,
)
from api_server_flask.api.roles.business import (
    create_role,
)

role_ns = Namespace(name="role", description="Store of roles by users", validate=True)
role_ns.models[role_model.name] = role_model
role_ns.models[pagination_load_model.name] = pagination_load_model
role_ns.models[pagination_links_model.name] = pagination_links_model
role_ns.models[pagination_model.name] = pagination_model


@role_ns.route("", endpoint="role_list")
class RoleList(Resource):
    """Handles HTTP requests to URL: /api/v1/auth/role."""

    @role_ns.doc(security="Bearer")
    @role_ns.response(int(HTTPStatus.CREATED), "Added new role.")
    @role_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @role_ns.response(int(HTTPStatus.CONFLICT), "Widget name already exists.")
    @role_ns.expect(role_model)
    def post(self):
        """Create a role"""
        from api_server_flask.util.schema_load import parser_schema_load
        data = parser_schema_load(RoleSchema())
        return create_role(data)

    @role_ns.doc(security="Bearer")
    @role_ns.response(HTTPStatus.OK, "Retrieved role list.", pagination_model)
    @role_ns.expect(pagination_load_model)
    def get(self):
        pass