from pydantic import BaseModel


class CadastroCarrinhoSchema(BaseModel):
  """ Define como deve ser a estrutura cadastro no banco de dados do Carrinho"""
  usuario: str
  produto: str
  quantidade: str
  preco: str
  status_compra: str


class MensagemCarrinhoSchema(BaseModel):
  """ Define como uma mensagem de aviso deve ser enviada após o cadastro na base de dados de Carrinho.
  """
  mensagem: str


class DadosCarrinho(BaseModel):
  """ Define como a quantidade e o preco total acumulado no carrinho será retornado
  """
  quantidade: int
  preco: float