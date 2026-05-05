# Defines Game table

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.db.base import Base

class Game(Base):
    """
    Game table
    """
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)

    # Teams involved in game
    home_team_id = Column(Integer, ForeignKey("teams.id"))
    away_team_id = Column(Integer, ForeignKey("teams.id"))

    # Scores
    home_score = Column(Integer)
    away_score = Column(Integer)

    # Game date
    date = Column(DateTime)