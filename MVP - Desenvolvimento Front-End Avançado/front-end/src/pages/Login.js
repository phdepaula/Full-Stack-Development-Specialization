import React, { useEffect } from 'react';
import Cookies from 'js-cookie';

import Logo from '../components/Logo'
import login from '../assets/general/login.svg'
import { useNavigate } from 'react-router-dom';

import '../style/login.css';

export default function Login() {
  const navigate = useNavigate();

  useEffect(() => {
    const cookieNomeUsuario = Cookies.get('nomeUsuario');
    
    if (cookieNomeUsuario) {
      navigate('/')
    }
  }, []);

  const verificar_login = (buttonId) => {
    let usuario = document.getElementById('usuario').value;
    let senha = document.getElementById('senha').value;

    if (usuario === '') {
      alert('Digite o nome do usuário!');
    } else if (senha === '') {
      alert('Digite a senha do usuário!');
    } else if (buttonId === 'entrar') {
      autenticar(usuario, senha)
    } else {
      criar_conta(usuario, senha)
    }
    }

  const autenticar = async (usuario, senha) => {
    const formData = new FormData();
    formData.append('usuario', usuario);
    formData.append('senha', senha);

    let url = 'http://127.0.0.1:5000/autenticar_login';
    
    fetch(url, {
      method: 'post',
      body: formData
    })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === true){
        alert('Login realizado!')
        Cookies.set('nomeUsuario', data.usuario);
        navigate('/')
      }
      else {
        alert('Dados incorretos!')
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }

  const criar_conta = async (usuario, senha) => {
    const formData = new FormData();
    formData.append('usuario', usuario);
    formData.append('senha', senha);

    let url = 'http://127.0.0.1:5000/cadastrar_login';
    
    fetch(url, {
      method: 'post',
      body: formData
    })
    .then((response) => response.json())
    .then((data) => {
      if (data.mensagem === 'Usuário cadastrado com sucesso!'){
        alert(data.mensagem)
      }
      else {
        alert('Erro ao criar conta!')
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }
  
  let cookieNomeUsuario = Cookies.get('nomeUsuario');

  return (
    <div>
      {cookieNomeUsuario ? (
        navigate('/')
      ): (
        <div className='Login'>
          <section className='SecaoDireita'>
            <div className='FrameDireita'>
              <Logo />
              <span id='FraseEmpresa'> Descubra a excelência em compras: nosso mercado online, onde qualidade e conveniência se encontram!</span>
            </div>
          </section >

          <section className='SecaoEsquerda'>
            <div className='FrameEsquerda'>
              <div className='TituloLogin'>
                <img src={ login } alt='Login' />
                <span>Login</span>
              </div>

              <div className='EntradaTexto'>
                <input type='text' id='usuario' placeholder='Usuário' required='required' autoComplete='off'/>
                <input type='password' id='senha' placeholder='Senha' required='required' autoComplete='off'/>
              </div>

              <div className='Botoes'>
                <button id='entrar' onClick={() => verificar_login('entrar')}>ENTRAR</button>
                <button id='criar-conta' onClick={() => verificar_login('criar-conta')}>CRIAR CONTA</button>
              </div>
            </div>
          </section >
        </div>
      )}
    </div>
  );
}