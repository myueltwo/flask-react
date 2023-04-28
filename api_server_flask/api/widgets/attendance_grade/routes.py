"""API endpoint definitions for /attendance_grades namespace"""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import pagination_load_model
from api_server_flask.api.widgets.attendance_grade.dto import (
    AttendanceGradeSchema,
    PaginationAttendanceGradeSchema,
    attendance_grade_model,
    pagination_attendance_grade_model,
)
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.attendance_grade import AttendanceGrade

attendance_grade_ns = Namespace(name="attendance_grade", description="Store of grades by attendance")
add_models(
    attendance_grade_ns,
    model=attendance_grade_model,
    pagination=pagination_attendance_grade_model,
    # rest_models=[grade_type_model, grade_subject_model],
)
widget = Widget(
    model=AttendanceGrade,
    name="attendance_grade",
    url="api.attendance_grade",
    url_list="api.attendance_grade_list",
    schema=AttendanceGradeSchema,
    pagination_schema=PaginationAttendanceGradeSchema,
)


@attendance_grade_ns.route("", endpoint="attendance_grade_list")
class AttendanceGradeList(Resource):
    """Handles HTTP requests to URL: /api/v1/attendance_grades."""

    @attendance_grade_ns.response(int(HTTPStatus.CREATED), "Added new grade by attendance.")
    @attendance_grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @attendance_grade_ns.expect(attendance_grade_model)
    def post(self):
        """Create a widget"""
        return create_widget_parser(widget)

    @attendance_grade_ns.response(HTTPStatus.OK, "Retrieved subject list.", pagination_attendance_grade_model)
    @attendance_grade_ns.expect(pagination_load_model)
    def get(self):
        """Get list of widgets"""
        return retrieve_widget_list_parser(widget)


@attendance_grade_ns.route("/<widget_id>", endpoint="attendance_grade")
@attendance_grade_ns.param("widget_id", "Attendance of grade id")
@attendance_grade_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@attendance_grade_ns.response(int(HTTPStatus.NOT_FOUND), "Grade by attendance not found.")
@attendance_grade_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@attendance_grade_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class AttendanceGrade(Resource):
    """Handles HTTP requests to URL: /attendance_grades/{widget_id}."""

    @attendance_grade_ns.response(int(HTTPStatus.OK), "Retrieved subject.", attendance_grade_model)
    def get(self, widget_id):
        """Retrieve a widget."""
        return widget.retrieve_widget(widget_id)

    @attendance_grade_ns.response(int(HTTPStatus.OK), "Widget was updated.", attendance_grade_model)
    @attendance_grade_ns.response(int(HTTPStatus.CREATED), "Added new widget.")
    @attendance_grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @attendance_grade_ns.expect(attendance_grade_model)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @attendance_grade_ns.response(int(HTTPStatus.NO_CONTENT), "Widget was deleted.")
    @attendance_grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
