"""Unit test for requests sent to api.group and api.group_list API endpoint"""

from api_server_flask.tests.widget.util import Widget


class TestWidget(Widget):
    url = "api.group"
    url_list = "api.group_list"
    name = "group"
