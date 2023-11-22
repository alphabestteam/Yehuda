import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators  } from '@angular/forms';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'angular-ex-6';
  profileForm = new FormGroup({
    name : new FormControl('', Validators.required ),
    email : new FormControl('', [Validators.required,Validators.email]),
    password : new FormControl('', Validators.required )
  })
  submit = false
  onsubmit(){
    this.submit= true
  } 
}
