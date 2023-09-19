from database.model.config_model import Base
from sqlalchemy import Column, Integer, String


class Login(Base):
    __tablename__ = "login"

    id_login = Column(
        "id_login", Integer, primary_key=True, autoincrement=True
    )
    usuario = Column("usuario", String(15), unique=True, nullable=False)
    nome = Column(String(140), nullable=False)
    senha = Column(String(30), nullable=False)

    def __init__(self, usuario: str, nome: str, senha: str) -> None:
        self.usuario = usuario
        self.nome = nome
        self.senha = senha
