import sqlite3 as sql


def crearPersonas():
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS personas(
            id_persona INTERGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            usuario TEXT,
            contraseña INTERGER,
            tipo INTERGER,
            tarjeta BOOL
        )"""
    )
    conn.commit()
    conn.close()


def insertar_persona(nombre, apellido, usuario, contraseña, tipo, tarjeta):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""INSERT INTO personas VALUES(NULL,{nombre},{apellido},{usuario},{contraseña},{tipo},{tarjeta})"""
    )
    conn.commit()
    conn.close()


def modificar_usuarioper(id_persona, usuario):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE personas SET usuario={usuario} WHERE id_persona={id_persona}"""
    )
    conn.commit()
    conn.close()


def modificar_contraper(id_persona, contraseña):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE personas contraseña={contraseña} WHERE id_persona={id_persona}"""
    )
    conn.commit()
    conn.close()


def modificar_tipoper(id_persona, tipo):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE personas tipo={tipo} WHERE id_persona={id_persona}"""
    )
    conn.commit()
    conn.close()


def modificar_tarjetaper(id_persona, tarjeta):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE personas tarjeta={tarjeta} WHERE id_persona={id_persona}"""
    )
    conn.commit()
    conn.close()


def borrar_persona(id_persona):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""DELETE FROM personas WHERE id_persona={id_persona}"""
    )
    conn.commit()
    conn.close()


def traer_personas():
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM personas""")
    personas = cursor.fetchall()
    for persona in personas:
        print(f"Persona:{persona}\n")
    conn.close()


def traer_unapersona(id_persona):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM personas WHERE id_persona={id_persona}""")
    persona = cursor.fetchone()
    print(f"Persona:{persona}\n")
    conn.close()
