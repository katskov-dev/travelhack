import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {User} from './interface';
  
@Injectable()
export class HttpService{
  
    constructor(private http: HttpClient){ }
     
    postData(user: User){
        const body = {
            date_start: user.date_start,
            city_from: user.city_from,
            city_in: user.city_in,
            count_days: user.count_days,
            count_peoples: user.count_peoples
        };
        return this.http.post('/api/get_tours?hu=true&tu=true', body); 
    }
}