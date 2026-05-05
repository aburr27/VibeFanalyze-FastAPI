# This file handles JWT token creation and validation

from datetime import datetime, timedelta
from jose import jwt
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    """
    Generates a JWT token for authenticated users data
    """
    to_encode = data.copy()

    # Set expiration time for token
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Encode token with secret key
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)