# University Ranking Web API

A RESTful Web API built with Django, Django REST Framework, and PostgreSQL to track and manage global university rankings.

## Requirements
- Python 3.10+
- PostgreSQL
- Virtual environment (recommended)

## Setup Instructions

1. **Clone the repository** (if applicable) and navigate to the project root.
2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Database**:
   Update the `.env` file with your PostgreSQL credentials:
   ```env
   DB_NAME=university_db
   DB_USER=postgres
   DB_PASSWORD=yourpassword
   DB_HOST=localhost
   DB_PORT=5432
   ```
5. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```
6. **Seed Data**:
   ```bash
   python manage.py seed_data
   ```
7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## API Documentation
Once the server is running, you can access the documentation at:
- **Swagger UI**: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- **Redoc**: [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)

## Features
- Full CRUD operations for Universities and Rankings.
- JWT Authentication for secure endpoints.
- Filtering by country, city, and year.
- Interactive API documentation with Swagger.
