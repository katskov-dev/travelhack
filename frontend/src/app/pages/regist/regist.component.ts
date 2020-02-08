import { Component, OnInit } from '@angular/core';
// import { User } from './interface';
// import { HttpService } from './http.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-regist',
  templateUrl: './regist.component.html',
  styleUrls: ['./regist.component.css']
  // providers: [HttpService],
})
export class RegistComponent  {

  passwordVisible = false;
  password: string;

  // user: User = new User(); // данные от пользователя
      
  // constructor(private httpService: HttpService, public router: Router){}

  // receivedData: User; // полученные данные
  // sendDataUser(user: User){
  //   if(user.Email == undefined && user.Login == undefined && user.Password == undefined ){alert('inputs values is empty!')}
  //   else if(user.Email == undefined){alert('email input value is empty!')}
  //   else if(user.Login == undefined){alert('username input value is empty!')}
  //   else if(user.Password == undefined){alert('password input value is empty!')}
  //   else{
  //   this.httpService.postData(user)
  //     .subscribe(
  //       (data: User) => {this.receivedData=data; this.router.navigate(['/auth'])},
  //       error => { if(error.status == 500){ alert('something wrong in server') } else {alert('a user with such email already exists!'); this.router.navigate(['/auth'])} }
  //     );
  //   }
  // };

}
