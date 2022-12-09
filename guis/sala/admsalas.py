import tkinter as tk
from tkinter import ttk
from basedatos.sala import *
from clases.salaclass import *


class FrameAdmSala(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=300)
        self.root = root
        self.root.title("Administrar Salas")
        self.campos_sala()
        self.deshabilitar_campos()
        self.tabla_salas()
        self.pack()
        self.id_sala = None

    def campos_sala(self):
        # Labels de cada campo
        self.label_idpeli = tk.Label(self, text="Pelicula: ")
        self.label_idpeli.grid(row=0, column=0)

        self.label_tipo = tk.Label(self, text="Tipo: ")
        self.label_tipo.grid(row=1, column=0)

        self.label_capacidad = tk.Label(self, text="Capacidad: ")
        self.label_capacidad.grid(row=2, column=0)

        # Entradas de cada campo
        self.mipeli = tk.StringVar(self)
        self.entrada_idpeli = tk.Entry(self, textvariable=self.mipeli)
        self.entrada_idpeli.config(width=80, state="disabled")
        self.entrada_idpeli.grid(
            row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mitipo = tk.StringVar(self)
        self.entrada_tipo = tk.Entry(self, textvariable=self.mitipo)
        self.entrada_tipo.config(width=80, state="disabled")
        self.entrada_tipo.grid(
            row=1, column=1, padx=10, pady=10, columnspan=2)

        self.micapacidad = tk.StringVar(self)
        self.entrada_capacidad = tk.Entry(
            self, textvariable=self.micapacidad)
        self.entrada_capacidad.config(width=80, state="disabled")
        self.entrada_capacidad.grid(
            row=2, column=1, padx=10, pady=10, columnspan=2)

        # Botones
        self.boton_agregar = tk.Button(
            self, text="Agregar", command=self.habilitar_campos)
        self.boton_agregar.config(
            width=20, cursor="hand2", bg="#158645", activebackground="#35BD6F")
        self.boton_agregar.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(
            self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(
            width=20, cursor="hand2", bg="#1658A2", activebackground="#3586DF")
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(
            self, text="Cancelar", command=self.deshabilitar_campos)
        self.boton_cancelar.config(
            width=20, cursor="hand2", bg="#BD152E", activebackground="#E15370")
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.mipeli.set("")
        self.mitipo.set("")
        self.micapacidad.set("")

        self.entrada_idpeli.config(state="normal")
        self.entrada_tipo.config(state="normal")
        self.entrada_capacidad.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    def deshabilitar_campos(self):

        self.id_sala = None
        self.mipeli.set("")
        self.mitipo.set("")
        self.micapacidad.set("")

        self.entrada_idpeli.config(state="disabled")
        self.entrada_tipo.config(state="disabled")
        self.entrada_capacidad.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    def guardar_datos(self):
        sala = Sala(self.mipeli.get(),
                    self.mitipo.get(), self.micapacidad.get())
        if self.id_sala == None:
            sala.crear()
        else:
            sala.modificar(self.id_sala)
            self.id_sala = None
        self.tabla_salas()
        self.deshabilitar_campos()

        # Tabla

    def tabla_salas(self):
        self.listasalas = traer_salas()
        self.listasalas.reverse()

        self.tabla = ttk.Treeview(self, column=(
            "Pelicula", "Tipo", "Capacidad"))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        # Scrollbar
        self.scroll = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=3, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text="ID")
        self.tabla.heading('#1', text="PELICULA")
        self.tabla.heading('#2', text="TIPO")
        self.tabla.heading('#3', text="CAPACIDAD")

        # Iterando la lista de salas
        for p in self.listasalas:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))
    # Botones
        self.boton_modificar = tk.Button(
            self, text="Modificar", command=self.editar_salas)
        self.boton_modificar.config(
            width=20, cursor="hand2", bg="#158645", activebackground="#35BD6F")
        self.boton_modificar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(
            self, text="Eliminar", command=self.eliminar_salas)
        self.boton_eliminar.config(
            width=20, cursor="hand2", bg="#BD152E", activebackground="#E15370")
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_salas(self):

        self.id_sala = self.tabla.item(self.tabla.selection())['text']
        self.id_peli = self.tabla.item(
            self.tabla.selection())['values'][0]
        self.tipo = self.tabla.item(
            self.tabla.selection())['values'][1]
        self.capacidad = self.tabla.item(
            self.tabla.selection())['values'][2]

        self.habilitar_campos()

        self.entrada_idpeli.insert(0, self.id_peli)
        self.entrada_tipo.insert(0, self.tipo)
        self.entrada_capacidad.insert(0, self.capacidad)

    def eliminar_salas(self):
        self.id_sala = self.tabla.item(self.tabla.selection())['text']
        borrar_sala(self.id_sala)
        self.id_sala = None
        self.tabla_salas()
