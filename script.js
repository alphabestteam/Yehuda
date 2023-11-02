// with at() you can use an negative numbers like -1 and is more shorter then arr[index]

function arrLetter(number,letter){
    arr =Array(number)
    return arr.fill(letter)
}
//alert(arrLetter(8,"a"))

arr =[1,2,3,4,5,6,7,8]
function removeN(arr,num){
     arr.splice(-num)
     return arr
}
//alert(removeN(arr,3))

function arrPush(number,arr){
    arr.unshift(number)
    return arr
}
//alert(arrPush(100,arr))

function addArrs(arrA,arrB){  
    return arrA.concat(arrB)
}
//alert(addArrs([1,2],[3,4]))


function arrToUppercase(arr){
   return arr.map((x) => x.toUpperCase());
}
//alert(arrToUppercase(["a","ufs"]))

function doubleDigitNumbers(arr){
    return arr.filter((num) => num.toString().length == 2);
 }
 //alert(doubleDigitNumbers([11,22,3,44,55,6]))

function isInArr(value,arr){
    return arr.includes(value)
}
//alert(isInArr(11,[11,22,3,44,55,6]))

function firstIndextUpto10(arr){
    return arr.find((num) => num > 10);
}
//alert(firstIndextUpto10([11,22,3,44,55,6]))

function isFirstIndextUpto10(arr){
    return firstIndextUpto10(arr) != null;
}
//alert(isFirstIndextUpto10([1,2,3,4,5]))

const arr1 =[1,30,4,21,100000]
alert(arr1.sort())

// because is look on the first digit and sort according to that 
// we add function(a,b)
arr1.sort(function(a, b){return a - b});

function arrSort(arr){
    return arr.sort(function(a, b){return a - b}).join("**")
}
alert(arrSort(arr1))

function ABCsort(arr){
    return arr.sort()
}
alert(ABCsort(['a','v','b','d','a']))

function isSmall(num,arr){
    return arr.every((number) => number < num+1)
}
alert(isSmall(9,[1,2,3,4,5,6]))

function isBigerNumber(num,arr){
    return (isSmall(num,arr) == false)
}
alert(isBigerNumber(5,[1,2,3,4,5,6]))

