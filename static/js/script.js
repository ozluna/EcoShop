$(window).on('load',delayShow);

function delayShow(){ setTimeout(() => {
    $('#newsLetter').modal('show');
    console.log("modal function works");
}, 3000);}
/// clear out the delayshow if it is called once(after it called once)
document.addEventListener("DOMContentLoaded", function(event) {
    console.log("Hello! I am loaded");
    });
/// cartand product details quantity control

