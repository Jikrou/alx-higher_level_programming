#!/usr/bin/python3
""" A script that delete all the State obj
    that contains the letter a.
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
    for d in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(d)
    session.commit()
