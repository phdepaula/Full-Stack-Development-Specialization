from flask import redirect
from urllib.parse import unquote

import lib.comum as comum
from config_app import *

from database.model.login import Login
from database.model.produto import Produto

from schemas.login import *
from schemas.produto import *


# API de documentacao
@app.get('/', tags = [home_tag])
def documentacao():    
  """Redireciona para a rota /openapi, tela que permite a escolha do estilo de documentação."""
  return redirect('/openapi')


#API's de Login
@app.post('/autenticar_login', tags = [login_tag],
          responses={'200': RespostaVerificaLoginSchema, '400': RespostaVerificaLoginSchema})
def autenticar_login(form: VerificaLoginSchema):
  """Verifica se os dados de login fornecidos pelo usuário estão corretos."""
  try:
    usuario = comum.tratar_usuario(unquote(unquote(form.usuario)))
    senha = unquote(unquote(form.senha))

    usuario_cadastrado = comum.consultar_parametro(Login.usuario, Login.usuario, usuario)

    if usuario_cadastrado == None:
      return {'status': False, 'mensagem': 'Usuário inexistente!'}, 200
    else:
      senha_cadastrada = comum.consultar_parametro(Login.senha, Login.usuario, usuario)[0]

      if senha == senha_cadastrada:
        return {'status': True, 'usuario': usuario}, 200
      else:
        return {'status': False, 'mensagem': 'Senha Incorreta!'}, 200

  except Exception as e:
    return {'status': False, 'mensagem': f'ERRO: {e}'}, 400


@app.post('/cadastrar_login', tags = [login_tag],
          responses={'200': RespostaVerificaLoginSchema, '400': RespostaVerificaLoginSchema})
def cadastrar_login(form: VerificaLoginSchema):
  """Cadastra um novo item a base de dados de login."""
  try:
    usuario = comum.tratar_usuario(unquote(unquote(form.usuario)))
    senha = unquote(unquote(form.senha))
    
    usuario_cadastrado = comum.consultar_parametro(Login.usuario, Login.usuario, usuario)

    if usuario_cadastrado == None:
      novo_cadastro_login = Login(usuario = usuario, senha= senha)
      comum.inserir_banco(novo_cadastro_login)

      return apresentar_cadastro_login(usuario, senha, 'Usuário cadastrado com sucesso!'), 200
    else:
      return {'status': False, 'mensagem': 'Usuário já existente, tente outro!'}, 200

  except Exception as e:
    return {'status': False, 'mensagem': f'ERRO: {e}'}, 400
  

#API's de Produto
@app.get('/listar_produto', tags = [produto_tag],
        responses={'200': ListaProdutoSchema, '201': ListaProdutoSchemaMensagem, '400': ListaProdutoSchemaMensagem})
def listar_produto(query: BuscaCategoriaProdutoSchema):
  """Lista os produtos cadastradas para uma dada categoria"""
  try:
    categoria = unquote(unquote(query.categoria))

    if categoria == 'Destaques':
      produtos = comum.consultar_dados_gerais_banco(Produto, Produto.destaques, 'S', Produto.nome)
    else:
      produtos = comum.consultar_dados_gerais_banco(Produto, Produto.categoria, categoria, Produto.nome)

    if produtos:
      return listar_produto_modelo(produtos), 200
    else:
      return {'mensagem': f'Nenhum produto foi encontrado para a categoria {categoria}.'}, 201
  except Exception as e:
    return {'mensagem': f'ERRO: {e}'}, 400


@app.post('/buscar_produto', tags = [produto_tag],
        responses={'200': BuscaProdutoSchema, '201': BuscaProdutoSchemaMensagem, '400': BuscaProdutoSchemaMensagem})
def buscar_produto(form: BuscaNomeProdutoSchema):
  """Lista os produtos cadastradas para uma dada categoria"""
  try:
    id_produto = comum.gerar_id_produto(unquote(unquote(form.nome)))
    produto = comum.consultar_parametro(Produto, Produto.id_produtos, id_produto)

    if produto:
      return buscar_produto_modelo(produto), 200
    else:
      return {'status': False, 'mensagem': f'Nenhum produto foi encontrado com o id {id_produto}.'}, 201
  except Exception as e:
    return {'status': False, 'mensagem': f'ERRO: {e}'}, 400   