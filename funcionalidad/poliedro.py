from selenium.webdriver.common.keys import Keys
import time

class Poliedro:

    def definirBrowser(self, browser):
        self.browser = browser

    def seleccionAcceso(self, opcion):
        self.link2='https://poliedrodist.comcel.com.co/activaciones/http/REINGENIERIA/pagDispatcherEntradaModernizacion.asp?Site=1'
        self.browser.selectPage(self.link2)
        self.browser.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[1]/div[1]/div[2]/div/span/span[1]/span/span[1]')
        self.browser.write('/html/body/span/span/span[1]/input', opcion)
        self.browser.write('/html/body/span/span/span[1]/input', Keys.ENTER)
        self.opcion = opcion

    def seleccionNit(self):
        self.browser.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div[2]/div[1]/div[1]/div[1]/div/span/span[1]/span/span[1]')
        self.browser.write('/html/body/span/span/span[1]/input', 'nit')
        self.browser.write('/html/body/span/span/span[1]/input', Keys.ENTER)
        
    
    def rellenoFormulario(self,campos,lista):

        for i in range (campos):
            if len(lista[i]) == 2: lista[i].append('xpath')
            self.browser.insert(lista[i][0],lista[i][1],lista[i][2])
    
    def reinicio(self):
        self.browser.click('/html/body/div/div[2]/section/div/div[1]/aside/nav/div[2]/ul/li[10]/a')
        self.browser.click('/html/body/p/table[2]/tbody/tr[2]/td[1]/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[13]/td[1]/a')
        self.seleccionAcceso(self.opcion)
    
    def saludo(self):
        self.browser.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[1]/div/span/span[1]/span/span[1]')
        self.browser.write('/html/body/span/span/span[1]/input', 'r')
        self.browser.write('/html/body/span/span/span[1]/input', Keys.ENTER)

    def correo(self):
        self.browser.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[4]/div/input','acruz@teamcomunicaciones.com')

    def tipoDoc(self, tipo):
        tipoDoc = self.browser.read('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[1]/div/span/span[1]/span/span[1]')
        if 'Seleccione' in tipoDoc:
            self.browser.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[1]/div/span/span[1]/span/span[1]')
            self.browser.write('/html/body/span/span/span[1]/input', tipo)
            self.browser.write('/html/body/span/span/span[1]/input', Keys.ENTER)

    def rellenoNombre(self, nombre):
        readonly = self.browser.readonly('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[2]/div/input')
        if readonly != True:
            self.browser.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[2]/div/input', nombre)

    def rellenoApellido(self, apellido):
        readonly = self.browser.readonly('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[3]/div/input')
        if readonly != True:
            self.browser.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[3]/div/input', apellido)
    
    def rellenoCedula(self, cedula):
        readonly = self.browser.readonly('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[2]/div/input')
        if readonly != True:
            self.browser.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[2]/div/input', cedula)

    def rellenoNumero(self):
        self.browser.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[5]/div[2]/fieldset/div/div[1]/div/span/span[1]/span/span[1]')
        self.browser.write('/html/body/span/span/span[1]/input', 'fijo')
        self.browser.write('/html/body/span/span/span[1]/input', Keys.ENTER)
        self.browser.click('//html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[5]/div[2]/fieldset/div/div[2]/div/span/span[1]/span/span[1]')
        time.sleep(1)
        self.browser.write('/html/body/span/span/span[1]/input', '604')
        self.browser.write('/html/body/span/span/span[1]/input', Keys.ENTER)
        self.browser.write('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[1]/div[5]/div[2]/fieldset/div/div[3]/div/input', '3131234')
     
    def rellenoDireccion(self):
        self.browser.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[1]/div[1]/span/span[1]/span/span[1]')
        self.browser.write('/html/body/span/span/span[1]/input', 'otras')
        self.browser.write('/html/body/span/span/span[1]/input', Keys.ENTER)
        self.browser.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[2]/div/input', 'central')
        self.browser.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[3]/div/span/span[1]/span/span[1]')
        self.browser.write('/html/body/span/span/span[1]/input', 'antio')
        self.browser.write('/html/body/span/span/span[1]/input', Keys.ENTER)
        self.browser.click('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[4]/div/span/span[1]/span/span[1]')
        self.browser.write('/html/body/span/span/span[1]/input', 'mede')
        self.browser.write('/html/body/span/span/span[1]/input', Keys.ENTER)
        self.browser.insert('/html/body/div/div[2]/section/div/div[2]/div[2]/main/form/div/div[1]/div/div[2]/div[3]/div[2]/fieldset/div[5]/div/input', 'central')