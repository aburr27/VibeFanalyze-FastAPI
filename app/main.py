from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Vibe-Fanalyze API")

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Vibe-Fanalyze API is running"}
