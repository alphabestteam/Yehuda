const map =new Map()

map.set('Main character','spongebob')
map.set('Best friend','patrick')
map.set('pet','gary')
map.set('word buddy','squidward')
map.set('manager','Mr. Krabs')
map.set('teacher','Mrs. Puff')
map.set('location','bikini bottom')

let list = "";
for (const x of map.entries()) {
  list += x;
}
console.log(list)

list = "";
for (const x of map.keys()) {
  list += x;
}
console.log(list)

console.log(map.get('location'))
console.log(map.size)
console.log(map.delete('location'))
console.log(map.size)

list = "";
for (const x of map.entries()) {
  list += x;
}
console.log(list);

console.log(map.has('location'));