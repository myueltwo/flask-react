"""API endpoint definitions for /grade_users namespace"""
from http import HTTPStatus
from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import pagination_load_model
from api_server_flask.api.widgets.grade_users.dto import (
    GradeUsersSchema,
    PaginationGradeUsersSchema,
    grade_users_model,
    pagination_grade_users_model,
)
from api_server_flask.api.widgets.grades.dto import grade_model
from api_server_flask.api.auth.dto import user_model
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.grade_users import GradeUsers

grade_users_ns = Namespace(name="grade_users", description="Store of user's grade")
add_models(
    grade_users_ns,
    model=grade_users_model,
    pagination=pagination_grade_users_model,
    rest_models=[grade_model, user_model],
)
widget = Widget(
    model=GradeUsers,
    name="grade_users",
    url="api.grade_users",
    url_list="api.grade_users_list",
    schema=GradeUsersSchema,
    pagination_schema=PaginationGradeUsersSchema,
)


@grade_users_ns.route("", endpoint="grade_users_list")
@grade_users_ns.doc(body=grade_model)
class GradeList(Resource):
    """Handles HTTP requests to URL: /api/v1/grade_users."""

    @grade_users_ns.response(int(HTTPStatus.CREATED), "Added new grade by user.")
    @grade_users_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @grade_users_ns.expect(grade_users_model)
    @grade_users_ns.doc(body=user_model)
    def post(self):
        """Create a widget"""
        return create_widget_parser(widget)

    @grade_users_ns.response(
        HTTPStatus.OK, "Retrieved user's grade list.", pagination_grade_users_model
    )
    @grade_users_ns.expect(pagination_load_model)
    def get(self):
        """Get list of widgets"""
        return retrieve_widget_list_parser(widget)


@grade_users_ns.route("/<widget_id>", endpoint="grade_users")
@grade_users_ns.param("widget_id", "Grade users id")
@grade_users_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@grade_users_ns.response(int(HTTPStatus.NOT_FOUND), "Grade not found.")
@grade_users_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@grade_users_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
@grade_users_ns.doc(body=grade_model)
class Grade(Resource):
    """Handles HTTP requests to URL: /grade_users/{widget_id}."""

    @grade_users_ns.response(
        int(HTTPStatus.OK), "Retrieved grade by user.", grade_users_model
    )
    def get(self, widget_id):
        """Retrieve a widget."""
        return widget.retrieve_widget(widget_id)

    @grade_users_ns.response(
        int(HTTPStatus.OK), "Grade grade by user was updated.", grade_users_model
    )
    @grade_users_ns.response(int(HTTPStatus.CREATED), "Added new grade by user.")
    @grade_users_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @grade_users_ns.expect(grade_users_model)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @grade_users_ns.response(int(HTTPStatus.NO_CONTENT), "Grade by user was deleted.")
    @grade_users_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
