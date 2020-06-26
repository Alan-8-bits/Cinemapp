from flask import Flask, jsonify, request
import mysql.connector
from funciones import existe_usuario, crear_usuario, iniciar_sesion, insertar_pelicula, get_peliculas, get_pelicula,eliminar_pelicula,modificar_pelicula,login

app = Flask(__name__)
bd = mysql.connector.connect(user='alan', password='12345678', database='cinemapp')

@app.route("/api/v1/usuario", methods=["GET", "POST"])
@app.route("/api/v1/usuario/<int:id>/<path:sub>")
def usuario(id=None, sub=None):
    if request.method == "GET" and id is not None and sub == "pelicula":
        return jsonify(get_peliculas(bd, id))
    elif request.method == "GET":
        correo = request.args.get("correo")
        contra = request.args.get("contrasenia")
        if iniciar_sesion(bd, correo, contra):
            return jsonify({"code": "ok"})
        else:
            return jsonify({"code": "no"})
        return jsonify({"code": "error"})
    elif request.method == "POST" and request.is_json:
        data = request.get_json()
        correo = data["correo"]
        contra = data["contrasenia"]
        if existe_usuario(bd, correo):
           return jsonify({"code": "existe"})
        else:
            crear_usuario(bd, correo, contra)
            return jsonify({"code": "ok"})
        return jsonify({"code": "error"})
    return jsonify({"code": "error"})

@app.route("/api/v1/pelicula", methods=["GET", "POST"])
@app.route("/api/v1/pelicula/<id>", methods=["GET", "DELETE", "PUT"])
def pelicula(id=None):
    if request.method == "POST" and request.is_json:
        data = request.get_json()
        print(data)
        if insertar_pelicula(bd, data):
            return jsonify({"code": "ok"})
        else:
            return jsonify({"code": "error"})
    elif request.method == "GET" and id is None:
        return jsonify(get_peliculas(bd))
    elif request.method == "GET" and id is not None:
        return jsonify(get_pelicula(bd, id))
    elif request.method == "DELETE" and id is not None:
        if eliminar_pelicula(bd, id):
            return jsonify({"code": "ok"})
        else:
            return jsonify({"code": "no"})
    elif request.method == "PUT" and id is not None and request.is_json:
        data = request.get_json()
        columna = data['columna']
        valor = data['valor']
        if modificar_pelicula(bd, id, columna, valor):
            return jsonify({"code": "ok"})
        else:
            return jsonify({"code": "no"})
            
    return jsonify({"code": "error"})

@app.route("/api/v1/sesion", methods=["POST"])
def sesion():
    if request.method == "POST" and request.is_json:
        data = request.get_json()
        correo = data["correo"]
        contra = data["contrasenia"]
        id, ok = login(bd, correo, contra)
        if ok:
            return jsonify({"code": "ok", "id": id})
        else:
            return jsonify({"code": "no"})
        return jsonify({"code": "error"})

app.run(debug=True)