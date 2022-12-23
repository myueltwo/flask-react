"""API endpoint definitions for /grades namespace"""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import pagination_load_model
from api_server_flask.api.widgets.grades.dto import (
    GradeSchema,
    PaginationGradeSchema,
    grade_subject_model,
    grade_type_model,
    grade_model,
    pagination_grade_model,
)
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.grade import Grade

grade_ns = Namespace(name="grade", description="Store of grades")
add_models(
    grade_ns,
    model=grade_model,
    pagination=pagination_grade_model,
    rest_models=[grade_type_model, grade_subject_model]
)
widget = Widget(
    model=Grade,
    name="grade",
    url="api.grade",
    url_list="api.grade_list",
    schema=GradeSchema,
    pagination_schema=PaginationGradeSchema,
)


@grade_ns.route("", endpoint="grade_list")
@grade_ns.doc(body=grade_type_model)
class GradeList(Resource):
    """Handles HTTP requests to URL: /api/v1/grades."""

    @grade_ns.response(int(HTTPStatus.CREATED), "Added new grade.")
    @grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @grade_ns.expect(grade_model)
    @grade_ns.doc(body=grade_subject_model)
    def post(self):
        """Create a widget"""
        return create_widget_parser(widget)

    @grade_ns.response(
        HTTPStatus.OK, "Retrieved subject list.", pagination_grade_model
    )
    @grade_ns.expect(pagination_load_model)
    def get(self):
        """Get list of widgets"""
        return retrieve_widget_list_parser(widget)


@grade_ns.route("/<widget_id>", endpoint="grade")
@grade_ns.param("widget_id", "Grade id")
@grade_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@grade_ns.response(int(HTTPStatus.NOT_FOUND), "Grade not found.")
@grade_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@grade_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
@grade_ns.doc(body=grade_subject_model)
class Grade(Resource):
    """Handles HTTP requests to URL: /grades/{widget_id}."""

    @grade_ns.response(int(HTTPStatus.OK), "Retrieved subject.", grade_model)
    def get(self, widget_id):
        """Retrieve a widget."""
        return widget.retrieve_widget(widget_id)

    @grade_ns.response(int(HTTPStatus.OK), "Grade was updated.", grade_model)
    @grade_ns.response(int(HTTPStatus.CREATED), "Added new grade.")
    @grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @grade_ns.expect(grade_model)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @grade_ns.response(int(HTTPStatus.NO_CONTENT), "Grade was deleted.")
    @grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
