from flask import redirect
from urllib.parse import unquote

from config_app import *
from database.model.config_model import session_maker
from database.model.login import Login
from schemas.login import *

# API de documentacao
@app.get('/', tags = [home_tag])
def documentacao():    
  """Redireciona para a rota /openapi, tela que permite a escolha do estilo de documentação."""
  return redirect('/openapi')

#API de Login
@app.post('/verificar_login', tags = [login_tag],
          responses={'200': RespostaVerificaLoginSchema, '400': RespostaVerificaLoginSchema})
def verificar_login(form: VerificaLoginSchema):
  """Verifica se os dados de login fornecidos pelo usuário estão corretos."""
  try:
    session = session_maker()
    usuario = unquote(unquote(form.usuario)).upper()
    senha = unquote(unquote(form.senha))
    usuario_cadastrado = session.query(Login.usuario).filter(Login.usuario == usuario).first()

    if usuario_cadastrado == None:
      return {'status': False, 'mensagem': 'Usuário inexistente!'}, 400
    else:
      senha_cadastrada = session.query(Login.senha).filter(Login.usuario == usuario).first()[0]

      if senha == senha_cadastrada:
        return {'status': True, 'mensagem': 'Login realizado!'}, 200
      else:
        return {'status': False, 'mensagem': 'Senha Incorreta!'}, 400

  except Exception as e:
    return {'status': False, 'mensagem': f'ERRO: {e}'}, 400


@app.post('/cadastrar_login', tags = [login_tag],
          responses={'200': RespostaVerificaLoginSchema, '400': RespostaVerificaLoginSchema})
def cadastrar_login(form: VerificaLoginSchema):
  """Cadastra um novo item a base de dados de login."""
  try:
    session = session_maker()

    usuario = unquote(unquote(form.usuario)).upper()
    senha = unquote(unquote(form.senha))

    usuario_cadastrado = session.query(Login.usuario).filter(Login.usuario == usuario).first()

    if usuario_cadastrado == None:
      novo_cadastro_login = Login(usuario = usuario, senha= senha)
      
      session.add(novo_cadastro_login)
      session.commit()

      return apresentar_cadastro_login(novo_cadastro_login, 'Usuário cadastrado com sucesso!')
    else:
      return {'status': False, 'mensagem': 'Usuário já existente, tente outro!'}, 400

  except Exception as e:
    return {'status': False, 'mensagem': f'ERRO: {e}'}, 400