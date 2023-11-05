const main  =document.getElementById("main-heading")
console.log(main.id);
console.log(main.className);
console.log(main.classList);
console.log(main.getAttribute("data-standard"));

console.log(main.textContent);
console.log(main.textContent.replaceAll(/\s/g,''));
main.innerHTML = 'Hello there pearl!'
var x = document.createElement("SPAN");  
var b= document.createElement("BR");
var t = document.createTextNode("its me SpongeBob!")
x.appendChild(b)
  x.appendChild(t);
  main.appendChild(x);

  console.log(main);

  let cloned =main.cloneNode(true);
  console.log(cloned);

  let subHeading = document.createElement("h2")
  let text = document.createTextNode("jellyfish hunting is the best");
  subHeading.appendChild(text)
  document.body.appendChild(subHeading)

  lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
  const loremArr = lorem.split(" ");
  const colors = ["red","orange","yellow","greenyellow","lightblue","mediumpurple"]  
  
  function reandomColor(){
    let x =Math.floor(Math.random() *colors.length);
    console.log(x);
    return colors[x]
  }
  
  randomWords = document.getElementById("random-words")
  
  loremArr.forEach(word => { 
    
      const span = document.createElement("span")
      const style = "background-color: " + reandomColor();
      span.setAttribute("style",style)
      span.textContent = word
      span.className = "random-word";
      randomWords.appendChild(span)
  });