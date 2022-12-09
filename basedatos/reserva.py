import sqlite3 as sql


def crearReservas():
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS reservas(
            id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
            id_persona INTEGER,
            id_sala INTEGER,
            precio INTEGER,
            FOREIGN KEY (id_persona) REFERENCES personas (id_persona),
            FOREIGN KEY (id_sala) REFERENCES salas (id_salas)
        )"""
    )
    conn.commit()
    conn.close()


def insertar_reserva(id_persona, id_sala, precio):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""INSERT INTO reservas VALUES(NULL,{id_persona},{id_sala},{precio})"""
    )
    conn.commit()
    conn.close()


def modificar_persona(id_reserva, id_persona, id_sala, precio):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE reservas SET id_persona={id_persona}, id_sala={id_sala}, precio={precio} WHERE id_reserva={id_reserva}"""
    )
    conn.commit()
    conn.close()


def modificar_personares(id_reserva, id_persona):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE reservas SET id_persona={id_persona} WHERE id_reserva={id_reserva}"""
    )
    conn.commit()
    conn.close()


def modificar_salares(id_reserva, id_sala):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE reservas id_sala={id_sala} WHERE id_reserva={id_reserva}"""
    )
    conn.commit()
    conn.close()


def modificar_preciores(id_reserva, precio):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""UPDATE reservas precio={precio} WHERE id_reserva={id_reserva}"""
    )
    conn.commit()
    conn.close()


def borrar_reserva(id_reserva):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(
        f"""DELETE FROM reservas WHERE id_reserva={id_reserva}"""
    )
    conn.commit()
    conn.close()


def traer_reservas():
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM reservas""")
    reservas = cursor.fetchall()
    conn.close()
    return reservas


def traer_unareserva(id_reserva):
    conn = sql.connect("CinemarPlaza.db")
    cursor = conn.cursor()
    cursor.execute(f"""SELECT * FROM reservas WHERE id_reserva={id_reserva}""")
    reserva = cursor.fetchone()
    print(f"Reserva:{reserva}\n")
    conn.close()


crearReservas()
