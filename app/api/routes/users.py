# User-related endpoints (protected)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
def get_current_user_info(user: User = Depends(get_current_user)):
    """
    Returns the currently logged-in user
    """
    return user

@router.get("/")
def get_all_users(db: Session = Depends(get_db), user=Depends(get_current_user)):
    """
    Returns all users (protected route)
    """
    return db.query(User).all()