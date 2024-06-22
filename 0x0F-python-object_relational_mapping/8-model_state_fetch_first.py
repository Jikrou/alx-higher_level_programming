#!/usr/bin/python3
""" A script that print the first State object from a database."""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    session = Session(engine)
    obj_state = session.query(State).first()

    if obj_state is None:
        print('Nothing')
    else:
        print(f"{obj_state.id}: {obj_state.name}")
