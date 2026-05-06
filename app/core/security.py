# This file handles JWT token creation and validation

from datetime import datetime, timedelta, timezone
from jose import jwt  # type: ignore[reportMissingModuleSource]
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    """
    Generates a JWT token for authenticated users data
    """
    to_encode = data.copy()

    # Set expiration time for token
    # Use timezone-aware UTC datetime
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Encode token with secret key
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)