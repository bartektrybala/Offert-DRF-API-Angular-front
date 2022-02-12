import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class GetApiService {

  constructor(
    private http: HttpClient
  ) { }
  apiCall()
  {
    let headers = new HttpHeaders();
    return this.http.get('http://127.0.0.1:8000/offers');
  }
}
