import os

import pymysql  # noqa
from sqlalchemy import create_engine

# Database config
DB_CONNECTION_STR = os.getenv("DB_CONNECTION_STR")
engine = create_engine(DB_CONNECTION_STR)
