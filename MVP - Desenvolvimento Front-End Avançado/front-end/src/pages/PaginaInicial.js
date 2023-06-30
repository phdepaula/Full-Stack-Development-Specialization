import React, { useState }  from 'react';

import Header from '../components/Header'
import Navegacao from '../components/Navegacao'
import Rodape from '../components/Rodape'

import '../style/produtos.css'

export default function PaginaInicial() {
  const quantidade = 0;
  const [categoria, setCategoria] = useState('Destaques');

  const tipoCategoria = (infoCategoria) => {
    setCategoria(infoCategoria)
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
          <span>Body</span>
        </div>
      </main>

      <footer>
        <Rodape />
      </footer>
    </div>
  );
}