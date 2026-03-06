# Project Technical Report: University Ranking Web API

## 1. Introduction
This project implements a data-driven RESTful Web API for tracking and managing global university rankings. It fulfills the requirements specified in the project brief, focusing on robustness, security, and clear documentation.

## 2. Technical Stack
- **Backend Framework**: Django & Django Ninja (Migrated from DRF for performance)
- **Database**: PostgreSQL
- **Authentication**: Token-based Authentication (Bearer)
- **Documentation**: OpenAPI 3.0 (Built-in Django Ninja)

## 3. Architectural Choices
- **Django Ninja**: Chosen for its speed, simplicity, and Python type-hint integration.
- **RESTful Principles**: The API follows standard REST conventions.
- **Security**: Authentication is required for all data modification requests (POST/PUT/DELETE).

## 4. Requirements Compliance Audit
Based on `Task.pdf`:
- [x] **CRUD Capabilities**: Fully implemented for Universities and Rankings.
- [x] **RESTful Design**: 5+ endpoints implemented (List, Get, Create, Update, Delete).
- [x] **Data Handling**: User inputs validated via Pydantic schemas; JSON responses returned.
- [x] **HTTP Standards**: Correct status codes (201 Created, 204 No Content, 401 Unauthorized) used.
- [x] **Public Dataset**: Integrated with "World University Rankings" (Kaggle).
- [x] **Authentication**: Bearer Token authentication implemented for secure endpoints.
- [x] **Documentation**: Interactive Swagger documentation provided at `/api/v1/docs`.
- [x] **Codebase**: Git repository initialized with clear development history.

## 5. Dataset Sources
The project is designed to be populated with data from the following public sources:
- **Kaggle**: [World University Rankings](https://www.kaggle.com/datasets/mylesoneill/world-university-rankings)
- **Kaggle**: [QS World University Rankings 2025](https://www.kaggle.com/datasets/melissamf/qs-world-university-rankings-2025)

## 6. Generative AI Usage Declaration
- **Tool**: Gemini 2.0 (Antigravity Agent)
- **Reason**: Planning, boilerplate generation, migration from DRF to Django Ninja, and requirements auditing.
