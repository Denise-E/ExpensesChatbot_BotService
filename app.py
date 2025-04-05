import asyncio

from flask import Flask, jsonify, request
from sqlalchemy.orm import Session

from src.database.config import SessionLocal
from src.service.expenses_service import ExpensesService
from src.service.users_service import UsersService

app = Flask(__name__)

session: Session = SessionLocal()  # Instancia la sesión


# Routes

# Endpoint to verify that the system is running
@app.route("/api/health", methods=['GET'])
def health():
    try:
        return {"msg": "OK"}, 200
    except Exception as e:
        return jsonify({"msg": e}), 400


# Endpoint for expense creation
@app.route("/api/create/expenses", methods=['POST'])
def create_expense():
    try:
        body = request.get_json()

        response = asyncio.run(
            ExpensesService.create_expense(
                session=session,
                telegram_id=body.get("telegram_id"),
                expense_info=body.get("text")
            )
        )
        return jsonify(response), 200
    except Exception as e:
        msg = f"Unable to create expense: {e}"
        return {"msg": msg}, 400


@app.route("/api/create/users", methods=['POST'])
def create_user():
    try:
        data = request.json
        res = UsersService.create_user(session, data)
        return res
    except Exception as e:
        msg = f"Unable to create user: {e}"
        return {"msg": msg}, 400


if __name__ == '__main__':
    app.run(port=5002)
