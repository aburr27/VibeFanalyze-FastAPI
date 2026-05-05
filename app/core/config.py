# This file loads environment variables so we can use them in the app

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Store values in variables for easy access
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# Convert expiration to integer
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))