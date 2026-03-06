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
   - Token is hardcoded for demo: `ninja-token-2024`
   - Use token: `Authorization: Bearer ninja-token-2024`

4. **Documentation**:
   - Visit: `http://127.0.0.1:8000/api/v1/docs`
