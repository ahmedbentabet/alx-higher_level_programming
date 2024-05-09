#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
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

    # Creating a new State object
    new_state = State(name="Louisiana")
    # Adding the new State object to the session and committing changes to db
    session.add(new_state)
    session.commit()

    # Printing the new state's ID after creation
    print(new_state.id)

    session.close()
