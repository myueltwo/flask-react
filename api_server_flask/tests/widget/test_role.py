"""Test cases for requests requests sent to the api.role
and api.role_list API endpoint """
from api_server_flask.tests.widget.util import Widget
from api_server_flask.tests.util import (
    STUDENT_ROLE_NAME,
    TUTOR_ROLE_NAME,
    ADMIN_ROLE_NAME,
)


class TestWidget(Widget):
    url = "api.role"
    url_list = "api.role_list"
    name = "role"
    default_names = [
        {"name": STUDENT_ROLE_NAME},
        {"name": TUTOR_ROLE_NAME},
        {"name": ADMIN_ROLE_NAME},
    ]
