from flask import Blueprint, request

import app
from src.service.users_service import UsersService

users = Blueprint("users", __name__)


@users.route("/create", methods=['POST'])
def create_user():
    try:
        session = app.session
        data = request.get_json()
        res = UsersService.create_user(session, data)
        return res
    except Exception as e:
        msg = f"Unable to create user: {e}"
        return {"msg": msg}, 400
