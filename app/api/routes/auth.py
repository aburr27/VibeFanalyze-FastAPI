# This file handles authentication endpoints (register + login)

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.api.deps import get_db
from app.utils.hashing import hash_password, verify_password
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post(
    "/register",
    responses={400: {"description": "Email already registered"}},
)
def register(user_data: UserCreate, db: Annotated[Session, Depends(get_db)]):
    """
    Registers a new user
    """
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password before storing
    hashed_pw = hash_password(user_data.password)

    # Create user object
    new_user = User(
        email=user_data.email,
        hashed_password=hashed_pw
    )

    # Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

@router.post(
    "/login",
    responses={400: {"description": "Invalid credentials"}},
)
def login(user_data: UserLogin, db: Annotated[Session, Depends(get_db)]):
    """
    Logs user in and returns JWT token
    """
    # Find user by email
    user = db.query(User).filter(User.email == user_data.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Verify password
    if not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create JWT token (store user ID in "sub")
    token = create_access_token(data={"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }