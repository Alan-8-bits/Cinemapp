import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams , AlertController } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';

/**
 * Generated class for the AddPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-add',
  templateUrl: 'add.html',
})
export class AddPage {
  id=0;

  titulo = "";
  director = "";
  anio = "2020";
  fecha = "2020-01-01";
  image = "";

  constructor(public navCtrl: NavController, public navParams: NavParams,public http:HttpClient,public alert:AlertController) {
    this.id = navParams.get('id');
    console.log(this.id);
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad AddPage');
  }

  addMovie() {
    const params = {
      "titulo": this.titulo,
      "imagen": this.image,
      "fecha_visto": this.fecha,
      "director": this.director,
      "anio": this.anio,
      "usuario": this.id
    };
    console.log(JSON.stringify(params));
    this.http.post("/cinemapp/api/v1/pelicula", params)
    .subscribe(
      res => {
        let msg = "";

        if (res['code'] == "ok") {
          const alert = this.alert.create(
            {
              title: "Aviso",
              message: "Se agregó la película",
              buttons: ["ok"]
            }
          );
          alert.present(); 
          this.navCtrl.pop();
        } else if (res['code'] == "error") {
          msg = "Ocurrió un error"
          const alert = this.alert.create(
            {
              title: "Aviso",
              message: msg,
              buttons: ["ok"]
            }
          );
          alert.present();
        }        
      },
      error => {
        console.log(JSON.stringify(error))
      }
    )
  }

}
