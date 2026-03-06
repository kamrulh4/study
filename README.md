# University Ranking Web API (Django REST Framework)

This is the **main** branch containing the production-ready implementation using **Django REST Framework (DRF)**.

## 🛠 Tech Stack
- **Backend**: Django & DRF
- **Database**: PostgreSQL
- **Auth**: JWT (SimpleJWT)
- **Docs**: Swagger UI / Redoc (drf-spectacular)

## 📦 Requirements Fulfillment
- **CRUD Operations**: Complete for Universities and Rankings.
- **RESTful Design**: Standard HTTP methods and status codes used.
- **Security**: JWT Authentication required for POST/PUT/DELETE.
- **Public Data**: Integrated with Kaggle "World University Rankings".

## 🚀 Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

## 📖 Documentation
- **Swagger**: `http://127.0.0.1:8000/api/docs/`
- **Redoc**: `http://127.0.0.1:8000/api/redoc/`
