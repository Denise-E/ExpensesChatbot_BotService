import datetime as dt

from sqlalchemy.orm import Session

from src.data.schemas import Expense
from src.database.models.users import Users
from src.service.database_services.expenses_db_service import ExpensesDBService
from src.service.database_services.users_db_service import UsersDBService
from src.service.models_service import ModelsService
from src.utils.logger import logger


class ExpensesService:

    @classmethod
    async def create_expense(
            cls, session: Session, telegram_id: str, expense_info: str
    ):
        logger.info("Creating expense")
        try:
            user = cls.validate_user(session, telegram_id)

            expense = await ModelsService.is_expense(expense_info)

            if not expense.is_expense:
                logger.info(f"The input is not an expense: {expense_info}")
                return {}

            expense_values, category_classification = await ModelsService.extract_and_categorize(expense_info)

            if not expense_values.amount:
                raise Exception("Invalid amount")

            """            
            In order to make sure the expense is saved, we set 'Other' as the default category the
            category classification model don´t return a category.
            """
            expense_info = {
                "user_id": user.id,
                # .capitalize() for the text to start with a capital letter
                "description": expense_values.description.capitalize(),
                "amount": expense_values.amount,
                "category": "Other" if not category_classification.category else category_classification.category,
                "added_at": dt.datetime.now()
            }

            ExpensesDBService.create_expense(session, expense_info)
            return expense_info
        except Exception as e:
            logger.error(f"Error: {e}")
            raise Exception(e)

    @classmethod
    def get_user_expenses(cls, session: Session, telegram_id: str) -> list:
        try:
            logger.info("Getting user expenses")
            cls.validate_user(session, telegram_id)
            db_expenses = ExpensesDBService.get_user_expenses(session, telegram_id)

            if not db_expenses:
                return []

            expenses = []
            for expense in db_expenses:
                expense_data = {
                    "id": expense.id,
                    "user_id": expense.user_id,
                    "description": expense.description,
                    "amount": expense.amount,
                    "category": expense.category,
                    "added_at": expense.added_at
                }
                validated = Expense(**expense_data).dict()
                expenses.append(validated)

            return expenses
        except Exception as e:
            logger.error(f"Error: {e}")
            raise Exception(e)

    @classmethod
    def validate_user(cls, session: Session, telegram_id: str) -> Users:
        # Verifies if the user is in the database (enabled for using the system)
        user = UsersDBService.get_user_by_telegram_id(session, telegram_id)

        # If the user is not in the database, it throws an exception
        if not user:
            raise Exception("User not found")

        return user
