
# FastAPI Blog API

A simple blog API built with FastAPI. This project supports user registration, login (with JWT authentication), adding posts, viewing posts, and deleting posts. The database used is SQLite (out-of-the-box, no setup required).

## Project Structure

```

app/
├── auth.py
├── config.py
├── crud.py
├── database.py
├── dependencies.py
├── main.py
├── models.py
├── routers/
│    ├── posts.py
│    └── users.py
├── schemas.py
└── utils.py
fastapi_app.db
requirements.txt

````

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/fastapi-blog-api.git
cd fastapi-blog-api
````

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

### 5. Open Swagger UI (API docs)

Go to: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Main Endpoints

* **POST /signup** — User registration
* **POST /login** — User login (returns JWT token)
* **POST /add\_post** — Add a new post (requires authentication)
* **GET /get\_posts** — View all posts (requires authentication)
* **DELETE /delete\_post/{post\_id}** — Delete a post (requires authentication)

---

## Authentication

This API uses JWT (Bearer Token) for authentication.
After signing up or logging in, you will receive an access token.
Click the **Authorize** button in Swagger UI (top right) and enter:

```
Bearer <your_access_token>
```

---

## Technologies Used

* **Python 3.10+**
* **FastAPI**
* **SQLite + SQLAlchemy**
* **JWT (PyJWT)**
* **Pydantic**
* **Passlib (bcrypt)**

---




## Contact

My mail: zahra.amanli.za@gmail.com

My LinkedIn profile: www.linkedin.com/in/zahra-amanli 



---

**Zahra Amanli..**



