import React from 'react';

import Header from '../components/Header'

import '../style/produtos.css'

export default function PaginaInicial() {
  const quantidade = 0;

  return (
    <header>
      <Header quantidade={quantidade} />
    </header>
  );
}