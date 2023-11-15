"""API endpoint definitions for /labs_grade namespace"""
from http import HTTPStatus
from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import pagination_load_model
from api_server_flask.api.widgets.labs_grade.dto import (
    LabGradeSchema,
    PaginationLabGradeSchema,
    lab_grade_model,
    pagination_lab_grade_model,
)
from api_server_flask.api.widgets.labs.dto import lab_model
from api_server_flask.api.auth.dto import user_model
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.labs_grade import LabsGrade

labs_grade_ns = Namespace(name="labs_grade", description="Store of user's grade by labs")
add_models(
    labs_grade_ns,
    model=lab_grade_model,
    pagination=pagination_lab_grade_model,
    rest_models=[lab_model, user_model],
)
widget = Widget(
    model=LabsGrade,
    name="labs_grade",
    url="api.labs_grade",
    url_list="api.labs_grade_list",
    schema=LabGradeSchema,
    pagination_schema=PaginationLabGradeSchema,
)


@labs_grade_ns.route("", endpoint="labs_grade_list")
@labs_grade_ns.doc(body=lab_model)
class LabGradeList(Resource):
    """Handles HTTP requests to URL: /api/v1/lab_grades."""

    @labs_grade_ns.response(int(HTTPStatus.CREATED), "Added new grade by lab.")
    @labs_grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @labs_grade_ns.expect(lab_grade_model)
    @labs_grade_ns.doc(body=user_model)
    def post(self):
        """Create a widget"""
        return create_widget_parser(widget)

    @labs_grade_ns.response(
        HTTPStatus.OK, "Retrieved user's grade list.", pagination_lab_grade_model
    )
    @labs_grade_ns.expect(pagination_load_model)
    def get(self):
        """Get list of widgets"""
        return retrieve_widget_list_parser(widget)


@labs_grade_ns.route("/<widget_id>", endpoint="labs_grade")
@labs_grade_ns.param("widget_id", "Grade of lab by users id")
@labs_grade_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@labs_grade_ns.response(int(HTTPStatus.NOT_FOUND), "Grade of lab not found.")
@labs_grade_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@labs_grade_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
@labs_grade_ns.doc(body=lab_grade_model)
class LabGrade(Resource):
    """Handles HTTP requests to URL: /lab_grades/{widget_id}."""

    @labs_grade_ns.response(
        int(HTTPStatus.OK), "Retrieved grade by user.", lab_grade_model
    )
    def get(self, widget_id):
        """Retrieve a widget."""
        return widget.retrieve_widget(widget_id)

    @labs_grade_ns.response(
        int(HTTPStatus.OK), "Grade of lab by user was updated.", lab_grade_model
    )
    @labs_grade_ns.response(int(HTTPStatus.CREATED), "Added new grade of lab by user.")
    @labs_grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @labs_grade_ns.expect(lab_grade_model)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @labs_grade_ns.response(
        int(HTTPStatus.NO_CONTENT), "Grade of lab by user was deleted."
    )
    @labs_grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
