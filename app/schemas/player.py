# Defines how Player data is validated and returned

from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str
    position: str
    team_id: int  # links player to a team

class PlayerCreate(PlayerBase):
    # Used when creating a player (same fields as base)
    pass

class PlayerResponse(PlayerBase):
    id: int  # include ID in response

    class Config:
        from_attributes = True  # allows ORM -> JSON conversion