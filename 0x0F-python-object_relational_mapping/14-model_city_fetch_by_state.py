#!/workspace/alx/alx-higher_level_programming/0x0F-python-object_relational_mapping/my_venv/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Querying all City objects, joining with State objects to get state names
    cities = session.query(State, City) \
        .filter(State.id == City.state_id) \
        .order_by(City.id).all()

    # Printing the results
    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
