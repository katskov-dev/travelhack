import { Component, OnInit } from '@angular/core';
import { trigger, style, animate, transition } from '@angular/animations';
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
})
export class MainComponent implements OnInit {

  selectedCity = null;
  selectedCountry = null;

  ValueHuman = 2;
  ValueDays = 5;

  openModal: boolean=false;

  isCollapsed = false;
  
  isLoadingOne = false;

  constructor() { }

  ModalEvent(type){
    this.isLoadingOne = true;
    if(type == 1){
      setTimeout(() => {
        this.isLoadingOne = false;
        this.openModal = true
      }, 500);
    }else{
      this.openModal = false
      this.isLoadingOne = false;
    }

  }
  CountHuman = (value: number) => `${value} человека`;
  CountDays = (value: number) => `${value} ночей`;
  // kek(ValueHuman){
  //   console.log(ValueHuman)
  //   if(ValueHuman >= 5){
  //     this.ValueHuman = `${ValueHuman} человек`
  //     // this.ValueHuman = Number
  //     console.log(this.formatterPercent)
  //   }else{
  //     this.ValueHuman = `${ValueHuman} человека`
  //     console.log(typeof(this.ValueHuman))
  //     // this.ValueHuman = Number
  //   }
  // }
  
  
  ngOnInit() {
    
  }


}
