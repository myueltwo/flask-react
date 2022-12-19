"""API endpoint definitions for /type_grades namespace"""
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
from api_server_flask.api.models.type_grade import TypeGrade

type_grade_ns = Namespace(
    name="type_grade", description="Store of type's grades by students"
)
add_models(type_grade_ns)
widget = Widget(
    model=TypeGrade,
    name="type's grade",
    url="api.type_grade",
    url_list="api.type_grade_list",
)


@type_grade_ns.route("", endpoint="type_grade_list")
class TypeGradeList(Resource):
    """Handles HTTP requests to URL: /api/v1/widgets/type_grades."""

    @type_grade_ns.response(int(HTTPStatus.CREATED), "Added new type's grade.")
    @type_grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @type_grade_ns.expect(widget_model)
    def post(self):
        """Create a type's grade"""
        return create_widget_parser(widget)

    @type_grade_ns.response(
        HTTPStatus.OK, "Retrieved type's grade list.", pagination_model
    )
    @type_grade_ns.expect(pagination_load_model)
    def get(self):
        """Get list of type's grades"""
        return retrieve_widget_list_parser(widget)


@type_grade_ns.route("/<widget_id>", endpoint="type_grade")
@type_grade_ns.param("widget_id", "Type's grade id")
@type_grade_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
@type_grade_ns.response(int(HTTPStatus.NOT_FOUND), "Role not found.")
@type_grade_ns.response(int(HTTPStatus.UNAUTHORIZED), "Unauthorized.")
@type_grade_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class TypeGrade(Resource):
    """Handles HTTP requests to URL: /type_grades/{widget_id}."""

    @type_grade_ns.response(int(HTTPStatus.OK), "Retrieved type's grade.", widget_model)
    def get(self, widget_id):
        """Retrieve a type's grade."""
        return widget.retrieve_widget(widget_id)

    @type_grade_ns.response(
        int(HTTPStatus.OK), "Type's grade was updated.", widget_model
    )
    @type_grade_ns.response(int(HTTPStatus.CREATED), "Added new type's grade.")
    @type_grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    @type_grade_ns.expect(widget_model, validate=False)
    def put(self, widget_id):
        """Update a widget."""
        return update_widget_parser(widget, widget_id)

    @type_grade_ns.response(int(HTTPStatus.NO_CONTENT), "Type's grade was deleted.")
    @type_grade_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    def delete(self, widget_id):
        """Delete a widget."""
        return widget.delete_widget(widget_id)
