"""API endpoint definitions for /attendance_type namespace"""
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
from api_server_flask.api.models.attendance_type import AttendanceType

attendance_type_ns = Namespace(
    name="attendance_type", description="Store of type's attendance by subjects"
)
add_models(attendance_type_ns)
widget = Widget(
    model=AttendanceType,
    name="type's attendance",
    url="api.attendance_type",
    url_list="api.attendance_type_list",
)


@attendance_type_ns.route("", endpoint="attendance_type_list")
class AttendanceTypeList(Resource):
    """Handles HTTP requests to URL: /api/v1/widgets/attendance_type."""

    @attendance_type_ns.response(int(HTTPStatus.CREATED), "Added new type's attendance.")
    @attendance_type_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @attendance_type_ns.expect(widget_model)
    def post(self):
        """Create a type's attendance"""
        return create_widget_parser(widget)

    @attendance_type_ns.response(
        HTTPStatus.OK, "Retrieved type's attendance list.", pagination_model
    )
    @attendance_type_ns.expect(pagination_load_model)
    def get(self):
        """Get list of type's attendances"""
        return retrieve_widget_list_parser(widget)


@attendance_type_ns.route("/<widget_id>", endpoint="attendance_type")
@attendance_type_ns.param("widget_id", "Type's attendance id")
@attendance_type_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@attendance_type_ns.response(int(HTTPStatus.NOT_FOUND), "Type's attendance not found.")
@attendance_type_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@attendance_type_ns.response(
    int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error."
)
class AttendanceType(Resource):
    """Handles HTTP requests to URL: /attendance_type/{widget_id}."""

    @attendance_type_ns.response(
        int(HTTPStatus.OK), "Retrieved type's attendance.", widget_model
    )
    def get(self, widget_id):
        """Retrieve a type's attendance."""
        return widget.retrieve_widget(widget_id)

    @attendance_type_ns.response(
        int(HTTPStatus.OK), "Type's attendance was updated.", widget_model
    )
    @attendance_type_ns.response(int(HTTPStatus.CREATED), "Added new type's attendance.")
    @attendance_type_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    @attendance_type_ns.expect(widget_model, validate=False)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @attendance_type_ns.response(
        int(HTTPStatus.NO_CONTENT), "Type's attendance was deleted."
    )
    @attendance_type_ns.response(
        int(HTTPStatus.FORBIDDEN), "Administrator token required."
    )
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
