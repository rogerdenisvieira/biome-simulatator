// import Subject from './subject.js'


function setup() {
    var canvas = createCanvas(800, 800, WEBGL);
    canvas.parent('canvas-holder')
  }
  
function draw() {
    const fixAcc = 0.01
    var varAcc = document.getElementById('slider-acc').value 
    background(220)
    rotateX(frameCount * fixAcc * varAcc);
    rotateY(frameCount * fixAcc * varAcc);

    cylinder(20,50,10,10)
    // box(50)

  }