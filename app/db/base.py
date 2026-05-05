# Base class for all database models

from sqlalchemy.orm import declarative_base

# All models will inherit from this
Base = declarative_base()