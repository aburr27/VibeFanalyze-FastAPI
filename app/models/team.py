# Defines Team table

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Team(Base):
    """
    Team table
    """
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    city = Column(String(100))

    # Relationship: One team has many players
    players = relationship("Player", back_populates="team")