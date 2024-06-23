#!/usr/bin/python3
""" A script that print the State id of the newly creates in a database."""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                            sys.argv[3]), pool_pre_ping=True)

    newsta = State()
    newsta.name = 'Louisiana'
    with Session(engine) as session:
        session.add(newsta)
        session.commit()
        print(newsta.id)
