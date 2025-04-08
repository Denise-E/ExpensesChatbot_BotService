from sqlalchemy.orm import Session

from src.database.models.users import Users
from src.utils.logger import logger


class UsersDBService:

    @classmethod
    def get_user_by_telegram_id(cls, session: Session, telegram_id: str) -> Users | None:
        try:
            logger.info("Getting user from database")
            return session.query(Users).filter(Users.telegram_id == telegram_id).one_or_none()
        except Exception as e:
            logger.error(f"Unable to get user from database: {e}")
            session.rollback()
            raise Exception("Unable to get user")

    @classmethod
    def create_user(cls, session: Session, user_info: dict) -> Users:
        try:
            logger.info("Creating user in the database")
            user = Users(**user_info)
            session.add(user)
            session.commit()
            return user
        except Exception as e:
            logger.error(f"Unable to create user in database: {e}")
            session.rollback()
            raise Exception("Unable to create user")
