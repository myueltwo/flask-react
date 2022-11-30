"""API endpoint definitions for /role namespace."""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.api.roles.dto import (
    role_model,
    pagination_load_model,
    pagination_links_model,
    pagination_model,
    RoleSchema,
    PaginationLoadScheme,
)
from api_server_flask.api.roles.business import (
    create_role,
    retrieve_role_list,
    retrieve_role,
    update_role,
    delete_role,
)
from api_server_flask.util.schema_load import parser_schema_load

role_ns = Namespace(name="role", description="Store of roles by users", validate=True)
role_ns.models[role_model.name] = role_model
role_ns.models[pagination_load_model.name] = pagination_load_model
role_ns.models[pagination_links_model.name] = pagination_links_model
role_ns.models[pagination_model.name] = pagination_model


@role_ns.route("", endpoint="role_list")
class RoleList(Resource):
    """Handles HTTP requests to URL: /api/v1/roles."""

    @role_ns.response(int(HTTPStatus.CREATED), "Added new role.")
    @role_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @role_ns.expect(role_model, validate=False)
    def post(self):
        """Create a role"""
        data = parser_schema_load(RoleSchema())
        return create_role(data)

    @role_ns.response(HTTPStatus.OK, "Retrieved role list.", pagination_model)
    @role_ns.expect(pagination_load_model, validate=False)
    def get(self):
        """Get list of roles"""
        data = parser_schema_load(PaginationLoadScheme())
        page = data.get("page")
        per_page = data.get("per_page")
        return retrieve_role_list(page, per_page)


@role_ns.route("/<role_id>", endpoint="role")
@role_ns.param("role_id", "Role id")
@role_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@role_ns.response(int(HTTPStatus.NOT_FOUND), "Role not found.")
@role_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@role_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class Role(Resource):
    """Handles HTTP requests to URL: /roles/{role_id}."""

    @role_ns.response(int(HTTPStatus.OK), "Retrieved role.", role_model)
    def get(self, role_id):
        """Retrieve a role."""
        return retrieve_role(role_id)

    @role_ns.response(int(HTTPStatus.OK), "Role was updated.", role_model)
    @role_ns.response(int(HTTPStatus.CREATED), "Added new role.")
    @role_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @role_ns.expect(role_model)
    def put(self, role_id):
        """Update a role."""
        data = parser_schema_load(RoleSchema())
        return update_role(role_id, data)

    @role_ns.response(int(HTTPStatus.NO_CONTENT), "Role was deleted.")
    @role_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, role_id):
        """Delete a widget."""
        return delete_role(role_id)
