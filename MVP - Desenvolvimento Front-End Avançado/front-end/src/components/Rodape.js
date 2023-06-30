import Logo from '../components/Logo'

import '../style/produtos.css'

export default function Rodape() {
  return (
    <div className='Rodape'>
      <div className='RodapeSuperior'>
        <span>Voltar para o início</span>
      </div>

      <div className='RodapeInferior'>
        <Logo />
        <span>Descubra a excelência em compras: nosso mercado online, onde qualidade e conveniência se encontram!</span>
      </div>
    </div>
  );
}