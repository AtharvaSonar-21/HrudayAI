
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import check_database_connection
from app.core.database import Base, check_database_connection, engine
import app.models
from app.api.patients import router as patients_router

app = FastAPI(
    title="HrudayAI API",
    description="Cardiovascular clinical decision support research platform",
    version="0.1.0",
)

app.include_router(patients_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "HrudayAI API is running",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "hrudayai-backend",
    }

@app.get("/health/database")
def database_health_check():
    try:
        check_database_connection()
        return {
            "status": "healthy",
            "database": "connected",
        }
    except Exception:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        )

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

