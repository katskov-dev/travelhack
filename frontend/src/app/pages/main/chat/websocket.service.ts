import { Observable, Subject } from 'rxjs';
import * as io from 'socket.io-client';
// let url = 'http://127.0.0.1:8000';
let url = 'http://192.168.43.67:8000'
const socketio = io(url)

export class WebsocketService {

  
  sendMessage(message, uuid){
    socketio.emit('sendMes', {message, uuid});    
  }
  
  sendUiid(message){
    // this.socket = io(this.url)
    socketio.emit('sendUiid', message);    
  }

  getMessages() {
    // this.socket = io(this.url)
    // this.socket.emit('getMes', 'говно');
    
    
    let observable = new Observable(observer => {
     socketio.on('getMes', (data) => {
        observer.next(data);   

      }); 
      // return () => {
      //   this.socket.disconnect();
      // };  
    })   
    console.log('lol->', observable)  
    return observable;


  //   return Observable.create((observer) => {
  //     socketio.on('getMes', (data) => {
  //         observer.next(data );
  //     });
  // });
  }  
}