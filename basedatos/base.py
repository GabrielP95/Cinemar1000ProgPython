import sqlite3 as sql

def crearBase():
    conn = sql.connect("CinemarPlaza.db")
    conn.commit()
    conn.close()