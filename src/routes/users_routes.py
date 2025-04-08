import logging

from flask import Blueprint, request, jsonify

import app
from src.data.schemas import CreateUserInput, CreateUserOutput
from src.service.users_service import UsersService

users = Blueprint("users", __name__)


@users.route("/create", methods=['POST'])  # User creation endpoint
def create_user():
    try:
        body = request.get_json()
        try:
            # Input pydantic schema validation
            validated_body = CreateUserInput(**body)
        except Exception as e:
            logging.info(f"Pydantic input error: {e}")
            raise Exception("Invalid input")

        session = app.session
        response = UsersService.create_user(session, validated_body.dict())

        # Output pydantic schema validation
        output = CreateUserOutput(**response)

        return jsonify(output.dict()), 200
    except Exception as e:
        logging.error(f"Unable to create user: {e}")
        return {"error": str(e)}, 400
