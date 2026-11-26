from fastapi import FastAPI  # pyright: ignore[reportMissingImports]
from fastapi.middleware.cors import CORSMiddleware # pyright: ignore[reportMissingImports]
from app.database import get_connection


app = FastAPI(
  title="ContextFlow API",
  version="0.1.0"
)

@app.get("/health")
def health():
  return {
    "status": "ok",
    "service":"ContextFlow API",
  }

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://contextflow-ai-app.vercel.app"
    ],
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/health/db")
def database_health():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT 1")
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return {
        "status": "connected",
        "database": "PostgreSQL",
        "result": result[0]
    }
