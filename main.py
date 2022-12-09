import tkinter as tk
from guis.persona.admper import *
from guis.pelicula.admpelis import *
from guis.reserva.admres import *
from guis.sala.admsalas import *


def main():
    root = tk.Tk()
    root.title("Cinemar Plaza")
    root.iconbitmap('img/compu.ico')

    a = 4
    if a == 1:
        root = FrameAdmPer(root=root)
    if a == 2:
        root = FrameAdmPelis(root=root)
    if a == 3:
        root = FrameAdmRes(root=root)
    if a == 4:
        root = FrameAdmSala(root=root)
    root.mainloop()


if __name__ == "__main__":
    main()
