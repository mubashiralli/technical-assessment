def get_mock_data():
    return {
        "students": [
            {
                "id": 1007717,
                "first_name": "John",
                "last_name": "Smith",
            "email": "john.smith@example.ac.uk",
            "mail_optin": False,
            "enrolments": [
                {
                    "programme_id": 560883,
                    "title": "Introducing Mapping, Spatial Data and GIS",
                    "start_date": "2023-10-06",
                }
            ],
        },
        {
            "id": 1007718,
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.ac.uk",
            "mail_optin": True,
            "enrolments": [
                {
                    "programme_id": 560883,
                    "title": "Introducing Mapping, Spatial Data and GIS",
                    "start_date": "2023-10-06",
                },
                {
                    "programme_id": 560884,
                    "title": "Discovering String Quartets",
                    "start_date": "2024-01-15",
                },
            ],
        },
        {
            "id": 1007719,
            "first_name": "Ahmed",
            "last_name": "Khan",
            "email": "ahmed.khan@example.ac.uk",
            "mail_optin": False,
            "enrolments": [],
        },
        {
            "id": 1007720,
            "first_name": "Maria",
            "last_name": "Garcia",
            "email": "maria.garcia@example.ac.uk",
            "mail_optin": True,
            "enrolments": [
                {
                    "programme_id": 560885,
                    "title": "Building a Habitable Planet: A Brief History of the Earth",
                    "start_date": "2024-03-01",
                }
            ],
        },
        {
            "id": 1007721,
            "first_name": "David",
            "last_name": "Chen",
            "email": "david.chen@example.ac.uk",
            "mail_optin": False,
            "enrolments": [
                {
                    "programme_id": 560884,
                    "title": "Discovering String Quartets",
                    "start_date": "2024-01-15",
                }
            ],
        },
    ]
}
