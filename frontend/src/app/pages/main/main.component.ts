import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  CountHuman = (value: number) => `${value} человека`;
  CountDays = (value: number) => `${value} ночей`;
  
  selectedCity = null;
  selectedCountry = null;

  ValueHuman = 2;
  ValueDays = 5;

  openModal: boolean=false;

  isCollapsed = false;
  
  isLoadingOne = false;

  constructor() { }

  ngOnInit() {
  }

  ModalEvent(type){
    this.isLoadingOne = true;
    if(type == 1){
      setTimeout(() => {
        this.isLoadingOne = false;
        this.openModal = true
      }, 2000);
    }else{
      this.openModal = false
      this.isLoadingOne = false;
    }
  }
  

}
