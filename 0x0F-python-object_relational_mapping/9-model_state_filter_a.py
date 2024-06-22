#!/usr/bin/python3
""" A script that list all State objects that
    contains the letter a from a database.
    """
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                            sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    statelist = session.query(State).filter(State.name.like('%a%'))

    for obj_state in statelist.order_by(State.id):
        print(f"{obj_state.id}: {obj_state.name}")
