def tratar_usuario(usuario):
  #Colocando em CamelCase
  palavras = usuario.split(' ')
  quantidade_palavras = int(len(palavras))
  usuario_tratado = []             

  posicao = 0

  while posicao < quantidade_palavras:
    usuario_tratado.append(palavras[posicao].capitalize())
    posicao = posicao + 1
  
  usuario = ' '.join(usuario_tratado)

  return usuario