from sqlalchemy.orm import Session

from src.database.models.expenses import Expenses
from src.utils.logger import logger


class ExpensesDBService:

    @classmethod
    def create_expense(cls, session: Session, expense_info: dict) -> None:
        try:
            logger.info("Creating expense on database")
            expense = Expenses(**expense_info)
            session.add(expense)
            session.commit()
        except Exception as e:
            logger.error(f"Unable to create expense on database: {e}")
            session.rollback()
