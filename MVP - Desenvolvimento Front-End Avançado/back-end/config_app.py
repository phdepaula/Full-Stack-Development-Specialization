from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS

from lib.comum import definir_secao

# Definindo configurações da API
info = Info(title="Mercado", version="1.0.0")
app = OpenAPI(__name__, info = info)
app.secret_key = 'MVP_PUC_RIO'
CORS(app)

# Definindo Tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc.")
login_tag = Tag(name="Login", description="Controle dos dados de Login do Mercado.")
produto_tag = Tag(name="Produtos", description="Controle dos produtos vendidos pelo Mercado.")
carrinho_tag = Tag(name="Carrinho", description="Controle dos produtos adicionados ao Carrinho.")

# Definindo seção atual
definir_secao()