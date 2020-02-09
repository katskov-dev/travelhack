import { Component, OnInit } from '@angular/core';
import * as L from "leaflet";
let countriesGeoJson = require('./countries.geojson');
countriesGeoJson = JSON.parse(countriesGeoJson);
@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
// import countries_jeoJson
export class MapComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  options = {
    layers: [
      L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 18, attribution: '...' }),
      L.geoJson(countriesGeoJson)
    ],
    zoom: 5,
    center: L.latLng(46.879966, -121.726909)
  };

}
