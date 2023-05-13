let header = document.querySelector("#header1");

let d1 = document.querySelector("#divh1");
let d2 = document.querySelector("#divh2");
let d3 = document.querySelector("#divh3");
let d4 = document.querySelector("#divh4");
let d5 = document.querySelector("#divh5");
let d6 = document.querySelector("#divh6");


header.addEventListener("mouseover", openheder)
header.addEventListener("mouseout", closeheder)

function openheder() {
    d1.innerHTML = "";
    d2.innerHTML = "";
    d3.innerHTML = "";
    d4.innerHTML = "";
    d5.innerHTML = "";
    d6.innerHTML = "";
}
function closeheder() {
    d1.innerHTML = "Philip";
    d2.innerHTML = "Mama";
    d3.innerHTML = "Anat";
    d4.innerHTML = "Gala";
    d5.innerHTML = "Marina";
    d6.innerHTML = "Masha";

}