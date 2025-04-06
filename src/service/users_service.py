from sqlalchemy.orm import Session

from src.service.database_services.users_db_service import UsersDBService
from src.utils.logger import logger


class UsersService:

    @classmethod
    def create_user(cls, session: Session, user_info: dict) -> dict:
        try:
            db_user = UsersDBService.get_user_by_telegram_id(session, user_info["telegram_id"])

            # If the user already exists, the existing user is returned
            if db_user:
                logger.info("User already exists on database, returning it")
                return {"id": db_user.id, "telegram_id": db_user.telegram_id}

            # If not, a new user is created on the database
            user = UsersDBService.create_user(session, user_info)
            return {"id": user.id, "telegram_id": user.telegram_id}
        except Exception as e:
            logger.error(f"Unable to creat user in database: {e}")
            raise Exception("Unable to save user information on database")
