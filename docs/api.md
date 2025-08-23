# 📡 Truth or Dare API — Documentation

This document provides detailed information about the HTTP API for the **Truth or Dare API** backend.  
It contains available endpoints, request/response examples, and notes about access control.

**Base URL (development):**

```
http://127.0.0.1:8000/
```

All endpoints below are relative to the base URL.

---

## 🔑 Authentication & Access Control

- **Public (unauthenticated)** users:
    - Can read questions, categories, and rules.
    - Can fetch random questions for gameplay.
- **Admin users**:
    - Can create, update, and delete questions, categories, and rules.
    - Authentication is required (via Django/DRF session).
    - Token-based authentication is **not enabled** in this project by default.

---

## Endpoints overview

| Endpoint                 | Method           | Access           | Description                                          |
|--------------------------|------------------|------------------|------------------------------------------------------|
| `/api/questions/random/` | POST             | Public           | Get 5 random questions based on filters              |
| `/api/questions/`        | GET, POST        | Admin only       | List or create questions                             |
| `/api/questions/<id>/`   | GET, PUT, DELETE | Admin only       | Retrieve, update, or delete a question               |
| `/api/categories/`       | GET, POST        | GET — Public; POST — Admin | List all question categories / Create a new category |
| `/api/categories/<id>/`  | GET, PUT, DELETE | GET — Public; PUT/DELETE — Admin | View, update, or delete a single category            |
| `/api/rules/`            | GET              | Public           | Retrieve all rule pages                              |
| `/api/rules/<id>/`       | GET              | Public           | Retrieve a specific rule                             |

---

## 🎲 Questions API

### Fetch Random Questions

**Endpoint:**  
`POST /api/questions/random/`

**Request Body:**

```json
{
  "question_type": "dare",
  "category_ids": [
    1,
    2
  ],
  "excluded_ids": [
    5,
    12
  ]
}
```

**Response:**

```json
[
  {
    "id": 17,
    "text": "Do 10 pushups.",
    "question_type": "dare",
    "category": 1
  },
  {
    "id": 19,
    "text": "Sing a song loudly in the room.",
    "question_type": "dare",
    "category": 2
  }
]
```

> Response includes up to 5 unique questions per request.
> If fewer matching questions are available (e.g., only 2 meet the filters), then fewer will be returned.

- `question_type` — `"truth"` or `"dare"`
- `category_ids` — List of category IDs
- `excluded_ids` — Optional; list of already shown question IDs

---

## 📜 Rules Endpoints

### Get All Rules

```http
GET /api/rules/
```

**Response:**

```json
[
  {
    "id": 1,
    "text": "Players take turns clockwise."
  },
  {
    "id": 2,
    "text": "You may skip one question per game."
  }
]
```

### Get Rule by ID

```http
GET /api/rules/2/
```

**Response:**

```json
  {
  "id": 2,
  "text": "You may skip one question per game."
}
```

---

## 🗂️ Category Endpoints

### Get All Categories

```http
GET /api/categories/
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "Party",
    "is_adult": false
  },
  {
    "id": 2,
    "name": "Romantic",
    "is_adult": true
  },
  {
    "id": 3,
    "name": "Funny",
    "is_adult": false
  },
  {
    "id": 4,
    "name": "18+",
    "is_adult": true
  }
]
```

### Get Category by ID

```http
GET /api/categories/1/
```

**Response:**

```json
  {
  "id": 1,
  "name": "Party",
  "is_adult": false
}
```

---

## ❌ Error Responses

The API uses standard HTTP status codes to indicate success or failure.
Errors are always returned in JSON format with a `detail` field, and in some cases with additional context.

### Example of a validation error

```json
{
  "question_type": [
    "This field is required."
  ]
}
```

#### 404 — Not Found

Returned when the requested object does not exist.

```json
{
  "detail": "No Question matches the given query."
}
```

#### Other examples:

```json
{
  "detail": "No Rule matches the given query."
}
```

```json
{
  "detail": "No QuestionCategory matches the given query."
}
```

#### 405 — Method Not Allowed

Returned when trying to use an unsupported HTTP method for the endpoint.

```json
{
  "detail": "Method \"GET\" not allowed."
}
```
