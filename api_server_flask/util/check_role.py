import os


def is_student(role):
    return role == os.getenv("ROLE_STUDENT")


def is_tutor(role):
    return role == os.getenv("ROLE_TUTOR")


def is_deans_office(role):
    return role == os.getenv("ROLE_DECANAT")
