from database.config_model import session_maker
from sqlalchemy import asc
from datetime import datetime

global id_secao


def tratar_usuario(usuario):
  palavras = usuario.split(' ')
  quantidade_palavras = int(len(palavras))
  usuario_tratado = []             
  posicao = 0

  while posicao < quantidade_palavras:
    usuario_tratado.append(palavras[posicao].capitalize())
    posicao = posicao + 1
  
  usuario = ' '.join(usuario_tratado)

  return usuario


def consultar_parametro(dado_1, dado_2, dado_3):
  session = session_maker()
  parametro_cadastrado = session.query(dado_1).filter(dado_2 == dado_3).first()
  session.close()

  return parametro_cadastrado

  
def inserir_banco(novo_cadastro):
  session = session_maker()
  session.add(novo_cadastro)
  session.commit()
  session.close()


def consultar_dados_gerais_banco(database, coluna_filtro, valor, coluna_ordem):
  session = session_maker()
  tuplas = session.query(database).filter(coluna_filtro == valor).order_by(asc(coluna_ordem)).all()
  session.close()

  return tuplas


def gerar_id_produto (nome):
  id_produto = nome.upper().replace(' ', '')
  caracteres_especiais = { 'Á': 'A'
                         , 'É': 'E'
                         , 'Í': 'I'
                         , 'Ó': 'O'
                         , 'Ú': 'U'
                         , 'Ã': 'A' 
                         , 'Ç': 'C' }
                        
  for caracter, novo_caracter in caracteres_especiais.items():
    id_produto = id_produto.replace(caracter, novo_caracter)

  return id_produto


def definir_secao():
  global id_secao
  
  id_secao = f'secao_{datetime.now()}'