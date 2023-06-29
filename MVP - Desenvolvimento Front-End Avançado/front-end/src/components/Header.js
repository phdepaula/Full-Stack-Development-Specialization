import Cookies from 'js-cookie';
import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';

import Logo from './Logo'
import lupa from '../assets/lupa.svg'
import setaLogin from '../assets/seta-para-baixo.svg'
import carrinho from '../assets/carrinho.svg';

import produtos from '../produtos.json'

export default function Header(props) {
  const [clickLogin, setClickLogin] = useState(false);
  const cookieNomeUsuario = Cookies.get('nomeUsuario');
  const navigate = useNavigate();
  const loginArea = useRef(null);

  let quantidade = props.quantidade;
  let categoria =props.categoria;

  function mostrarDiv() {
    setClickLogin(!clickLogin);
  }

  useEffect(() => {
    function handleClickOutside(event) {
      if (loginArea.current && !loginArea.current.contains(event.target)) {
        setClickLogin(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);

    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  function acaoLogin() {
    if(cookieNomeUsuario) {
      alert('Logout realizado!')
      Cookies.remove('nomeUsuario');
      navigate('/login')
    } else {
      navigate('/login')
    }
  }

  function pesquisar() {
    let pesquisa = document.getElementById('barra-busca').value;

    if(pesquisa.trim().length === 0) {
      alert('Favor digitar o nome produto!')
    } else if (produtos[categoria] && produtos[categoria].some(item => item.nome === pesquisa)) {
      navigate('/produto/' + pesquisa)
    } else {
      alert('O produto nao existe!')
    }
  }

  return (
    <div className='Header'>
      <Logo />

      <div className='Busca'>
        <input type='text' id='barra-busca' placeholder='Busque aqui seu produto' autoComplete='off' />
        <img src={lupa} alt='lupa' onClick={pesquisar}/>
      </div>

      <div className='StatusLogin'>
        <span>Olá, {cookieNomeUsuario ? `${cookieNomeUsuario}!` : 'faça seu login'}</span>

        <div className='Contas'>
          <span>Contas</span>
          <img src={setaLogin} alt='setalogin' onClick={mostrarDiv} />
        </div>
      </div>
    
      {clickLogin && (
          <div className='LoginOculto'>
            <div className='EscurecerFundo' />
            <div className='BGLogin' ref={loginArea}>
              <button id='ButtonLogin' onClick={acaoLogin}>{cookieNomeUsuario ? 'Fazer Logout' : 'Fazer Login'}</button>
            </div>
          </div>
        )
      }

      <div className='Carrinho'>
        <img src={carrinho} alt='setalogin' />
        <span> {quantidade}</span>
      </div>
    </div>
  );
}
