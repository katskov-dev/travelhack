import { Component, OnInit } from '@angular/core';
import { User } from './interface';
import { HttpService } from './http.service';
import { Router } from '@angular/router';
// import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css'],
  providers: [HttpService],
})
export class AuthComponent{

  passwordVisible = false;
  password: string;
  stem = "none";

  user: User = new User(); // данные от пользователя
      
  constructor(private httpService: HttpService, public router: Router){}

  receivedData: User; // полученные данные
  sendDataUser(user: User){
    if(user.Login == undefined && user.Password == undefined ){alert('inputs values is empty!')}
    else if(user.Login == undefined){alert('username input value is empty!')}
    else if(user.Password == undefined){alert('password input value is empty!')}
    else{
    this.httpService.postData(user)
      .subscribe(
        (data: User) => {this.receivedData=data,console.log('_ak_', this.receivedData.access_token),alert('authorization is done!'); let username = this.user.Login; this.router.navigate(['/'], { queryParams: { username } })},
        error => { if(error.status == 500){ alert('invalid login'); this.stem = "block"; } else {alert('invalid password'); this.stem = "block"; }}
      );
    }
  };  
}
