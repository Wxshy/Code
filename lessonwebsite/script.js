function retrieveData(){
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;
    console.log(name, email, message);

};





var i = 0;
function gallery(){
    var images = ["IMG_5434.JPG",'hockey.JPG', '20190901_142110.jpg'];
    i ++;
    if (i >= images.length){
        i = 0;
    };
    document.body.style.backgroundImage= "url("+images[i]+")";
};