from pydantic import BaseModel

class VerificaLoginSchema(BaseModel):
  """ Define como deve ser a estrutura de busca para um cadastro no banco de dados de login."""
  nome: str
  senha: str

class RespostaVerificaLoginSchema(BaseModel):
  """ Define como deve ser a resposta para consulta de dados cadastrados no banco de dados de login
  após ser feita uma solitação de login pelo usuário.
  """
  status: bool
  mensagem: str