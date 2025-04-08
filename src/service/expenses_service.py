import datetime as dt

from sqlalchemy.orm import Session

from src.service.database_services.expenses_db_service import ExpensesDBService
from src.service.models_service import ModelsService
from src.service.users_service import UsersService
from src.utils.logger import logger


class ExpensesService:

    @classmethod
    def create_expense(cls, session: Session, telegram_id: str, expense_info: str):
        logger.info("Creating expense")

        try:
            # Check if the user is in the whitelist
            user = UsersService.validate_user(session, telegram_id)

            # If the user is in the whitelist, the input text is analyzed by the LLM model
            result = ModelsService.analyze_expense_model(expense_info)

            # Validates the received text is about an expense
            if not result.is_expense:
                # If it's a non-expense texts it throws an exception
                logger.info(f"The input is not an expense: {expense_info}")
                raise Exception("Input is not an expense")

            # If it's an expense texts but is not completed, it throws an exception
            if not result.amount:
                raise Exception("Invalid amount")

            expense_info = {
                "user_id": user.id,
                "description": result.description.strip().capitalize(),
                "amount": result.amount,
                "category": result.category or "Other",
                "added_at": dt.datetime.now()
            }

            # Saves the expense into de database
            ExpensesDBService.create_expense(session, expense_info)
            return expense_info
        except Exception as e:
            logger.error(f"Error: {e}")
            raise e

    @classmethod
    def get_user_expenses(cls, session: Session, telegram_id: str) -> list:
        logger.info("Getting user expenses")
        try:
            # Check if the user is in the whitelist
            UsersService.validate_user(session, telegram_id)

            # If the user is in the whitelist, get the expenses from database
            db_expenses = ExpensesDBService.get_user_expenses(session, telegram_id)

            # If not expenses found, an empty list is returned
            if not db_expenses:
                return []

            expenses = []

            # Expense formatting
            for expense in db_expenses:
                expense_data = {
                    "id": expense.id,
                    "user_id": expense.user_id,
                    "description": expense.description.strip().capitalize(),
                    "amount": expense.amount,
                    "category": expense.category,
                    "added_at": expense.added_at
                }
                expenses.append(expense_data)

            return expenses
        except Exception as e:
            logger.error(f"Error: {e}")
            raise e
