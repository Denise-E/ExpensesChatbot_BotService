import asyncio
import logging

from flask import Blueprint, request, jsonify
import app
from src.data.schemas import CreateExpenseOutput, CreateExpenseInput
from src.service.expenses_service import ExpensesService

expenses = Blueprint("expenses", __name__)


@expenses.route("/create", methods=['POST'])
def create_expense():
    try:
        body = request.get_json()

        try:
            validated_body = CreateExpenseInput(**body)
        except Exception as e:
            logging.info(f"Pydantic input error: {e}")
            raise Exception("Invalid input")

        session = app.session

        response = asyncio.run(
            ExpensesService.create_expense(
                session=session,
                telegram_id=validated_body.telegram_id,
                expense_info=validated_body.message
            )
        )
        output = CreateExpenseOutput(**response)

        return jsonify(output.dict()), 200
    except Exception as e:
        logging.error(f"Unable to create expense: {e}")
        return {"msg": str(e)}, 400
