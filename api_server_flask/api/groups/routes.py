"""API endpoint definitions for /group namespace"""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import (
    widget_model,
    pagination_load_model,
    pagination_model,
)
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.group import Group

group_ns = Namespace(name="group", description="Store of groups by students")
add_models(group_ns)
group_widget = Widget(
    model=Group, name="group", url="api.group", url_list="api.group_list"
)


@group_ns.route("", endpoint="group_list")
class GroupList(Resource):
    """Handles HTTP requests to URL: /api/v1/groups."""

    @group_ns.response(int(HTTPStatus.CREATED), "Added new group.")
    @group_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @group_ns.expect(widget_model)
    def post(self):
        """Create a group"""
        return create_widget_parser(group_widget)

    @group_ns.response(HTTPStatus.OK, "Retrieved group list.", pagination_model)
    @group_ns.expect(pagination_load_model)
    def get(self):
        """Get list of groups"""
        return retrieve_widget_list_parser(group_widget)


@group_ns.route("/<widget_id>", endpoint="group")
@group_ns.param("widget_id", "Group id")
@group_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@group_ns.response(int(HTTPStatus.NOT_FOUND), "Role not found.")
@group_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@group_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class Role(Resource):
    """Handles HTTP requests to URL: /groups/{widget_id}."""

    @group_ns.response(int(HTTPStatus.OK), "Retrieved group.", widget_model)
    def get(self, widget_id):
        """Retrieve a group."""
        return group_widget.retrieve_widget(widget_id)

    @group_ns.response(int(HTTPStatus.OK), "Group was updated.", widget_model)
    @group_ns.response(int(HTTPStatus.CREATED), "Added new group.")
    @group_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @group_ns.expect(widget_model, validate=False)
    def put(self, widget_id):
        """Update a group."""
        return update_widget_parser(group_widget, widget_id)

    @group_ns.response(int(HTTPStatus.NO_CONTENT), "Group was deleted.")
    @group_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a widget."""
        return group_widget.delete_widget(widget_id)
