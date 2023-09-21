from pydantic import BaseModel


class CadastroCarrinhoSchema(BaseModel):
    """Define como deve ser a estrutura cadastro \
    no banco de dados do Carrinho"""

    usuario: str
    produto: str
    quantidade: str
    preco: str


class MensagemCarrinhoSchema(BaseModel):
    """Define como uma mensagem de aviso deve ser \
    enviada após o cadastro na base de dados de Carrinho."""

    mensagem: str


class UpdateCarrinhoSchema(BaseModel):
    """Define como uma mensagem de aviso deve ser \
    enviada após o cadastro na base de dados de Carrinho."""

    mensagem: str
    novo_produto: list


class DadosCarrinho(BaseModel):
    """Define como a quantidade e o preco total acumulado \
    no carrinho será retornado"""

    quantidade: int
    preco: float


class CancelaCarrinhoSchema(BaseModel):
    """Define como deve ser a estrutura informada para cancelar um pedido"""

    produto: str
    quantidade: str
    preco: str


def apresentar_atualizacao(produto, nova_quantidade, novo_preco, mensagem):
    """Define um modelo de resposta para um cancelamento de comprar."""
    result = {
        "Produto": produto,
        "Nova Quantidade": nova_quantidade,
        "Novo Preço": novo_preco,
    }

    return {"mensagem": mensagem, "cadastro_login": result}
