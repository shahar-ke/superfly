function ageIncrease() {
  davidAge = parseInt(document.getElementById("DavidAge").innerHTML);
  emmaAge = parseInt(document.getElementById("EmmaAge").innerHTML);
  davidAge += 5;
  emmaAge += 5;
  document.getElementById("DavidAge").innerHTML = davidAge;
  document.getElementById("EmmaAge").innerHTML = emmaAge;
}