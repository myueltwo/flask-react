"""API endpoint definitions for /activity_sub_type namespace"""
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
from api_server_flask.api.models.activity_sub_type import ActivitySubType

activity_sub_type_ns = Namespace(
    name="activity_sub_type", description="Store of subtype's activities by users"
)
add_models(activity_sub_type_ns)
widget = Widget(
    model=ActivitySubType,
    name="subtype's activities",
    url="api.activity_sub_type",
    url_list="api.activity_sub_type_list",
)


@activity_sub_type_ns.route("", endpoint="activity_sub_type_list")
class ActivitySubTypeList(Resource):
    """Handles HTTP requests to URL: /api/v1/widgets/activity_sub_type."""

    @activity_sub_type_ns.response(int(HTTPStatus.CREATED), "Added new subtype's activity.")
    @activity_sub_type_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @activity_sub_type_ns.expect(widget_model)
    def post(self):
        """Create a subtype's activity"""
        return create_widget_parser(widget)

    @activity_sub_type_ns.response(
        HTTPStatus.OK, "Retrieved subtype's activity list.", pagination_model
    )
    @activity_sub_type_ns.expect(pagination_load_model)
    def get(self):
        """Get list of subtype's activities"""
        return retrieve_widget_list_parser(widget)


@activity_sub_type_ns.route("/<widget_id>", endpoint="activity_sub_type")
@activity_sub_type_ns.param("widget_id", "Subtype's activity id")
@activity_sub_type_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@activity_sub_type_ns.response(int(HTTPStatus.NOT_FOUND), "Subtype's activity not found.")
@activity_sub_type_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@activity_sub_type_ns.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error."
)
class ActivitySubType(Resource):
    """Handles HTTP requests to URL: /activity_sub_type/{widget_id}."""

    @activity_sub_type_ns.response(
        int(HTTPStatus.OK), "Retrieved subtype's activity.", widget_model
    )
    def get(self, widget_id):
        """Retrieve a subtype's activity."""
        return widget.retrieve_widget(widget_id)

    @activity_sub_type_ns.response(
        int(HTTPStatus.OK), "Subtype's activity was updated.", widget_model
    )
    @activity_sub_type_ns.response(int(HTTPStatus.CREATED), "Added new subtype's activity.")
    @activity_sub_type_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @activity_sub_type_ns.expect(widget_model, validate=False)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @activity_sub_type_ns.response(
        int(HTTPStatus.NO_CONTENT), "Subtype's activity was deleted."
    )
    @activity_sub_type_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
