import Slider from 'react-slick';

import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

import banner1 from '../assets/banner-1.svg'
import banner2 from '../assets/banner-2.svg'
import banner3 from '../assets/banner-3.svg'

export default function BannerCarousel() {
  const configuracaoCarousel = {
    infinite: true,
    speed: 3000,
    autoplaySpeed: 6000,
    autoplay: true,
    slidesToShow: 1,
    slidesToScroll: 1
  };

  const banners = [ <img src={banner1} alt="Banner1" id="Banner1" />
                  , <img src={banner2} alt="Banner2" id="Banner2"/>
                  , <img src={banner3} alt="Banner3" id="Banner3"/>];
  
  return (
    <div className='BannerCarouselComponente'>
      <Slider {...configuracaoCarousel}>
        {banners}
      </Slider>
    </div>
  )
}