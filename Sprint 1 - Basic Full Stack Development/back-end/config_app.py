import os
from urllib.parse import unquote

from flask import flash, redirect, render_template, url_for
from flask_cors import CORS
from flask_openapi3 import Info, OpenAPI, Tag
from sqlalchemy.exc import IntegrityError

from database.model.automovel import Automovel
from database.model.config_model import session_maker
from database.model.login import Login
from database.model.vendas import Vendas
from schemas.automovel import *
from schemas.login import *
from schemas.mensagem import *
from schemas.vendas import *

# Definindo configurações da API
info = Info(title="API de Controle de Vendas de Automóveis", version="1.0.0")
template_folder = os.path.join("..", "front-end", "templates")
static_folder = os.path.join("..", "front-end", "static")
app = OpenAPI(
    __name__, info=info, template_folder=template_folder, static_folder=static_folder
)
app.secret_key = "MVP_PUC_RIO"
CORS(app)

# Definindo váriavel de controle de Login
status_login = {"usuario": None, "status": "desconectado"}

# Definindo Tags
home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc.",
)
login_tag = Tag(name="Login", description="Controle dos dados de Login.")
vendas_tag = Tag(name="Vendas", description="Controle dos dados de Vendas.")
automovel_tag = Tag(name="Automóvel", description="Controle dos dados de Automóveis.")
