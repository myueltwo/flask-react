from http import HTTPStatus
from api_server_flask.api.models.role import Role
from api_server_flask.api import db
from flask import jsonify, url_for
from api_server_flask.api.auth.decorators import token_required, admin_token_required
from api_server_flask.api.roles.dto import PaginationSchema, RoleSchema


@admin_token_required
def create_role(role_dict):
    name = role_dict.get("name")
    role = Role(**role_dict)
    db.session.add(role)
    db.session.commit()
    response = jsonify(
        status="success", message=f"New role added: {name}.", role_id=role.id
    )
    response.status_code = HTTPStatus.CREATED
    response.headers["Location"] = url_for("api.role", role_id=role.id)
    return response


@token_required
def retrieve_role_list(page, per_page):
    pagination = Role.query.paginate(page, per_page, error_out=False)
    for item in pagination.items:
        setattr(item, "link", url_for("api.role", role_id=item.id))
    pagination_schema = PaginationSchema()
    response_data = pagination_schema.dump(pagination)
    response_data["links"] = _pagination_nav_links(pagination)
    response = jsonify(response_data)
    response.headers["Link"] = _pagination_nav_header_links(pagination)
    response.headers["Total-Count"] = pagination.total
    return response


@token_required
def retrieve_role(role_id):
    role = Role.query.get_or_404(
        role_id, description=f"{role_id} not found in database."
    )
    return RoleSchema().dump(role)


@admin_token_required
def update_role(role_id, role_dict):
    role = Role.query.get(role_id)
    if role:
        for k, v in role_dict.items():
            setattr(role, k, v)
        db.session.commit()
        message = f"'{role_id}' was successfully updated"
        response_dict = dict(status="success", message=message)
        return response_dict, HTTPStatus.OK
    return create_role(role_dict)


@admin_token_required
def delete_role(role_id):
    role = Role.query.get_or_404(
        role_id, description=f"{role_id} not found in database."
    )
    db.session.delete(role)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT


def _pagination_nav_links(pagination):
    nav_links = {}
    per_page = pagination.per_page
    this_page = pagination.page
    last_page = pagination.pages
    nav_links["self"] = url_for("api.role_list", page=this_page, per_page=per_page)
    nav_links["first"] = url_for("api.role_list", page=1, per_page=per_page)
    if pagination.has_prev:
        nav_links["prev"] = url_for(
            "api.role_list", page=this_page - 1, per_page=per_page
        )
    if pagination.has_next:
        nav_links["next"] = url_for(
            "api.role_list", page=this_page + 1, per_page=per_page
        )
    nav_links["last"] = url_for("api.role_list", page=last_page, per_page=per_page)
    return nav_links


def _pagination_nav_header_links(pagination):
    url_dict = _pagination_nav_links(pagination)
    link_header = ""
    for rel, url in url_dict.items():
        link_header += f'<{url}>; rel="{rel}", '
    return link_header.strip().strip(",")
