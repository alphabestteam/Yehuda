import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  Password = "tuna"
  clicked = false
  count:number  =1
  arr:number[]=[];

  isclick(){ 
    
    this.clicked=!this.clicked
    if (this.clicked){
      this.count++
      this.arr.push(this.count)
    } 
    
  }
}
