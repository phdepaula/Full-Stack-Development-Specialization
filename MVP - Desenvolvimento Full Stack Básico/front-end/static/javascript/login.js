const verificar_login = () => {
  let inputUsuario = document.getElementById("usuario").value;
  let inputSenha = document.getElementById("senha").value;

  if (inputUsuario === '') {
    alert("Digite o nome do usuário!");
  } else if (inputSenha === '') {
    alert("Digite a senha do usuário!");
  } else {
    autenticar(inputUsuario, inputSenha)
  }
}


const autenticar = async (inputUsuario, inputSenha) => {

  let url = 'http://127.0.0.1:5000/autenticar?usuario=' + inputUsuario +'&senha=' + inputSenha;
  fetch(url, {
    method: 'post',
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.mensagem)
      if (data.mensagem === 'Login realizado com sucesso!'){
        window.location.href = "http://127.0.0.1:5000/vendas";
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


const logout = async () => {

  let url = 'http://127.0.0.1:5000/logout';
  fetch(url, {
    method: 'post',
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.mensagem)
      if (data.mensagem === 'O usuário foi desconectado!'){
        window.location.href = "http://127.0.0.1:5000/login";
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}