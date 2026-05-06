# 🎯 Truth or Dare

![Python](https://img.shields.io/badge/Python-3.11.2-blue?logo=python&style=flat-square)
![Django](https://img.shields.io/badge/Django-5.1.6-%234092E5?logo=django&logoColor=white&style=flat-square)
![DRF](https://img.shields.io/badge/DRF-3.15.2-%23456394?logo=django&logoColor=white&style=flat-square)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-%234983db?logo=postgresql&logoColor=white&style=flat-square)
![dotenv](https://img.shields.io/badge/python--dotenv-1.0.1-%23E64398?logo=python&logoColor=white&style=flat-square)

![License](https://img.shields.io/badge/License-MIT-brightgreen?style=flat-square)

**Truth or Dare API** is a lightweight, production-ready RESTful backend for the classic party game *Truth or Dare*,
built with Django REST Framework.

It provides random, categorized questions filtered by player preferences, along with game rules and content filtering (
e.g. 18+ categories). Public users can fetch data, while admin users have full CRUD access via the API or Django Admin
interface.

---

## 🚀 Key Features

- 🎲 **Question Randomizer**  
  Delivers up to 5 unique questions per request, filtered by `question_type` (`"truth"` or `"dare"`) and selected
  categories.  
  Allows exclusion of previously seen questions to ensure smooth, non-repetitive gameplay.

- 🧩 **Flexible Category System**  
  Questions are organized into fully customizable categories with optional age restrictions (e.g., 18+), descriptive
  content, and icon support —  
  enabling clients to tailor experiences for different audiences.

- 📜 **Public Game Rules API**  
  Provides a read-only endpoint to retrieve gameplay rules, presented in a predefined order for easy integration.

- 🔐 **Role-Based API Access**  
  Read operations are publicly accessible, while create, update, and delete actions for questions and categories are
  restricted to admins.  
  Access is securely enforced via custom DRF permissions.

- ⚙️ **Clean & Modular Codebase**  
  Built following Django best practices with a clear separation of concerns and a RESTful API design.

- ✅ **Automated Testing with Pytest**  
  Comprehensive test coverage using `pytest` and `pytest-django`, including unit and integration tests for all major
  endpoints.

---

## 🛠️ Tech Stack

- 🐍 Python 3.11.2
- 🧩 Django 5.1.6
- 🛠 Django REST Framework 3.15.2
- 🗃 PostgreSQL (via `psycopg2` 2.9.10)  
  _Can be swapped to SQLite, MySQL, or another Django‑supported engine by updating the `DATABASES` settings
  in `settings.py` or your `.env`._
- 🧪 Pytest & DRF test tools
- 📦 Modular project structure (`apps/gameplay/`)
- 🔐 Custom DRF permissions for role-based access control
- 📦 Environment management with `python-dotenv`
- 🖼 Pillow for image processing

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/tigdav/truth-or-dare.git
cd truth-or-dare/backend
```

### 2. Create and activate virtual environment

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (cmd):

```bash
python -m venv .venv
.venv\Scripts\activate.bat
```

On Windows (PowerShell):

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations and start the development server

```bash
python manage.py migrate
python manage.py runserver
```

> The server will start at http://127.0.0.1:8000/ by default.

---

## 🔧 Environment Configuration

Before running the project, set up environment variables.

Copy the example file and fill in your local secrets:

```bash
cp .env.example .env
```

> 🔐 Do **not** commit the real `.env` file to version control — use it for local development or deployment only.

Minimal contents of `.env.example`:

```env
# Django settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=truth_or_dare_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

## 📡 API Documentation

The API reference, including available endpoints, request/response examples, and usage notes,  
is provided in a separate document: [docs/api.md](./docs/api.md).

---

## 🧪 Running Tests

Using Django's test runner:

```bash
python manage.py test
```

Or with Pytest:

```bash
pytest apps/gameplay/
```

Comprehensive tests cover key functionality and endpoints.

---

## 📁 Project Structure

```
truth-or-dare/
├── backend/
│   ├── manage.py
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── .env.example
│   ├── config/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── apps/
│       ├── __init__.py
│       └── gameplay/
│           ├── __init__.py
│           ├── admin.py
│           ├── apps.py
│           ├── models.py
│           ├── permissions.py
│           ├── serializers.py
│           ├── urls.py
│           ├── views.py
│           ├── migrations/ # Database migration files
│           └── tests/      # Integration tests
├── docs/
│   └── api.md              # API documentation
├── .gitignore
└── README.md
```

---

## 📝 License

This project is licensed under the MIT License.  
Feel free to use it for both personal and commercial projects.

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests. Please include relevant tests and clear commit messages.
