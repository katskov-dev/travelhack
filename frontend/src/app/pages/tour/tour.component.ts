import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpService } from './http.service';

@Component({
  selector: 'app-tour',
  templateUrl: './tour.component.html',
  styleUrls: ['./tour.component.css'],
  providers: [HttpService]
})
export class TourComponent implements OnInit {

  constructor(private httpService: HttpService, private params: ActivatedRoute) { }
  ngOnInit() { 
    this.sendDataTour(this.params.snapshot.queryParams['id'])
  }
  receivedData
  list_tours = []
  min_sum_tour;
  sendDataTour(id){
    console.log(id)
    let promise = new Promise((resolve, reject) => {
      this.httpService.getData(id).toPromise()
      .then(
          (data) => {
            this.receivedData=data, 
            // console.log('tours: ', this.receivedData),
            this.list_tours = this.receivedData,
            console.log('tours: ', this.list_tours)
            // if (this.list_tours.length > 0) this.min_sum_tour = this.list_tours[0].sum;
            // for(let i = 1; i < this.list_tours.length - 2; i ++ ){
            //   if(this.list_tours[i].sum < this.min_sum_tour){
            //     this.min_sum_tour = this.list_tours[i].sum
            //   }
            // }
          },
          error => { if(error.status == 500){ alert('сервер лег!');  } else {alert('интернет лег!') }}
          )
    })
    return promise
  }

}
