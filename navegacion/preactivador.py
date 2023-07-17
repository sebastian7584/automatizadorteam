from navegacion import sub_menu as sm, ventana_informacion
from recursos import  label, botones, colors
from funcionalidad import  web_controller, poliedro, excel
from subprocess import Popen
import threading
import tkinter as tk
import customtkinter as ctk
import time

class Preactivador:

    def __init__(self,master, on_of):
        self.on_of = on_of
        self.poliedro = poliedro.Poliedro()
        self.excel = excel.Excel_controller()
        self.link= 'https://poliedrodist.comcel.com.co/'
        self.link2='https://poliedrodist.comcel.com.co/activaciones/http/REINGENIERIA/pagDispatcherEntradaModernizacion.asp?Site=1'
        self.titulo = label.Label().create_label(master, 'PREACTIVADOR DE SIM', 0.2, 0.0, 0.5,0.2, letterSize= 25)
        self.ventana_informacion =  ventana_informacion.Ventana_informacion(master)
        self.menu = sm.Sub_menu(master,3, boton1=['ABRIR LISTA', self.abrir_excel], boton2=['ABRIR PAGINA', self.abrir_pagina], boton3=['START', self.ejecuccionHilo])
        self.preactivador = ''
        self.time = tk.StringVar()
        self.time.set('0')
        self.titulo = label.Label().create_label(self.menu.submenu, 'Intervalos', 0.0, 0.65, 0.5,0.2, letterSize= 16)
        input_widget = ctk.CTkEntry(self.menu.submenu, textvariable=self.time)
        input_widget.place(relx=0.5, rely=0.73, relheight=0.05, relwidth=0.2)
        boton = botones.Buttons()
        color = colors.Colors()
        self.okBotton = boton.create_button(self.menu.submenu, 'OK', 0.7, 0.73, 0.15, 0.05, self.cambioIntervalo)
        self.okBotton.configure(fg_color= color.team, text_color= 'white')
        self.correo = 'cjgomez@teamcomunicaciones.com'
        self.correoEdit = tk.StringVar()
        self.correoEdit.set(self.correo) 
        input_widget2 = ctk.CTkEntry(self.menu.submenu, textvariable=self.correoEdit)
        input_widget2.place(relx=0.15, rely=0.89, relheight=0.05, relwidth=0.7)
        self.okBotton2 = boton.create_button(self.menu.submenu, 'confirmar', 0.3, 0.95, 0.40, 0.05, self.cambioCorreo)
        self.okBotton2.configure(fg_color= color.team, text_color= 'white')
       
        
    
    def abrir_excel(self):
        self.ventana_informacion.write('excel equipos abierto recuerde cerrar antes de iniciar')
        p = Popen("src\preactivador\openExcel.bat")
        stdout, stderr = p.communicate()
    
    def cambioIntervalo(self):
        self.preactivador.actualizarIntervalo(self.time.get())
        self.ventana_informacion.write(f'intervalo {self.time.get()} segundos')

    def cambioCorreo(self):
        self.correo = self.correoEdit.get()
        self.ventana_informacion.write(f'Correo actualizado por {self.correo}')
    
    def abrir_pagina(self):
        self.ventana_informacion.write('Navegador abierto')
        class Abrir_pagina1(web_controller.Web_Controller):pass
        self.preactivador = Abrir_pagina1(int(self.time.get()))
        self.preactivador.openEdge()
        self.preactivador.selectPage(self.link)
    
    def ejecuccionHilo(self):
        hilo_equipos = threading.Thread(target=self.ejecuccion)
        hilo_equipos.start()
        
    def ejecuccion(self):
        self.on_of(False)
        self.ventana_informacion.write('Empezando ejecuccion')
        self.poliedro.definirBrowser(self.preactivador)
        self.poliedro.seleccionAcceso('195')
        self.excel.leer_excel('src\preactivador\preactivador.xlsx','Iccid')
        self.excel.quitarFormatoCientifico('Iccid')
        self.ciclo = True
        self.contador = 0

        while self.ciclo:
            if self.contador == self.excel.cantidad:
                ciclo = False
            else:
                self.mensaje = ''
                self.EquiposInd()
        self.ventana_informacion.write('Proceso terminado')
        self.on_of(True)
    

    def EquiposInd(self):
        self.ventana_informacion.write(f'Activando Equipo {self.contador+1} de {self.excel.cantidad}')
        self.iccid = str(self.excel.excel['Iccid'][self.contador])[-12:] 
        
        try:
            self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[1]/div[2]/div[1]/div/span/span[1]/span/span[1]')
            self.preactivador.click('/html/body/span/span/span[2]/ul/li[3]')
            self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[1]/div[2]/div[2]/div/input', '900206401')
            self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[1]/div[3]/div[1]/div/span/span[1]/span/span[1]')
            self.preactivador.click('/html/body/span/span/span[2]/ul/li[2]')
            self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[1]/div[3]/div[3]/div/input', self.iccid)
            self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[5]/input[1]')
            self.preactivador.waitExist('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[7]/input[1]')
            optionsList = [
                ['/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[6]/div/span'],
            ]
            funcionList = [
                self.terminarActivacion
            ]
            self.poliedro.detectOption(optionsList, funcionList, NoneFunc=self.errorValidacion)



        except:
            self.ventana_informacion.write(f'Activacion erronea de equipo {self.iccid}')
            self.poliedro.reinicio()
            self.contador += 1
        time.sleep(0.5)
        self.ventana_informacion.write(f'Activacion exitosa de equipo {self.iccid}')
        self.guardarData()
        self.poliedro.reinicio()
        self.contador += 1

    def errorValidacion(self):
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[7]/input[1]')
        self.preactivador.erase('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[1]/div[3]/div[3]/div/input')
        self.preactivador.erase('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[1]/div[2]/div[2]/div/input')
        self.min = ''
        self.mensaje = 'Error en activacion'
    
    def terminarActivacion(self):
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[7]/input[3]')
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[1]/div/span/span[1]/span/span[1]')
        self.preactivador.click('/html/body/span/span/span[2]/ul/li[2]')
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[4]/div/input', self.correo)
        time.sleep(2)
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[5]/div[2]/fieldset/div/div[1]/div/select', 'fijo')
        time.sleep(2)
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[5]/div[2]/fieldset/div/div[2]/div/select', '604')
        time.sleep(2)
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[5]/div[2]/fieldset/div/div[3]/div/input', '3131234')
        time.sleep(2)
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[1]/div[1]/select', 'Otras')
        time.sleep(2)
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[2]/div/input', 'CENTRO')
        time.sleep(2)
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[3]/div/select','ANTIOQUIA')
        time.sleep(4)
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[4]/div/select', 'MEDELLIN')
        time.sleep(2)
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[5]/div/input', 'CENTRO')
        time.sleep(2)
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[3]/input[2]')
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div/div[1]/div[2]/div/span/span[1]/span/span[1]')
        self.preactivador.click('/html/body/span/span/span[2]/ul/li[2]')
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div/div[1]/div[3]/div/span/span[1]/span/span[1]')
        self.preactivador.click('/html/body/span/span/span[2]/ul/li[2]')
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[3]/input[2]')
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/div/strong/strong/div/input[2]')
        self.min = self.preactivador.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/div/div/div/strong/strong/div/div/div/p/strong[3]')
        self.min = self.min[-10:]
        self.mensaje = ''
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/div/strong/strong/div/input[1]')
        self.preactivador.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[1]/div[1]/div[1]/div/div/ul/li[1]/span/input')
        self.preactivador.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[2]/div/div[1]/div/input', '1010014821')


    def guardarData(self):
        self.excel.guardar(self.contador, 'Min', self.min, 'src\equipos\equipos.xlsx')
        self.excel.guardar(self.contador, 'Mensaje', self.mensaje, 'src\equipos\equipos.xlsx')
