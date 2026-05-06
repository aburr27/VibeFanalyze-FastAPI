# 🧠 Vibe-Fanalyze API

A scalable sports analytics API built with FastAPI, designed to power data-driven insights, predictions, and interactive dashboards.

---

## 🚀 Overview

Vibe-Fanalyze is a backend system that:
- Manages sports data (teams, players, games)
- Provides secure JWT-based authentication
- Supports analytics and prediction logic
- Serves as the backend for a future data visualization dashboard

This project demonstrates **real-world backend engineering practices** including API design, authentication, database relationships, and modular architecture.

---

## 🧱 Tech Stack

- **FastAPI** – high-performance API framework
- **MySQL** – relational database
- **SQLAlchemy** – ORM for database operations
- **Pydantic** – data validation
- **JWT (python-jose)** – authentication
- **Passlib (bcrypt)** – password hashing

---

## 🔐 Features

### Authentication
- User registration & login
- JWT token-based authentication
- Protected routes
- Team / Player / Game Management
- Prediction Engine

### Core Modules
- Users
- Teams
- Players
- Games

### API Capabilities
- CRUD operations
- Relational data (players → teams, games → teams)
- Modular routing structure

### Analytics
- Basic prediction engine (game outcome logic)
- Extendable for advanced stats & ML models

---

## 📁 Project Structure
vibe-fanalyze-api/
  - app/
    - main.py
    - core/
      - config.py
      - security.py
    - db/
      - session.py
      - base.py
    - models/
      - user.py
      - team.py
      - player.py
      - game.py
    - schemas/
      - user.py
      - team.py
      - player.py
      - game.py
    - api/
      - deps.py
      - routes/
        - auth.py
        - users.py
        - teams.py
        - players.py
        - games.py
    - services/
      - prediction.py
    - utils/
      - hashing.py
    - docs/
      - api-overview.md
      - database-schema.md
      - auth-flow.md
      - endpoints.md
  - requirements.txt
  - .env
  - README.md

## Run Locally
```bash
uvicorn app.main:app --reload
