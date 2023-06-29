import React from 'react';

import Header from '../components/Header'

import '../style/produtos.css'

export default function PaginaInicial() {
  const quantidade = 0;
  const categoria = 'carnes';

  return (
    <div className='Page'>
      <header>
        <div className='Topo'>
          <Header quantidade={quantidade} categoria ={categoria}/>
        </div>
        
        <div className='Navegacao'>
          <span>OI</span>
        </div>
      </header>
    </div>
  );
}