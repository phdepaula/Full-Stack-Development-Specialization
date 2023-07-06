from flask import redirect
from urllib.parse import unquote

import comum
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
@app.post('/autenticar_login', tags = [login_tag],
          responses={'200': RespostaVerificaLoginSchema, '400': RespostaVerificaLoginSchema})
def autenticar_login(form: VerificaLoginSchema):
  """Verifica se os dados de login fornecidos pelo usuário estão corretos."""
  try:
    usuario = comum.tratar_usuario(unquote(unquote(form.usuario)))
    senha = unquote(unquote(form.senha))

    session = session_maker()
    usuario_cadastrado = comum.consultar_parametro(session, Login.usuario, Login.usuario, usuario)

    if usuario_cadastrado == None:
      return {'status': False, 'mensagem': 'Usuário inexistente!'}, 400
    else:
      senha_cadastrada = comum.consultar_parametro(session, Login.senha, Login.usuario, usuario)[0]

      if senha == senha_cadastrada:
        return {'status': True, 'usuario': usuario}, 200
      else:
        return {'status': False, 'mensagem': 'Senha Incorreta!'}, 400

  except Exception as e:
    return {'status': False, 'mensagem': f'ERRO: {e}'}, 400


@app.post('/cadastrar_login', tags = [login_tag],
          responses={'200': RespostaVerificaLoginSchema, '400': RespostaVerificaLoginSchema})
def cadastrar_login(form: VerificaLoginSchema):
  """Cadastra um novo item a base de dados de login."""
  try:
    usuario = comum.tratar_usuario(unquote(unquote(form.usuario)))
    senha = unquote(unquote(form.senha))
    
    session = session_maker()
    usuario_cadastrado = comum.consultar_parametro(session, Login.usuario, Login.usuario, usuario)

    if usuario_cadastrado == None:
      novo_cadastro_login = Login(usuario = usuario, senha= senha)
      Login.cadastrar_login_banco(novo_cadastro_login, session)

      return apresentar_cadastro_login(novo_cadastro_login, 'Usuário cadastrado com sucesso!')
    else:
      return {'status': False, 'mensagem': 'Usuário já existente, tente outro!'}, 400

  except Exception as e:
    return {'status': False, 'mensagem': f'ERRO: {e}'}, 400