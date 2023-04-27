from config_app import *


# API de documentacao
@app.get('/', tags = [home_tag])
def documentacao():    
    """Redireciona para a rota /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')


# APIs de Login
@app.get('/login', tags = [login_tag])
def login():    
    """Redireciona para a rota /login, tela que permite o usuario logar no sistema."""
    return render_template('login.html')


@app.post('/logout', tags= [login_tag], responses={"200": MensagemSchema})
def logout():
    """Realiza o logout do usuário logado no sistema.
    Se o usuário ainda não estiver logado, informa que o login ainda não foi realizado.
    """
    global status_login

    if status_login['status'] == 'conectado':
        mensagem = f"O usuário foi desconectado!"
        status_login['usuario'] = None
        status_login['status'] = 'desconectado'
    else:
        mensagem = f'O login ainda não foi realizado!'
    
    return {"mensagem": mensagem}, 200


@app.post('/autenticar', tags = [login_tag],
           responses={"200": LoginViewSchema, "400": MensagemSchema, "404": MensagemSchema})
def autenticar(query: LoginSchema):
    """Autentica o usuario e a senha digitados na rota \login.
    Se os dados preenchidos estiverem corretos, redireciona para a rota /vendas.
    Se os dados preenchidos estiverem incorretos, redireciona para a rota /login.
    """
    global status_login
    
    try:
        if status_login['status'] == 'conectado':
            mensagem = 'Já existe um usuário conectado!'
            return {"mensagem": mensagem}, 400
        else:
            session = session_maker()

            usuario_form = unquote(unquote(query.usuario))
            senha_form = unquote(unquote(query.senha))

            query_login = session.query(Login.id_login, Login.usuario, Login.nome, Login.senha).filter(Login.usuario == usuario_form).first()
            
            if query_login == None:
                mensagem = 'Usuário inexistente!'
                return {"mensagem": mensagem}, 404
            else:
                dados_login = {
                    "id_login": query_login[0], 
                    "usuario": query_login[1], 
                    "nome": query_login[2],
                    "senha": query_login[3],
                }

                if dados_login["senha"] == senha_form:
                    mensagem = 'Login realizado com sucesso!'
                    status_login['usuario'] = usuario_form
                    status_login['status'] = 'conectado'
                    return apresenta_login(query_login, mensagem), 200
                else:
                    mensagem = 'Senha incorreta! Tentar novamente!'
                    return {"mensagem": mensagem}, 404
            
    except Exception as e:
        mensagem = f'ERRO: {e}'
        return {"mensagem": mensagem}, 400


# API's de Automovel
@app.get('/automovel', tags = [automovel_tag])
def automovel():    
    """Redireciona para a rota /automovel, tela que permite o usuario realizar o controle de automovéis."""
    global status_login

    if status_login['status'] == 'conectado':
        return render_template('automovel.html')
    else:
        return redirect('/login')


@app.post('/cadastar_automovel', tags = [automovel_tag],
          responses={"200": AutomovelViewSchema, "400": MensagemSchema, "409": MensagemSchema})
def cadastrar_automovel(form: AutomovelSchema):
    """Adiciona um novo automovel à base de dados.
    """
    automovel = Automovel(nome=form.nome.capitalize(), marca=form.marca.capitalize(), tipo=form.tipo.capitalize())

    try:
        session = session_maker()
        session.add(automovel)
        session.commit()
        mensagem = "SUCESSO! Automóvel cadastrado!"
        return apresentar_automovel(automovel, mensagem), 200
    
    except IntegrityError as e:
        mensagem = 'ERRO! Automóvel já cadastrado na base de dados!'
        return {"mensagem": mensagem}, 409
    
    except Exception as e:
        mensagem = f'ERRO: {e}'
        return {"mensagem": mensagem}, 400


@app.get('/listar_automovel', tags = [automovel_tag],
          responses={"200": ListagemAutomovelSchema, "201": MensagemSchema, "400": MensagemSchema})
def listar_automovel():
    """Lista todos os automóveis cadastrados na base de dados.
    """
    try:
        session = session_maker()
        automoveis_banco = session.query(Automovel).all()

        if automoveis_banco:
            return listar_automovel_all(automoveis_banco), 200
        else:
            mensagem = f'Não existem automóveis cadastrados!'
            return {"mensagem": mensagem}, 201

    except Exception as e:
        mensagem = f'ERRO: {e}'
        return {"mensagem": mensagem}, 400


@app.delete('/deletar_automovel', tags = [automovel_tag],
          responses={"200": AutomovelDelSchema, "400": MensagemSchema})
def deletar_automovel(query: AutomovelBuscaSchema):
    """Deleta um automóvel a partir de um nome informado.
    Somente autoriza a deleção se o automóvel não estiver cadastrado na tabela de vendas.
    Retorna uma mensagem de confirmação da remoção.
    """
    try:
        nome_automovel = unquote(unquote(query.nome))

        session = session_maker()

        venda_cadastrada = session.query(Vendas.id_vendas).filter(Vendas.id_automovel == (session.query(Automovel.id_automovel).filter(Automovel.nome == nome_automovel.capitalize()).first()[0])).first()
        print(venda_cadastrada)

        if venda_cadastrada:
            mensagem = f"ERRO! O Automóvel não pode ser deletado pois já está cadastrado na tabela de vendas!"
            return {"mensagem": mensagem}, 400
        else:
            delete = session.query(Automovel).filter(Automovel.nome == nome_automovel.capitalize()).delete()
            session.commit()

            if delete:
                mensagem = "SUCESSO! Automóvel deletado!"
                return {"mensagem": mensagem , "nome": nome_automovel}, 200
            else:
                mensagem = "ERRO! Automóvel não encontrado!"
                return {"mensagem": mensagem}, 400
    
    except Exception as e:
        mensagem = f'ERRO: ERRO! Automóvel não encontrado!'
        return {"mensagem": mensagem}, 400


# API's de Venda
@app.get('/vendas', tags = [vendas_tag])
def vendas():    
    """Redireciona para a rota /vendas, tela que permite o usuario realizar o controle de vendas."""
    global status_login

    if status_login['status'] == 'conectado':
        return render_template('vendas.html'), 'oi'
    else:
        return redirect('/login')


@app.post('/cadastar_vendas', tags = [vendas_tag],
          responses={"200": VendaViewSchema, "400": MensagemSchema})
def cadastrar_venda(form: VendaSchema):
    """Adiciona uma nova venda à base de dados.
    """ 
    try:
        nome_automovel = form.automovel.capitalize()

        session = session_maker()
        id_automovel = session.query(Automovel.id_automovel).filter(Automovel.nome == nome_automovel).first()

        if id_automovel == None:
            mensagem = f'ERRO! Automóvel não cadastrado, favor cadastrar no controle de automóveis para seguir com a venda!'
            return {"mensagem": mensagem}, 409
        else:
            venda = Vendas(proprietario = form.proprietario.capitalize(),
                           valor = round(form.valor, 2),
                           ano = int(form.ano),
                           status = form.status.capitalize(),
                           id_automovel = id_automovel[0]
                           )
            session.add(venda)
            session.commit()
            mensagem = "SUCESSO! Venda cadastrada!"
            return apresentar_venda(venda, mensagem), 200

    except Exception as e:
        mensagem = f'ERRO: {e}'
        return {"mensagem": mensagem}, 400
    

@app.get('/listar_vendas', tags = [vendas_tag],
          responses={"200": ListagemVendaSchema, "201": MensagemSchema, "400": MensagemSchema})
def listar_vendas():
    """Lista todos as vendas cadastrados na base de dados.
    Nessa consulta, é realizado um join conectando as tabelas vendas e automóvel para melhor visualização dos dados.
    """
    try:
        session = session_maker()
        vendas_banco = session.query(Vendas.id_vendas, Vendas.proprietario, Automovel.nome, 
                                     Automovel.marca, Vendas.ano, Vendas.valor, Automovel.tipo, 
                                     Vendas.data_entrada, Vendas.status).join(Automovel).all()

        if vendas_banco:
            return listar_vendas_all(vendas_banco), 200
        else:
            mensagem = f'Não existem vendas cadastradas!'
            return {"mensagem": mensagem}, 201

    except Exception as e:
        mensagem = f'ERRO: {e}'
        return {"mensagem": mensagem}, 400
    

@app.delete('/deletar_vendas', tags = [vendas_tag],
          responses={"200": VendaDelSchema, "400": MensagemSchema})
def deletar_vendas(query: VendaBuscaSchema):
    """Deleta uma Venda a partir do id informado.
    Retorna uma mensagem de confirmação da remoção.
    """
    try:
        id_vendas = int(unquote(unquote(query.id)))
        print(id_vendas)

        session = session_maker()
        delete = session.query(Vendas).filter(Vendas.id_vendas == id_vendas).delete()
        session.commit()

        if delete:
            mensagem = "SUCESSO! Venda deletada!"
            return {"mensagem": mensagem , "id venda": id_vendas}, 200
        else:
            mensagem = "ERRO! Venda não encontrada!"
            return {"mensagem": mensagem}, 400
    
    except Exception as e:
        mensagem = f'ERRO: {e}'
        return {"mensagem": mensagem}, 400