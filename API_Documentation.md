# API Documentation: University Ranking Web API

## 1. Authentication
The API uses **HttpBearer** authentication for all modification requests (POST, PUT, DELETE).

- **Header**: `Authorization: Bearer <token>`
- **Demo Token**: `ninja-token-2024`

> [!IMPORTANT]
> GET requests do NOT require authentication for easier data exploration.

---

## 2. Endpoints

### 2.1 Universities

#### List Universities
- **URL**: `/api/v1/universities`
- **Method**: `GET`
- **Description**: Returns a list of all universities and their associated rankings.
- **Response (200 OK)**:
  ```json
  [
    {
      "id": 1,
      "name": "Harvard University",
      "country": "USA",
      "city": "Cambridge",
      "website": "https://www.harvard.edu",
      "founded_year": 1636,
      "rankings": [...]
    }
  ]
  ```

#### Get University Detail
- **URL**: `/api/v1/universities/{id}`
- **Method**: `GET`
- **Response (200 OK)**: University object.
- **Response (404 Not Found)**: `{"detail": "Not Found"}`

#### Create University
- **URL**: `/api/v1/universities`
- **Method**: `POST`
- **Auth Required**: Yes
- **Input (JSON)**:
  ```json
  {
    "name": "New University",
    "country": "UK",
    "city": "London",
    "website": "https://newuni.ac.uk",
    "founded_year": 2024
  }
  ```
- **Response (201 Created)**: Created University object.

#### Update University
- **URL**: `/api/v1/universities/{id}`
- **Method**: `PUT`
- **Auth Required**: Yes
- **Input (JSON)**: Partial updates supported.
- **Response (200 OK)**: Updated University object.

#### Delete University
- **URL**: `/api/v1/universities/{id}`
- **Method**: `DELETE`
- **Auth Required**: Yes
- **Response (204 No Content)**: Empty body.

---

### 2.2 Rankings

#### List Rankings
- **URL**: `/api/v1/rankings`
- **Method**: `GET`
- **Description**: Returns all ranking entries across all years.

---

## 3. Error Codes

| Status Code | Meaning | Reason |
| :--- | :--- | :--- |
| **200** | OK | Request succeeded. |
| **201** | Created | Resource successfully created. |
| **204** | No Content | Resource successfully deleted. |
| **401** | Unauthorized | Missing or invalid Bearer token. |
| **404** | Not Found | Resource ID does not exist. |
| **422** | Unprocessable Entity | Validation error (check JSON schema). |

---

## 4. Example Usage (cURL)

```bash
# Get Universities
curl -X GET http://127.0.0.1:8000/api/v1/universities

# Create University (Requires Auth)
curl -X POST http://127.0.0.1:8000/api/v1/universities \
     -H "Authorization: Bearer ninja-token-2024" \
     -H "Content-Type: application/json" \
     -d '{"name": "Oxford", "country": "UK", "city": "Oxford"}'
```
