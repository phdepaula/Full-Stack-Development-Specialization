import os
from sqlalchemy_utils import database_exists, create_database

from database.config_model import Base, engine, session_maker
from database.model.login import Login
from database.model.produto import Produto
from database.inserts.inserts_produtos import produtos

dir_database = os.path.join(os.getcwd(), 'database', 'database-file')

if not os.path.isdir(dir_database):
  os.makedirs(dir_database)

if not database_exists(engine.url):
  create_database(engine.url)

Base.metadata.create_all(engine)

for produto in produtos:
  session = session_maker()
  parametro_cadastrado = session.query(Produto.id_produtos).filter(Produto.id_produtos == produto.id_produtos).first()

  if not(parametro_cadastrado):
    session.add(produto)
    session.commit()
    session.close()