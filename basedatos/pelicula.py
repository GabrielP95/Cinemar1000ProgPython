import sqlite3 as sql


def crearPeliculas():
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS peliculas(
            id_pelicula INTERGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            categoria TEXT,
            descripcion TEXT,
        )"""
    )
    conn.commit()
    conn.close()


def insertar_pelicula(nombre, categoria, descripcion):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""INSERT INTO peliculas VALUES(NULL,{nombre},{categoria},{descripcion})"""
    )
    conn.commit()
    conn.close()


def modificar_nombrepeli(id_pelicula, nombre):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE peliculas SET nombre={nombre} WHERE id_pelicula={id_pelicula}"""
    )
    conn.commit()
    conn.close()


def modificar_categoriapeli(id_pelicula, categoria):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE peliculas categoria={categoria} WHERE id_pelicula={id_pelicula}"""
    )
    conn.commit()
    conn.close()


def modificar_descripcionpeli(id_pelicula, descripcion):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE peliculas descripcion={descripcion} WHERE id_pelicula={id_pelicula}"""
    )
    conn.commit()
    conn.close()


def borrar_peli(id_pelicula):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""DELETE FROM peliculas WHERE id_pelicula={id_pelicula}"""
    )
    conn.commit()
    conn.close()


def traer_peliculas():
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM peliculas""")
    peliculas = cursor.fetchall()
    for pelicula in peliculas:
        print(f"Pelicula:{pelicula}\n")
    conn.close()


def traer_unapelicula(id_pelicula):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT * FROM  peliculas WHERE id_pelicula={id_pelicula}""")
    pelicula = cursor.fetchone()
    print(f"Pelicula:{pelicula}\n")
    conn.close()
