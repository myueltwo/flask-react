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
STUDENT_ROLE_NAME = "Студент"
TUTOR_ROLE_NAME = "Преподаватель"
ADMIN_ROLE_NAME = "Деканат"


def create_default_roles(db):
    import os
    from api_server_flask.api.models.role import Role

    role_student_id, role_tutor_id, role_deans_office_id = (
        os.getenv("ROLE_STUDENT"),
        os.getenv("ROLE_TUTOR"),
        os.getenv("ROLE_DECANAT"),
    )

    if not Role.query.get(role_student_id):
        role_student = Role(id=os.getenv("ROLE_STUDENT"), name=STUDENT_ROLE_NAME)
        db.session.add(role_student)
    if not Role.query.get(role_tutor_id):
        role_tutor = Role(id=os.getenv("ROLE_TUTOR"), name=TUTOR_ROLE_NAME)
        db.session.add(role_tutor)
    if not Role.query.get(role_deans_office_id):
        role_deans_office = Role(id=os.getenv("ROLE_DECANAT"), name=ADMIN_ROLE_NAME)
        db.session.add(role_deans_office)
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


def retrieve_role_list(test_client, access_token, page=None, per_page=None):
    return test_client.get(
        url_for("api.role_list", page=page, per_page=per_page),
        headers={"Authorization": f"Bearer {access_token}"},
    )


def retrieve_role(test_client, access_token, role_id):
    return test_client.get(
        url_for("api.role", role_id=role_id),
        headers={"Authorization": f"Bearer {access_token}"},
    )


def update_role(test_client, access_token, role_id, role_name):
    return test_client.put(
        url_for("api.role", role_id=role_id),
        headers={"Authorization": f"Bearer {access_token}"},
        data=f"name={role_name}",
        content_type="application/x-www-form-urlencoded",
    )
