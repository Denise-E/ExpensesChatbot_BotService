import logging

from flask import Blueprint, request, jsonify

import app
from src.data.schemas import CreateExpenseOutput, CreateExpenseInput, GetAllUserExpensesOutput
from src.exceptions.users_exceptions import UserNotFoundException
from src.service.expenses_service import ExpensesService

expenses = Blueprint("expenses", __name__)


@expenses.route("/create", methods=['POST'])  # Expense creation endpoint
def create_expense():
    try:
        body = request.get_json()

        try:
            # Input pydantic schema validation
            validated_body = CreateExpenseInput(**body)
        except Exception as e:
            logging.info(f"Pydantic input error: {e}")
            raise Exception("Invalid input")

        session = app.session

        response = ExpensesService.create_expense(
            session=session,
            telegram_id=validated_body.telegram_id,
            expense_info=validated_body.message
        )
        # Output pydantic schema validation
        output = CreateExpenseOutput(**response)

        return jsonify(output.dict()), 200
    except UserNotFoundException as e:
        logging.error(f"Unable to create expense: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logging.error(f"Unable to create expense: {e}")
        return {"error": str(e)}, 400


@expenses.route("/get/<telegram_id>/all", methods=['GET'])  # Get user expenses endpoint
def get_user_expenses(telegram_id):
    try:
        session = app.session

        response = ExpensesService.get_user_expenses(session, telegram_id)

        # Output pydantic schema validation
        validated = GetAllUserExpensesOutput(expenses=response).dict()
        return jsonify(validated), 200
    except UserNotFoundException as e:
        logging.error(f"Unable to get expenses: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logging.error(f"Unable to get expense: {e}")
        return {"error": str(e)}, 400
