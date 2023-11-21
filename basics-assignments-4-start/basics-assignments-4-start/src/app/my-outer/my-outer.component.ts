import { Component } from '@angular/core';

@Component({
  selector: 'app-my-outer',
  templateUrl:'./my-outer.component.html',
  styleUrls: ['./my-outer.component.css']
})
export class MyOuterComponent {
  countOuter =0

  changeCountOuter(num:number){
    this.countOuter+=num
  }
}
