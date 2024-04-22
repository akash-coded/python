# User Service

This microservice handles user-related functionalities such as user registration, authentication, and user profile management.

## Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```

2. Activate the virtual environment:
   ```bash
   source myenv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `/users/`: Create a new user or retrieve a list of users.
- `/users/{id}/`: Retrieve, update, or delete a specific user.

For more details on the API endpoints and request/response formats, please refer to the API documentation.