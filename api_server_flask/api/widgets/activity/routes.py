"""API endpoint definitions for /activity namespace"""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import pagination_load_model
from api_server_flask.api.widgets.activity.dto import (
    ActivitySchema,
    PaginationActivitySchema,
    activity_model,
    pagination_activity_model,
)
from api_server_flask.api.widgets.rate_activity.dto import rate_activity_model
from api_server_flask.api.auth.dto import user_model
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.activity import Activity

activity_ns = Namespace(
    name="activity", description="Store of activity by users"
)
add_models(
    activity_ns,
    model=activity_model,
    pagination=pagination_activity_model,
    rest_models=[rate_activity_model, user_model],
)
widget = Widget(
    model=Activity,
    name="activity",
    url="api.activity",
    url_list="api.activity_list",
    schema=ActivitySchema,
    pagination_schema=PaginationActivitySchema,
)


@activity_ns.route("", endpoint="activity_list")
class ActivityList(Resource):
    """Handles HTTP requests to URL: /api/v1/activity."""

    @activity_ns.response(
        int(HTTPStatus.CREATED), "Added new activity by user."
    )
    @activity_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @activity_ns.expect(rate_activity_model)
    def post(self):
        """Create a widget"""
        return create_widget_parser(widget)

    @activity_ns.response(
        HTTPStatus.OK, "Retrieved activity list.", pagination_activity_model
    )
    @activity_ns.expect(pagination_load_model)
    def get(self):
        """Get list of widgets"""
        return retrieve_widget_list_parser(widget)


@activity_ns.route("/<widget_id>", endpoint="activity")
@activity_ns.param("widget_id", "Activity of user")
@activity_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@activity_ns.response(
    int(HTTPStatus.NOT_FOUND), "Activity by user not found."
)
@activity_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@activity_ns.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error."
)
class Activity(Resource):
    """Handles HTTP requests to URL: /activity/{widget_id}."""

    @activity_ns.response(
        int(HTTPStatus.OK), "Retrieved activity.", activity_model
    )
    def get(self, widget_id):
        """Retrieve a widget."""
        return widget.retrieve_widget(widget_id)

    @activity_ns.response(
        int(HTTPStatus.OK), "Widget was updated.", activity_model
    )
    @activity_ns.response(int(HTTPStatus.CREATED), "Added new widget.")
    @activity_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @activity_ns.expect(activity_model)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @activity_ns.response(int(HTTPStatus.NO_CONTENT), "Widget was deleted.")
    @activity_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
