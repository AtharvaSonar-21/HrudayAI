
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import check_database_connection

app = FastAPI(
    title="HrudayAI API",
    description="Cardiovascular clinical decision support research prototype",
    version="0.1.0",
)

# Allow the local Vite frontend to call the backend.
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