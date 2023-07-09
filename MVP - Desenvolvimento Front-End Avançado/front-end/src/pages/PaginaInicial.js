import Cookies from 'js-cookie';
import React, { useState, useEffect }  from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'

import Header from '../components/Header'
import Navegacao from '../components/Navegacao'
import Rodape from '../components/Rodape'
import BannerCarousel from '../components/Banner-Carousel'
import CardProduto from '../components/Card-Produto'

import '../style/produtos.css'

export default function PaginaInicial() {
  const cookieNomeUsuario = Cookies.get('nomeUsuario');
  const navigate = useNavigate();
  const [produtosLista, setProdutosLista] = useState([]);
  const [categoria, setCategoria] = useState('Destaques');
  const [quantidade, setQuantidade] = useState(0);
  const [valorTotal, setValorTotal] = useState(0);
  const [scrollPosicao, setScrollPosicao] = useState(0);
  const [statusAPI, setStatusAPI] = useState(0);
  const larguratela = window.innerWidth;
  const numeroCards = produtosLista.length;
  const numeroCardsVisiveis = Math.round((larguratela/(221)));
  let [cardAtual, setCardAtual] = useState(numeroCardsVisiveis)

  const tipoCategoria = (infoCategoria) => {
    setCategoria(infoCategoria)
  }

  const scrollEsquerda = () => {
    const novaPosicao = scrollPosicao - 230

    if(cardAtual > numeroCardsVisiveis) {
      setCardAtual(cardAtual - 1)
      setScrollPosicao(novaPosicao)
    }
  };

  const scrollDireita = () => {
    const novaPosicao = scrollPosicao + 230

    if(cardAtual <= numeroCards) {
      setCardAtual(cardAtual + 1)
      setScrollPosicao(novaPosicao)
    }
  }

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/listar_produto', {
      params: {categoria: categoria}
    })
      .then(res => setProdutosLista(res.data.produtos))
      .catch(error => console.log(error))
  }, [categoria])

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/obter_dados_carrinho')
      .then(res => {
        setQuantidade(res.data.quantidade);
        setValorTotal(res.data.preco.toFixed(2));
      })
      .catch(error => console.log(error));
  }, [statusAPI]);
   
  async function quantidadeCompras (nomeProduto, numCompras, preco) {
    try {
      if (cookieNomeUsuario) {
        const valor = (numCompras * preco).toFixed(2);

        if (window.confirm(`Deseja adicionar a compra no valor de R$ ${valor} ao carrinho?`)) {
          const formData = new FormData();
          formData.append('usuario', cookieNomeUsuario);
          formData.append('produto', nomeProduto);
          formData.append('quantidade', numCompras);
          formData.append('preco', valor);

          const url = 'http://127.0.0.1:5000/inserir_compra';
          const response = await axios.post(url, formData);
          const data = response.data;
          
          setStatusAPI(prevCounter => -prevCounter);

          alert(data.mensagem)
        }
      } else {
        alert('É necessário realizar login para adicionar compras ao carrinho!')
      }
    } catch (error) {
      console.error('Error: ', error)
    }   
  }

  async function finalizarCarrinho () {
    try {
      if (quantidade === 0) {
        alert('Não existem items no carrinho!')
      } else if (window.confirm(`Deseja realizar a compra no valor de R$ ${valorTotal}?`)) {
        let url = 'http://127.0.0.1:5000/finalizar_carrinho';
        const response = await axios.put(url);
        const data = response.data;

        alert(data.mensagem);

        setStatusAPI(prevCounter => -prevCounter);
      } else {
        alert('Continue comprando!')
      }
    } catch (error) {
      console.error('Error: ', error)
     }
  }

  async function cancelarCarrinho () {
    try {
      if (quantidade === 0) {
        alert('Não existem items no carrinho!')
      } else if (window.confirm(`Deseja cancelar a compra no valor de R$ ${valorTotal}?`)) {
        let url = 'http://127.0.0.1:5000/cancelar_carrinho';
        const response = await axios.put(url);
        const data = response.data;
        
        alert(data.mensagem);
        
        setStatusAPI(prevCounter => -prevCounter);       
      } else {
        alert('Continue comprando!')
      }
    } catch (error) {
      console.error('Error: ', error)
     }
  }
  
  return (
    <div className='Page'>
      <header>
        <div className='Topo'>
          <Header quantidade={quantidade} valor={valorTotal} comprar={finalizarCarrinho} cancelar={cancelarCarrinho}/>
        </div>
        
        <div className='Navegacao'>
          <Navegacao tipoCategoria={tipoCategoria} />
        </div>
      </header>

      <main>
        <div className='Body'>
          <div className='LocalizadorPagina'> 
            <span id='LocalizadorInicial'onClick={() => navigate('/')}>Pagina Inicial</span>
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