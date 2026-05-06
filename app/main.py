# Main entry point of the application
from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine

# Import all routes
from app.api.routes import auth, games, players, teams, users

app = FastAPI(title="Vibe-Fanalyze API")

# Create DB tables automatically
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(auth.router)
app.include_router(games.router)
app.include_router(players.router)
app.include_router(teams.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Vibe-Fanalyze API is running"}
