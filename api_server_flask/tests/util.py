from flask import url_for

LOGIN = "yakhina.ee"
PASSWORD = "yakhina.ee123"
BAD_REQUEST = "Input payload validation failed"
UNAUTHORIZED = "Unauthorized"
FORBIDDEN = "You are not an administrator"
WWW_AUTH_NO_TOKEN = 'Bearer realm="registered_users@mydomain.com"'


def login_user(test_client, login=LOGIN, password=PASSWORD):
    return test_client.post(
        url_for("api.auth_login_user"),
        data=f"login={login}&password={password}",
        content_type="application/x-www-form-urlencoded",
    )


def logout_user(test_client, access_token):
    return test_client.post(
        url_for("api.auth_logout"), headers={"Authorization": f"Bearer {access_token}"}
    )
