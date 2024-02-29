from datetime import datetime
from .settings import Base
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Boolean,
)

class DBUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    hashed_id = Column(String(100), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)


class DBToken(Base):
    __tablename__ = "token"
    user_id = Column(String(100), nullable=False)
    access_token = Column(String(450), primary_key=True)
    refresh_token = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.now)