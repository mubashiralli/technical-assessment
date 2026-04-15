# Technical Assessment API

Small FastAPI service backed by an in-memory data store initialized from mock data.

## Requirements

- Python 3.9+
- `pip`

## Installation

From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run The API

From the project root:

```bash
uvicorn main:app --reload
```

API endpoints and docs:

- API base: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Postman Testing

### 1. Get all students

- Method: `GET`
- URL: `http://127.0.0.1:8000/students`

Optional query parameter:

- `mail_optin=true`
- `mail_optin=false`

Example:

- `GET http://127.0.0.1:8000/students?mail_optin=true`

### 2. Create a new student

- Method: `POST`
- URL: `http://127.0.0.1:8000/students`
- Headers: `Content-Type: application/json`

Sample payload:

```json
{
  "id": 2000001,
  "first_name": "Alice",
  "last_name": "Johnson",
  "email": "alice.johnson@example.ac.uk",
  "mail_optin": true,
  "enrolments": [
    {
      "programme_id": 560999,
      "title": "Intro to Data Engineering",
      "start_date": "2026-04-20"
    }
  ]
}
```

Expected response:

- Status: `201 Created`
- Body: created student payload

### 3. Duplicate email validation

If you submit an email that already exists, the API returns:

- Status: `409 Conflict`
- Body detail: `Student Email already exists.`

Sample duplicate payload:

```json
{
  "id": 2000002,
  "first_name": "Bob",
  "last_name": "Taylor",
  "email": "john.smith@example.ac.uk",
  "mail_optin": false,
  "enrolments": []
}
```

## Data Reset Behavior

This API uses an in-memory database loaded from mock data.

- Data is reset whenever the app process restarts.
- With `--reload`, code changes trigger a restart, so runtime additions are reset.

## Biggest Compromise

The app uses the provided aggregated in-memory structure rather than a normalized persistence layer.
This keeps the task small and aligned with the exercise.
In production, I would separate domain entities and persistence concerns, likely with a repository/service layer and real storage.

Also, in a production-ready application, I would separate enrolment from the student model into a separate model that holds student ID and course ID.
This makes querying faster and keeps the student model more normal and memory-efficient.
For this exercise, it was intentionally kept aligned with the provided mock database shape.
