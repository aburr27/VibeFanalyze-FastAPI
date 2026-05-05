# Defines Player table

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Player(Base):
    """
    Player table
    """
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    position = Column(String(50))

    # Foreign key links player to team
    team_id = Column(Integer, ForeignKey("teams.id"))

    # Relationship back to team
    team = relationship("Team", back_populates="players")