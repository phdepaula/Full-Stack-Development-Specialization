from pydantic import BaseModel
from typing import List

from database.model.produto import Produto


class ProdutoSchema(BaseModel):
  """ Defini a estrutura de um produto
  """
  id_produtos: str
  nome: str
  preco: float
  fornecedor: str
  categoria: str
  informacao: str
  detalhamento: str
  destaques: str


class BuscaCategoriaProdutoSchema(BaseModel):
  """ Defini como a busca por categoria será feita pelos produtos.
  """
  categoria: str


class ListaProdutoSchema(BaseModel):
  """ Define como deve ser a estrutura de resposta para uma busca de um produto
      de uma determinada categoria.
  """
  produtos: List[ProdutoSchema]


class ListaProdutoSchemaMensagem(BaseModel):
  """ Defini como a busca será feita pelos produtos.
  """
  mensagem: str


class BuscaNomeProdutoSchema(BaseModel):
  """ Defini como a busca por nome será feita pelos produtos.
  """
  nome: str


class BuscaProdutoSchema(BaseModel):
  """ Define como deve ser a estrutura de resposta para uma busca de um produto
      com base em seu nome.
  """
  status: bool
  produtos: List[ProdutoSchema]


class BuscaProdutoSchemaMensagem(BaseModel):
  """ Defini como a busca será feita pelos produtos.
  """
  status: bool
  mensagem: str


def listar_produto_modelo(produtos: List[Produto]):
  """Define um modelo de resposta para quando for solicitado uma lista dos produtos
    cadastrados na base de dados.
  """
  result = []

  for produto in produtos:
    result.append({
          'id': produto.id_produtos
        , 'nome': produto.nome
        , 'preco': '{:.2f}'.format(produto.preco)
        , 'fornecedor': produto.fornecedor
        , 'categoria': produto.categoria
        , 'informacao': produto.informacao
        , 'detalhamento': produto.detalhamento
        , 'destaques': produto.destaques
    })

  return {'produtos': result}


def buscar_produto_modelo(produto: Produto):
  """Define um modelo de resposta para quando for solicitado um produto a base de dados.
  """
  result = { 'id': produto.id_produtos
           , 'nome': produto.nome
           , 'preco': produto.preco
           , 'fornecedor': produto.fornecedor
           , 'categoria': produto.categoria
           , 'informacao': produto.informacao
           , 'detalhamento': produto.detalhamento
           , 'destaques': produto.destaques }

  return {'status': True, 'produto': result}