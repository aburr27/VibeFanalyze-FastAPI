# Defines Game API data structure

from pydantic import BaseModel
from datetime import datetime

class GameBase(BaseModel):
    home_team_id: int
    away_team_id: int
    home_score: int
    away_score: int
    date: datetime

class GameCreate(GameBase):
    pass

class GameResponse(GameBase):
    id: int

    class Config:
        from_attributes = True