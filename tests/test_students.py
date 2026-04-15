import pathlib
import sys
from typing import Generator

import pytest
from fastapi.testclient import TestClient

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from app import main, services
from app.mock_data import get_mock_data

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_in_memory_db() -> Generator[None, None, None]:
    test_db = services.InMemoryDatabase()
    main.app.dependency_overrides[services.get_db] = lambda: test_db
    yield
    main.app.dependency_overrides.clear()


def test_get_students_returns_seeded_data() -> None:
    response = client.get("/students")

    assert response.status_code == 200
    payload = response.json()
    seeded_data = get_mock_data()

    assert "students" in payload
    assert len(payload["students"]) == len(seeded_data["students"])
    assert payload["students"][0]["email"] == seeded_data["students"][0]["email"]


def test_post_students_adds_new_student() -> None:
    new_student = {
        "id": 2000001,
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@example.ac.uk",
        "mail_optin": True,
        "enrolments": [],
    }

    create_response = client.post("/students", json=new_student)
    assert create_response.status_code == 201
    assert create_response.json()["email"] == new_student["email"]

    list_response = client.get("/students")
    students = list_response.json()["students"]
    seeded_data = get_mock_data()

    assert len(students) == len(seeded_data["students"]) + 1
    assert any(student["email"] == new_student["email"] for student in students)


def test_post_students_duplicate_email_returns_409() -> None:
    duplicate_student = {
        "id": 2000002,
        "first_name": "Bob",
        "last_name": "Taylor",
        "email": get_mock_data()["students"][0]["email"],
        "mail_optin": False,
        "enrolments": [],
    }

    response = client.post("/students", json=duplicate_student)

    assert response.status_code == 409
    assert response.json()["detail"] == "Student Email already exists."
