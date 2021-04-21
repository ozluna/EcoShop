$(window).on('load',delayShow);

function delayShow(){ setTimeout(() => {
    $('#newsLetter').modal('show');
    console.log("modal function works");
}, 3000);}
document.addEventListener("DOMContentLoaded", function(event) {
    console.log("Hello! I am loaded");
    });


