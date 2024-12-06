from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.constants.db_connections import USER_NAME, PASSWORD, HOST, PORT, DB_NAME
from app.models.db import *


class DBsession:
    session = None
    engine = None


def create_db_engine(conn_string):
    engine = create_engine(conn_string,
                           echo=False,
                           pool_size=10,
                           max_overflow=0,
                           pool_pre_ping=True,
                           pool_use_lifo=True)
    return engine


def get_db():
    conn_string = f"postgresql://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    DBsession.engine = create_db_engine(conn_string)
    Base.metadata.create_all(DBsession.engine)
    DBsession.session = sessionmaker(bind=DBsession.engine)

    return DBsession.session()
