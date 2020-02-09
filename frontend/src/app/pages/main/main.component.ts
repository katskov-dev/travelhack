import { Component, OnInit } from '@angular/core';
import { trigger, style, animate, transition } from '@angular/animations';
import {User} from './interface';
import { HttpService } from './http.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css'],
  animations: [
    trigger(
      'enterAnimation', [
        transition(':enter', [
          style({transform: 'translateY(100%)', opacity: 0}),
          animate('500ms', style({transform: 'translateY(0)', opacity: 1}))
        ]),
        transition(':leave', [
          style({transform: 'translateY(0)', opacity: 1}),
          animate('500ms', style({transform: 'translateY(100%)', opacity: 0}))
        ])
      ]
    )
  ],
  providers: [HttpService]
})
export class MainComponent implements OnInit {


  paramFrom;
  paramBefore;

  selectedCity = null;
  selectedCountry = null;

  ValueHuman = 2;
  ValueDays = 5;

  openModal: boolean=false;
  openSearch: boolean=true;

  isCollapsed = false;
  
  isLoadingOne = false;



  CountHuman = (value: number) => `${value} человека`;
  CountDays = (value: number) => `${value} ночей`;  
  
  ngOnInit() {

  }
  dateFormat = 'yyyy/MM/dd';

  ModalEvent(type, user: User){
    console.log('dasha->', this.user.date_start)
    this.isLoadingOne = true;
    if(type == 1){
      setTimeout(() => {
        this.sendDataUser(user)
      }, 0);
    }else{
      this.openModal = false
      this.openSearch = true
      this.isLoadingOne = false;
    }

  }

  
  constructor(private httpService: HttpService, public router: Router){}

  redirectTour(id){
    this.router.navigate(['/tour'], { queryParams: { id } })
  }
  
  user: User = new User(); // данные от пользователя
  
  receivedData: User; // полученные данные
  
  list_tours = []
  min_sum_tour;
  sendDataUser(user: User){
    let promise = new Promise((resolve, reject) => {
      this.httpService.postData(user).toPromise()
      .then(
          (data: User) => {
            this.receivedData=data, 
            // console.log('tours: ', this.receivedData),
            this.isLoadingOne = false,
            this.openModal = true,
            this.openSearch = false, 
            this.list_tours = this.receivedData.tours,
            console.log('tours: ', this.list_tours)
            if (this.list_tours.length > 0) this.min_sum_tour = this.list_tours[0].sum;
            for(let i = 1; i < this.list_tours.length - 2; i ++ ){
              if(this.list_tours[i].sum < this.min_sum_tour){
                this.min_sum_tour = this.list_tours[i].sum
              }
            }
          },
          error => { if(error.status == 500){ alert('сервер лег!');  } else {alert('интернет лег!') }}
          )
    })
    return promise
  }



}
