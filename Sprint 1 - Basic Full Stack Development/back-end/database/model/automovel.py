from database.model.config_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Automovel(Base):
    __tablename__ = "automovel"

    id_automovel = Column(
        "id_automovel", Integer, primary_key=True, autoincrement=True
    )
    nome = Column(String(20), unique=True, nullable=False)
    marca = Column(String(20), nullable=False)
    tipo = Column(String(30), nullable=False)

    vendas = relationship("Vendas")

    def __init__(self, nome: str, marca: str, tipo: str) -> None:
        self.nome = nome
        self.marca = marca
        self.tipo = tipo
