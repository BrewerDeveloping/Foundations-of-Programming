document.querySelector("#turnRed").addEventListener("click", turnRedFunction);
document.querySelector("#turnBlue").addEventListener("click", turnBlueFunction);
document.querySelector("#turnPurple").addEventListener("click", turnPurpleFunction);
document.querySelector("#turnRandom").addEventListener("click", turnRandomFunction);

function turnRedFunction() {
  document.querySelector("body").style.backgroundColor = "red";
}

function turnBlueFunction() {
  document.querySelector("body").style.backgroundColor = "blue";
}

function turnPurpleFunction() {
  document.querySelector("body").style.backgroundColor = "purple";
}

function turnRandomFunction() {
  var x = Math.floor(Math.random() * 256);
  var y = Math.floor(Math.random() * 256);
  var z = Math.floor(Math.random() * 256);
  var random = "rgb(" + x + "," + y + "," + z + ")";  
  document.querySelector("body").style.backgroundColor = random;
}