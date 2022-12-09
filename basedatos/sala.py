import sqlite3 as sql


def crearSalas():
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS salas(
            id_sala INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pelicula INTEGER,
            tipo TEXT,
            capacidad INTEGER,
            FOREIGN KEY (id_pelicula) REFERENCES peliculas (id_peliculas)
        )"""
    )
    conn.commit()
    conn.close()


def insertar_sala(id_pelicula, tipo, capacidad):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""INSERT INTO salas VALUES(NULL,{id_pelicula},'{tipo}',{capacidad})"""
    )
    conn.commit()
    conn.close()


def modificar_sala(id_sala, id_pelicula, tipo, capacidad):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE salas SET id_pelicula={id_pelicula}, tipo='{tipo}', capacidad={capacidad} WHERE id_sala={id_sala}"""
    )
    conn.commit()
    conn.close()


def modificar_pelisala(id_sala, id_pelicula):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE salas SET id_pelicula={id_pelicula} WHERE id_sala={id_sala}"""
    )
    conn.commit()
    conn.close()


def modificar_tiposala(id_sala, tipo):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE salas tipo={tipo} WHERE id_sala={id_sala}"""
    )
    conn.commit()
    conn.close()


def modificar_capacidadsala(id_sala, capacidad):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE salas capacidad={capacidad} WHERE id_sala={id_sala}"""
    )
    conn.commit()
    conn.close()


def borrar_sala(id_sala):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""DELETE FROM salas WHERE id_sala={id_sala}"""
    )
    conn.commit()
    conn.close()


def traer_salas():
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM salas""")
    salas = cursor.fetchall()
    conn.close()
    return salas


def traer_unasala(id_sala):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM salas WHERE id_sala={id_sala}""")
    sala = cursor.fetchone()
    print(f"Sala:{sala}\n")
    conn.close()


crearSalas()
