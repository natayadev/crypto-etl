import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

load_dotenv()

def get_db_engine():
    """
    Creates and returns a SQLAlchemy engine for connecting to a PostgreSQL database
    using credentials and configuration from environment variables.
    """
    try:
        USER = os.getenv("DATABASE_USER")
        PASSWORD = os.getenv("DATABASE_PASSWORD")
        HOST = os.getenv("DATABASE_HOST")
        PORT = os.getenv("DATABASE_PORT")
        DATABASE = os.getenv("DATABASE_NAME")

        # SQLAlchemy configuration
        DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
        engine = create_engine(DATABASE_URL)
        
        return engine
    except SQLAlchemyError as e:
        raise RuntimeError("Failed to create SQLAlchemy engine") from e
