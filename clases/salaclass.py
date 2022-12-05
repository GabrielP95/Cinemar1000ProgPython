from basedatos.sala import *


class Sala:
    def __init__(self, id, idpeli, tipo, capacidad):
        self.__id = id
        self.__idpeli = idpeli
        self.__tipo = tipo
        self.__capacidad = capacidad

    @property
    def id(self):
        return self.__id

    @property
    def idpeli(self):
        return self.__idpeli

    @idpeli.setter
    def idpeli(self, nuevapeli):
        self.__idpeli = nuevapeli

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevotipo):
        self.__tipo = nuevotipo

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, nuevacapacidad):
        self.__capacidad = nuevacapacidad

    def crear(self):
        insertar_sala(self.__idpeli, self.__tipo, self.__capacidad)

    def modificar_peli(self):
        modificar_pelisala(self.__id, self.__idpeli)

    def modificar_tipo(self):
        modificar_tiposala(self.__id, self.__tipo)

    def modificar_capacidad(self):
        modificar_capacidadsala(self.__id, self.__capacidad)

    def borrar(self):
        borrar_sala(self.__id)
