"""Unit test for requests sent to api.activity_sub_type and
api.activity_sub_type_list API endpoint"""

from api_server_flask.tests.widget.util import Widget


class TestWidget(Widget):
    url = "api.activity_sub_type"
    url_list = "api.activity_sub_type_list"
    name = "subtype's activities"
