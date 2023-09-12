import '../style/produtos.css'

export default function Navegacao({tipoCategoria}) {
  return (
    <div className='NavegacaoItems'>
      <div className='ContainerNavegacao'>
        <div className='NavegacaoSpan'>
          <span onClick={() => tipoCategoria('Destaques')}>Destaques</span>
        </div>

        <div className='NavegacaoSpan'>
          <span onClick={() => tipoCategoria('Bebidas')}>Bebidas</span>
        </div>

        <div className='NavegacaoSpan'>
          <span onClick={() => tipoCategoria('Carnes')}>Carnes</span>
        </div>

        <div className='NavegacaoSpan'>
          <span onClick={() => tipoCategoria('Complementos')}>Complementos</span>
        </div>

        <div className='NavegacaoSpan'> 
          <span onClick={() => tipoCategoria('Frutas')}>Frutas</span>
        </div>

        <div className='NavegacaoSpan'>  
          <span onClick={() => tipoCategoria('Verduras')}>Verduras</span>
        </div>
      </div>
    </div>
  );
}
