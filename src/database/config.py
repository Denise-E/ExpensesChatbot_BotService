import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Database config
DB_CONNECTION_STR = os.getenv("DB_CONNECTION_STR")
engine = create_engine(DB_CONNECTION_STR)

# Crear una fábrica de sesiones
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


# Function to access the session instance
def get_db():
    db = SessionLocal()
    try:
        yield db  # Returns de session instance
    finally:
        db.close()  # Ensures session closing
