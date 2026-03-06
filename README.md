# University Ranking Web API (Ninja Branch)

This branch contains the **Django Ninja** implementation of the Project.

## 🛠 Tech Stack
- **Django**: Core framework.
- **Django Ninja**: Fast API framework with Pydantic schemas.
- **PostgreSQL**: Production database.
- **HttpBearer**: Simple token-based authentication.
- **Native OpenAPI**: Documentation built directly into Ninja.

## 📥 Sample Data Source
You can find sample CSV data structure here:
- **Direct CSV Link (Kaggle)**: [cwurData.csv](https://raw.githubusercontent.com/yannick-mieleszko/world-university-rankings/master/cwurData.csv)
- **Repo Link**: [Kaggle World University Rankings](https://www.kaggle.com/datasets/mylesoneill/world-university-rankings)

## 🐳 Production Deployment (Docker)
This project is production-ready with Docker:
1. **Build and Run**:
   ```bash
   docker build -t university-api .
   docker run -p 8000:8000 -e DATABASE_URL="your_postgresql_url" university-api
   ```

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
