from http import HTTPStatus
from api_server_flask.api import db
from flask import jsonify, url_for
from flask_restx import Namespace
from api_server_flask.api.auth.decorators import token_required, admin_token_required
from api_server_flask.util.widget.dto import (
    PaginationSchema,
    WidgetSchema,
    PaginationLoadScheme,
    widget_model,
    pagination_load_model,
    pagination_links_model,
    pagination_model,
)
from api_server_flask.util.schema_load import parser_schema_load


class Widget:
    """Class for simple action on model"""

    def __init__(
        self,
        model: db.Model,
        url,
        url_list,
        name,
        schema=None,
        pagination_schema=None,
        order_by_field=None,
    ):
        self.Model = model
        self.url = url
        self.url_list = url_list
        self.name = name
        self.order_by_field = order_by_field
        if schema is None:
            schema = WidgetSchema
        self.schema = schema
        if pagination_schema is None:
            pagination_schema = PaginationSchema
        self.pagination_schema = pagination_schema

    def __str__(self):
        """Informal string representation of a widget."""
        return self.name

    def __repr__(self):
        """Official string representation of a widget."""
        return f"<Widget name={self.name} model={self.Model}>"

    @admin_token_required
    def create_widget(self, widget_dict):
        widget = self.Model(**widget_dict)
        db.session.add(widget)
        db.session.commit()
        response = jsonify(
            status="success",
            message=f"New {self.name} added: {widget.id}.",
            widget_id=widget.id,
        )
        response.status_code = HTTPStatus.CREATED
        response.headers["Location"] = url_for(self.url, widget_id=widget.id)
        return response

    @admin_token_required
    def retrieve_widget_list(self, page, per_page):
        model = self.Model.query.order_by(self.order_by_field) if self.order_by_field is not None else self.Model.query
        pagination = model.paginate(page, per_page, error_out=False)
        for item in pagination.items:
            setattr(item, "link", url_for(self.url, widget_id=item.id))
        pagination_schema = self.pagination_schema()
        response_data = pagination_schema.dump(pagination)
        response_data["links"] = self._pagination_nav_links(pagination)
        response = jsonify(response_data)
        response.headers["Link"] = self._pagination_nav_header_links(pagination)
        response.headers["Total-Count"] = pagination.total
        return response

    @token_required
    def retrieve_widget(self, widget_id):
        widget = self.Model.query.get_or_404(
            widget_id, description=f"{widget_id} not found in database."
        )
        return self.schema().dump(widget)

    @admin_token_required
    def update_widget(self, widget_id, role_dict):
        widget = self.Model.query.get(widget_id)
        if widget:
            for k, v in role_dict.items():
                setattr(widget, k, v)
            db.session.commit()
            message = f"'{widget_id}' was successfully updated"
            response_dict = dict(status="success", message=message)
            return response_dict, HTTPStatus.OK
        return self.create_widget(role_dict)

    @admin_token_required
    def delete_widget(self, widget_id):
        widget = self.Model.query.get_or_404(
            widget_id, description=f"{widget_id} not found in database."
        )
        db.session.delete(widget)
        db.session.commit()
        return "", HTTPStatus.NO_CONTENT

    def _pagination_nav_links(self, pagination):
        nav_links = {}
        per_page = pagination.per_page
        this_page = pagination.page
        last_page = pagination.pages
        nav_links["self"] = url_for(self.url_list, page=this_page, per_page=per_page)
        nav_links["first"] = url_for(self.url_list, page=1, per_page=per_page)
        if pagination.has_prev:
            nav_links["prev"] = url_for(
                self.url_list, page=this_page - 1, per_page=per_page
            )
        if pagination.has_next:
            nav_links["next"] = url_for(
                self.url_list, page=this_page + 1, per_page=per_page
            )
        nav_links["last"] = url_for(self.url_list, page=last_page, per_page=per_page)
        return nav_links

    def _pagination_nav_header_links(self, pagination):
        url_dict = self._pagination_nav_links(pagination)
        link_header = ""
        for rel, url in url_dict.items():
            link_header += f'<{url}>; rel="{rel}", '
        return link_header.strip().strip(",")


def add_models(
    ns: Namespace, model=widget_model, pagination=pagination_model, rest_models=None
):
    ns.models[model.name] = model
    ns.models[pagination_load_model.name] = pagination_load_model
    ns.models[pagination_links_model.name] = pagination_links_model
    ns.models[pagination.name] = pagination
    if rest_models:
        for i_model in rest_models:
            ns.models[i_model.name] = i_model


def create_widget_parser(widget: Widget):
    data = parser_schema_load(widget.schema())
    return widget.create_widget(data)


def retrieve_widget_list_parser(widget: Widget):
    data = parser_schema_load(PaginationLoadScheme())
    if isinstance(data, tuple):
        return data
    page = data.get("page")
    per_page = data.get("per_page")
    return widget.retrieve_widget_list(page, per_page)


def update_widget_parser(widget: Widget, widget_id):
    data = parser_schema_load(widget.schema())
    return widget.update_widget(widget_id, data)
