"""API endpoint definitions for /attendance namespace"""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import pagination_load_model
from api_server_flask.api.widgets.attendance.dto import (
    AttendanceSchema,
    PaginationAttendanceSchema,
    attendance_model,
    attendance_group_model,
    attendance_type_model,
    pagination_attendance_model,
)
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.attendance import Attendance

attendance_ns = Namespace(name="attendance", description="Store of attendances")
add_models(
    attendance_ns,
    model=attendance_model,
    pagination=pagination_attendance_model,
    rest_models=[attendance_group_model, attendance_type_model],
)
widget = Widget(
    model=Attendance,
    name="attendance",
    url="api.attendance",
    url_list="api.attendance_list",
    schema=AttendanceSchema,
    pagination_schema=PaginationAttendanceSchema,
)


@attendance_ns.route("", endpoint="attendance_list")
@attendance_ns.doc(body=attendance_type_model)
class GradeList(Resource):
    """Handles HTTP requests to URL: /api/v1/attendance."""

    @attendance_ns.response(int(HTTPStatus.CREATED), "Added new attendance.")
    @attendance_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @attendance_ns.expect(attendance_model)
    @attendance_ns.doc(body=attendance_group_model)
    def post(self):
        """Create a widget"""
        return create_widget_parser(widget)

    @attendance_ns.response(HTTPStatus.OK, "Retrieved attendance list.", pagination_attendance_model)
    @attendance_ns.expect(pagination_load_model)
    def get(self):
        """Get list of widgets"""
        return retrieve_widget_list_parser(widget)


@attendance_ns.route("/<widget_id>", endpoint="attendance")
@attendance_ns.param("widget_id", "Attendance id")
@attendance_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@attendance_ns.response(int(HTTPStatus.NOT_FOUND), "Attendance not found.")
@attendance_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@attendance_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
@attendance_ns.doc(body=attendance_group_model)
class Grade(Resource):
    """Handles HTTP requests to URL: /attendance/{widget_id}."""

    @attendance_ns.response(int(HTTPStatus.OK), "Retrieved subject.", attendance_model)
    def get(self, widget_id):
        """Retrieve a widget."""
        return widget.retrieve_widget(widget_id)

    @attendance_ns.response(int(HTTPStatus.OK), "Attendance was updated.", attendance_model)
    @attendance_ns.response(int(HTTPStatus.CREATED), "Added new attendance.")
    @attendance_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @attendance_ns.expect(attendance_model)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @attendance_ns.response(int(HTTPStatus.NO_CONTENT), "Attendance was deleted.")
    @attendance_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
