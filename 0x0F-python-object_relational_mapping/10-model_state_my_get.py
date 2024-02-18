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
    sql_query = session.query(State).order_by(State.id).all()

    s_list = []
    for state in sql_query:
        s_list.append(state.name)

    sql_query = session.query(State).filter(
        State.name == "{}".format(sys.argv[4], )).first()
    if sys.argv[4] not in s_list:
        print("Not found")
    else:
        print(sql_query.id)

    session.close()
