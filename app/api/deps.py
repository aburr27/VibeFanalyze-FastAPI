# Dependency file for shared dependencies (DB + Auth) logic like DB session and auth

from app.db.session import SessionLocal
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.core.config import SECRET_KEY, ALGORITHM
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer

# This tells FastAPI where login happens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
    """
    Creates a new DB session for each request
    Closes it after request finishes
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Extracts user from JWT token
    Used to protect routes
    """
    try:
        # Decode token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Token error")

    # Fetch user from DB
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user
