# db_setup.py

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from os.path import abspath

db_folder = abspath("ftd_main/fixed_deposit.db")

db_location =  "".join(["sqlite:////", db_folder])


engine = create_engine(db_location, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import ftd_main.models
    Base.metadata.create_all(bind=engine)


#https://stackoverflow.com/questions/15175339/sqlalchemy-what-is-declarative-base
