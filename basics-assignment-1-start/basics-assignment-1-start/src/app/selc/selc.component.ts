import {Component,Input} from '@angular/core';
import {MatSelectModule} from '@angular/material/select';
import {MatFormFieldModule} from '@angular/material/form-field';
import { Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-selc',
  templateUrl: './selc.component.html',
  styleUrl: './selc.component.css',
  standalone: true,
  imports: [MatFormFieldModule, MatSelectModule],
})
export class SelcComponent {
selected = 1;



  @Output() newItemEvent = new EventEmitter<number>();

  addNewItem(value: number) {   
    this.newItemEvent.emit(value);
  }
}
