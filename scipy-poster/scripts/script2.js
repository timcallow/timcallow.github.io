var slider = document.getElementById("Range2");
var output = document.getElementById("value");

output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;

  var img = document.getElementById("img_adam");
  img.setAttribute("src", "figures/He_dos_" + this.value + ".svg");
}
