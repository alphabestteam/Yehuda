function helloworld(){
    return"hello world"
}
console.log(helloworld());

function helloName(name){
    return 'hello ' + name
}
console.log(helloName("yoda"));

function square(num){
    return num*num
}
console.log(square(3))

function rectangleArea(x,y){
    return x*y
}
console.log(rectangleArea(3,5));

function circleValues(radius){
    return[radius*2*Math.PI,radius*radius*Math.PI]
}
console.log(circleValues(4));

function countVowels(str){
    return str.match(/[aeiou]/gi).length;
}
console.log(countVowels("haii who are you"));

function isSameLength(arr1 ,arr2){
    return arr1.length == arr2.length
}
console.log(isSameLength([34],['89']));

function numberToArray(num){
    // num.toString().split("")
    return Array.from(String(num),(num)=>Number(num))
}
console.log(numberToArray(1234));

function getTruthyFalsyArr(arr){
    return Array.from(arr ,(arr)=> Boolean(arr))
}
console.log(getTruthyFalsyArr(["" , 0 , 1, 3, 4,null]));