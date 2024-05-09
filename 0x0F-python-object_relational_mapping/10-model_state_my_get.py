#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
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

    # Querying State object with the provided state name
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
