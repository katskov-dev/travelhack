import { Component, OnInit } from '@angular/core';
import { User } from './interface';
import { HttpService } from './http.service';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

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
      
  constructor(private httpService: HttpService, public router: Router, private cookieService: CookieService){}

  receivedData: User; // полученные данные
  sendDataUser(user: User){
    if(user.Phone == undefined && user.Password == undefined ){alert('поля пустые, заполните пожалуйста!')}
    else if(user.Phone == undefined){alert('поле для номера телефона пустое!')}
    else if(user.Password == undefined){alert('поле для пароля пустое!')}
    else if(user.Password != 'admin'){alert('неверный пароль!')}
    else{
    this.httpService.postData(user)
      .subscribe(
        (data: User) => {this.receivedData=data,console.log('_ak_', this.receivedData), this.cookieService.set( 'phone', this.receivedData.Phone), this.router.navigate(['/'])},
        error => { if(error.status == 500){ alert('сервер лег'); this.stem = "block"; } else {alert('сервер лег'); this.stem = "block"; }}
      );
    }
  };  
}
