from pydantic import BaseModel


class VerificaLoginSchema(BaseModel):
    """Define como deve ser a estrutura de busca para \
    um cadastro no banco de dados de login."""

    usuario: str
    senha: str


class RespostaVerificaLoginSchema(BaseModel):
    """Define como deve ser a resposta para consulta de dados \
    cadastrados no banco de dados de login após \
    ser feita uma solitação de login pelo usuário.
    """

    status: bool
    string: str


def apresentar_cadastro_login(usuario, senha, mensagem):
    """Define um modelo de resposta para quando um \
    login for cadastrado à base de dados."""
    result = {"usuario": usuario, "senha": senha}

    return {"mensagem": mensagem, "cadastro_login": result}
