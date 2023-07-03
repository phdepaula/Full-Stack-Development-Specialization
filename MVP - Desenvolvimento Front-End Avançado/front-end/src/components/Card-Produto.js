import { useState, useEffect } from "react";

import adicionar from '../assets/general/mais.svg'
import remover from '../assets/general/menos.svg'
import { imagensProdutos }  from './Imagens'

export default function CardProduto(props) {
  const produto = props.produto;
  const compras = props.quantidadeCompras;
  
  const [quantidade, setQuantidade] = useState(1);
  const [imagem, setImagem] = useState(null);

  const mais = () => {
    setQuantidade(quantidade + 1);
  };

  const menos = () => {
    if (quantidade > 1) {
      setQuantidade(quantidade - 1);
    } else {
      alert('A quantidade mínima do produto é 1!')
    }
  };

  useEffect(() => {
    if (produto.id in imagensProdutos) {
      setImagem(imagensProdutos[produto.id]);
    }
  }, [produto.id]);

  return (
    <article className='CardProduto'>
      <div className='ImagemProduto'>
        <img src={imagem} alt='Imagem do Produto' />
      </div>

      <div className='DetalhesProduto'>
        <span id='NomeProduto'>{produto.nome}</span>
        <span id='DescricaoProduto'>{produto.descricao}</span>
        <span id='Preco'>R$ {produto.preco}</span>
      </div>

      <div className='QuantidadeCard'>
        <span id='TextoQuantidade'>Quantidade:</span>
        <span id='ItensQuantidade'>{quantidade}</span>
        <img src={adicionar} alt="mais" onClick={mais}/>
        <img src={remover} alt="menos" onClick={menos}/>
      </div>

      <div className='ComprarCard'>
        <button id='ButtonComprarCard' onClick={() => compras(quantidade, produto.preco)}>Comprar</button>
      </div>
    </article>
  );
}
