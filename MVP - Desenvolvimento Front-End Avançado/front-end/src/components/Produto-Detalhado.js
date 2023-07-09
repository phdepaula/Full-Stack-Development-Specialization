import { useState } from "react";

import { imagensProdutos } from "./Imagens"
import adicionar from '../assets/general/mais.svg'
import remover from '../assets/general/menos.svg'

export default function ProdutoDetalhado(props) {
  const produto = props.produto
  const compras = props.quantidadeCompras;
  const cancelarPagamento = props.cancelarPagamento
  const imagem = imagensProdutos[produto.id]
  const [quantidade, setQuantidade] = useState(1);
  let valor = (quantidade*produto.preco).toFixed(2);

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

  return (
    <div className='Produto'>
      <div className='DadosProdutos'>
        <div className='ImagemProdutoDetalhado'>
          <img src={imagem} alt='Imagem do Produto'/>
        </div>

        <div className='InformacoesAdicionais'>
          <span id='TituloProduto'>{produto.nome}</span>
          <span id='Detalhamento'>{produto.detalhamento}</span>

          <div className='Estrutura'>
            <div className='Topicos'>
              <div className='Categoria'>
                <span id='categoria'>Categoria:</span>
                <span id='nomecategoria'>{produto.categoria}</span>
              </div>
              <div className='Fornecedor'>
                <span id='fornecedor'>Fornecedor:</span>
                <span id='nomefornecedor'>{produto.fornecedor}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className='Pagamento'>
        <span id='TituloPagamento'>Pagamento</span>

        <div className='InformacoesPagamento'>
          <div className='PrecoPagamentoObsevacao'>
            <div className='PrecoPagamento'>
              <span id='precopagamento'>Preço:</span>
              <span id='valorunitario'>R$ {produto.preco}</span>
            </div>

            <div className='Observacao'>
              <span id='observacao'>{produto.informacao}</span>
            </div>
          </div>

          <div className='GrupoQuantidadePreco'>
            <div className='PrecoTotal'>
              <span id='total'>Total:</span>
              <span id='valortotal'>R$ {valor}</span>
            </div>

            <div className='QuantidadePagamento'>
              <span id='TextoQuantidadePagamento'>Quantidade:</span>
              <span id='NumQuantidadePagamento'>{quantidade}</span>
              <img src={adicionar} alt="mais" onClick={mais}/>
              <img src={remover} alt="menos" onClick={menos}/>
            </div>
          </div>

          <div className='ButtonsPagamento'>
            <button id='ButtonComprarPagamento' onClick={() => compras(produto.nome, quantidade, produto.preco)}>Comprar</button>
            <button id='ButtonCancelarPagamento' onClick={() => cancelarPagamento(produto.nome, quantidade, produto.preco)}>Cancelar</button>
          </div>
        </div>
      </div>
    </div>
  )
}