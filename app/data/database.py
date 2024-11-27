from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/beatsheet_db")

settings = Settings()

# Database connection
engine = create_engine(settings.DATABASE_URL)

# Session local class to interact with DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for models
Base = declarative_base()

def get_db() -> Session:
    """Dependency to get a database session for each request."""
    db = SessionLocal()
    try:
        yield db  # Using yield allows the session to be used within a 'with' block
    finally:
        db.close()  # Ensures that the session is closed when done
