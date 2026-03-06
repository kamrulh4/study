# Project Worklog: University Ranking Web API

This document provides a detailed log of the development process for both the **Main (Django REST Framework)** branch and the **Django Ninja** experimental branch.

## 📅 Project Timeline

### Phase 1: Planning & Setup
- **Requirement Analysis**: Read `Task.pdf` and outlined core requirements (CRUD, Auth, Docs, Public Dataset).
- **Initialization**: Initialized Django project named `app` and the `universities` app.
- **Environment**: Setup virtual environment and `requirements.txt`.
- **Git Init**: Initialized Git repository with base configuration.

### Phase 2: Core implementation (Main Branch - DRF)
- **Data Modeling**: Defined `University` and `Ranking` models with relational integrity.
- **REST features (DRF)**:
    - Implemented `ModelSerializers`.
    - Created `ModelViewSets` for full CRUD.
    - Configured `SimpleJWT` for authentication.
    - Integrated `drf-spectacular` for OpenAPI/Swagger docs.
- **Seeding**: Created a custom management command `seed_data` to populate initial dataset.
- **Verification**: Built and ran unit tests using `APIClient`.

### Phase 3: Modernization (feat/django-ninja Branch)
- **Migration**: Branched to `feat/django-ninja` to explore a more modern, performant alternative.
- **Ninja Implementation**:
    - Replaced Serializers with Pydantic-based `ModelSchema`.
    - Converted ViewSets to function-based API decorators.
    - Implemented Bearer Token authentication.
    - simplified URL structure.
- **Verification**: Refactored tests to use standard `django.test.Client` for Ninja compatibility.

---

## 🛠 Branch Comparison

| Feature | Main (DRF) | feat/django-ninja |
|---------|------------|-------------------|
| **Framework** | Django REST Framework | Django Ninja |
| **Validation** | DRF Serializers | Pydantic Schemas |
| **Auth** | JWT (SimpleJWT) | Bearer Token (Custom) |
| **Docs** | drf-spectacular | Built-in Ninja Docs |
| **Philosophy** | Industry Standard / Robust | Modern / Fast / Type-safe |

## 📦 Deliverables Produced
- Fully functional Django API.
- Integrated Swagger UI documentation.
- Automated Test Suite.
- `README.md` and `Technical_Report.md`.
- Comprehensive Git History.
