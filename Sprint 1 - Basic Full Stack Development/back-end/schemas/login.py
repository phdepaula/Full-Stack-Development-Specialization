from database.model.login import Login
from pydantic import BaseModel


class LoginSchema(BaseModel):
    """Define como um login deve ser realizado."""

    usuario: str = "root"
    senha: str = "PUC2023"


class LoginViewSchema(BaseModel):
    """Define como uma mensagem de Login será apresentada."""

    id_login: int = 1
    usuario: str = "root"
    nome: str = "Usuario Root"
    senha: str = "PUC2023"


def apresenta_login(dados_login: Login, mensagem):
    """Define um modelo de resposta para quando for realizado um login."""
    result = {
        "id_login": dados_login.id_login,
        "usuário": dados_login.usuario,
        "nome": dados_login.nome,
        "senha": dados_login.senha,
    }
    return {"login": result, "mensagem": mensagem}
