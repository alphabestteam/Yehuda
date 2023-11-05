
const person1 = {name:"yoda geller",
age:22,
grade:[89,99,98,95],
average:function (){
        sum =this.name.match(/[aeiou]/gi).length;
        this.grade.forEach((num) => { sum += num })
        return sum/this.grade.length
    }
 };
 
 const person2 = {name:"dni orlik",
 age:23,
 grade:[79,89,88,85],
 average:function (){
     sum =this.name.match(/[aeiou]/gi).length;
     this.grade.forEach((num) => { sum += num })
     return sum/this.grade.length
    }
};

const person3 = {name:"ari wizner",
 age:15,
 grade:[70,80,80,85],
 average:function (){
     sum =this.name.match(/[aeiou]/gi).length;
     this.grade.forEach((num) => { sum += num })
     return sum/this.grade.length
    }
};
const student = [person1,person2,person3]

console.table(student)
console.log(JSON.stringify(student, null, 4));

adults = student.filter((student)=>student.age>18)
console.log(adults);

const MyCar = {
    manufacturers :'china',
    model :'mazda',
    productionYear :new Date("06/24/2008"),
    carAge: function carAge(){
        return Date().now() - this.productionYear
    }
}
console.log(JSON.stringify(MyCar));
 
