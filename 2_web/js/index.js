const canvas_image = document.getElementById ("image");
const ctx_image = canvas_image.getContext("2d");

const img_tiger = new Image();


 //img_tiger.onload = function() {
  //   ctx_image.drawImage(img_tiger, 0, 0, 50, 50);
// }
 //img_tiger.src ="/2_web/image/tiger.PNG";


const canavasSizeX = 500;
const canavasSizeY = 500;
const dx = 1;
const dy = 1;
var x = 1;
var y = 1;



function init() {
    img_tiger.src ="/2_web/image/tiger.PNG"
    window.requestAnimationFrame(draw);
}


function draw() {
    ctx_image.clearRect(0,0,500,500);

    if (x > canavasSizeX) {
      ctx_image.translate(-canavasSizeX, -canavasSizeY);
        x = 1;
        y = 1;
    } else {
        ctx_image.translate(-canavasSizeX, -canavasSizeY);
        ctx_image.translate(dx,dy);
        x = x + dx;
        y = y + dy;
    }
    window.requestAnimationFrame(draw);
}

init ()