#!/workspace/alx/alx-higher_level_programming/0x0F-python-object_relational_mapping/my_venv/bin/python3
"""Defines the State class and creates Base instance."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
    """
    City class that represents a city table in the database.

    Attributes:
        id (int): Represents a column of an integer (primary key).
        name (str): Represents a column of a string of 128 characters.
        state_id (int): Represents a column of an integer (foreign key to states.id).
    """

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define the relationship with the State class
    # state = relationship(State, back_populates("cities"))
