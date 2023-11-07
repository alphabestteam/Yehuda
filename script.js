const quotes = [
  "I'm ready, I'm ready, I'm ready! - SpongeBob SquarePants",
  "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! - SpongeBob SquarePants",
  "I'm not just ready, I'm ready Freddy! - SpongeBob SquarePants",
  "Remember, licking doorknobs is illegal on other planets. - SpongeBob SquarePants",
  "The inner machinations of my mind are an enigma. - Patrick Star",
  "I can't hear you, it's too dark in here! - Patrick Star",
  "I'm ugly and I'm proud! - SpongeBob SquarePants",
  "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. - Squidward Tentacles",
  "Once there was an ugly barnacle. He was so ugly that everyone died. The end. - Patrick Star",
  "Is mayonnaise an instrument? - Patrick Star",
  "Can you give SpongeBob his brain back? - Patrick Star",
  "I guess hibernation is the opposite of beauty sleep. - Squidward Tentacles",
  "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! - SpongeBob SquarePants",
  "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! - SpongeBob SquarePants",
  "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. - Bubble Bass",
  "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
  "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
  "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. - Squidward: What's that? - SpongeBob: Outdoors.",
  "SpongeBob: Can I be excused for the rest of my life?",
  "SpongeBob: I'm not just ready, I'm ready Freddy!",
  "SpongeBob: You don't need a license to drive a sandwich.",
  "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
  "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
  "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
  "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end.",
];

input = document.getElementById("input");

function getRandomQuote() {
  return quotes[Math.floor(Math.random() * quotes.length)];
}

const element = document.getElementById("timer");

let time = 0;
let interval;
let randomQuote;

word = document.createElement("p");
sec = document.createElement("p");
speed = document.createElement("p");
accuracy = document.createElement("p");

function startGame() {
  word.innerHTML = "";
  sec.innerHTML = "";
  speed.innerHTML = "";
  accuracy.innerHTML = "";

  randomQuote = getRandomQuote();
  time = 0;
  clearInterval(interval);
  interval = setInterval(function () {
    element.innerHTML = "Time: " + time + " s";
    time++;
  }, 1000);
  // clearInterval(t);
  console.log();
  document.getElementById("quote").innerHTML = "";

  const arrRandomQuote = randomQuote.split("");
  arrRandomQuote.forEach((letter) => {
    const span = document.createElement("span");
    const style = "background-color: ";
    span.setAttribute("style", style);
    span.textContent = letter;
    span.className = "typing";
    document.getElementById("quote").appendChild(span);
  });

  input.addEventListener("input", () => {
    checkInput();
  });
}

function checkInput() {
  const typing = document.getElementsByClassName("typing");
  arrInput = input.value.split("");

  if (typing.length >= arrInput.length) {
    for (let i = 0; i < typing.length; i++) {
      typing[i].classList.remove("correct");
      typing[i].classList.remove("incorrect");
    }
    for (let i = 0; i < arrInput.length; i++) {
    //   console.log(typing[i].textContent);
      if (typing[i].textContent == arrInput[i]) {
        typing[i].classList.add("correct");
      } else {
        typing[i].classList.add("incorrect");
      }
    }
    if (typing.length == arrInput.length) {
      endGame();
    }
  } else {
    endGame();
  }
}

function countMatchingChars(strA, strB) {
  let count = 0;
  for (let i = 0; i < strA.length; i++) {
    if (strA[i] == strB[i]) {
      count++;
    }
  }
  return count;
}

function endGame() {
  clearInterval(interval);
  correctWords = countMatchingChars(randomQuote.split(""), arrInput);

  word.innerHTML = "you typed " + randomQuote.split(" ").length + " words ";
  sec.innerHTML = "in " + (time - 1) + " seconds";
  speed.innerHTML =
    "Your speed  is" +
    Math.floor((randomQuote.split(" ").length / 5 / time) * 100) +
    " Wpm";
  accuracy.innerHTML =
    "with" +
    Math.floor((correctWords / randomQuote.split("").length) * 100) +
    "% accuracy";

  document.getElementById("result").append(word);
  document.getElementById("result").append(sec);
  document.getElementById("result").append(speed);
  document.getElementById("result").append(accuracy);
}
