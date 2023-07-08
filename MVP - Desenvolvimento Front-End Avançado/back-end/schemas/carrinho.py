from pydantic import BaseModel


class CadastroCarrinhoSchema(BaseModel):
  """ Define como deve ser a estrutura cadastro no banco de dados do Carrinho"""
  usuario: str
  produto: str
  quantidade: str
  preco: str
  status_compra: str
  status_secao:str


class MensagemCadastroCarrinhoSchema(BaseModel):
  """ Define como uma mensagem de aviso deve ser enviada após o cadastro na base de dados de Carrinho.
  """
  mensagem: str