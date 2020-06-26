import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';
import { AddPage } from '../add/add';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  id=0;
  peliculas = [];

  constructor(public navCtrl: NavController,public navParams: NavParams,public http:HttpClient) {
    console.log(JSON.stringify(navParams));
    this.id=navParams.get("id");
    this.get_peliculas(this.id);
  }

  ionViewWillEnter() {
    this.get_peliculas(this.id);
  }

  get_peliculas(id) {
    this.http.get<any[]>("/cinemapp/api/v1/usuario/" + id + "/pelicula")
    .subscribe(
      res => {
        console.log(JSON.stringify(res));
        this.peliculas = res;
      },
      error => {
        console.log(JSON.stringify(error))
      }
    );
  }

  clickAdd() {
    this.navCtrl.push(AddPage, {id: this.id});
  }

}