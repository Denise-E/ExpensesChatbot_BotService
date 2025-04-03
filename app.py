from sqlalchemy.orm import Session

from src.service.expenses_service import ExpenseService
from src.database.config import SessionLocal
from flask import Flask, jsonify, request
from src.utils.logger import logger

app = Flask(__name__)

session: Session = SessionLocal()  # Instancia la sesión


# Routes

# Endpoint to verify that the system is running
@app.route("/health", methods=['GET'])
def health():
    try:
        return {"msg": "OK"}, 200
    except Exception as e:
        return jsonify({"msg": e}), 400


# Endpoint for expense creation
@app.route("/create/expense", methods=['POST'])
def create_expense():
    try:
        logger.info('Creating expense')
        data = request.json
        res = ExpenseService.create_expense(session, data["telegram_id"], data["text"])
        return res
    except Exception as e:
        msg = f"Unable to create expense: {e}"
        return {"msg": msg}, 400


if __name__ == '__main__':
    app.run(port=5002)
