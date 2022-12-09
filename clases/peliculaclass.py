from basedatos.pelicula import *


class Pelicula:
    def __init__(self, nombre, categoria, descripcion):
        self.__id = None
        self.__nombre = nombre
        self.__categoria = categoria
        self.__descripcion = descripcion

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevonombre):
        self.__nombre = nuevonombre

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, nuevacategoria):
        self.__categoria = nuevacategoria

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, nuevadescripcion):
        self.__descripcion = nuevadescripcion

    def crear(self):
        crearPeliculas()

    def insertarpeli(self):
        insertar_pelicula(self.__nombre, self.__categoria, self.__descripcion)

    def modificar(self, id_peli):
        modificar_peli(id_peli, self.__nombre,
                       self.__categoria, self.__descripcion)

    def modificar_nombre(self):
        modificar_nombrepeli(self.__id, self.__nombre)

    def modificarcate(self):
        modificar_nombrepeli(self.__id, self.__categoria)

    def modificardesc(self):
        modificar_nombrepeli(self.__id, self.__descripcion)
