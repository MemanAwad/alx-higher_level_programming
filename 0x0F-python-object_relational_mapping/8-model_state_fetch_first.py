#!/usr/bin/python3
""" script to print the first state from datadase"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query_state = session.query(State).order_by(State.id).first()

    if query_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(query_state.id, query_state.name))

    session.close()
