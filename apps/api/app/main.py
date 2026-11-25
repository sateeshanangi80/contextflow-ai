from fastapi import FastAPI  # pyright: ignore[reportMissingImports]
from fastapi.middleware.cors import CORSMiddleware # pyright: ignore[reportMissingImports]

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
  allow_origins=["http://localhost:3000"],
  allow_methods=["*"],
  allow_headers=["*"]
)
