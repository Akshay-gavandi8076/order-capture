from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./app/orders.db"
# database connections and execution of SQL statements
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# creating database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class (Base) for all SQLAlchemy models
Base = declarative_base()

# Initialize Database Schema
def init_db():
    Base.metadata.create_all(bind=engine) # Create the database schema based on the defined models

