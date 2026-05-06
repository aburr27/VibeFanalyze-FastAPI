# Player endpoints

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.player import Player

router = APIRouter(prefix="/players", tags=["Players"])

@router.post("/")
def create_player(name: str, position: str, team_id: int,
                  db: Session = Depends(get_db),
                  user=Depends(get_current_user)):
    """
    Create a new player (protected)
    """
    player = Player(name=name, position=position, team_id=team_id)

    db.add(player)
    db.commit()
    db.refresh(player)

    return player

@router.get("/")
def get_players(db: Session = Depends(get_db)):
    """
    Get all players (public)
    """
    return db.query(Player).all()

@router.get("/{player_id}")
def get_player(player_id: int, db: Session = Depends(get_db)):
    """
    Get a single player by ID
    """
    player = db.query(Player).filter(Player.id == player_id).first()

    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    return player