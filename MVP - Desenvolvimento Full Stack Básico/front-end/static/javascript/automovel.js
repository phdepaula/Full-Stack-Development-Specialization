const getAutomovel = async () => {
  let url = 'http://127.0.0.1:5000/listar_automovel';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.automovel.forEach(item => insertListAutomovel(item.nome, item.marca, item.tipo))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


getAutomovel()


const insertListAutomovel = (nome, marca, tipo) => {
  var item = [nome, marca, tipo]
  var table = document.getElementById('TableAutomovel');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("nome").value = "";
  document.getElementById("marca").value = "";
  document.getElementById("tipo").value = "";

  removeElement()
}


const insertButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteAutomovel(nomeItem)
        alert("Removido!")
      }
    }
  }
}


const deleteAutomovel = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/deletar_automovel?nome=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


const verificar_carro = () => {
  let inputNome = document.getElementById("nome").value;
  let inputMarca = document.getElementById("marca").value;
  let inputTipo = document.getElementById("tipo").value;

  if (inputNome === '') {
    alert("Digite o nome do automóvel!");
  } else if (inputMarca === '') {
    alert("Digite a marca do automóvel!");
  } else if (inputTipo === '') {
      alert("Digite o tipo do automóvel!");
  } else {
    cadastrar_automovel(inputNome, inputMarca, inputTipo)
  }
}


const cadastrar_automovel = async (inputNome, inputMarca, inputTipo) => {
  const formData = new FormData();
  formData.append('nome', inputNome);
  formData.append('marca', inputMarca);
  formData.append('tipo', inputTipo);

  let url = 'http://127.0.0.1:5000/cadastar_automovel';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.mensagem)
      if (data.mensagem === 'SUCESSO! Automóvel cadastrado!'){
        insertListAutomovel(data.automovel.nome, data.automovel.marca, data.automovel.tipo)
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }


const direcionar_vendas = () => {
  window.location.href = "http://127.0.0.1:5000/vendas";
}


const direcionar_automovel = () => {
  window.location.href = "http://127.0.0.1:5000/automovel";
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