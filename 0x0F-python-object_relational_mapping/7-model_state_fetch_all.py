#!/usr/bin/python3
""" A script that list all State objects from a database."""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                            sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    for obj_state in session.query(State).order_by(State.id):
        print(f"{obj_state.id}: {obj_state.name}")
