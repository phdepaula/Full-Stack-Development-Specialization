const getVendas = async () => {
  let url = 'http://127.0.0.1:5000/listar_vendas';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.vendas.forEach(item => insertListVendas(item.id_vendas, item.proprietario, item.nome, item.marca, item.ano, item.valor, item.tipo, item.data_entrada, item.status))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


getVendas()


const insertListVendas = (id_vendas, proprietario, nome, marca, ano, valor, tipo, data_entrada, status) => {
  var item = [id_vendas, proprietario, nome, marca, ano, valor, tipo, data_entrada, status]
  var table = document.getElementById('TableVendas');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
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
      const idItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteVenda(idItem)
        alert("Removido!")
      }
    }
  }
}


const deleteVenda = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/deletar_vendas?id=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


const verificar_venda = () => {
    let inputProprietario = document.getElementById("proprietario").value;
    let inputAutomovel = document.getElementById("automovel").value;
    let inputValor = document.getElementById("valor").value;
    let inputAno = document.getElementById("ano").value;
    let inputStatus = document.getElementById("status").value;
     
    if (inputProprietario === '') {
      alert("Digite o nome do proprietário!");
    } else if (inputAutomovel === '') {
      alert("Digite o nome do automóvel!");
    } else if (inputValor === '') {
        alert("Digite o valor da venda!");
    } else if (inputAno === '') {
      alert("Digite o ano do automóvel!");
    } else if (inputStatus === '') {
      alert("Digite o status da venda!");
    } else {
      cadastrar_vendas(inputProprietario, inputAutomovel, inputValor, inputAno, inputStatus)
      window.location.href = "http://127.0.0.1:5000/vendas"
    }
  }
  

  const cadastrar_vendas = async (inputProprietario, inputAutomovel, inputValor, inputAno, inputStatus) => {
    const formData = new FormData();
    formData.append('proprietario', inputProprietario);
    formData.append('automovel', inputAutomovel);
    formData.append('valor', inputValor);
    formData.append('ano', inputAno);
    formData.append('status', inputStatus);

    let url = 'http://127.0.0.1:5000/cadastar_vendas';
    fetch(url, {
      method: 'post',
      body: formData
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.mensagem)
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  
  const direcionar_automovel = () => {
    window.location.href = "http://127.0.0.1:5000/automovel";
  }


  const direcionar_vendas = () => {
    window.location.href = "http://127.0.0.1:5000/vendas";
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