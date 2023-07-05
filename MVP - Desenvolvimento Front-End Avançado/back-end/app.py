from flask import redirect
from urllib.parse import unquote

from config_app import *
from database.model.config_model import session_maker
from schemas.login import *

# API de documentacao
@app.get('/', tags = [home_tag])
def documentacao():    
  """Redireciona para a rota /openapi, tela que permite a escolha do estilo de documentação."""
  return redirect('/openapi')

#API de Login
@app.get('/verificar_login', tags = [login_tag],
          responses={'200': RespostaVerificaLoginSchema, '400': RespostaVerificaLoginSchema})
def verificar_login(query: VerificaLoginSchema):
  try:
    usuario = unquote(unquote(query.usuario))
    senha = unquote(unquote(query.senha))

    session = session_maker()

  except Exception as e:
    return {'status': False, 'erro': e}