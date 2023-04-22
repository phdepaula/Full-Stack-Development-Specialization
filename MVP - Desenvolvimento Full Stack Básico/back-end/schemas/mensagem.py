from pydantic import BaseModel


class MensagemSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    messagem: str