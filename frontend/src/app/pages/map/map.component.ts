import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import * as L from "leaflet";
<<<<<<< HEAD
=======
// let countriesGeoJson = require('./countries.geojson');
// countriesGeoJson = JSON.parse(countriesGeoJson);
>>>>>>> 821c43e174bc47fd894e88421e3a5d39fbffe380
@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
// import countries_jeoJson
export class MapComponent implements OnInit {
  map: L.Map;
  json;
  options = {
    layers: [
<<<<<<< HEAD
      L.tileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 5,
        attribution: ""
      })
=======
      L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 18, attribution: '...' }),
      // L.geoJson(countriesGeoJson)
>>>>>>> 821c43e174bc47fd894e88421e3a5d39fbffe380
    ],
    zoom: 2,
    center: L.latLng(47.482019, -1)
  };
  constructor(private http: HttpClient) { }

  ngOnInit() {
  }

  onMapReady(map: L.Map) {
    this.http.get("http://cdn.katskov.ru/countries.geojson").subscribe((json: any) => {
      console.log(json);
      this.json = json;
      function getColor(properties) {
        if ("filters" in properties){
          console.log(properties.filters[0])
          if (properties.filters[0] == "1"){
            return "#944";
          }
          if (properties.filters[0] == "2"){
            return "#494";
          }
          if (properties.filters[0] == "3"){
            return "#449";
          }
          
        }
        return "#999";
      }
      function style(feature) {
        return {
            fillColor: getColor(feature.properties),
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.7
        };
    };
      L.geoJSON(this.json, {style: style}).addTo(map);
    });
  }

  

}
