from sqlalchemy.orm import Session

from src.database.models.users import Users
from src.utils.logger import logger


class UsersDBService:

    @classmethod
    def get_user_by_telegram_id(cls, session: Session, telegram_id: int) -> Users | None:
        logger.info("Getting user from database")
        telegram_id = str(telegram_id)
        return session.query(Users.id).filter(Users.telegram_id == telegram_id).one_or_none()
