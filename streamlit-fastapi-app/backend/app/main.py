from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import items

app = FastAPI(title="Sample Backend API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router, prefix="/api/items", tags=["items"])


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}
