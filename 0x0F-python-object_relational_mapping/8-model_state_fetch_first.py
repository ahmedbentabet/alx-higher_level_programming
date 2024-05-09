#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Extracting command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    # Creating engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, database), pool_pre_ping=True
        )

    # Create Session class bound to the engine
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    # Query all State objects and sort them by id in ascending order
    first_state = session.query(State).order_by(State.id).first()
    # Checking if any state exists
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    session.close()
