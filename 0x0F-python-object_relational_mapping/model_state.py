#!/usr/bin/python3
""" definetion of state and base class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ inhirits from base"""

    __tablename__ = 'states'
    id = Column(
            Integer, primary_key=True,
            nullable=False, unique=True,
            autoincrement=True
    )
    name = Column(String(128), nullable=False)
