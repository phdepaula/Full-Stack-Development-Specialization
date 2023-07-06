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


def consultar_parametro(session, dado_1, dado_2, dado_3):
  parametro_cadastrado = session.query(dado_1).filter(dado_2 == dado_3).first()

  return parametro_cadastrado