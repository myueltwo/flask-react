from flask import url_for

LOGIN = "yakhina.ee"
PASSWORD = "yakhina.ee123"
ADMIN_LOGIN = "urazbakhtina.yo"
ADMIN_PASSWORD = "urazbakhtina.yo123"
BAD_REQUEST = "Input payload validation failed"
UNAUTHORIZED = "Unauthorized"
FORBIDDEN = "You are not an administrator"
WWW_AUTH_NO_TOKEN = 'Bearer realm="registered_users@mydomain.com"'

DEFAULT_ROLE_NAME = "some role"


def create_default_roles(db):
    import os
    from api_server_flask.api.models.role import Role

    role_student = Role(id=os.getenv("ROLE_STUDENT"), name="Студент")
    role_tutor = Role(id=os.getenv("ROLE_TUTOR"), name="Преподаватель")
    role_deans_office = Role(id=os.getenv("ROLE_DECANAT"), name="Деканат")
    db.session.add_all([role_student, role_tutor, role_deans_office])
    db.session.commit()


def login_user(test_client, login=LOGIN, password=PASSWORD):
    return test_client.post(
        url_for("api.auth_login"),
        data=f"login={login}&password={password}",
        content_type="application/x-www-form-urlencoded",
    )


def logout_user(test_client, access_token):
    return test_client.post(
        url_for("api.auth_logout"), headers={"Authorization": f"Bearer {access_token}"}
    )


def get_user(test_client, access_token):
    return test_client.get(
        url_for("api.auth_user"), headers={"Authorization": f"Bearer {access_token}"}
    )


def create_role(test_client, access_token, role_name=DEFAULT_ROLE_NAME):
    return test_client.post(
        url_for("api.role_list"),
        headers={"Authorization": f"Bearer {access_token}"},
        data=f"name={role_name}",
        content_type="application/x-www-form-urlencoded",
    )
