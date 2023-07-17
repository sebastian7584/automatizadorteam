from navegacion import sub_menu as sm, ventana_informacion
from recursos import  label, botones, colors
from funcionalidad import  web_controller, poliedro, excel
from subprocess import Popen
import threading
import tkinter as tk
import customtkinter as ctk
import time

class Equipos:

    def __init__(self,master, on_of):
        self.on_of = on_of
        self.poliedro = poliedro.Poliedro()
        self.excel = excel.Excel_controller()
        self.link= 'https://poliedrodist.comcel.com.co/'
        self.link2='https://poliedrodist.comcel.com.co/activaciones/http/REINGENIERIA/pagDispatcherEntradaModernizacion.asp?Site=1'
        self.titulo = label.Label().create_label(master, 'ACTIVADOR DE EQUIPO', 0.2, 0.0, 0.5,0.2, letterSize= 25)
        self.ventana_informacion =  ventana_informacion.Ventana_informacion(master)
        self.menu = sm.Sub_menu(master,3, boton1=['ABRIR LISTA', self.abrir_excel], boton2=['ABRIR PAGINA', self.abrir_pagina], boton3=['START', self.ejecuccionHilo])
        self.equipos = ''
        self.time = tk.StringVar()
        self.time.set('0')
        self.titulo = label.Label().create_label(self.menu.submenu, 'Intervalos', 0.0, 0.65, 0.5,0.2, letterSize= 16)
        input_widget = ctk.CTkEntry(self.menu.submenu, textvariable=self.time)
        input_widget.place(relx=0.5, rely=0.73, relheight=0.05, relwidth=0.2)
        boton = botones.Buttons()
        color = colors.Colors()
        self.okBotton = boton.create_button(self.menu.submenu, 'OK', 0.7, 0.73, 0.15, 0.05, self.cambioIntervalo)
        self.okBotton.configure(fg_color= color.team, text_color= 'white')
       
        
    
    def abrir_excel(self):
        self.ventana_informacion.write('excel equipos abierto recuerde cerrar antes de iniciar')
        p = Popen("src\equipos\openExcel.bat")
        stdout, stderr = p.communicate()
    
    def cambioIntervalo(self):
        self.equipos.actualizarIntervalo(self.time.get())
        self.ventana_informacion.write(f'intervalo {self.time.get()} segundos')

    def cambioCorreo(self):
        self.correo = self.correoEdit.get()
        self.ventana_informacion.write(f'Correo actualizado por {self.correo}')
    
    def abrir_pagina(self):
        self.ventana_informacion.write('Navegador abierto')
        class Abrir_pagina1(web_controller.Web_Controller):pass
        self.equipos = Abrir_pagina1(int(self.time.get()))
        self.equipos.openEdge()
        self.equipos.selectPage(self.link)
    
    def ejecuccionHilo(self):
        hilo_equipos = threading.Thread(target=self.ejecuccion)
        hilo_equipos.start()
        
    def ejecuccion(self):
        self.on_of(False)
        self.ventana_informacion.write('Empezando ejecuccion')
        self.poliedro.definirBrowser(self.equipos)
        self.poliedro.seleccionAcceso('194')
        self.excel.leer_excel('src\equipos\equipos.xlsx','Iccid')
        self.excel.quitarFormatoCientifico('Iccid')
        self.excel.quitarFormatoCientifico('Imei')
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
        self.imei = str(self.excel.excel['Imei'][self.contador])
        self.cedulaVendedor = str(self.excel.excel['Cedula vendedor'][self.contador]).replace('.0','')
        

        primerFormulario = [
            ['DetailProduct_SellerId', self.cedulaVendedor, 'id'],
            ['DetailProduct_Imei', self.imei, 'id'],
            ['DetailProduct_Iccid', self.iccid, 'id'],
        ]
        try:
            self.poliedro.rellenoFormulario(3, primerFormulario)
            self.equipos.click('btnNext', 'id')
        except:
            self.ventana_informacion.write(f'Activacion erronea de equipo {self.imei}')
            self.poliedro.reinicio()
            self.contador += 1
        optionsList = [
            ['/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[6]/div/span'],
            ['/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[4]/ul/li'],
        ]
        funcionList = [
            self.validado,
            self.error1
        ]
        self.poliedro.detectOption(optionsList, funcionList, NoneFunc=self.error2)
        time.sleep(0.5)
        self.ventana_informacion.write(f'Activacion exitosa de equipo {self.imei}')
        self.guardarData()
        self.poliedro.reinicio()
        self.contador += 1
    
    def validado(self):
        self.icc = ""
        self.imei = ""
        self.vTecnologia = ""
        self.vKit = ""
        self.vLista = ""
        self.vEquipo = ""
        self.vRegion = ""
        self.equipos.click('btnNext', 'id')
        self.equipos.click('btnNext', 'id')
        self.equipos.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div/div[1]/div[3]/div/span/span[1]/span/span[1]')
        self.equipos.click('/html/body/span/span/span[2]/ul/li[2]')
        self.equipos.click('btnNext', 'id')
        self.equipos.click('btnNext', 'id')
        self.min = self.equipos.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/div/div/div/strong/strong/div/div/div/p/strong[2]')
            

    def error1(self):
        self.icc = ""
        self.imei = ""
        self.vTecnologia = ""
        self.vKit = ""
        self.vLista = ""
        self.vEquipo = ""
        self.vRegion = ""
        self.min = ""

    def error2(self):
        self.mensaje = 'No deja preactivar por seriales en uso o principal'
        self.icc = self.equipos.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[3]/div[2]/div[1]/div/div/div')
        self.imei = self.equipos.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[3]/div[2]/div[2]/div/div/div')
        self.vTecnologia = self.equipos.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[3]/div[2]/div[3]/div/div/div')
        self.vKit = self.equipos.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[3]/div[2]/div[4]/div/div/div')
        self.vLista = self.equipos.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[3]/div[2]/div[5]/div/div/div')
        self.vEquipo = self.equipos.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[3]/div[2]/div[6]/div/div/div')
        self.vRegion = self.equipos.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[3]/div[2]/div[7]/div/div/div')
        self.min= ""

    def guardarData(self):
        self.excel.guardar(self.contador, 'Min', self.min, 'src\equipos\equipos.xlsx')
        self.excel.guardar(self.contador, 'Mensaje', self.mensaje, 'src\equipos\equipos.xlsx')
        self.excel.guardar(self.contador, 'ICC_ID_Identificacion_Tarjeta_de_Circuito_Integrada', self.icc, 'src\equipos\equipos.xlsx')
        self.excel.guardar(self.contador, 'IMEI_Identificacion_Internacional_del_Equipo_Movil', self.imei, 'src\equipos\equipos.xlsx')
        self.excel.guardar(self.contador, 'Validacion_Tecnologia', self.vTecnologia, 'src\equipos\equipos.xlsx')
        self.excel.guardar(self.contador, 'Validacion_Kit_Prepago', self.vKit, 'src\equipos\equipos.xlsx')
        self.excel.guardar(self.contador, 'Validacion_Region_ICCID_Distribuidor', self.vRegion, 'src\equipos\equipos.xlsx')
        self.excel.guardar(self.contador, 'Validacion_Equipo', self.vEquipo, 'src\equipos\equipos.xlsx')
        self.excel.guardar(self.contador, 'Validacion_Lista', self.vLista, 'src\equipos\equipos.xlsx')