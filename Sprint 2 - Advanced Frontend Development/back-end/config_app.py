from flask_cors import CORS
from flask_openapi3 import Info, OpenAPI, Tag

from lib.comum import definir_secao

# Definindo configurações da API
info = Info(title="Mercado", version="1.0.0")
app = OpenAPI(__name__, info=info)
app.secret_key = "MVP_PUC_RIO"
CORS(app)

# Definindo Tags
home_tag = Tag(
    name="Documentação",
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc.",
)
login_tag = Tag(
    name="Login",
    description="Controle dos dados de login."
)
produto_tag = Tag(
    name="Produtos",
    description="Controle dos produtos vendidos."
)
carrinho_tag = Tag(
    name="Carrinho",
    description="Controle das compras adicionadas ao carrinho."
)

# Definindo seção atual
definir_secao()
