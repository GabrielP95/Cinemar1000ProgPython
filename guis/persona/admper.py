import tkinter as tk
from tkinter import ttk
from basedatos.persona import *
from clases.personaclass import *


class FrameAdmPer(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=580, height=300)
        self.root = root
        self.root.title("Administrar Personas")
        self.campos_persona()
        self.deshabilitar_campos()
        self.tabla_personas()
        self.pack()
        self.id_persona = None

    def campos_persona(self):
        # Labels de cada campo
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.grid(row=0, column=0)

        self.label_apellido = tk.Label(self, text="Apellido: ")
        self.label_apellido.grid(row=1, column=0)

        self.label_usuario = tk.Label(self, text="Usuario: ")
        self.label_usuario.grid(row=2, column=0)

        self.label_contraseña = tk.Label(self, text="Contraseña: ")
        self.label_contraseña.grid(row=3, column=0)

        self.label_tipo = tk.Label(self, text="Tipo: ")
        self.label_tipo.grid(row=4, column=0)

        self.label_tipo = tk.Label(self, text="Tarjeta: ")
        self.label_tipo.grid(row=5, column=0)

        # Entradas de cada campo
        self.minombre = tk.StringVar(self)
        self.entrada_nombre = tk.Entry(self, textvariable=self.minombre)
        self.entrada_nombre.config(width=100)
        self.entrada_nombre.grid(
            row=0, column=1, columnspan=2, padx=10, pady=10)

        self.miapellido = tk.StringVar(self)
        self.entrada_apellido = tk.Entry(self, textvariable=self.miapellido)
        self.entrada_apellido.config(width=100)
        self.entrada_apellido.grid(
            row=1, column=1, columnspan=2, padx=10, pady=10)

        self.miusuario = tk.StringVar(self)
        self.entrada_usuario = tk.Entry(self, textvariable=self.miusuario)
        self.entrada_usuario.config(width=100)
        self.entrada_usuario.grid(
            row=2, column=1, columnspan=2, padx=10, pady=10)

        self.micontraseña = tk.StringVar(self)
        self.entrada_contraseña = tk.Entry(
            self, textvariable=self.micontraseña)
        self.entrada_contraseña.config(width=100)
        self.entrada_contraseña.grid(
            row=3, column=1, columnspan=2, padx=10, pady=10)

        self.mitipo = tk.StringVar(self)
        self.entrada_tipo = tk.Entry(self, textvariable=self.mitipo)
        self.entrada_tipo.config(width=100)
        self.entrada_tipo.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

        self.mitarjeta = tk.StringVar(self)
        self.entrada_tarjeta = tk.Entry(self, textvariable=self.mitarjeta)
        self.entrada_tarjeta.config(width=100)
        self.entrada_tarjeta.grid(
            row=5, column=1, columnspan=2, padx=10, pady=10)

        # Botones
        self.boton_agregar = tk.Button(
            self, text="Agregar", command=self.habilitar_campos)
        self.boton_agregar.config(
            width=20, cursor="hand2", bg="#158645", activebackground="#35BD6F")
        self.boton_agregar.grid(row=6, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(
            self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(
            width=20, cursor="hand2", bg="#1658A2", activebackground="#3586DF")
        self.boton_guardar.grid(row=6, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(
            self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(
            width=20, cursor="hand2", bg="#BD152E", activebackground="#E15370")
        self.boton_cancelar.grid(row=6, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.minombre.set("")
        self.miapellido.set("")
        self.miusuario.set("")
        self.micontraseña.set("")
        self.mitipo.set("")
        self.mitarjeta.set("")

        self.entrada_nombre.config(state="normal")
        self.entrada_apellido.config(state="normal")
        self.entrada_usuario.config(state="normal")
        self.entrada_contraseña.config(state="normal")
        self.entrada_tipo.config(state="normal")
        self.entrada_tarjeta.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    def deshabilitar_campos(self):
        self.id_persona = None
        self.minombre.set("")
        self.miapellido.set("")
        self.miusuario.set("")
        self.micontraseña.set("")
        self.mitipo.set("")
        self.mitarjeta.set("")

        self.entrada_nombre.config(state="disabled")
        self.entrada_apellido.config(state="disabled")
        self.entrada_usuario.config(state="disabled")
        self.entrada_contraseña.config(state="disabled")
        self.entrada_tipo.config(state="disabled")
        self.entrada_tarjeta.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    def guardar_datos(self):
        persona = Persona(self.minombre.get(),
                          self.miapellido.get(), self.miusuario.get(), self.micontraseña.get(), self.mitipo.get(), self.mitarjeta.get())
        if self.id_persona == None:
            persona.insertarpersona()
        else:
            persona.modificar(self.id_persona)
            self.id_persona = None
        self.tabla_personas()
        self.deshabilitar_campos()

        # Tabla

    def tabla_personas(self):
        self.listapersonas = traer_personas()
        self.listapersonas.reverse()

        self.tabla = ttk.Treeview(self, column=(
            "Nombre", "Apellido", "Usuario", "Contraseña", "Tipo", "Tarjeta"))
        self.tabla.grid(row=7, column=0, columnspan=6, sticky='nsw')

        # Scrollbar
        self.scrolly = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla.yview)
        self.scrolly.grid(row=7, column=0, sticky='nsw')
        self.tabla.configure(yscrollcommand=self.scrolly.set)

        """self.scrollx = ttk.Scrollbar(
            self, orient='horizontal', command=self.tabla.xview)
        self.scrollx.grid(row=7, column=0, sticky='swe')
        self.tabla.configure(xscrollcommand=self.scrollx.set)"""

        self.tabla.heading('#0', text="ID")
        self.tabla.heading('#1', text="NOMBRE")
        self.tabla.heading('#2', text="APELLIDO")
        self.tabla.heading('#3', text="USUARIO")
        self.tabla.heading('#4', text="CONTRASEÑA")
        self.tabla.heading('#5', text="TIPO")
        self.tabla.heading('#6', text="TARJETA")

        # Iterando la lista de personas
        for p in self.listapersonas:
            self.tabla.insert('', 0, text=p[0], values=(
                p[1], p[2], p[3], p[4], p[5], p[6]))
    # Botones
        self.boton_modificar = tk.Button(
            self, text="Modificar", command=self.editar_per)
        self.boton_modificar.config(
            width=20, cursor="hand2", bg="#158645", activebackground="#35BD6F")
        self.boton_modificar.grid(row=8, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(
            self, text="Eliminar", command=self.eliminar_per)
        self.boton_eliminar.config(
            width=20, cursor="hand2", bg="#BD152E", activebackground="#E15370")
        self.boton_eliminar.grid(row=8, column=1, padx=10, pady=10)

    def editar_per(self):

        self.id_persona = self.tabla.item(self.tabla.selection())['text']
        self.nombre_per = self.tabla.item(
            self.tabla.selection())['values'][0]
        self.apellido_per = self.tabla.item(
            self.tabla.selection())['values'][1]
        self.usuario_per = self.tabla.item(
            self.tabla.selection())['values'][2]
        self.contraseña_per = self.tabla.item(
            self.tabla.selection())['values'][3]
        self.tipo_per = self.tabla.item(
            self.tabla.selection())['values'][4]
        self.tarjeta_per = self.tabla.item(
            self.tabla.selection())['values'][5]

        self.habilitar_campos()

        self.entrada_nombre.insert(0, self.nombre_per)
        self.entrada_apellido.insert(0, self.apellido_per)
        self.entrada_usuario.insert(0, self.usuario_per)
        self.entrada_contraseña.insert(0, self.contraseña_per)
        self.entrada_tipo.insert(0, self.tipo_per)
        self.entrada_tarjeta.insert(0, self.tarjeta_per)

    def eliminar_per(self):
        self.id_persona = self.tabla.item(self.tabla.selection())['text']
        borrar_persona(self.id_persona)
        self.id_persona = None
        self.tabla_personas()
