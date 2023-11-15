"""API endpoint definitions for /lab namespace"""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import pagination_load_model
from api_server_flask.api.widgets.labs.dto import (
    LabSchema,
    PaginationLabSchema,
    lab_model,
    pagination_lab_model,
)
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.lab import Lab

lab_ns = Namespace(name="lab", description="Store of labs")
add_models(
    lab_ns,
    model=lab_model,
    pagination=pagination_lab_model,
)
widget = Widget(
    model=Lab,
    name="lab",
    url="api.lab",
    url_list="api.lab_list",
    schema=LabSchema,
    pagination_schema=PaginationLabSchema,
)


@lab_ns.route("/<widget_id>", endpoint="lab")
@lab_ns.param("widget_id", "Lab id")
@lab_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@lab_ns.response(int(HTTPStatus.NOT_FOUND), "Lab not found.")
@lab_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@lab_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class Lab(Resource):
    """Handles HTTP requests to URL: /lab/{widget_id}."""

    @lab_ns.response(int(HTTPStatus.OK), "Retrieved lab.", lab_model)
    def get(self, widget_id):
        """Retrieve a widget."""
        return widget.retrieve_widget(widget_id)

    @lab_ns.response(int(HTTPStatus.OK), "Lab was updated.", lab_model)
    @lab_ns.response(int(HTTPStatus.CREATED), "Added new lab.")
    @lab_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @lab_ns.expect(lab_model)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @lab_ns.response(int(HTTPStatus.NO_CONTENT), "Lab was deleted.")
    @lab_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)


@lab_ns.route("", endpoint="lab_list")
class AttendanceList(Resource):
    """Handles HTTP requests to URL: /api/v1/attendance."""

    @lab_ns.response(int(HTTPStatus.CREATED), "Added new lab.")
    @lab_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @lab_ns.expect(lab_model)
    def post(self):
        """Create a widget"""
        return create_widget_parser(widget)

    @lab_ns.response(HTTPStatus.OK, "Retrieved attendance list.", pagination_lab_model)
    @lab_ns.expect(pagination_load_model)
    def get(self):
        """Get list of widgets"""
        return retrieve_widget_list_parser(widget)
