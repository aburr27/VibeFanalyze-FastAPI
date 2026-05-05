# This file handles password hashing and verification

from passlib.context import CryptContext

# Configure hashing algorithm (bcrypt is secure and standard)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Converts plain password into a secure hashed version
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compares plain password with stored hashed password
    Returns True if they match
    """
    return pwd_context.verify(plain_password, hashed_password)
