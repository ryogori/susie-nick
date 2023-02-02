
const swiper = new Swiper('.swiper', {
  slidesPerView: 1, //表示させるスライド数
  spaceBetween: 10, //スライド間の余白
  loop:true,//画像ループの有無

  //ボタンのやつ。
  navigation: {
  nextEl: '.swiper-button-next',
  prevEl: '.swiper-button-prev',
  },

  observer: true, 
  observeParents: true,
  observeSlideChildren: true,

  autoplay:{
    delay: 5000,
    disableOnInteraction: false,
    waitForTransition: false,
  },
});