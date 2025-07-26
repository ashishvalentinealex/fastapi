# FastAPI Book Management API

![FastAPI Logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

A simple Book Management REST API built with **FastAPI**, **SQLAlchemy**, **Alembic**, and **PostgreSQL**. This project demonstrates CRUD operations with full database integration using Pydantic models and dependency injection.

> [!NOTE]
> This is a beginner-friendly backend project, ideal for understanding how to use FastAPI with PostgreSQL in real-world use cases.

---

## 📚 Features

- 🚀 FastAPI framework for blazing-fast APIs
- 🗃️ PostgreSQL database with SQLAlchemy ORM
- 🔄 Full CRUD support: Create, Read, Update, Delete
- 🛡️ Pydantic-based data validation
- ♻️ Dependency Injection via `Depends()`
- 🔧 Alembic for future migrations

---

## 🛠️ Stack

- **FastAPI** – web framework
- **Uvicorn** – ASGI server
- **SQLAlchemy** – ORM layer
- **Pydantic** – request/response validation
- **PostgreSQL** – relational database
- **Alembic** – migrations (optional setup)
- **Python 3.11+**

---

## 🚀 Quick Start

### 1. Clone the project

```bash
git clone https://github.com/yourusername/fastapi-book-api.git
cd fastapi-book-api


```bash 
uvicorn book:app --reload

