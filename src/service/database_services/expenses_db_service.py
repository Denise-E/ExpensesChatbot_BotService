from sqlalchemy import desc
from sqlalchemy.orm import Session

from src.database.config import SessionLocal
from src.database.models.expenses import Expenses
from src.database.models.users import Users
from src.utils.logger import logger


class ExpensesDBService:

    @classmethod
    def create_expense(cls, session: Session, expense_info: dict) -> None:
        logger.info("Creating expense on database")
        try:
            expense = Expenses(**expense_info)
            logger.info("Adding expense to session")
            session.add(expense)

            logger.info("Committing session")
            session.commit()

            logger.info("Expense committed successfully")
        except Exception as e:
            logger.error(f"Unable to create expense on database: {e}")
            session.rollback()
            raise Exception("Unable to create expense")

    @classmethod
    def get_user_expenses(cls, session: Session, telegram_id: str) -> list:
        logger.info("Getting user expenses from database")
        try:
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
            raise Exception("Unable to get expenses")
