import tkinter as tk
from tkinter import ttk
from basedatos.reserva import *
from clases.reservaclass import *


class FrameAdmRes(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=300)
        self.root = root
        self.root.title("Administrar Reservas")
        self.campos_reserva()
        self.deshabilitar_campos()
        self.tabla_reservas()
        self.pack()
        self.id_res = None

    def campos_reserva(self):
        # Labels de cada campo
        self.label_idpersona = tk.Label(self, text="Persona: ")
        self.label_idpersona.grid(row=0, column=0)

        self.label_idsala = tk.Label(self, text="Sala: ")
        self.label_idsala.grid(row=1, column=0)

        self.label_precio = tk.Label(self, text="Precio: ")
        self.label_precio.grid(row=2, column=0)

        # Entradas de cada campo
        self.mipersona = tk.StringVar(self)
        self.entrada_idpersona = tk.Entry(self, textvariable=self.mipersona)
        self.entrada_idpersona.config(width=80, state="disabled")
        self.entrada_idpersona.grid(
            row=0, column=1, padx=10, pady=10, columnspan=2)

        self.misala = tk.StringVar(self)
        self.entrada_idsala = tk.Entry(self, textvariable=self.misala)
        self.entrada_idsala.config(width=80, state="disabled")
        self.entrada_idsala.grid(
            row=1, column=1, padx=10, pady=10, columnspan=2)

        self.miprecio = tk.StringVar(self)
        self.entrada_precio = tk.Entry(
            self, textvariable=self.miprecio)
        self.entrada_precio.config(width=80, state="disabled")
        self.entrada_precio.grid(
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
        self.mipersona.set("")
        self.misala.set("")
        self.miprecio.set("")

        self.entrada_idpersona.config(state="normal")
        self.entrada_idsala.config(state="normal")
        self.entrada_precio.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    def deshabilitar_campos(self):

        self.id_res = None
        self.mipersona.set("")
        self.misala.set("")
        self.miprecio.set("")

        self.entrada_idpersona.config(state="disabled")
        self.entrada_idsala.config(state="disabled")
        self.entrada_precio.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    def guardar_datos(self):
        reserva = Reserva(self.mipersona.get(),
                          self.misala.get(), self.miprecio.get())
        if self.id_res == None:
            reserva.crear()
        else:
            reserva.modificar(self.id_res)
            self.id_res = None
        self.tabla_reservas()
        self.deshabilitar_campos()

        # Tabla

    def tabla_reservas(self):
        self.listareservas = traer_reservas()
        self.listareservas.reverse()

        self.tabla = ttk.Treeview(self, column=(
            "Persona", "Sala", "Precio"))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        # Scrollbar
        self.scroll = ttk.Scrollbar(
            self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=3, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text="ID")
        self.tabla.heading('#1', text="PERSONA")
        self.tabla.heading('#2', text="SALA")
        self.tabla.heading('#3', text="PRECIO")

        # Iterando la lista de reservas
        for p in self.listareservas:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))
    # Botones
        self.boton_modificar = tk.Button(
            self, text="Modificar", command=self.editar_res)
        self.boton_modificar.config(
            width=20, cursor="hand2", bg="#158645", activebackground="#35BD6F")
        self.boton_modificar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(
            self, text="Eliminar", command=self.eliminar_res)
        self.boton_eliminar.config(
            width=20, cursor="hand2", bg="#BD152E", activebackground="#E15370")
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_res(self):

        self.id_res = self.tabla.item(self.tabla.selection())['text']
        self.id_persona = self.tabla.item(
            self.tabla.selection())['values'][0]
        self.id_sala = self.tabla.item(
            self.tabla.selection())['values'][1]
        self.precio = self.tabla.item(
            self.tabla.selection())['values'][2]

        self.habilitar_campos()

        self.entrada_idpersona.insert(0, self.id_persona)
        self.entrada_idsala.insert(0, self.id_sala)
        self.entrada_precio.insert(0, self.precio)

    def eliminar_res(self):
        self.id_res = self.tabla.item(self.tabla.selection())['text']
        borrar_reserva(self.id_res)
        self.id_res = None
        self.tabla_reservas()
