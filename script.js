
function isGoodGrade(){
    console.log("0"); 
    const p1 = document.createElement("p");
    const p2 = document.createElement("p");
    let grade = document.getElementById("frm1");
    grade = grade.grade.value

    let char=" "
    if(grade >100 || grade<0){
        window.location.reload();
        alert("enter number 0 -100")
    }

 
    else if (grade == 100) {
        char ="A+" 
    }
    else if (grade <100 && grade>=90) {
        char ="A" 
    }
    else if (grade <90 && grade>=80) {
        char ="B" 
    }
    else if (grade <80 && grade>=70) {
        char ="C" 
    }
    else if (grade <70 && grade>=60) {
        char ="D" 
    }
    else if (grade <60 && grade>=50) {
        char ="E" 
    }
    else if ( grade<50) {
        char ="F" 
    }
    console.log(char);
    let letterGrade=document.createTextNode(char);
    
    let sentence
        switch (char) {
            case "A+":
                console.log("2");
                sentence =  "Perfect!"
                break;
            case "A":
                console.log("3");
                sentence = "Amazing!"
                break;
            case "B":
                sentence = "Nicely done!"
                break;
            case "C":
                sentence = "This is fine!"
                break;
            case "D":
                sentence = "You can do better!"
                break;
            case "E":
                sentence = "Moed B is an option!"
                break;
            case "F":
                sentence = "Moed B is a must!"
                break;
            default:
                sentence = ""
                break;
            }   
            let theSentence =document.createTextNode(sentence);
            
            p1.appendChild(letterGrade);
            p2.appendChild(theSentence);
            const element = document.getElementById("frm1");
            element.appendChild(p1);
            element.appendChild(p2);
}