import Cookies from 'js-cookie';
import { useState } from "react";

import Logo from './Logo'
import lupa from '../assets/lupa.svg'
import setaLogin from '../assets/seta-para-baixo.svg'
import carrinho from '../assets/carrinho.svg'

export default function Header(props) {
  const cookieNomeUsuario = Cookies.get('nomeUsuario');
  let quantidade = props.quantidade

  return (
    <div className='Header'>
      <Logo />

      <div className='Busca'>
        <input type='text' id='barra-busca' placeholder='Busque aqui seu produto' autocomplete='off'/>
        <img src={ lupa } alt='lupa' />
      </div>

      <div className='StatusLogin'>
        <p>Olá, {cookieNomeUsuario ? `${cookieNomeUsuario}!` : 'faça seu login'}</p>
        
        <div className='Contas'>
          <p>Contas</p>
          <img src={ setaLogin } alt='setalogin' />
        </div>
      </div>

      <div className='Carrinho'>
        <img src={ carrinho } alt='setalogin' />
        <p> { quantidade }</p>
      </div>  
    </div>
  )
}