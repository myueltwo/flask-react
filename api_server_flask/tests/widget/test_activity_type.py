"""Unit test for requests sent to api.activity_type and
api.activity_type_list API endpoint"""

from api_server_flask.tests.widget.util import Widget


class TestWidget(Widget):
    url = "api.activity_type"
    url_list = "api.activity_type_list"
    name = "type's activities"
