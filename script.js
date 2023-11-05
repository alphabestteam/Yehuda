const button = document.getElementById('the-button');
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");

button.innerHTML ="hide bob"
const toggleBob = function(){
    if (bobGif.classList.contains("hide")) {   
        bobGif.classList.remove("hide")
        button.innerHTML ="hide bob"
    }
    else{
        bobGif.classList.add("hide")
        button.innerHTML ="show me Bob"

    }
}; 
