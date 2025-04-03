import datetime as dt

from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, Numeric

from src.database.base_model.base_model import Base


class Expenses(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    description = Column(Text, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    category = Column(Text, nullable=False)
    added_at = Column(TIMESTAMP, nullable=False, default=dt.datetime.now)

    def as_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "amount": float(self.amount),
            "category": self.category,
            "added_at": None if not self.added_at else self.added_at.isoformat(),
        }
