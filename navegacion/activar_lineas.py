
from navegacion import sub_menu as sm, ventana_informacion
from recursos import create_frame, label, botones

class Activar_lineas:

    def __init__(self,master):

        self.titulo = label.Label().create_label(master, 'ACTIVADOR DE LINEAS', 0.2, 0.0, 0.2,0.2)
        self.ventana_informacion =  ventana_informacion.Ventana_informacion(master)
        self.menu = sm.Sub_menu(master,0, boton1=['ABRIR LISTA', self.abrir_excel], boton2=['ABRIR PAGINA', self.abrir_pagina])
    
    def abrir_excel(self):
        self.ventana_informacion.write('abrir excel')
    
    def abrir_pagina(self):
        self.ventana_informacion.write('abrir pagina')
        
    
