"""Unit test for requests sent to api.attendance_type and
api.attendance_type_list API endpoint"""

from api_server_flask.tests.widget.util import Widget


class TestWidget(Widget):
    url = "api.attendance_type"
    url_list = "api.attendance_type_list"
    name = "type's attendance"
