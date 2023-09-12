import star from '../assets/general/star.svg'

export default function Logo() {
  return (
    <div className='LogoPadrao'>
      <p>MERCADO</p>
      <img src={ star } alt='Star' />
    </div>
  )
}