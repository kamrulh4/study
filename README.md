# University Ranking Web API (Django Ninja)

This is the **feat/django-ninja** branch containing the high-performance implementation using **Django Ninja**.

## 🛠 Tech Stack
- **Backend**: Django & Django Ninja
- **Database**: PostgreSQL
- **Auth**: Bearer Token
- **Docs**: Native OpenAPI/Swagger

## 📦 Requirements Fulfillment
- **Full CRUD**: Implemented via Ninja path decorators.
- **Modern Architecture**: Uses Python type-hints and Pydantic.
- **Speed**: Optimized for fast serialization.
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
- **Swagger UI**: `http://127.0.0.1:8000/api/v1/docs`
