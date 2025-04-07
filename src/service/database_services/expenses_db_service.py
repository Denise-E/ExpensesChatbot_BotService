from sqlalchemy import desc
from sqlalchemy.orm import Session

from src.database.models.expenses import Expenses
from src.database.models.users import Users
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

    @classmethod
    def get_user_expenses(cls, session: Session, telegram_id: str) -> list:
        try:
            logger.info("Getting user expenses from database")
            expenses = (
                session.query(
                    Expenses
                ).join(
                    Users, Users.id == Expenses.user_id
                ).filter(
                    Users.telegram_id == telegram_id
                ).order_by(desc(Expenses.added_at)).all()
            )
            return expenses
        except Exception as e:
            logger.error(f"Unable to get expenses from database: {e}")
            session.rollback()
