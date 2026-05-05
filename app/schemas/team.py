# Defines how team data is sent/received via API

from pydantic import BaseModel

class TeamBase(BaseModel):
    name: str
    city: str

class TeamCreate(TeamBase):
    pass  # same fields as base

class TeamResponse(TeamBase):
    id: int

    class Config:
        from_attributes = True