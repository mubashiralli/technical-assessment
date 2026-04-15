from __future__ import annotations

from datetime import date
from typing import List

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Enrolment(BaseModel):
    programme_id: int = Field(description="Unique identifier for the programme.")
    title: str = Field(description="Programme title.")
    start_date: date = Field(description="Programme start date.")


class Student(BaseModel):
    id: int = Field(description="Unique student identifier.")
    first_name: str = Field(description="Student first name.")
    last_name: str = Field(description="Student last name.")
    email: EmailStr = Field(description="Student email address.")
    mail_optin: bool = Field(
        description="Whether the student has opted into email updates."
    )
    enrolments: List[Enrolment] = Field(
        description="List of programmes the student is enrolled in."
    )


class StudentListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    students: List[Student] = Field(
        description="Collection of students returned by the API."
    )
