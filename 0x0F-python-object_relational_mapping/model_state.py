#!/usr/bin/python3
"""Class definition of a state and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class for State"""
    _tablename_ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
