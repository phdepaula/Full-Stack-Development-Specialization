import Logo from '../components/Logo'

import '../style/produtos.css'

export default function Rodape() {

  const RolarParaCima = () => {
    const pageElement = document.querySelector('.Page');
    if (pageElement) {
      pageElement.scrollTop = 0;
    }
  };

  return (
    <div className='Rodape'>
      <div className='RodapeSuperior'>
        <span id='VoltarInicio' onClick={RolarParaCima}>Voltar para o início</span>
      </div>

      <div className='RodapeInferior'>
        <Logo />
        <span>Descubra a excelência em compras: nosso mercado online, onde qualidade e conveniência se encontram!</span>
      </div>
    </div>
  );
}