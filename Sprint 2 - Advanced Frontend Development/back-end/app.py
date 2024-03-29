from urllib.parse import unquote

from flask import redirect

import lib.comum as comum
from config_app import app, home_tag, login_tag, produto_tag, carrinho_tag
from database.model.carrinho import Carrinho
from database.model.login import Login
from database.model.produto import Produto
from schemas.carrinho import (
    CadastroCarrinhoSchema,
    MensagemCarrinhoSchema,
    UpdateCarrinhoSchema,
    CancelaCarrinhoSchema,
    apresentar_atualizacao,
)
from schemas.login import (
    VerificaLoginSchema,
    RespostaVerificaLoginSchema,
    apresentar_cadastro_login
)
from schemas.produto import (
    BuscaCategoriaProdutoSchema,
    ListaProdutoSchema,
    ListaProdutoSchemaMensagem,
    BuscaNomeProdutoSchema,
    BuscaProdutoSchema,
    BuscaProdutoSchemaMensagem,
    listar_produto_modelo,
    buscar_produto_modelo
)


# API de documentacao
@app.get("/", tags=[home_tag])
def documentacao():
    """Redireciona para a rota /openapi, tela que \
    permite a escolha do estilo de documentação."""
    return redirect("/openapi")


# API's de Login
@app.post(
    "/autenticar_login",
    tags=[login_tag],
    responses={
        "200": RespostaVerificaLoginSchema,
        "400": RespostaVerificaLoginSchema
    },
)
def autenticar_login(form: VerificaLoginSchema):
    """Verifica se os dados de login fornecidos pelo usuário estão corretos."""
    try:
        usuario = comum.tratar_usuario(unquote(unquote(form.usuario)))
        senha = unquote(unquote(form.senha))

        usuario_cadastrado = comum.consultar_parametro(
            Login.usuario, Login.usuario, usuario
        )

        if usuario_cadastrado is None:
            return {"status": False, "mensagem": "Usuário inexistente!"}, 200
        else:
            senha_cadastrada = comum.consultar_parametro(
                Login.senha, Login.usuario, usuario
            )[0]

            if senha == senha_cadastrada:
                return {"status": True, "usuario": usuario}, 200
            else:
                return {"status": False, "mensagem": "Senha Incorreta!"}, 200
    except Exception as error:
        return {"status": False, "mensagem": f"ERRO: {error}"}, 400


@app.post(
    "/cadastrar_login",
    tags=[login_tag],
    responses={
        "200": RespostaVerificaLoginSchema,
        "400": RespostaVerificaLoginSchema
    },
)
def cadastrar_login(form: VerificaLoginSchema):
    """Cadastra um novo item a base de dados de login."""
    try:
        usuario = comum.tratar_usuario(unquote(unquote(form.usuario)))
        senha = unquote(unquote(form.senha))

        usuario_cadastrado = comum.consultar_parametro(
            Login.usuario, Login.usuario, usuario
        )

        if usuario_cadastrado is None:
            novo_cadastro_login = Login(usuario=usuario, senha=senha)
            comum.inserir_banco(novo_cadastro_login)

            return (
                apresentar_cadastro_login(
                    usuario, senha, "Usuário cadastrado com sucesso!"
                ),
                200,
            )
        else:
            return {
                "status": False,
                "mensagem": "Usuário já existente, tente outro!",
            }, 200
    except Exception as error:
        return {"status": False, "mensagem": f"ERRO: {error}"}, 400


# API's de Produto
@app.get(
    "/listar_produto",
    tags=[produto_tag],
    responses={
        "200": ListaProdutoSchema,
        "201": ListaProdutoSchemaMensagem,
        "400": ListaProdutoSchemaMensagem,
    },
)
def listar_produto(query: BuscaCategoriaProdutoSchema):
    """Lista os produtos cadastradas para uma dada categoria."""
    try:
        categoria = unquote(unquote(query.categoria))

        if categoria == "Destaques":
            produtos = comum.consultar_dados_gerais_banco(
                Produto, Produto.destaques, "S", Produto.nome
            )
        else:
            produtos = comum.consultar_dados_gerais_banco(
                Produto, Produto.categoria, categoria, Produto.nome
            )

        if produtos:
            return listar_produto_modelo(produtos), 200
        else:
            return {
                "mensagem": (
                    "Nenhum produto foi encontrado para a"
                    + f" categoria {categoria}."""
                )
            }, 201
    except Exception as error:
        return {"mensagem": f"ERRO: {error}"}, 400


@app.post(
    "/buscar_produto",
    tags=[produto_tag],
    responses={
        "200": BuscaProdutoSchema,
        "201": BuscaProdutoSchemaMensagem,
        "400": BuscaProdutoSchemaMensagem,
    },
)
def buscar_produto(form: BuscaNomeProdutoSchema):
    """Busca um produto com base no nome fornecido."""
    try:
        id_produto = comum.gerar_id_produto(unquote(unquote(form.nome)))
        produto = comum.consultar_parametro(
            Produto, Produto.id_produtos, id_produto
        )

        if produto:
            return buscar_produto_modelo(produto), 200
        else:
            return {
                "status": False,
                "mensagem": (
                    f"Nenhum produto foi encontrado com o id {id_produto}."
                ),
            }, 201
    except Exception as error:
        return {"status": False, "mensagem": f"ERRO: {error}"}, 400


# API's do Carrinho
@app.post(
    "/inserir_compra",
    tags=[carrinho_tag],
    responses={"200": MensagemCarrinhoSchema, "400": MensagemCarrinhoSchema},
)
def inserir_compra(form: CadastroCarrinhoSchema):
    """Cadastra um novo pedido de compra a base de dados de carrinho."""
    try:
        usuario = unquote(unquote(form.usuario))
        produto = unquote(unquote(form.produto))
        quantidade_informada = int(unquote(unquote(form.quantidade)))
        preco_informado = round(float(unquote(unquote(form.preco))), 2)
        status_compra = "Em andamento"

        compra_cadastrada = comum.consultar_parametro_secao(
            Carrinho.produto,
            Carrinho.produto,
            produto,
            Carrinho.secao,
            comum.id_secao
        )

        if compra_cadastrada is None:
            novo_cadastro_carrinho = Carrinho(
                secao=comum.id_secao,
                usuario=usuario,
                produto=produto,
                quantidade=quantidade_informada,
                preco=preco_informado,
                status_compra=status_compra,
            )
            comum.inserir_banco(novo_cadastro_carrinho)

            return {
                "mensagem": "Novo item adicionado ao carrinho com sucesso!"
            }, 200
        else:
            quantidade_atual = int(
                comum.somar_condicional(
                    Carrinho.quantidade,
                    Carrinho.produto,
                    produto,
                    Carrinho.secao,
                    comum.id_secao,
                )
            )
            preco_atual = round(
                float(
                    comum.somar_condicional(
                        Carrinho.preco,
                        Carrinho.produto,
                        produto,
                        Carrinho.secao,
                        comum.id_secao,
                    )
                ),
                2,
            )
            nova_quantidade = quantidade_atual + quantidade_informada
            novo_preco = round(preco_atual + preco_informado, 2)

            comum.atualizar_banco(
                Carrinho,
                Carrinho.produto,
                produto,
                Carrinho.secao,
                comum.id_secao,
                Carrinho.quantidade,
                nova_quantidade,
            )
            comum.atualizar_banco(
                Carrinho,
                Carrinho.produto,
                produto,
                Carrinho.secao,
                comum.id_secao,
                Carrinho.preco,
                novo_preco,
            )

            return {
                "mensagem": (
                    "Item já existente no carrinho, atualizando pedidos!"
                )
            }, 200
    except Exception as error:
        return {"mensagem": f"ERRO: {error}"}, 400


@app.get(
    "/obter_dados_carrinho",
    tags=[carrinho_tag],
    responses={"200": MensagemCarrinhoSchema, "400": MensagemCarrinhoSchema},
)
def obter_dados_carrinho():
    """Obtem a quantidade de compras e o preço atual \
    acumulado no carrinho na seção atual."""
    try:
        quantidade_total = int(
            comum.obter_valor_total(
                Carrinho.quantidade, Carrinho.secao, comum.id_secao
            )
        )
        preco_total = round(
            float(
                comum.obter_valor_total(
                    Carrinho.preco, Carrinho.secao, comum.id_secao
                )
            ),
            2,
        )

        return {"quantidade": quantidade_total, "preco": preco_total}, 200
    except Exception as error:
        return {"mensagem": f"ERRO: {error}"}, 400


@app.put(
    "/cancelar_compra",
    tags=[carrinho_tag],
    responses={
        "200": UpdateCarrinhoSchema,
        "201": MensagemCarrinhoSchema,
        "400": MensagemCarrinhoSchema,
    },
)
def cancelar_compra(form: CancelaCarrinhoSchema):
    """Cancela uma determinada quantidade de itens adicionados \
    ao carrinho de um determinado produto na seção atual."""
    try:
        produto_cancelado = str(unquote(unquote(form.produto)))
        quantidade_cancelada = int(unquote(unquote(form.quantidade)))
        preco_cancelado = round(float(unquote(unquote(form.preco))), 2)

        quantidade_atual = int(
            comum.somar_condicional(
                Carrinho.quantidade,
                Carrinho.produto,
                produto_cancelado,
                Carrinho.secao,
                comum.id_secao,
            )
        )
        preco_atual = round(
            float(
                comum.somar_condicional(
                    Carrinho.preco,
                    Carrinho.produto,
                    produto_cancelado,
                    Carrinho.secao,
                    comum.id_secao,
                )
            ),
            2,
        )

        if quantidade_cancelada > quantidade_atual:
            return {
                "mensagem": f"Não existem {quantidade_cancelada}"
                + " itens no carrinho!"
            }, 201
        else:
            nova_quantidade = quantidade_atual - quantidade_cancelada
            novo_preco = round(preco_atual - preco_cancelado, 2)

            comum.atualizar_banco(
                Carrinho,
                Carrinho.produto,
                produto_cancelado,
                Carrinho.secao,
                comum.id_secao,
                Carrinho.quantidade,
                nova_quantidade,
            )
            comum.atualizar_banco(
                Carrinho,
                Carrinho.produto,
                produto_cancelado,
                Carrinho.secao,
                comum.id_secao,
                Carrinho.preco,
                novo_preco,
            )

        return (
            apresentar_atualizacao(
                produto_cancelado,
                nova_quantidade,
                novo_preco,
                "Compras canceladas!"
            ),
            200,
        )
    except Exception as error:
        return {"mensagem": f"ERRO: {error}"}, 400


@app.put(
    "/finalizar_carrinho",
    tags=[carrinho_tag],
    responses={"200": MensagemCarrinhoSchema, "400": MensagemCarrinhoSchema},
)
def finalizar_carrinho():
    """Finaliza as compras inseridas no carrinho na seção atual."""
    try:
        secao_atual = comum.id_secao

        comum.atualizar_banco(
            Carrinho,
            Carrinho.status_compra,
            "Em andamento",
            Carrinho.secao,
            secao_atual,
            Carrinho.status_compra,
            "Finalizada",
        )
        comum.definir_secao()

        return {"mensagem": "Seção finalizada!"}, 200
    except Exception as error:
        return {"mensagem": f"ERRO: {error}"}, 400


@app.put(
    "/cancelar_carrinho",
    tags=[carrinho_tag],
    responses={"200": MensagemCarrinhoSchema, "400": MensagemCarrinhoSchema},
)
def cancelar_carrinho():
    """Cancela todas as compras inseridas no carrinho na seção atual."""
    try:
        secao_atual = comum.id_secao

        comum.atualizar_banco(
            Carrinho,
            Carrinho.status_compra,
            "Em andamento",
            Carrinho.secao,
            secao_atual,
            Carrinho.quantidade,
            0,
        )
        comum.atualizar_banco(
            Carrinho,
            Carrinho.status_compra,
            "Em andamento",
            Carrinho.secao,
            secao_atual,
            Carrinho.preco,
            0,
        )
        comum.atualizar_banco(
            Carrinho,
            Carrinho.status_compra,
            "Em andamento",
            Carrinho.secao,
            secao_atual,
            Carrinho.status_compra,
            "Cancelada",
        )
        comum.definir_secao()

        return {"mensagem": "Seção cancelada!"}, 200
    except Exception as error:
        return {"mensagem": f"ERRO: {error}"}, 400
