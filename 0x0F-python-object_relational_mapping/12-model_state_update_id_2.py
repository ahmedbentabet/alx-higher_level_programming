#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Creating engine to connect to MySQL database
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3336/{}"
        .format(username, password, database), pool_pre_ping=True
        )

    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Checking if state is found
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.add(state_to_update)
        session.commit()
    else:
        print("State with id = 2 not found")

    session.close()
