#!/usr/bin/python3
""" A script that updates the name of the State
    with id 2 to 'New Mexico'.
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
    sn = session.query(State).filter(State.id == 2).first()
    sn.name = 'Alaska'
    session.commit()
