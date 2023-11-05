const main = document.querySelector('main');

// const naiveHead1 = createHeading('red', 'naive 1');
// const naiveHead2 = createHeading('blue', 'naive 2');

//this is to be changed to append a header we create by using the higher order function headingFactory(color).
// main.appendChild(naiveHead1);
// main.appendChild(naiveHead2);

// function createHeading(color, text){
//     const heading = document.createElement('h1');
//     heading.setAttribute('style', 'color: ' + color);
//     heading.textContent = text;
//     return heading;
// }

// let count = 1
function headingFactory(color){
    const heading = document.createElement('h1');
    heading.setAttribute('style', 'color: ' + color);
    function createHeading(text){
    heading.textContent = text;
    main.appendChild(heading)
    }
    return createHeading
}
const createHeaderRed = headingFactory("red")
const createHeaderBlue = headingFactory("blue")

createHeaderRed("using factory 1")
createHeaderBlue("using factory 2")


//implement the closure here and use it. 
//keep in mind you return a function. think about how one should use what this function will return.