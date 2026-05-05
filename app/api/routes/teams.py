# Team endpoints

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.team import Team

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/")
def create_team(name: str, city: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    """
    Create a team (protected route)
    """
    team = Team(name=name, city=city)
    db.add(team)
    db.commit()
    db.refresh(team)

    return team

@router.get("/")
def get_teams(db: Session = Depends(get_db)):
    """
    Public route to get all teams
    """
    return db.query(Team).all()