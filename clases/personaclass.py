from basedatos.persona import *


class Persona:
    def __init__(self, nombre, apellido, usuario, contraseña, tipo, tarjeta):
        self.__id = None
        self.__nombre = nombre
        self.__apellido = apellido
        self.__usuario = usuario
        self.__contraseña = contraseña
        self.__tipo = tipo
        self.__tarjeta = tarjeta

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
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevoapellido):
        self.__apellido = nuevoapellido

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, nuevousuario):
        self.__usuario = nuevousuario

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nuevacontraseña):
        self.__contraseña = nuevacontraseña

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevotipo):
        self.__tipo = nuevotipo

    @property
    def tarjeta(self):
        return self.__tarjeta

    @tarjeta.setter
    def tarjeta(self, bool):
        self.__tarjeta = bool

    def insertarpersona(self):
        insertar_persona(self.__nombre, self.__apellido, self.__usuario,
                         self.__contraseña, self.__tipo, self.__tarjeta)

    def modificar(self, id_persona):
        modificar_persona(id_persona, self.__nombre,
                          self.__apellido, self.__usuario, self.__contraseña, self.__tipo, self.__tarjeta)

    def modificar_usuario(self):
        modificar_usuarioper(self.__id, self.__nombre)

    def modificar_contraseña(self):
        modificar_contraper(self, self.__contraseña)

    def modificar_tipo(self):
        modificar_tipoper(self, self.__tipo)

    def modificar_tarjeta(self):
        modificar_tarjetaper(self, self.__tarjeta)

    def borrar(self):
        borrar_persona(self.__id)
