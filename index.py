from navegacion import applicacion
from recursos import botones
from tkinter import messagebox


def alertas(mensaje):
    root.root.attributes("-topmost", True)
    messagebox.showwarning(message=mensaje, title="Mensaje")   
    root.root.attributes("-topmost", False)



if __name__ == '__main__':
    app = applicacion.App
    root = app('1080x720', 'Team Comunicaciones', 'version: 1.6.2', alertas)
    root.start()

