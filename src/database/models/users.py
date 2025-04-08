from sqlalchemy import Column, Integer, Text

from src.database.base_model.base_model import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(Text, unique=True, nullable=False)
