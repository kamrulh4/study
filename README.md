# University Ranking Web API

### Project Progress
- **V1 (DRF)**: Initial prototyping with Django REST Framework.
- **V2 (Ninja)**: Migrated to Django Ninja for performance and type safety (Final Version).
- **Data Integration**: Successfully integrated QS World University Rankings 2026 dataset (1,501 entries).
- **Infrastructure**: Fully Dockerized with PostgreSQL 18 and automated Healthchecks.

### Source Control
- **main**: Current production-ready codebase (Django Ninja).

## 🛠 Tech Stack
- **Django 6.0**: Modern core framework.
- **Django Ninja**: Fast API with Pydantic and Python 3.13 types.
- **PostgreSQL 18**: Latest production-grade relational database.
- **Docker Compose**: Multi-container orchestration.

## 📥 Data Sources
This project uses data derived from:
- **QS World University Rankings 2026** ([Kaggle Dataset](https://www.kaggle.com/datasets/akashbommidi/2026-qs-world-university-rankings))
- **Times Higher Education (THE)** World University Rankings.

## 🐳 Launch with Docker Compose
The easiest way to run the entire stack (App + DB) is using Docker Compose:
```bash
docker-compose up --build
```
- **API URL**: `http://localhost:8001/api/v1/universities`
- **Database**: PostgreSQL 18 running on port 5435.

## 🗄 Database Configuration
The API supports **PostgreSQL**. Set the `DATABASE_URL` environment variable:
- Format: `postgres://user:password@host:port/dbname`
- Fallback: Uses `db.sqlite3` if no URL is provided.

## 📄 Project Documentation
- **[Technical Report](Technical_Report.md)**: 5-page detailed architectural and design report.
- **[API Documentation](API_Documentation.md)**: Full list of endpoints, schemas, and authentication.
- **[Task List](file:///Users/kamrul/.gemini/antigravity/brain/296927a7-795f-4379-bd6a-7977710d92a5/task.md)**: Evolution of project tasks.

> [!NOTE]
> Per requirement, the `API_Documentation.md` should be converted to **PDF** for the final submission.

## 🚀 Local Setup & Launch
1. **Prepare Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```
3. **Authentication**:
   - Token-based Header: `Authorization: Bearer ninja-token-2024`

4. **Interactive Docs**:
   - Visit: `http://127.0.0.1:8000/api/v1/docs`
