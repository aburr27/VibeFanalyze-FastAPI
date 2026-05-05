# This file defines how data is validated and returned via API

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """
    Schema for incoming user registration data
    """
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    """
    Schema for login requests
    """
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    """
    Schema for outgoing user data (what API returns)
    """
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # allows ORM -> response conversion