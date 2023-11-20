import {Component, Input} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  clicked = true
  warningOrSuccess = " warning alert "

  warningSuccess(){
    this.clicked = !this.clicked
    if(this.clicked){
      this.warningOrSuccess = " warning alert "
    }
    else{
      this.warningOrSuccess = " success alert "
    }
  }

  arr:number[]=[0];
  changArr(newItem:string) {
    console.log(typeof(newItem));
    
    this.arr = Array(parseInt(newItem)).fill(0);
    console.log(this.arr);
    
  }
  
  
  


}