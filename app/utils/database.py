from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.constants.db_connections import USER_NAME, PASSWORD, HOST, PORT, DB_NAME

DATABASE_URL = f"postgresql://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"  # Replace with your credentials

engine = create_engine(DATABASE_URL)
Base = declarative_base()
# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

