from pydantic import BaseModel

from database.model.login import Login


class VerificaLoginSchema(BaseModel):
  """ Define como deve ser a estrutura de busca para um cadastro no banco de dados de login."""
  usuario: str
  senha: str


class RespostaVerificaLoginSchema(BaseModel):
  """ Define como deve ser a resposta para consulta de dados cadastrados no banco de dados de login
  após ser feita uma solitação de login pelo usuário.
  """
  status: bool
  string: str


def apresentar_cadastro_login(dados_cadastro: Login, mensagem):
  """ Define um modelo de resposta para quando um login for cadastrado à base de dados.
  """
  result = { 'usuario': dados_cadastro.usuario
           , 'senha': dados_cadastro.senha }

  return {'mensagem': mensagem, 'cadastro_login': result}