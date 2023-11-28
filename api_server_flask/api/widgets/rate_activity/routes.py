"""API endpoint definitions for /rate_activity namespace"""
from http import HTTPStatus
from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import pagination_load_model
from api_server_flask.api.widgets.rate_activity.dto import (
    RateActivitySchema,
    PaginationRateActivitySchema,
    rate_activity_model,
    pagination_rate_activity_model,
)
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.rate_activity import RateActivity

rate_activity_ns = Namespace(
    name="rate_activity", description="Store of user's rate by activities"
)
add_models(
    rate_activity_ns,
    model=rate_activity_model,
    pagination=pagination_rate_activity_model,
)
widget = Widget(
    model=RateActivity,
    name="rate_activity",
    url="api.rate_activity",
    url_list="api.rate_activity_list",
    schema=RateActivitySchema,
    pagination_schema=PaginationRateActivitySchema,
)


@rate_activity_ns.route("", endpoint="rate_activity_list")
class RateActivityList(Resource):
    """Handles HTTP requests to URL: /api/v1/rate_activity."""

    @rate_activity_ns.response(int(HTTPStatus.CREATED), "Added new rate by activity.")
    @rate_activity_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @rate_activity_ns.expect(rate_activity_model)
    def post(self):
        """Create a widget"""
        return create_widget_parser(widget)

    @rate_activity_ns.response(
        HTTPStatus.OK, "Retrieved rate's activity list.", pagination_rate_activity_model
    )
    @rate_activity_ns.expect(pagination_load_model)
    def get(self):
        """Get list of widgets"""
        return retrieve_widget_list_parser(widget)


@rate_activity_ns.route("/<widget_id>", endpoint="rate_activity")
@rate_activity_ns.param("widget_id", "Rate of activity by users")
@rate_activity_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@rate_activity_ns.response(int(HTTPStatus.NOT_FOUND), "Rate of activity not found.")
@rate_activity_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@rate_activity_ns.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error."
)
@rate_activity_ns.doc(body=rate_activity_model)
class RateActivity(Resource):
    """Handles HTTP requests to URL: /rate_activity/{widget_id}."""

    @rate_activity_ns.response(
        int(HTTPStatus.OK), "Retrieved rate by activity.", rate_activity_model
    )
    def get(self, widget_id):
        """Retrieve a widget."""
        return widget.retrieve_widget(widget_id)

    @rate_activity_ns.response(
        int(HTTPStatus.OK), "Rate of activity by user was updated.", rate_activity_model
    )
    @rate_activity_ns.response(
        int(HTTPStatus.CREATED), "Added new rate of activity by user."
    )
    @rate_activity_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @rate_activity_ns.expect(rate_activity_model)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @rate_activity_ns.response(
        int(HTTPStatus.NO_CONTENT), "Rate of activity by user was deleted."
    )
    @rate_activity_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
