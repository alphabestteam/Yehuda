function sequenceA() {
    setTimeout(_ => console.log('Sponge'), 0);
    console.log("Bob");
}

function sequenceB(){
    setTimeout(_ => console.log(`🍅 Timeout at B`), 0);
    Promise.resolve().then(_ => console.log('🍍 Promise at B'));
}

function sequenceC(){
    setTimeout(_ => console.log(`🍅 Timeout at C`), 0);
    Promise.resolve().then(_ => setTimeout(console.log('🍍 Promise at C'), 1000));
}

function sequenceD(){
    console.log('Sponge');
    setTimeout(_ => console.log('Square'), 0);
    Promise.resolve().then(_ => console.log('Pants'));
    console.log('Bob');
}

function questionA(){
    sequenceA();
}

function questionB(){
    sequenceB();
}

function questionC(){
    sequenceC();
}

function questionD(){
    sequenceD();
}

function questionE(){
    sequenceB();
    sequenceC();
}

//questionA(); // because there is a time out even he set to 0 he go after because the computer see that as Synchronous a  move all the time out the anther place a tor
//questionB(); // for promis has anther thread so he do that first  
//questionC(); // because the time out is synchronous he wait after the promise end 
//questionD(); // the console.log is be the first then promise and the end setTimeout so is print sponge bob pants square
//questionE(); // promise is go first and then the timeout 