"""API endpoint definitions for /subjects namespace"""
from http import HTTPStatus

from flask_restx import Namespace, Resource
from api_server_flask.util.widget.dto import pagination_load_model
from api_server_flask.api.widgets.subjects.dto import (
    SubjectSchema,
    PaginationSubjectSchema,
    subject_model,
    pagination_subject_model,
)
from api_server_flask.util.widget.business import (
    Widget,
    add_models,
    create_widget_parser,
    retrieve_widget_list_parser,
    update_widget_parser,
)
from api_server_flask.api.models.subject import Subject

subject_ns = Namespace(name="subject", description="Store of subjects")
add_models(subject_ns, model=subject_model, pagination=pagination_subject_model)
widget = Widget(
    model=Subject,
    name="subject",
    url="api.subject",
    url_list="api.subject_list",
    schema=SubjectSchema,
    pagination_schema=PaginationSubjectSchema,
)


@subject_ns.route("", endpoint="subject_list")
class SubjectList(Resource):
    """Handles HTTP requests to URL: /api/v1/subjects."""

    @subject_ns.response(int(HTTPStatus.CREATED), "Added new subject.")
    @subject_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @subject_ns.expect(subject_model)
    def post(self):
        """Create a subject"""
        return create_widget_parser(widget)

    @subject_ns.response(
        HTTPStatus.OK, "Retrieved subject list.", pagination_subject_model
    )
    @subject_ns.expect(pagination_load_model)
    def get(self):
        """Get list of subjects"""
        return retrieve_widget_list_parser(widget)


@subject_ns.route("/<widget_id>", endpoint="subject")
@subject_ns.param("widget_id", "Subject id")
@subject_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@subject_ns.response(int(HTTPStatus.NOT_FOUND), "Subject not found.")
@subject_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@subject_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class Subject(Resource):
    """Handles HTTP requests to URL: /subjects/{widget_id}."""

    @subject_ns.response(int(HTTPStatus.OK), "Retrieved subject.", subject_model)
    def get(self, widget_id):
        """Retrieve a subject."""
        return widget.retrieve_widget(widget_id)

    @subject_ns.response(int(HTTPStatus.OK), "Subject was updated.", subject_model)
    @subject_ns.response(int(HTTPStatus.CREATED), "Added new subject.")
    @subject_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @subject_ns.expect(subject_model)
    def put(self, widget_id):
        """Update a subject."""
        return update_widget_parser(widget, widget_id)

    @subject_ns.response(int(HTTPStatus.NO_CONTENT), "Subject was deleted.")
    @subject_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a subject."""
        return widget.delete_widget(widget_id)
