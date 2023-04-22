from sqlalchemy import Column, Float, ForeignKey, Integer, String, Date
from datetime import datetime
from typing import Union

from database.model.config_model import Base


class Vendas(Base):
    __tablename__ = 'vendas'

    id_vendas = Column("id_vendas", Integer, primary_key=True, autoincrement=True)
    proprietario = Column(String(140), nullable=False)
    valor = Column(Float, nullable=False)
    ano = Column(Integer, nullable=False)
    data_entrada = Column(Date, default=datetime.today())
    status = Column(String(10), nullable=False)
    id_automovel = Column(Integer, ForeignKey("automovel.id_automovel"), nullable=False)
    
    def __init__(self, proprietario: str, valor: float, ano: int, id_automovel: str, status: str,
                 data_entrada: Union[Date, None] = None) -> None:
        self.proprietario = proprietario
        self.valor = valor
        self.ano = ano
        self.data_entrada = data_entrada
        self.status = status
        self.id_automovel = id_automovel