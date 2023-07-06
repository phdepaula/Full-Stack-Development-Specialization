from sqlalchemy_utils import database_exists, create_database

from database.model.config_model import Base, engine
from database.model.login import Login
from database.model.produto import Produto

if not database_exists(engine.url):
  create_database(engine.url)

Base.metadata.create_all(engine)

picanha = Produto( id_produtos ='picanha'
                 , nome = 'Picanha'
                 , fornecedor = 'Frigorífico Argentino'
                 , preco =  30
                 , categoria = 'carnes'
                 , informacao = 'Quantidade minina: 150 gramas'
                 , detalhamento = 'Na nossa busca incessante pela perfeição gastronômica, apresentamos a Picanha Suprema: um verdadeiro tesouro de sabor e maciez. Cuidadosamente selecionada a partir das melhores raças de gado, nossa picanha é uma sinfonia de suculência e textura que transcende todas as expectativas. Proveniente da parte traseira do boi, próxima à cauda, esse corte triangular é um presente para os amantes de churrasco e apreciadores da alta gastronomia. Com seu marmoreio perfeito e a camada de gordura que se derrete durante o cozimento, a Picanha Suprema proporciona uma experiência sensorial única, onde cada mordida revela um sabor intenso e suculento.'
                 , destaques = 'S')

Produto.cadastrar_produto(picanha)