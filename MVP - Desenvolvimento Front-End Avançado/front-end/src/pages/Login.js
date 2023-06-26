import React, { useEffect, useState } from 'react';
import Cookies from 'js-cookie';

import Logo from '../components/Logo'
import login from '../assets/login.svg'
import { useNavigate } from 'react-router-dom';

import '../style/login.css';

function Login() {
  const navigate = useNavigate();
  const [isLogado, setIsLogado] = useState(false);

  useEffect(() => {
    const storedIsLogado = Cookies.get('isLogado');
    
    if (storedIsLogado === 'true') {
      setIsLogado(true);
    }
  }, []);

  const verificar_login = (buttonId) => {
    let inputUsuario = document.getElementById("usuario").value;
    let inputSenha = document.getElementById("senha").value;

    if (inputUsuario === '') {
      alert("Digite o nome do usuário!");
    } else if (inputSenha === '') {
      alert("Digite a senha do usuário!");
    } else if (buttonId === 'entrar') {
      autenticar(inputUsuario, inputSenha)
    } else {
      criar_conta(inputUsuario, inputSenha)
    }
    }

  const autenticar = async (inputUsuario, inputSenha) => {
    let resposta_api = 'True'

    if (resposta_api === 'True'){
      alert('Login realizado!')
      setIsLogado(true);
      Cookies.set('isLogado', 'true');
      navigate('/')
    }
    else {
      alert('Dados Incorretos!')
    }
  }

  const criar_conta = async (inputUsuario, inputSenha) => {
    let resposta_api = 'True'

    if (resposta_api === 'True'){
      alert('Conta criada com sucesso!')
      setIsLogado(true);
      Cookies.set('isLogado', 'true');
      navigate('/')
    }
    else {
      alert('Erro ao criar conta!')
    }
  }
  
  if (isLogado === true) {
    navigate('/')
  }

  return (
    <div>
      {isLogado ? (
        navigate('/')
      ): (
        <div className='Login'>
          <section className='SecaoDireita'>
            <div className='FrameDireita'>
              <Logo />
              <p id='FraseEmpresa'> Descubra a excelência em compras: nosso mercado online, onde qualidade e conveniência se encontram!</p>
            </div>
          </section >

          <section className='SecaoEsquerda'>
            <div className='FrameEsquerda'>
              <div className='TituloLogin'>
                <img src={ login } alt='Login' />
                <p>Login</p>
              </div>

              <div className='EntradaTexto'>
                <input type='text' id='usuario' placeholder='Usuário' required='required' autocomplete='off'/>
                <input type='text' id='senha' placeholder='Senha' required='required' autocomplete='off'/>
              </div>

              <div className='Botoes'>
                <button id='entrar' onClick= {() => verificar_login('entrar')}>ENTRAR</button>
                <button id='criar-conta' onClick= {() => verificar_login('criar-conta')}>CRIAR CONTA</button>
              </div>
            </div>
          </section >
        </div>
      )}
    </div>
  );
}

export default Login;