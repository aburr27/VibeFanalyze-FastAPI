# Game endpoints

from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, Any
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.game import Game

router = APIRouter(prefix="/games", tags=["Games"])

@router.post("/")
def create_game(home_team_id: int, away_team_id: int,
                home_score: int, away_score: int,
                db: Annotated[Session, Depends(get_db)],
                _user: Annotated[Any, Depends(get_current_user)]):
    """
    Create a game (protected)
    """
    game = Game(
        home_team_id=home_team_id,
        away_team_id=away_team_id,
        home_score=home_score,
        away_score=away_score
    )

    db.add(game)
    db.commit()
    db.refresh(game)

    return game

@router.get("/")
def get_games(db: Annotated[Session, Depends(get_db)]):
    """
    Get all games
    """
    return db.query(Game).all()

@router.get("/{game_id}", responses={404: {"description": "Game not found"}})
def get_game(game_id: int, db: Annotated[Session, Depends(get_db)]):
    """
    Get game by ID
    """
    game = db.query(Game).filter(Game.id == game_id).first()

    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    return game