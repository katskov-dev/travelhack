import { Component, OnInit, AfterViewChecked, ChangeDetectorRef, ElementRef, ViewChild, QueryList, ViewChildren, HostListener } from '@angular/core';
import { WebsocketService } from './websocket.service';
import { trigger, style, animate, transition } from '@angular/animations';
import { HttpService } from './http.service';
import { Tour } from './interface';
import * as uuid from 'uuid';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
  providers: [WebsocketService,HttpService],
  animations: [
    trigger(
      'enterAnimation', [
        transition(':enter', [
          style({transform: 'translateX(100%)', opacity: 0}),
          animate('500ms', style({transform: 'translateX(0)', opacity: 1}))
        ]),
        transition(':leave', [
          style({transform: 'translateX(0)', opacity: 1}),
          animate('500ms', style({transform: 'translateX(100%)', opacity: 0}))
        ])
      ]
    )
  ],
})
export class ChatComponent implements OnInit, AfterViewChecked {

  @ViewChild('scrollMe', {static: false}) private myScrollContainer: ElementRef;

  constructor(private websocketService: WebsocketService, private httpService: HttpService, private cookieService: CookieService, private cdr: ChangeDetectorRef) {
  } 
  
  tour: Tour = new Tour();
  messages = [];
  msg_user = [];
  msg_bot = [];

  ngOnInit() {
    const ui = uuid.v4();
    if(this.cookieService.get('Uuid') == '' || this.cookieService.get('Uuid') == null || this.cookieService.get('Uuid') == undefined){
      this.cookieService.set( 'Uuid', ui);
    }else{
      this.websocketService.sendUiid(this.cookieService.get('Uuid'));
      console.log(this.cookieService.get('Uuid'))
      
      this.websocketService.getMessages().subscribe((data: Tour) => {
        let arrayFromServer = new Array
        arrayFromServer.push(data.messages)
        console.log(arrayFromServer)
        for (let i = 0; i < arrayFromServer[0].length; i ++ ){
          console.log('kek1---> ', data.messages[i].type, data.messages[i].content)
          this.messages.push(data.messages[i]);

          
        }
        this.cdr.detectChanges();
        this.scrollToBottom();
      })
    }
    // this.httpService.getData()
    // .subscribe(
    //   (data: Tour) => {console.log(data.access_token)},
    //   error => { console.log(error)}
    // );
  }

  ngAfterViewChecked() {   
    this.cdr.detectChanges();   

    this.scrollToBottom();   
  } 

  scrollToBottom(): void {
    try {
        this.myScrollContainer.nativeElement.scrollTop = this.myScrollContainer.nativeElement.scrollHeight;
    } catch(err) { }                 
  }

  chatBlock: boolean= false;
  eventChatBlock:boolean = false;
  openChat(){
    if(this.eventChatBlock == false){
      this.chatBlock = true;
      this.eventChatBlock = true;
    }else{
      this.chatBlock = false;
      this.eventChatBlock = false;
    }
  }
  username: string;
  message: string;
  sendMes(){
    if(this.message == null || this.message ==  ''){
      alert('kek')
    }else{
      this.websocketService.sendMessage(this.message, this.cookieService.get('Uuid'));
      this.message = "";
    }

  } 
}
