import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Offer } from './offer'


@Component({
  selector: 'app-offers',
  templateUrl: './offers.component.html',
  styleUrls: ['./offers.component.css']
})
export class OffersComponent implements OnInit {

  offers: Offer[] = [];
  constructor(
    private httpClient: HttpClient
  ) { }

  ngOnInit(): void {
    this.getFriends();
  }
  
  getFriends(){
    this.httpClient.get<any>('http://127.0.0.1:8000/offers').subscribe(
      response => {
        this.offers = response;
      }
    );
  }

}
