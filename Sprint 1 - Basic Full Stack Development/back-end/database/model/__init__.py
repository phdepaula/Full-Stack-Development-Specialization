from database.model.automovel import Automovel
from database.model.config_model import Base, engine, session
from database.model.login import Login
from database.model.vendas import Vendas
from sqlalchemy_utils import create_database, database_exists

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)

query_root = (
    session.query(Login.usuario).filter(Login.usuario == "root").first()
)

# Criando usuário root
if query_root is None:
    root = Login("root", "Usuario Root", "PUC2023")
    session.add(root)
    session.commit()
