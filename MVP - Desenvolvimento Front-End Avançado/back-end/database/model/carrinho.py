from sqlalchemy import Column, Integer, Float, String, Date
from typing import Union
from datetime import datetime

from database.config_model import Base


class Carrinho(Base):
  __tablename__ = 'carrinho'

  id_carrinho = Column("id_carrinho", Integer, primary_key=True, autoincrement=True)
  secao = Column(String(100), nullable=False)
  data = Column(Date, default = datetime.today())
  usuario = Column(String(50), nullable=False)
  produto = Column(String(30), nullable=False)
  quantidade = Column(Integer, nullable=False )
  preco = Column(Float, nullable=False)
  status_compra = Column(String(20), nullable=False)
  status_secao = Column(String(20), nullable=False)


  def __init__( self, secao: str, usuario: str, produto:str, quantidade: int, preco: float
              , status_compra: str, status_secao: str, data: Union[Date, None] = None ) -> None:
    self.secao = secao
    self.usuario = usuario
    self.produto = produto
    self.quantidade = quantidade
    self.preco = preco
    self.status_compra = status_compra
    self.status_secao = status_secao
    self.data = data