var count = 0;

function myFunction(x){
    var element = document.getElementById('showCount');
    if (x == 'b1'){
        window.count ++ ;
    } if (x == 'b2'){
        window.count = 0;
    }
    element.textContent = count;
}