import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Database config
DB_CONNECTION_STR = os.getenv("DB_CONNECTION_STR")
engine = create_engine(DB_CONNECTION_STR)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
