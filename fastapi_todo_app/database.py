from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./todo.db"

# Connect to the SQLite database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create sessions to perform CRUD operations
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for the ORM models 
Base = declarative_base()