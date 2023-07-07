from sqlalchemy import Column, Numeric, String
from decimal import Decimal

from database.config_model import Base


class Produto(Base):
  __tablename__ = 'produtos'

  id_produtos = Column('id', String(30), primary_key=True)
  nome = Column(String(30))
  preco = Column(Numeric(precision = 4, scale = 2), default = Decimal('0.00'))
  fornecedor = Column(String(100))
  categoria = Column(String(20))
  informacao = Column(String(200))
  detalhamento = Column(String(10000))
  destaques = Column(String(1))


  def __init__( self, id_produtos: str, nome: str, preco: float, fornecedor: str, categoria: str
              , informacao: str, detalhamento: str, destaques: str ) -> None:
    self.id_produtos = id_produtos
    self.nome = nome
    self.preco = preco
    self.fornecedor = fornecedor
    self.categoria = categoria
    self.informacao = informacao
    self.detalhamento = detalhamento
    self.destaques = destaques