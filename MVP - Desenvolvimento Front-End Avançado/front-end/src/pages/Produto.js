import Cookies from 'js-cookie';
import React, { useState, useEffect }  from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import axios from 'axios'

import Header from '../components/Header'
import Navegacao from '../components/Navegacao'
import Rodape from '../components/Rodape'
import ProdutoDetalhado from '../components/Produto-Detalhado';
import CardProduto from '../components/Card-Produto'

import '../style/produtos.css'

import PaginaNaoEncontrada from './PaginaNaoEncontrada';

export default function PaginaInicial() {
  const cookieNomeUsuario = Cookies.get('nomeUsuario');
  const { nome } = useParams();
  const navigate = useNavigate();
  const [produtosLista, setProdutosLista] = useState([]);
  const [categoria, setCategoria] = useState('Destaques');
  const [quantidade, setQuantidade] = useState(0);
  const [valorTotal, setValorTotal] = useState(0);
  const [scrollPosicao, setScrollPosicao] = useState(0);
  const [statusProduto, setStatusProduto] = useState(false);
  const [dadosProduto, setDadosProduto] = useState([]);
  const larguratela = window.innerWidth;
  const numeroCards = produtosLista.length;
  const numeroCardsVisiveis = Math.round((larguratela/(221)));
  let [cardAtual, setCardAtual] = useState(numeroCardsVisiveis)

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/listar_produto', {
      params: {categoria: categoria}
    })
      .then(res => setProdutosLista(res.data.produtos))
      .catch(error => console.log(error))
  }, [categoria])

  useEffect(() => {
    const buscarProduto = async () => {
      try {
        const formData = new FormData();
        formData.append('nome', nome);
  
        let url = 'http://127.0.0.1:5000/buscar_produto';
        const response = await axios.post(url, formData);
        const data = response.data;
  
        if (data.status === true) {
          setStatusProduto(true)
          setDadosProduto(data.produto)
        }
      } catch (error) {
        console.error('Error:', error);
      }
    };
  
    buscarProduto();
  }, [nome]);
  
  const tipoCategoria = (infoCategoria) => {
    setCategoria(infoCategoria)
  }
  
  const quantidadeCompras = (numCompras, preco) => {
    if(cookieNomeUsuario) {
      const valor = Math.round((numCompras*preco))

      if (window.confirm(`Deseja adicionar a compra no valor de R$ ${valor} ao carrinho?`)) {
        setQuantidade(quantidade + numCompras)
        setValorTotal(valorTotal + valor)
        alert('Compra adicionada ao carrinho!')
      }
    } else {
      alert('É necessário realizar login para adicionar compras ao carrinho!')
    }    
  }

  const finalizarCompra = () => {
    if (quantidade === 0) {
      alert('Não existem items no carrinho!')
    } else if (window.confirm(`Deseja realizar a compra no valor de R$ ${valorTotal}?`)) {
      setValorTotal(0)
      setQuantidade(0);
      alert('Compra realizada com sucesso!')
    } else if (window.confirm(`Deseja cancelar a compra no valor de R$ ${valorTotal}?`)) {
      setValorTotal(0)
      setQuantidade(0);
      alert('Compra cancelada!')
    } else {
      alert('Continue comprando!')
    }
  }

  const cancelarPagamento = (quantidadeCancelada, preco) => {
    if (quantidade === 0) {
      alert('Não existem compras no carrinho!')
    }else if (window.confirm(`Deseja cancelar ${quantidadeCancelada} compras(s) de ${nome}?`)) {
      const valorCancelado = Math.round((quantidadeCancelada*preco))
      
      alert('Compra(s) canceladas!')
      setQuantidade(quantidade - quantidadeCancelada);
      setValorTotal(valorTotal - valorCancelado)
    } else {
      alert('Continue comprando!')
    }
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

  return (
    statusProduto.status === false ? <PaginaNaoEncontrada/>:
    <div className='Page'>
      <header>
        <div className='Topo'>
          <Header quantidade={quantidade} comprar={finalizarCompra} />
        </div>
        
        <div className='Navegacao'>
          <Navegacao tipoCategoria={tipoCategoria} />
        </div>
      </header>

      <main>
        <div className='Body'>
          <div className='LocalizadorPagina'>
            <span id='LocalizadorInicial'onClick={() => navigate('/')}>Pagina Inicial</span>
            <span>{'>'}</span>
            <span>{'Produto'}</span>
            <span>{'>'}</span>
            <span>{nome}</span>
          </div>

          <div className='ProdutosDetalhados'>
            <ProdutoDetalhado produto={dadosProduto} quantidadeCompras={quantidadeCompras} cancelarPagamento={cancelarPagamento}/>
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