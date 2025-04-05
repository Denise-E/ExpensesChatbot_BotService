from sqlalchemy.orm import Session

from src.service.database_services.users_db_service import UsersDBService
from src.utils.logger import logger


class UsersService:

    @classmethod
    def create_user(cls, session: Session, user_info: dict) -> dict:
        try:
            user = UsersDBService.create_user(session, user_info)
            return {"id": user.id, "telegram_id": user.telegram_id}
        except Exception as e:
            logger.error(f"Unable to creat user in database: {e}")
            raise Exception("Unable to save user information on database")
