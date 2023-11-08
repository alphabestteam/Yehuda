/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/

let objMenu;


const formatter = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

async function getText(file) {
  let x = await fetch(file);
  let y = await x.json();
  objMenu = y;

  const listMwnu = document.createElement("div");
  document.querySelector("div").innerHTML = "";

  Object.entries(objMenu.items).map((entry) => {
    let value = entry[1];
    const div = document.createElement("div");
    const hederPlusPrice = document.createElement("h3");
    const discription = document.createElement("p");
    const input = document.createElement("input");
    const text = document.createElement("p");

    discription.innerHTML = value.description;
    hederPlusPrice.innerHTML = value.name;
    hederPlusPrice.innerHTML += " (" + formatter.format(value.price) + ")";
    text.innerText = " quantity : ";
    input.type = "number";
    input.id = value.id;
    input.max = "5";
    input.min = "0";
    text.style = "display: flex;";

    div.style =
      "margin-bottom: 1rem;padding: 1rem;border: 1px solid #666666;background-color: #434242;border-radius: 5px;";

    div.appendChild(hederPlusPrice);
    div.appendChild(discription);
    div.appendChild(text);
    div.appendChild(input);
    listMwnu.appendChild(div);
    div.classList.add("order-summary");
    console.log(value.name);
  });
  document.querySelector("div").append(listMwnu);
  AllInput = document.querySelectorAll("input");
  console.log(AllInput);
  console.log(objMenu.items);

  let krabbyPattytotal = 0;
  let krustyKrabPizzatotal = 0;
  let ChumBurgertotal = 0;
  let KelpFriestotal = 0;

  AllInput.forEach(function (input) {
    input.addEventListener("click", function () {
      if (input.value > 1 || input.value < 6) {
        if (input.id == 1) {
          krabbyPattytotal = 3.88 * input.value;
          KrabbyPatty.innerHTML =
            "Krabby Patty (" +
            input.value +
            " x " +
            3.88 +
            " = " +
            3.88 * input.value +
            "$)";
        } else if (input.id == 2) {
          krustyKrabPizzatotal = 5.55 * input.value;
          KrustyKrabPizza.innerHTML =
            "Krusty Krab Pizza (" +
            input.value +
            " x " +
            5.55 +
            " = " +
            5.55 * input.value +
            "$)";
        } else if (input.id == 3) {
          ChumBurgertotal = 2.97 * input.value;
          ChumBurger.innerHTML =
            "Chum Burger (" +
            input.value +
            " x " +
            2.97 +
            " = " +
            2.97 * input.value +
            "$)";
        } else if (input.id == 4) {
          KelpFriestotal = 1.01 * input.value;
          KelpFries.innerHTML =
            "Kelp Fries (" +
            input.value +
            " x " +
            1.01 +
            " = " +
            1.01 * input.value +
            "$)";
        }
      }
      if (input.value == 0) {
        if (input.id == 1) {
          KrabbyPatty.innerHTML = "";
        } else if (input.id == 2) {
          KrustyKrabPizza.innerHTML = "";
        } else if (input.id == 3) {
          ChumBurger.innerHTML = "";
        } else if (input.id == 4) {
          KelpFries.innerHTML = "";
        }
      }
    });
  });
  submitOrder = document.getElementById("submit-button");
  submitOrder.addEventListener("click", function () {
    datajson = {
      "Chum Burger": ChumBurgertotal,
      "Kelp Fries": KelpFriestotal,
      "Krabby Patty": krabbyPattytotal,
      "Krusty Krab Pizza": krustyKrabPizzatotal,
    };

    fetch("http://localhost:8000/orders", {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      method: "POST",
      body: JSON.stringify(objMenu),
    })
      .then(function (res) {
        alert(res);
      })
      .catch(function (res) {
        alert(res);
      });
  });
}
getText("http://localhost:8000/menu").then(console.log("finsh"));

p = document.querySelector("p");

const KrabbyPatty = document.createElement("p");
const KrustyKrabPizza = document.createElement("p");
const ChumBurger = document.createElement("p");
const KelpFries = document.createElement("p");

p.appendChild(KrabbyPatty);
p.appendChild(KrustyKrabPizza);
p.appendChild(ChumBurger);
p.appendChild(KelpFries);

let AllInput;
console.log(AllInput);
