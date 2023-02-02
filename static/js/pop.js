window.addEventListener('load', function() {
var del = document.getElementById('del');
 
del.addEventListener('click', function() {
    var result = window.confirm('削除しますか？');
    
    if( result ) {
        console.log('削除されました');
    }
    else {
        console.log('');
    }
})
})