# This file defines how the User table looks in the database

from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    """
    SQLAlchemy model for users table
    Represents a user in the database
    User table structure
    """
    __tablename__ = "users"  # table name in MySQL

    id = Column(Integer, primary_key=True, index=True)  # unique user ID
    email = Column(String(255), unique=True, index=True, nullable=False)  # login email
    hashed_password = Column(String(255), nullable=False)  # stored hashed password
