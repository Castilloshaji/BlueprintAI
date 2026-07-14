# 🚀 BlueprintAI

BlueprintAI is an AI-powered software architecture generation platform that helps developers transform software ideas into structured project blueprints.

Instead of starting from a blank document, users can describe their project in natural language, and BlueprintAI generates a complete software blueprint including architecture, database schema, API design, folder structure, and development roadmap.

---

## ✨ Features

### 🔐 Authentication
- User Registration
- JWT Authentication
- Secure Login
- Protected API Endpoints

### 📁 Project Management
- Create Projects
- Retrieve User Projects
- Owner-Based Authorization

### 🤖 AI Blueprint Generation
- Generate complete software blueprints using Groq LLM
- Prompt Engineering Pipeline
- AI Response Validation
- Structured JSON Parsing

### 📄 Blueprint Management
- Versioned Blueprints
- Automatic Version Increment
- JSONB Storage in PostgreSQL
- Retrieve Blueprint History

---

## 🏗 Architecture

Frontend (Coming Soon)

↓

FastAPI Backend

↓

Authentication

↓

Project Service

↓

Blueprint Service

↓

Prompt Builder

↓

Groq LLM

↓

Response Parser

↓

Blueprint Validator

↓

PostgreSQL (JSONB)

---

## 🛠 Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic

### AI
- Groq API
- Llama 3.3 70B
- Prompt Engineering

### Authentication
- JWT
- Passlib (bcrypt)

### Database
- PostgreSQL
- JSONB

### Development
- Python
- Git
- GitHub

---

## 📂 Project Structure

backend/
│
├── app/
│ ├── ai/
│ ├── api/
│ ├── core/
│ ├── database/
│ ├── dto/
│ ├── models/
│ ├── repositories/
│ ├── schemas/
│ └── services/
│
├── alembic/
│
└── requirements.txt

---

## 🚀 Current Workflow

1. User logs in
2. Creates a project
3. Provides a project prompt
4. Prompt Builder constructs the AI prompt
5. Groq generates a structured blueprint
6. Response Parser validates JSON
7. Blueprint is stored in PostgreSQL
8. Version history is maintained automatically

---

## 📌 Current Sprint

### ✅ Sprint 1
- Authentication
- JWT
- User Management
- Project CRUD
- PostgreSQL Integration

### ✅ Sprint 2
- AI Integration
- Prompt Builder
- Blueprint Generator
- Response Parser
- Blueprint Validator
- Blueprint Versioning
- JSONB Storage

### 🚧 Sprint 3 (In Progress)
- Blueprint Comparison
- AI Architecture Review
- Interactive Visualization
- Frontend Dashboard

---

## 🎯 Future Roadmap

- Architecture Diagram Generation
- ER Diagram Generation
- API Documentation Generation
- AI Code Generation
- Blueprint Diff Viewer
- Multi-Agent Review
- Team Collaboration
- Export to PDF & Markdown

---

## ⚡ Installation

```bash
git clone https://github.com/Castilloshaji/BlueprintAI.git

cd BlueprintAI/backend

python -m venv .venv

source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt

alembic upgrade head

uvicorn app.main:app --reload
