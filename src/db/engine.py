from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker, Session
from src.db.models.settings import Base

engine: Engine | None = None
DBSession: Session = sessionmaker()


def init_db(db_url: str):
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    DBSession.configure(bind=engine)


def get_db():
    database = DBSession()
    try:
        yield database
    finally:
        database.close()