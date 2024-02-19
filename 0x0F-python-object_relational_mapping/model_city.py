#!/usr/bin/python3
""" definetion of state and base class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, ForeignKey, Column, Integer
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """ inhirits from base"""

    __tablename__ = 'cities'
    id = Column(
            Integer, primary_key=True,
            nullable=False, unique=True,
            autoincrement=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_keys='states.id')
