"""API endpoint definitions for /activity_type namespace"""
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
from api_server_flask.api.models.activity_type import ActivityType

activity_type_ns = Namespace(
    name="activity_type", description="Store of type's activities by users"
)
add_models(activity_type_ns)
widget = Widget(
    model=ActivityType,
    name="type's activities",
    url="api.activity_type",
    url_list="api.activity_type_list",
)


@activity_type_ns.route("", endpoint="activity_type_list")
class ActivityTypeList(Resource):
    """Handles HTTP requests to URL: /api/v1/widgets/activity_type."""

    @activity_type_ns.response(int(HTTPStatus.CREATED), "Added new type's activity.")
    @activity_type_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @activity_type_ns.expect(widget_model)
    def post(self):
        """Create a type's activity"""
        return create_widget_parser(widget)

    @activity_type_ns.response(
        HTTPStatus.OK, "Retrieved type's activity list.", pagination_model
    )
    @activity_type_ns.expect(pagination_load_model)
    def get(self):
        """Get list of type's activities"""
        return retrieve_widget_list_parser(widget)


@activity_type_ns.route("/<widget_id>", endpoint="activity_type")
@activity_type_ns.param("widget_id", "Type's activity id")
@activity_type_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@activity_type_ns.response(int(HTTPStatus.NOT_FOUND), "Type's activity not found.")
@activity_type_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@activity_type_ns.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error."
)
class ActivityType(Resource):
    """Handles HTTP requests to URL: /activity_type/{widget_id}."""

    @activity_type_ns.response(
        int(HTTPStatus.OK), "Retrieved type's activity.", widget_model
    )
    def get(self, widget_id):
        """Retrieve a type's activity."""
        return widget.retrieve_widget(widget_id)

    @activity_type_ns.response(
        int(HTTPStatus.OK), "Type's activity was updated.", widget_model
    )
    @activity_type_ns.response(int(HTTPStatus.CREATED), "Added new type's activity.")
    @activity_type_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @activity_type_ns.expect(widget_model, validate=False)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @activity_type_ns.response(
        int(HTTPStatus.NO_CONTENT), "Type's activity was deleted."
    )
    @activity_type_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
