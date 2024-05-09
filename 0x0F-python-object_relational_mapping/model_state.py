#!/usr/bin/python3
"""Defines the State class and creates Base instance."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating a base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """
    State class that represents a state table in the database.

    Attributes:
        id (int): Represents a column of an integer.
        name (str): Represents a column of a string.
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
