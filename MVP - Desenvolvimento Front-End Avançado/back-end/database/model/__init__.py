from sqlalchemy_utils import database_exists, create_database

from database.model.config_model import Base, engine
from database.model.login import Login

if not database_exists(engine.url):
  create_database(engine.url)

Base.metadata.create_all(engine)