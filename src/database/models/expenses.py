import datetime as dt

from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP

from src.database.base_model.base_model import Base


class Expenses(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(Text, nullable=False)
    amount = Column(Text, nullable=False)
    category = Column(Text, nullable=False)
    added_at = Column(TIMESTAMP, nullable=False, default=dt.datetime.now)
