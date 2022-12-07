"""API endpoint definitions for /role namespace."""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.api.models.role import Role
from api_server_flask.util.widget.dto import (
    widget_model,
    pagination_load_model,
    pagination_links_model,
    pagination_model,
    WidgetSchema,
    PaginationLoadScheme,
)
from api_server_flask.util.widget.business import Widget
from api_server_flask.util.schema_load import parser_schema_load

role_ns = Namespace(name="role", description="Store of roles by users", validate=True)
role_ns.models[widget_model.name] = widget_model
role_ns.models[pagination_load_model.name] = pagination_load_model
role_ns.models[pagination_links_model.name] = pagination_links_model
role_ns.models[pagination_model.name] = pagination_model
role_widget = Widget(model=Role, name="role", url="api.role", url_list="api.role_list")


@role_ns.route("", endpoint="role_list")
class RoleList(Resource):
    """Handles HTTP requests to URL: /api/v1/roles."""

    @role_ns.response(int(HTTPStatus.CREATED), "Added new role.")
    @role_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @role_ns.expect(widget_model, validate=False)
    def post(self):
        """Create a role"""
        data = parser_schema_load(WidgetSchema())
        return role_widget.create_widget(data)

    @role_ns.response(HTTPStatus.OK, "Retrieved role list.", pagination_model)
    @role_ns.expect(pagination_load_model, validate=False)
    def get(self):
        """Get list of roles"""
        data = parser_schema_load(PaginationLoadScheme())
        page = data.get("page")
        per_page = data.get("per_page")
        return role_widget.retrieve_widget_list(page, per_page)


@role_ns.route("/<widget_id>", endpoint="role")
@role_ns.param("widget_id", "Role id")
@role_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@role_ns.response(int(HTTPStatus.NOT_FOUND), "Role not found.")
@role_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@role_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class Role(Resource):
    """Handles HTTP requests to URL: /roles/{widget_id}."""

    @role_ns.response(int(HTTPStatus.OK), "Retrieved role.", widget_model)
    def get(self, widget_id):
        """Retrieve a role."""
        return role_widget.retrieve_widget(widget_id)

    @role_ns.response(int(HTTPStatus.OK), "Role was updated.", widget_model)
    @role_ns.response(int(HTTPStatus.CREATED), "Added new role.")
    @role_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @role_ns.expect(widget_model, validate=False)
    def put(self, widget_id):
        """Update a role."""
        data = parser_schema_load(WidgetSchema())
        return role_widget.update_widget(widget_id, data)

    @role_ns.response(int(HTTPStatus.NO_CONTENT), "Role was deleted.")
    @role_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a widget."""
        return role_widget.delete_widget(widget_id)
