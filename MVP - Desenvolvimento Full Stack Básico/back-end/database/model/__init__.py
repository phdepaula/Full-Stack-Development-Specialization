from sqlalchemy_utils import database_exists, create_database

from database.model.config_model import Base, engine, session
from database.model.automovel import Automovel
from database.model.login import Login
from database.model.vendas import Vendas

if not database_exists(engine.url):
    create_database(engine.url) 

Base.metadata.create_all(engine)

query_root = session.query(Login.usuario).filter(Login.usuario == 'root').first()

# Criando usuário root 
if query_root == None:
    root = Login('root', 'Usuario Root', 'PUC2023')
    session.add(root)
    session.commit()