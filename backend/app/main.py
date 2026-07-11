from fastapi import FastAPI
from app.api.routes.database import router as database_router
from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router
from app.api.routes.project import router as project_router
app = FastAPI(
    title="BlueprintAI API",
    description="AI-powered software architect backend",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(database_router)
app.include_router(auth_router)
app.include_router(project_router)


@app.get("/")
async def root():
    return {
        "project": "BlueprintAI",
        "version": "1.0.0",
        "status": "Running",
        "phase": "Phase 1 - Project Foundation",
        "message": "Welcome to BlueprintAI 🚀",
        "documentation": "/docs",
    }