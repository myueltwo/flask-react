"""Test cases for GET requests sent to the api.role_list API endpoint."""
from http import HTTPStatus

from api_server_flask.tests.util import (
    ADMIN_LOGIN,
    ADMIN_PASSWORD,
    login_user,
    create_role,
    retrieve_role_list,
    STUDENT_ROLE_NAME,
    TUTOR_ROLE_NAME,
    ADMIN_ROLE_NAME,
)

NAMES = [
    "role1",
    "second_role",
    "role-thrice",
    "tetraROLE",
    "PENTA-role-GON-et",
    "hexa_role",
]


def test_retrieve_paginated_role_list(client, db, admin):
    response = login_user(client, login=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    assert "access_token" in response.json
    access_token = response.json["access_token"]

    # ADD SIX ROLE INSTANCES TO DATABASE
    for i in range(0, len(NAMES)):
        response = create_role(
            client,
            access_token,
            role_name=NAMES[i],
        )
        assert response.status_code == HTTPStatus.CREATED

    names_with_default = [STUDENT_ROLE_NAME, TUTOR_ROLE_NAME, ADMIN_ROLE_NAME]
    names_with_default.extend(NAMES)
    total_count_roles = len(names_with_default)

    # REQUEST PAGINATED LIST OF ROLES: 5 PER PAGE, PAGE #1
    response = retrieve_role_list(client, access_token, page=1, per_page=5)
    assert response.status_code == HTTPStatus.OK

    # VERIFY PAGINATION ATTRIBUTES FOR PAGE #1
    assert "has_prev" in response.json and not response.json["has_prev"]
    assert "has_next" in response.json and response.json["has_next"]
    assert "page" in response.json and response.json["page"] == 1
    assert "total_pages" in response.json and response.json["total_pages"] == 2
    assert "items_per_page" in response.json and response.json["items_per_page"] == 5
    assert (
        "total_items" in response.json
        and response.json["total_items"] == total_count_roles
    )
    assert "items" in response.json and len(response.json["items"]) == 5

    # VERIFY ATTRIBUTES OF ROLES #1-5
    for i in range(0, len(response.json["items"])):
        item = response.json["items"][i]
        assert "name" in item and item["name"] == names_with_default[i]

    # REQUEST PAGINATED LIST OF WIDGETS: 5 PER PAGE, PAGE #2
    response = retrieve_role_list(client, access_token, page=2, per_page=5)
    assert response.status_code == HTTPStatus.OK

    # VERIFY PAGINATION ATTRIBUTES FOR PAGE #2
    assert "has_prev" in response.json and response.json["has_prev"]
    assert "has_next" in response.json and not response.json["has_next"]
    assert "page" in response.json and response.json["page"] == 2
    assert "total_pages" in response.json and response.json["total_pages"] == 2
    assert "items_per_page" in response.json and response.json["items_per_page"] == 5
    assert (
        "total_items" in response.json
        and response.json["total_items"] == total_count_roles
    )
    assert "items" in response.json and len(response.json["items"]) == 4

    # VERIFY ATTRIBUTES OF ROLES #6-9
    for i in range(5, response.json["total_items"]):
        item = response.json["items"][i - 5]
        assert "name" in item and item["name"] == names_with_default[i]

    # REQUEST PAGINATED LIST OF WIDGETS: 10 PER PAGE, PAGE #1
    response = retrieve_role_list(client, access_token, page=1, per_page=10)
    assert response.status_code == HTTPStatus.OK

    # VERIFY PAGINATION ATTRIBUTES FOR PAGE #1
    assert "has_prev" in response.json and not response.json["has_prev"]
    assert "has_next" in response.json and not response.json["has_next"]
    assert "page" in response.json and response.json["page"] == 1
    assert "total_pages" in response.json and response.json["total_pages"] == 1
    assert "items_per_page" in response.json and response.json["items_per_page"] == 10
    assert (
        "total_items" in response.json
        and response.json["total_items"] == total_count_roles
    )
    assert "items" in response.json and len(response.json["items"]) == total_count_roles

    # VERIFY ATTRIBUTES OF ROLES #1-9
    for i in range(0, len(response.json["items"])):
        item = response.json["items"][i]
        assert "name" in item and item["name"] == names_with_default[i]

    # REQUEST PAGINATED LIST OF ROLES: DEFAULT PARAMETERS
    response = retrieve_role_list(client, access_token)
    assert response.status_code == HTTPStatus.OK

    # VERIFY PAGINATION ATTRIBUTES FOR PAGE #1
    assert "has_prev" in response.json and not response.json["has_prev"]
    assert "has_next" in response.json and not response.json["has_next"]
    assert "page" in response.json and response.json["page"] == 1
    assert "total_pages" in response.json and response.json["total_pages"] == 1
    assert "items_per_page" in response.json and response.json["items_per_page"] == 10
    assert (
        "total_items" in response.json
        and response.json["total_items"] == total_count_roles
    )
    assert "items" in response.json and len(response.json["items"]) == total_count_roles

    # VERIFY ATTRIBUTES OF WIDGETS #1-9
    for i in range(0, len(response.json["items"])):
        item = response.json["items"][i]
        assert "name" in item and item["name"] == names_with_default[i]
