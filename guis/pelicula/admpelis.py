import tkinter as tk
from tkinter import ttk
from basedatos.pelicula import *
from clases.peliculaclass import *


class FrameAdmPelis(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=300)
        self.root = root
        self.root.title("Administrar Peliculas")
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()
        self.pack()
        self.id_peli = None

    def campos_pelicula(self):
        # Labels de cada campo
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.grid(row=0, column=0)

        self.label_categoria = tk.Label(self, text="Categoria: ")
        self.label_categoria.grid(row=1, column=0)

        self.label_descripcion = tk.Label(self, text="Descripcion: ")
        self.label_descripcion.grid(row=2, column=0)

        # Entradas de cada campo
        self.minombre = tk.StringVar(self)
        self.entrada_nombre = tk.Entry(self, textvariable=self.minombre)
        self.entrada_nombre.config(width=80, state="disabled")
        self.entrada_nombre.grid(
            row=0, column=1, padx=10, pady=10, columnspan=2)

        self.micategoria = tk.StringVar(self)
        self.entrada_categoria = tk.Entry(self, textvariable=self.micategoria)
        self.entrada_categoria.config(width=80, state="disabled")
        self.entrada_categoria.grid(
            row=1, column=1, padx=10, pady=10, columnspan=2)

        self.midescripcion = tk.StringVar(self)
        self.entrada_descripcion = tk.Entry(
            self, textvariable=self.midescripcion)
        self.entrada_descripcion.config(width=80, state="disabled")
        self.entrada_descripcion.grid(
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
        self.minombre.set("")
        self.micategoria.set("")
        self.midescripcion.set("")

        self.entrada_nombre.config(state="normal")
        self.entrada_categoria.config(state="normal")
        self.entrada_descripcion.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    def deshabilitar_campos(self):

        self.id_peli = None
        self.minombre.set("")
        self.micategoria.set("")
        self.midescripcion.set("")

        self.entrada_nombre.config(state="disabled")
        self.entrada_categoria.config(state="disabled")
        self.entrada_descripcion.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    def guardar_datos(self):
        pelicula = Pelicula(self.minombre.get(),
                            self.micategoria.get(), self.midescripcion.get())
        if self.id_peli == None:
            pelicula.insertarpeli()
        else:
            pelicula.modificar(self.id_peli)
            self.id_peli = None
        self.tabla_peliculas()
        self.deshabilitar_campos()

        # Tabla

    def tabla_peliculas(self):
        self.listapeliculas = traer_peliculas()
        self.listapeliculas.reverse()

        self.tabla = ttk.Treeview(self, column=(
            "Nombre", "Categoria", "Descripcion"))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        # Scrollbar
        self.scroll = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=3, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text="ID")
        self.tabla.heading('#1', text="NOMBRE")
        self.tabla.heading('#2', text="CATEGORIA")
        self.tabla.heading('#3', text="DESCRIPCION")

        # Iterando la lista de peliculas
        for p in self.listapeliculas:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))
    # Botones
        self.boton_modificar = tk.Button(
            self, text="Modificar", command=self.editar_peli)
        self.boton_modificar.config(
            width=20, cursor="hand2", bg="#158645", activebackground="#35BD6F")
        self.boton_modificar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(
            self, text="Eliminar", command=self.eliminar_peli)
        self.boton_eliminar.config(
            width=20, cursor="hand2", bg="#BD152E", activebackground="#E15370")
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_peli(self):

        self.id_peli = self.tabla.item(self.tabla.selection())['text']
        self.nombre_peli = self.tabla.item(
            self.tabla.selection())['values'][0]
        self.categoria_peli = self.tabla.item(
            self.tabla.selection())['values'][1]
        self.descripcion_peli = self.tabla.item(
            self.tabla.selection())['values'][2]

        self.habilitar_campos()

        self.entrada_nombre.insert(0, self.nombre_peli)
        self.entrada_categoria.insert(0, self.categoria_peli)
        self.entrada_descripcion.insert(0, self.descripcion_peli)

    def eliminar_peli(self):
        self.id_peli = self.tabla.item(self.tabla.selection())['text']
        borrar_peli(self.id_peli)
        self.id_peli = None
        self.tabla_peliculas()
