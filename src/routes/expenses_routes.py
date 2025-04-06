import asyncio

from flask import Blueprint, request, jsonify
import app
from src.service.expenses_service import ExpensesService

expenses = Blueprint("expenses", __name__)


@expenses.route("/create", methods=['POST'])
def create_expense():
    try:
        body = request.get_json()
        session = app.session

        response = asyncio.run(
            ExpensesService.create_expense(
                session=session,
                telegram_id=body.get("telegram_id"),
                expense_info=body.get("message")
            )
        )
        return jsonify(response), 200
    except Exception as e:
        msg = f"Unable to create expense: {e}"
        return {"msg": msg}, 400
