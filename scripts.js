string =" Kung Fu Panda is a beloved animated movie about a clumsy, food-loving panda named Po who dreams of becoming a kung fu master.\nPo'sdream becomes a reality when he is unexpectedly chosen to become the Dragon Warrior and train with the Furious Five to protect the Valley of Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008, and grossed over $631 million worldwide, making it the highest-grossing non-sequel animated film at the time of its release.\nAlong the way, Po learns valuable lessons about inner strength, perseverance, and the importance of family and friendship.\nWith stunning animation, a heartwarming story, and a star-studded cast including Jack Black, Angelina Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for all ages. "

function stringToArr(string){
    const story = string.split(" ");
    return story
}
//alert(stringToArr(string))

function replaceOneWord(string,newWord){
    return string.replace('movie',newWord)
}
//alert(replaceOneWord(string ,"film"))

function replaceAllWord(string,newWord){
    return string.replaceAll('Panda',newWord)
}
//alert(replaceAllWord(string ,"Bear"))

//alert(string.toUpperCase())

//alert(string.toLowerCase())
indexPo = string.search("Po")
//alert(string.search("Po"))

//alert(string.slice(string.search("Po")))

//alert(string.replace(/\s/g, ''))

alert(string.slice(indexPo,string.indexOf(".",indexPo)))

alert(string.split(" "))

alert(string.lastIndexOf(".ages")!= -1)

alert(string.concat(" is one of my favorite movies!"))



