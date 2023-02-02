// $(function(){
//     var $dropdown = $('.dropdown_btn');
//     var DURATION = 200; //アニメーションの速さ
  
//     function fadeOutMenu(){
//       $dropdown.removeClass('is-active')
//         .next('.dropdown_btn-menu')
//         .stop()
//         .slideUp(DURATION);
//     }
  
//     //表示を切り替える
//     function toggleMenu(){
//       var $self = $(this); //thisにはクリックした時の要素が入る
//       //要素が.is-activeを持っていない場合
//       if(!$self.hasClass('is-active')){
//         fadeOutMenu();
//       }
//       //クリックした要素を表示させる
//       $self.toggleClass('is-active')
//         .next('.dropdown_btn-menu')
//         .stop().slideToggle(DURATION);
//     }
  
//     $dropdown.on('click', toggleMenu);
   
//   //別の場所をクリックすると閉じる処理
//     $(document).on('click touchend', function(event) {
//     if (!$(event.target).closest('body').length) {
//       // ここに処理;
//       fadeOutMenu();//関数呼びだし
//     }
//   });
//     });


// window.addEventListener('load', function() {
 
//     // 実行したい処理を書く
// const titel_list = document.getElementsByClassName('titel');
// for (const titel of titel_list) {
//     const str = titel.textContent;
//     const len = 50;

//     if(str.length > len){
//         titel.textContent = str.substring(0, len)+'...';
//     }else{
//         titel.innerHTML += "&emsp;".repeat(len - str.length);
//     }
//   }
// })


window.addEventListener('load', function() { 
    document.getElementById("dropdown_btn").onclick = (event)=>{
        document.getElementById("dropdown_list").style.display = "";
        event.stopPropagation();
    }
    for(const em of document.querySelectorAll(":not(#dropdown_btn)")){
        em.addEventListener('click', function() { document.getElementById("dropdown_list").style.display = "none";})

    }
})