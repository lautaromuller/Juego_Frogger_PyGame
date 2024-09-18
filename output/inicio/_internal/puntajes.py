import sqlite3

def crear_tabla():
    with sqlite3.connect("bd_puntos.db") as conexion:
        try:
            sentencia = ''' create table puntajes
            (
            id integer primary key autoincrement,
            nombre text,
            puntos integer,
            tiempo integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla puntajes")
        except sqlite3.OperationalError:
            print("La tabla puntajes ya existe")

def agregar_jugador(nombre:str, puntos:str, tiempo:int):
    with sqlite3.connect("bd_puntos.db") as conexion:
        try:
            conexion.execute("insert into puntajes(nombre,puntos,tiempo) values (?,?,?)", (nombre, puntos,tiempo))
            print("jugador añadido")
            conexion.commit()
        except:
            print("Error")

def mostrar_datos():
    with sqlite3.connect("bd_puntos.db") as conexion:
        lista = []
        cursor=conexion.execute("SELECT * FROM puntajes ORDER BY puntos DESC LIMIT 0,5")
        for fila in cursor:
            lista.append(fila[1:])
    return lista

def modificar_tabla(id):
    with sqlite3.connect("bd_puntos.db") as conexion:
        sentencia = "UPDATE puntajes SET nombre = 'JULIETA' WHERE id=?"
        cursor=conexion.execute(sentencia,(id,))
        filas=cursor.fetchall()
        for fila in filas:
            print(fila)