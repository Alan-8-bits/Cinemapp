def existe_usuario(bd, correo):
    cursor = bd.cursor()
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
    cursor.execute(query, (correo,))

    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False

import hashlib
def crear_usuario(bd, correo, contra):
    h = hashlib.new('sha256', bytes(contra, 'utf-8'))
    h = h.hexdigest()
    cursor = bd.cursor()
    insertar = ("INSERT INTO usuario(correo, contrasenia) VALUES(%s, %s)")
    cursor.execute(insertar, (correo, h))
    bd.commit()

def iniciar_sesion(bd, correo, contra):
    h = hashlib.new('sha256', bytes(contra, 'utf-8'))
    h = h.hexdigest()
    cursor = bd.cursor()
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s AND contrasenia = %s"
    cursor.execute(query, (correo, h))

    if cursor.fetchone()[0] == 1:
        return True
    else:
        return False

def insertar_pelicula(bd, pelicula):
    try:
        titulo = pelicula['titulo']
        imagen = pelicula['imagen']
        fecha_visto = pelicula['fecha_visto']
        director = pelicula['director']
        anio = int(pelicula['anio'])
        usuarioId = int(pelicula['usuario'])

        cursor = bd.cursor()
        insertar = "INSERT INTO pelicula(titulo, imagen, fecha_visto, director, anio, usuarioId) " \
                   "VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(insertar, (titulo, imagen, fecha_visto, director, anio, usuarioId))
        bd.commit()
        return True
    except:
        return False

def get_peliculas(bd, id):
    cursor = bd.cursor()
    query = "SELECT id, titulo, imagen, fecha_visto, director, anio " \
            "FROM pelicula WHERE usuarioId = %s"
    cursor.execute(query, (id,))
    peliculas = []
    for row in cursor.fetchall():
        pelicula = {
            'id': row[0],
            'titulo': row[1],
            'image': row[2],
            'fecha_visto': row[3],
            'director': row[4],
            'anio': row[5]
        }
        peliculas.append(pelicula)
    return peliculas

def get_pelicula(bd, id):
    cursor = bd.cursor()
    query = "SELECT * FROM pelicula WHERE id = %s"
    cursor.execute(query, (id,))
    pelicula = {}
    row = cursor.fetchone()
    if row:
        pelicula = {
            'id': row[0],
            'titulo': row[1],
            'fecha_visto': row[2],
            'image': row[3],
            'director': row[4],
            'anio': row[5],
            'valoracion': row[6],
            'favorito': row[7],
            'resenia': row[8],
            'compartido': row[9]
        }
    return pelicula

def eliminar_pelicula(bd, id):
    cursor = bd.cursor()
    query = "DELETE FROM pelicula WHERE id = %s"
    cursor.execute(query, (id,))
    bd.commit()
    if cursor.rowcount:
        return True
    else:
        return False

def modificar_pelicula(bd, id, columna, valor):
    cursor = bd.cursor()
    update = "UPDATE pelicula SET {} = %s WHERE id = %s".format(columna)
    cursor.execute(update, (valor, id))
    bd.commit()
    if cursor.rowcount:
        return True
    else:
        return False

def login(bd, correo, contra):
    h = hashlib.new('sha256', bytes(contra, 'utf-8'))
    h = h.hexdigest()
    cursor = bd.cursor()
    query = "SELECT id FROM usuario WHERE correo = %s AND contrasenia = %s"
    cursor.execute(query, (correo, h))
    id = cursor.fetchone()

    if id:
        return id[0], True
    else:
        return None, False