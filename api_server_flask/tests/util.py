from flask import url_for

LOGIN = "yakhina.ee"
PASSWORD = "yakhina.ee123"


def login_user(test_client, login=LOGIN, password=PASSWORD):
    return test_client.post(
        url_for("api.auth_login"),
        data=f"login={login}&password={password}",
        content_type="application/x-www-form-urlencoded",
    )
