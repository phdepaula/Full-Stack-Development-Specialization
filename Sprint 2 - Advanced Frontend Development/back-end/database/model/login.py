from database.config_model import Base
from sqlalchemy import Column, Integer, String


class Login(Base):
    __tablename__ = "login"

    id_login = Column(
        "id_login", Integer, primary_key=True, autoincrement=True
    )
    usuario = Column("usuario", String(50), unique=True, nullable=False)
    senha = Column(String(50), nullable=False)

    def __init__(self, usuario: str, senha: str) -> None:
        self.usuario = usuario
        self.senha = senha
