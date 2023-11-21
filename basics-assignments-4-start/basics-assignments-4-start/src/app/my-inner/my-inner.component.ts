import { Component } from '@angular/core';
import { Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})
export class MyInnerComponent {
 countInner =5
 
  @Output() newItemEvent = new EventEmitter<number>();

  addTen(value: number) {
    if(value == 10){
      this.newItemEvent.emit(10);
      this.countInner = 0
    }
    else{
      this.countInner++
    }
  }

  subTen(value: number) {
    if(value == -10){
      this.newItemEvent.emit(-10);
      this.countInner = 0
    }
    else{
      this.countInner--
    }
  }
}
