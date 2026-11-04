
# 🔐 SecureAuth – Authentication & Authorization Backend

SecureAuth is a Python-based Authentication and Authorization REST API built using FastAPI, SQLite, and SQLAlchemy.

The main goal of this project is to understand and implement secure user authentication, authorization, JWT-based security, and role-based access control (RBAC), following real-world backend development practices.

---

## 🚀 Project Overview

SecureAuth aims to provide the following features:

- User Registration and Login
- Secure Password Hashing
- JWT Authentication
- Protected API Endpoints
- User Profile Management
- Role-Based Access Control (RBAC)
- Admin-Only APIs
- Refresh Token Management
- Logout and Token Revocation
- Password Reset and Email Verification

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Programming |
| FastAPI | REST API Framework |
| SQLite | Database |
| SQLAlchemy | ORM and Database Management |
| Pydantic | Data Validation |
| JWT | Token-Based Authentication |

---

## 📂 Project Structure

```text
SecureAuth/
│
├── app/
│   ├── core/
│   │   └── config.py
│   │   └── pass_security.py
│   │   └── token_security.py
│   ├── models/
│   │   └── user.py
│   ├── routers/
│   │   └── auth.py
│   ├── schemas/
│   │   └── auth.py
│   │   └── user.py
│   ├── main.py
│   └── database.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md