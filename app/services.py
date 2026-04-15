from __future__ import annotations

from copy import deepcopy
from typing import List, Optional

from app.mock_data import get_mock_data
from app.models import Student


class InMemoryDatabase:
    def __init__(self) -> None:
        self._students: List[Student] = [
            Student.model_validate(student)
            for student in deepcopy(get_mock_data()["students"])
        ]
        self._emails = {student.email for student in self._students}

    def list_students(self, mail_optin: Optional[bool] = None) -> List[Student]:
        if mail_optin is None:
            return list(self._students)

        return [
            student for student in self._students if student.mail_optin == mail_optin
        ]

    def _if_email_exists(self, email: str) -> bool:
        return email in self._emails

    def add_student(self, student: Student) -> bool:
        if self._if_email_exists(student.email):
            return False
        self._students.append(student)
        self._emails.add(student.email)
        return True


db = InMemoryDatabase()


def get_db() -> InMemoryDatabase:
    return db
