from src.service.expenses_service import ExpenseService
from src.utils.logger import logger
from flask import Flask, jsonify, request

app = Flask(__name__)


# Routes
@app.route("/health", methods=['GET'])
def health():
    try:
        return {"msg": "OK"}, 200
    except Exception as e:
        return jsonify({"msg": e}), 400


@app.route("/expense", methods=['POST'])
def create_expense():
    try:
        logger.info('Creating expense')
        data = request.json
        res = ExpenseService.create_expense(data["text"])
        return res
    except Exception as e:
        msg = f"Unable to create expense: {e}"
        return {"msg": msg}, 400


if __name__ == '__main__':
    app.run(port=5002)
