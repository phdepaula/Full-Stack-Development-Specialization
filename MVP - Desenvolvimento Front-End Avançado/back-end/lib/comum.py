from database.config_model import session_maker


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


def consultar_dados_gerais_banco(database, coluna, valor):
  session = session_maker()
  tuplas = session.query(database).filter(coluna == valor).all()
  session.close()

  return tuplas