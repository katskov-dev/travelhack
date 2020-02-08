import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {User} from './interface';
  
@Injectable()
export class HttpService{
  
    constructor(private http: HttpClient){ }
     
    postData(user: User){
        const body = {login: user.Login, password: user.Password};
        return this.http.post('/api/test', body); 
    }
}