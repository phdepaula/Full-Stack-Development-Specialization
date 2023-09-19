from datetime import datetime
from typing import List

from database.model.vendas import Vendas
from pydantic import BaseModel


class VendaSchema(BaseModel):
    """Define como uma venda deve ser realizada."""

    proprietario: str = "João"
    valor: float = 90000.00
    ano: int = 2020
    status: str = "A venda"
    automovel: str = "Polo"


class VendaViewSchema(BaseModel):
    """Define como uma mensagem de venda será apresentada."""

    id_vendas: int = 1
    proprietario: str = "João"
    valor: float = 90000.00
    ano: int = 2020
    status: str = "A venda"
    id_automovel: int = 1


class VendaJoinAutomovelSchema(BaseModel):
    """Define nova estrutura que será apresentada quando \
    realizado o join entre as tabelas vendas e automóvel."""

    proprietario: str = "João"
    valor: float = 90000.00
    ano: int = 2020
    status: str = "A venda"
    data_entrada: datetime = datetime.today()
    nome: str = "Polo"
    marca: str = "Volkswagen"
    tipo: str = "Carro"


class ListagemVendaSchema(BaseModel):
    """Define como uma listagem de vendas será retornada."""

    vendas: List[VendaJoinAutomovelSchema]


class VendaDelSchema(BaseModel):
    """Define como deve ser a estrutura do dado retornado após uma requisição
    de remoção de venda.
    """

    mensagem: str
    id: int


class VendaBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca de uma venda.
    Será feita apenas com base em seu id.
    """

    id: str = "1"


def apresentar_venda(dados_venda: Vendas, mensagem):
    """Define um modelo de resposta para quando \
    uma venda for cadastrada à base de dados."""
    result = {
        "id_vendas": dados_venda.id_vendas,
        "proprietario": dados_venda.proprietario,
        "valor": dados_venda.valor,
        "ano": dados_venda.ano,
        "data_entrada": dados_venda.data_entrada,
        "status": dados_venda.status,
        "id_automovel": dados_venda.id_automovel,
    }
    return {"venda": result, "mensagem": mensagem}


def listar_vendas_all(lista_vendas: list):
    """Define um modelo de resposta para quando for solicitado \
    uma lista dos vendas cadastradas na base de dados."""
    result = []
    for venda in lista_vendas:
        result.append(
            {
                "id_vendas": str(venda[0]),
                "proprietario": venda[1],
                "nome": venda[2],
                "marca": venda[3],
                "ano": venda[4],
                "valor": venda[5],
                "tipo": venda[6],
                "data_entrada": venda[7].strftime("%d/%m/%Y"),
                "status": venda[8],
            }
        )

    return {"vendas": result}
