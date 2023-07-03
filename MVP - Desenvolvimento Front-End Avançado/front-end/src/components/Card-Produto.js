import { useState, useEffect } from "react";
import adicionar from '../assets/general/mais.svg'
import remover from '../assets/general/menos.svg'

import cerveja from '../assets/products/bebidas/cerveja.svg'
import cha from '../assets/products/bebidas/cha.svg'
import coca from '../assets/products/bebidas/coca.svg'
import guarana from '../assets/products/bebidas/guarana.svg'
import iorgute from '../assets/products/bebidas/iorgute.svg'
import leite from '../assets/products/bebidas/leite.svg'
import sucolaranja from '../assets/products/bebidas/suco-laranja.svg'
import sucouva from '../assets/products/bebidas/suco-uva.svg'

import picanha from '../assets/products/carnes/picanha.svg'
import alcatra from '../assets/products/carnes/alcatra.svg'
import cupim from '../assets/products/carnes/cupim.svg'
import fraldinha from '../assets/products/carnes/fraldinha.svg'
import frango from '../assets/products/carnes/frango.svg'
import linguica from '../assets/products/carnes/linguiça.svg'
import picanhasuina from '../assets/products/carnes/picanha-suina.svg'
import maminha from '../assets/products/carnes/maminha.svg'

import acucar from '../assets/products/complementos/açucar.svg'
import arroz from '../assets/products/complementos/arroz.svg'
import azeite from '../assets/products/complementos/azeite.svg'
import cremeleite from '../assets/products/complementos/creme-de-leite.svg'
import macarrao from '../assets/products/complementos/macarrao.svg'
import mussarela from '../assets/products/complementos/mussarela.svg'
import presunto from '../assets/products/complementos/presunto.svg'
import sal from '../assets/products/complementos/sal.svg'

import abacate from '../assets/products/frutas/abacate.svg'
import banana from '../assets/products/frutas/banana.svg'
import goiaba from '../assets/products/frutas/goiaba.svg'
import maca from '../assets/products/frutas/maça.svg'
import mamao from '../assets/products/frutas/mamao.svg'
import manga from '../assets/products/frutas/manga.svg'
import pera from '../assets/products/frutas/pera.svg'
import uva from '../assets/products/frutas/uva.svg'

import beterraba from '../assets/products/verduras/beterraba.svg'
import brocolis from '../assets/products/verduras/brocolis.svg'
import cebola from '../assets/products/verduras/cebola.svg'
import cenoura from '../assets/products/verduras/cenoura.svg'
import couveflor from '../assets/products/verduras/couve-flor.svg'
import couve from '../assets/products/verduras/couve.svg'
import pepino from '../assets/products/verduras/pepino.svg'
import tomate from '../assets/products/verduras/tomate.svg'

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
    }
  };

  useEffect(() => {
    const imagensProdutos = {
      picanha: picanha,
      alcatra: alcatra,
      maminha: maminha,
      cupim: cupim,
      fraldinha: fraldinha,
      frango: frango,
      picanhasuina: picanhasuina,
      linguica: linguica,
      cerveja: cerveja,
      cha: cha,
      coca: coca,
      guarana: guarana,
      iorgute: iorgute,
      leite: leite,
      sucolaranja: sucolaranja,
      sucouva: sucouva,
      acucar: acucar,
      arroz: arroz,
      azeite: azeite,
      cremeleite: cremeleite,
      macarrao: macarrao,
      mussarela: mussarela,
      presunto: presunto,
      sal: sal,
      abacate: abacate,
      banana: banana, 
      goiaba: goiaba,
      maca: maca,
      mamao: mamao,
      manga: manga,
      pera: pera,
      uva: uva,
      beterraba: beterraba,
      brocolis: brocolis, 
      cebola: cebola,
      cenoura: cenoura,
      couveflor: couveflor,
      couve: couve,
      pepino: pepino,
      tomate: tomate
    };
  
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
