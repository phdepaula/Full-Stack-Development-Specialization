import Cookies from 'js-cookie';
import React, { useState }  from 'react';
import { useNavigate } from 'react-router-dom';

import Header from '../components/Header'
import Navegacao from '../components/Navegacao'
import Rodape from '../components/Rodape'
import BannerCarousel from '../components/Banner-Carousel'
import CardProduto from '../components/Card-Produto'

import produtos from '../produtos.json'

import '../style/produtos.css'

export default function PaginaInicial() {
  const cookieNomeUsuario = Cookies.get('nomeUsuario');
  const navigate = useNavigate();
  
  const [produtosLista, setProdutosLista] = useState(produtos.produtos);
  const [categoria, setCategoria] = useState('Destaques');
  const [quantidade, setQuantidade] = useState(0);
  const [valorTotal, setValorTotal] = useState(0);
  const [scrollPosicao, setScrollPosicao] = useState(0);

  const larguratela = window.innerWidth;
  const numeroCards = produtosLista.length;
  const numeroCardsVisiveis = Math.round((larguratela/(221)));
  let [cardAtual, setCardAtual] = useState(numeroCardsVisiveis)

  const tipoCategoria = (infoCategoria) => {
    setCategoria(infoCategoria)
  }
  
  const quantidadeCompras = (numCompras, preco) => {
    if(cookieNomeUsuario) {
      const valor = Math.round((numCompras*preco));

      if (window.confirm(`Deseja adicionar a compra no valor de R$ ${valor} ao carrinho?`)) {
        setQuantidade(quantidade + numCompras);
        setValorTotal(valorTotal + valor)
        alert('Compra adicionada ao carrinho!')
      }
    } else {
      alert('É necessário realizar login para adicionar compras ao carrinho!')
    }    
  }
  
  const scrollEsquerda = () => {
    const novaPosicao = scrollPosicao - 221

    if(cardAtual > numeroCardsVisiveis) {
      setCardAtual(cardAtual - 1)
      setScrollPosicao(novaPosicao)
    }
  };

  const scrollDireita = () => {
    const novaPosicao = scrollPosicao + 221

    if(cardAtual <= numeroCards) {
      setCardAtual(cardAtual + 1)
      setScrollPosicao(novaPosicao)
    }
  }

  return (
    <div className='Page'>
      <header>
        <div className='Topo'>
          <Header quantidade={quantidade}/>
        </div>
        
        <div className='Navegacao'>
          <Navegacao tipoCategoria={tipoCategoria} />
        </div>
      </header>

      <main>
        <div className='Body'>
          <div className='LocalizadorPagina'> 
            <span onClick={() => navigate('/')}>Pagina Inicial</span>
          </div>

          <div className='BannerCarousel'>
            <BannerCarousel />
          </div>

          <div className='TituloCards'>
            <span>{categoria}</span>
          </div>

          <div className='Cards'>
            <div className='ListaProduto' style={{ transform: `translateX(-${scrollPosicao}px)`, flexGrow: 1 }}>
                {produtosLista.map((p, index) => (
                <CardProduto key={index} produto={p} quantidadeCompras={quantidadeCompras}/>
              ))}
            </div>

            <div className='SetasProdutos'>
              <button id='scrollEsquerda' onClick={scrollEsquerda}>&lt;</button>
              <button id='scrollDireita' onClick={scrollDireita}>&gt;</button>
            </div>
          </div>
        </div>
      </main>

      <footer>
        <Rodape />
      </footer>
    </div>
  );
}