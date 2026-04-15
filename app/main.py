from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Query, status

from app.models import Student, StudentListResponse
from app.services import get_db

app = FastAPI(title="Technical Assessment API", version="1.0.0")


@app.get(
    "/",
    summary="API status",
    description="Returns a small status payload with links to the interactive docs.",
)
def root() -> dict[str, str]:
    return {"message": "Technical Assessment API is running", "Swagger UI": "/docs", "Redoc": "/redoc"}


@app.get(
    "/students",
    response_model=StudentListResponse,
    summary="List students",
    description="Returns all students, or filters them by `mail_optin` when the query parameter is provided.",
    response_description="A list of students matching the requested filter.",
)
def list_students(
    mail_optin: Optional[bool] = Query(
        default=None,
        description="Optional filter for the student's email opt-in preference.",
    ),
    db=Depends(get_db),
) -> StudentListResponse:
    return StudentListResponse(students=db.list_students(mail_optin=mail_optin))


@app.post(
    "/students",
    summary="Create student",
    description="Creates a new student record and triggers a mock Mailchimp sync after persistence.",
    response_description="The student that was created.",
    status_code=status.HTTP_201_CREATED,
)
async def create_student(student: Student, db=Depends(get_db)) -> Student:
    if not db.add_student(student):
        raise HTTPException(status_code=409, detail=f"Student Email already exists.")

    # Trigger mock Mailchimp sync after successful student creation
    def sync_to_mailchimp(student_data) -> None:
        print(f"Mock Mailchimp sync successful for student: {student_data}")

    sync_to_mailchimp(student.model_dump())
    return student
