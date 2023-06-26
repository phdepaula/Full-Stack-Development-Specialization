import React from 'react';

import Logo from '../components/Logo'
import login from '../assets/login.svg'

import '../style/login.css';

function Login() {
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
    }
    else {
      alert('Dados Incorretos!')
    }
  }

  const criar_conta = async (inputUsuario, inputSenha) => {
    let resposta_api = 'True'

    if (resposta_api === 'True'){
      alert('Conta criada com sucesso!')
    }
    else {
      alert('Erro ao criar conta!')
    }
  }

  return (
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
  );
}

export default Login;