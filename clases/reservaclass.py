from basedatos.reserva import *


class Reserva:
    def __init__(self, idpersona, idsala, precio):
        self.__id = None
        self.__idpersona = idpersona
        self.__idsala = idsala
        self.__precio = precio

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
    def idpersona(self):
        return self.__idpersona

    @idpersona.setter
    def idpersona(self, nuevapersona):
        self.__idpersona = nuevapersona

    @property
    def idsala(self):
        return self.__idsala

    @idsala.setter
    def idsala(self, nuevasala):
        self.__idsala = nuevasala

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevoprecio):
        self.__precio = nuevoprecio

    def crear(self):
        insertar_reserva(self.__idpersona, self.__idsala, self.__precio)

    def modificar(self, id_reserva):
        modificar_persona(id_reserva, self.__idpersona,
                          self.__idsala, self.__precio)

    def modificar_persona(self):
        modificar_personares(self.__id, self.__idpersona)

    def modificar_sala(self):
        modificar_salares(self.__id, self.__idsala)

    def modificar_precio(self):
        modificar_preciores(self.__id, self.__precio)

    def borrar(self):
        borrar_reserva(self.__id)
