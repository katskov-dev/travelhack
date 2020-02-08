import { Component, OnInit } from '@angular/core';
// import { User } from './interface';
// import { HttpService } from './http.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-recover',
  templateUrl: './recover.component.html',
  styleUrls: ['./recover.component.css'],
  // providers: [HttpService],  
})
export class RecoverComponent {

  stem="none"
  // user: User = new User(); // данные от пользователя
      
  // constructor(private httpService: HttpService, public router: Router){}

  // receivedData: User; // полученные данные

  
  // sendDataUser(user: User){
  //   if(user.Email == undefined){alert('email input value is empty!')}
  //   else{
  //   this.httpService.postData(user)
  //     .subscribe(
  //       (data: User) => {this.receivedData=data, alert('we send new password in your mail adress!'); this.router.navigate(['/auth'])},
  //       error => { if(error.status == 500){ alert('invalid login')} else {alert('invalid password') }}
  //     );
  //   }
  // };

}
