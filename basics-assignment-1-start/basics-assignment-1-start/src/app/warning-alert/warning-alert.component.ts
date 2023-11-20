import { Component } from '@angular/core';

@Component({
  selector: 'app-warning-alert',
  templateUrl:'./warning-alert.component.html',
  styleUrl: './warning-alert.component.css'
})
export class WarningAlertComponent {
  a = false
  b = !this.a
  click(){
    this.a = !this.a
    console.log("work");
    
  }

}
