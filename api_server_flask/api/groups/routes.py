"""API endpoint definitions for /group namespace"""
from http import HTTPStatus

from flask_restx import Namespace, Resource

group_ns = Namespace(
    name="group", description="Store of groups by students", validate=True
)


@group_ns.route("", endpoint="group_list")
class GroupList(Resource):
    """Handles HTTP requests to URL: /api/v1/groups."""

    @group_ns.response(int(HTTPStatus.CREATED), "Added new role.")
    @group_ns.response(int(HTTPStatus.FORBIDDEN), "Administrator token required.")
    # @group_ns.expect(role_model, validate=False)
    def post(self):
        """Create a group"""
        pass
        # data = parser_schema_load(RoleSchema())
        # return create_role(data)

    # @role_ns.response(HTTPStatus.OK, "Retrieved role list.", pagination_model)
    # @role_ns.expect(pagination_load_model, validate=False)
    def get(self):
        """Get list of groups"""
        pass
        # data = parser_schema_load(PaginationLoadScheme())
        # page = data.get("page")
        # per_page = data.get("per_page")
        # return retrieve_role_list(page, per_page)
