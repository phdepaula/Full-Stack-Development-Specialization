from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

db_path = "database/"
db_url = 'sqlite:///%s/db.sqlite3' % db_path
engine = create_engine(db_url, echo=False, connect_args={"check_same_thread": False})
session_maker = sessionmaker(bind=engine)