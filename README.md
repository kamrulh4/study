# University Ranking Web API (Main Branch - DRF)

This branch contains the **Django REST Framework (DRF)** implementation of the Project.

## 🛠 Tech Stack
- **Django**: Core framework.
- **Django REST Framework**: For building the API.
- **PostgreSQL**: Production database (SQLite used for local dev).
- **SimpleJWT**: For Token-based Authentication.
- **drf-spectacular**: For Swagger/OpenAPI documentation.

## 📥 Sample Data Source
You can find sample CSV data structure here:
- **Direct CSV Link (Kaggle)**: [cwurData.csv](https://raw.githubusercontent.com/yannick-mieleszko/world-university-rankings/master/cwurData.csv)
- **Repo Link**: [Kaggle World University Rankings](https://www.kaggle.com/datasets/mylesoneill/world-university-rankings)

## 🚀 Setup & Launch
1. **Prepare Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Run Migrations & Seed**:
   ```bash
   python manage.py migrate
   python manage.py seed_data
   ```
3. **Authentication**:
   - Get token: `POST /api/token/` with credentials.
   - Use token: `Authorization: Bearer <your_token>`

4. **Documentation**:
   - Visit: `http://127.0.0.1:8000/api/docs/`
