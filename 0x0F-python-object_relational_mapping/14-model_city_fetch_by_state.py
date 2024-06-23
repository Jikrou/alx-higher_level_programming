#!/usr/bin/python3
""" A script that list all Stateand City objects from a database."""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                            sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    for s, c in session.query(State, City).\
            filter(State.id == City.state_id).all():
        print(f"{s.name}: ({c.id}) {c.name}")
