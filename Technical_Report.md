# Project Technical Report: University Ranking Web API

## 1. Introduction
This project implements a data-driven RESTful Web API for tracking and managing global university rankings. It fulfills the requirements specified in the project brief, focusing on robustness, security, and clear documentation.

## 2. Technical Stack
- **Backend Framework**: Django & Django REST Framework (DRF)
- **Database**: PostgreSQL (configured for production-ready data persistence)
- **Authentication**: JWT (JSON Web Token) via `djangorestframework-simplejwt`
- **Documentation**: OpenAPI 3.0 via `drf-spectacular`

## 3. Architectural Choices
- **RESTful Principles**: The API follows standard REST conventions for resource naming and HTTP methods.
- **Model-View-Serializer Pattern**: DRF's ViewSets and Serializers are used to maintain a clean separation of concerns.
- **Security**: JWT authentication is required for all data modification requests (POST/PUT/DELETE), while Read operations are publicly accessible as per `IsAuthenticatedOrReadOnly`.

## 4. Challenges and Solutions
- **Complex Hierarchical Data**: Managing the relationship between universities and their historical rankings. This was addressed using nested serializers and optimized database queries (`prefetch_related`).

## 5. Generative AI Usage Declaration
- **Tool**: Gemini 2.0 (Antigravity Agent)
- **Reason**: Planning, boilerplate generation, and debugging assistance.
- **Evidence**: The AI helped design the initial database schema and assisted in resolving system-level dependency issues during setup.
