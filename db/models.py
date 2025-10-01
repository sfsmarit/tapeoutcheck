from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from .connection import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)