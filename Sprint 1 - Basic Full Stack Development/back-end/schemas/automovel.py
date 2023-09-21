from typing import List

from database.model.automovel import Automovel
from pydantic import BaseModel


class AutomovelSchema(BaseModel):
    """Define como um automóvel deve ser cadastrado."""

    nome: str = "Polo"
    marca: str = "Volkswagen"
    tipo: str = "Carro"


class AutomovelViewSchema(BaseModel):
    """Define como uma mensagem de automóvel será apresentada."""

    id_automovel: int = 1
    nome: str = "Polo"
    marca: str = "Volkswagen"
    tipo: str = "Carro"


class AutomovelBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca de um \
    automóvel. Será feita apenas com base em seu nome.
    """

    nome: str = "Polo"


class AutomovelDelSchema(BaseModel):
    """Define como deve ser a estrutura do dado retornado após uma requisição \
    de remoção do automóvel.
    """

    mensagem: str
    nome: str


class ListagemAutomovelSchema(BaseModel):
    """Define como uma listagem de automovéis será retornada."""

    automoveis: List[AutomovelSchema]


def apresentar_automovel(dados_automovel: Automovel, mensagem):
    """Define um modelo de resposta para quando o automóvel \
    for cadastrado à base de dados."""
    result = {
        "id_automovel": dados_automovel.id_automovel,
        "nome": dados_automovel.nome,
        "marca": dados_automovel.marca,
        "tipo": dados_automovel.tipo,
    }
    return {"automovel": result, "mensagem": mensagem}


def listar_automovel_all(automoveis: List[Automovel]):
    """Define um modelo de resposta para quando for \
    solicitado uma lista dos automóveis cadastrados na base de dados."""
    result = []
    for automovel in automoveis:
        result.append(
            {
                "nome": automovel.nome,
                "marca": automovel.marca,
                "tipo": automovel.tipo,
            }
        )

    return {"automovel": result}
