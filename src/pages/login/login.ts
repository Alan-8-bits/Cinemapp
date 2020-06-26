import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { AlertController } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';
import { HomePage } from '../home/home';

/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',
})
export class LoginPage {

  correo ="";
  contra ="";

  constructor(public navCtrl: NavController, public navParams: NavParams, public http:HttpClient,public alert:AlertController) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad LoginPage');
  }

  registrarse(){
    const params = {
      correo: this.correo,
      contrasenia: this.contra
    };

    this.http.post("/cinemapp/api/v1/usuario", params)
    .subscribe(
      res => {
        let msg = "";

        if (res['code'] == "ok") {
          msg = "Usuario Registrado con Éxito"  
        } else if (res['code'] == "existe") {
          msg = "El correo ya está en uso"
        } else if (res['code'] == "error") {
          msg = "Ocurrió un error"
        }
        const alert = this.alert.create(
          {
            title: "Aviso",
            message: msg,
            buttons: ["ok"]
          }
        );
        alert.present();
      },
      error => {
        console.log(JSON.stringify(error))
      }
    );
  }

  iniciar_sesion() {
    const params = {
      correo: this.correo,
      contrasenia: this.contra
    };
    this.http.post("/cinemapp/api/v1/sesion", params)
    .subscribe(
      res => {
        let msg = "";

        if (res['code'] == "ok") {
          msg = "Iniciaste sesión" 
          this.navCtrl.setRoot(HomePage, {id: res['id']}); 
        } else if (res['code'] == "no") {
          msg = "El correo o la contraseña no son válidos"
        } else if (res['code'] == "error") {
          msg = "Ocurrió un error"
        }
        const alert = this.alert.create(
          {
            title: "Aviso",
            message: msg,
            buttons: ["ok"]
          }
        );
        alert.present();
      },
      error => {
        console.log(JSON.stringify(error))
      }
    );
  }

}
