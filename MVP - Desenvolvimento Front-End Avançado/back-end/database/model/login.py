from sqlalchemy import Column, Integer, String

from database.model.config_model import Base


class Login(Base):
  __tablename__ = 'login'
  
  id_login = Column("id_login", Integer, primary_key=True, autoincrement=True)
  usuario = Column("usuario", String(15), unique=True, nullable=False)
  senha = Column(String(15), nullable=False)
  
  
  def __init__(self, usuario: str, senha: str) -> None:
    self.usuario = usuario
    self.senha = senha