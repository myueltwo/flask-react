"""Unit test for requests sent to api.group and api.group_list API endpoint"""

from api_server_flask.tests.widget.util import Widget


class TestWidget(Widget):
    url = "api.type_grade"
    url_list = "api.type_grade_list"
    name = "type's grade"
