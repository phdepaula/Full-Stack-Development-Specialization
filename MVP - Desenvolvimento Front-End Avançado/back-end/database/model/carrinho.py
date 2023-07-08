from sqlalchemy import Column, Integer, Float, String, Date
from typing import Union
from datetime import datetime

from database.config_model import Base


class Carrinho(Base):
  __tablename__ = 'carrinho'

  id_secao = Column('id_secao', String(100), primary_key=True)
  usuario = Column(String(50), nullable=False)
  produto = Column(String(30), nullable=False)
  quantidade = Column(Integer, nullable=False )
  preco = Column(Float)
  status_compra = Column(String(20))
  data = Column(Date, default = datetime.today())


  def __init__( self, id_secao: str, usuario: str, produto:str, quantidade: int
              , preco: float, status_compra: str, data: Union[Date, None] = None ) -> None:
    self.id_secao = id_secao
    self.usuario = usuario
    self.produto = produto
    self.quantidade = quantidade
    self.preco = preco
    self.status_compra = status_compra
    self.data = data