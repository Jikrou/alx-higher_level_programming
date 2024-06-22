#!/usr/bin/python3
""" A script that print the State id if it exist in a database."""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                            sys.argv[3]), pool_pre_ping=True)

    thename = sys.argv[4]
    session = Session(engine)
    sn = session.query(State).filter(State.name == (thename,))
    try:
        print(sn[0].id)
    except IndexError:
        print("Not found")
