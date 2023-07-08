import Cookies from 'js-cookie';
import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios'

import Logo from './Logo'
import lupa from '../assets/general/lupa.svg'
import setaLogin from '../assets/general/seta-para-baixo.svg'
import carrinho from '../assets/general/carrinho.svg';


export default function Header(props) {
  const cookieNomeUsuario = Cookies.get('nomeUsuario');
  const navigate = useNavigate();
  const quantidade = props.quantidade;
  const comprar = props.comprar;
  const [clickLogin, setClickLogin] = useState(false);
  const loginArea = useRef(null);
  const [clickCarrinho, setClickCarrinho] = useState(false);
  const carrinhoArea = useRef(null);
 
  function mostrarDivLogin() {
    setClickLogin(!clickLogin);
  }

  useEffect(() => {
    function statusClickLogin(event) {
      if (loginArea.current && !loginArea.current.contains(event.target)) {
        setClickLogin(false);
      }
    }

    document.addEventListener('mousedown', statusClickLogin);

    return () => {
      document.removeEventListener('mousedown', statusClickLogin);
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

  async function pesquisar() {
   try {
    let pesquisa = document.getElementById('barra-busca').value;

    const formData = new FormData();
    formData.append('nome', pesquisa);

    if (pesquisa.trim().length === 0) {
      alert('Favor digitar o nome do produto!');
    } else {
      let url = 'http://127.0.0.1:5000/buscar_produto'
      const response = await axios.post(url, formData);
      const data = response.data;

      if (data.status === true) {
        navigate('/produto/' + data.produto.nome)
      } else {
        alert('O produto nao existe!')
      }
    } 
   } catch (error) {
    console.error('Error: ', error)
   }
  }
  
  function mostrarDivCarrinho() {
    setClickCarrinho(!clickLogin);
  }

  useEffect(() => {
    function statusClickCarrinho(event) {
      if (carrinhoArea.current && !carrinhoArea.current.contains(event.target)) {
        setClickCarrinho(false);
      }
    }

    document.addEventListener('mousedown', statusClickCarrinho);

    return () => {
      document.removeEventListener('mousedown', statusClickCarrinho);
    };
  }, []);

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
          <img src={setaLogin} alt='setalogin' onClick={mostrarDivLogin} />
        </div>
      </div>
    
      {clickLogin && (
          <div className='LoginOculto'>
            <div className='EscurecerFundo' />
            <div className='LoginArea' ref={loginArea}>
              <button id='ButtonLogin' onClick={acaoLogin}>{cookieNomeUsuario ? 'Fazer Logout' : 'Fazer Login'}</button>
            </div>
          </div>
        )
      }

      <div className='Carrinho' onClick={mostrarDivCarrinho}>
        <img src={carrinho} alt='setalogin' />
        <span> {quantidade}</span>
      </div>

      {clickCarrinho && (
          <div className='CarrinhoOculto' >
            <div className='EscurecerFundo' />
            <div className='CarrinhoArea' ref={carrinhoArea}>
              <button id='ButtonCarrinho' onClick={() => comprar()}>Finalizar Compra</button>
            </div>
          </div>
        )
      }
    </div>
  );
}
