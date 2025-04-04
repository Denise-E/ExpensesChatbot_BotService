import datetime as dt

from sqlalchemy.orm import Session

from src.service.database_services.expenses_db_service import ExpensesDBService
from src.service.database_services.users_db_service import UsersDBService
from src.service.models_service import ModelsService
from src.utils.logger import logger


class ExpenseService:

    @classmethod
    def create_expense(cls, session: Session, telegram_id: int, expense_info: str):
        logger.info("Creating expense")
        try:
            # Verifies if the user is in the database (enabled for using the system)
            user = UsersDBService.get_user_by_telegram_id(session, telegram_id)

            # If the user is not in the database, it throws an exception
            if not user:
                raise Exception("User not found")

            expense = ModelsService.is_expense(expense_info)

            if not expense.is_expense:
                return {}

            expense_info = {
                "user_id": user.id,
                "description": "example",  # TODO
                "amount": 150.02,  # TODO
                "category": "General",  # TODO
                "added_at": dt.datetime.now()
            }

            ExpensesDBService.create_expense(session, expense_info)
            return expense_info
        except Exception as e:
            logger.error(f"Error: {e}")
            raise Exception(e)
