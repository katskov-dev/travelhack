import { Component, OnInit, HostListener } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  hamburger: boolean= false;
  buttonsonheader: boolean = true;

  constructor() { }

  ngOnInit() {
    if(window.innerWidth <= 768){
      this.hamburger = true
      this.buttonsonheader = false
    }else{
      this.hamburger = false
      this.buttonsonheader = true
    }
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: any) {
      if(event.target.innerWidth <= 768){
        this.hamburger = true
        this.buttonsonheader = false
      }else{
        this.hamburger = false
        this.buttonsonheader = true
      }
  }

}
