from selenium.webdriver.chrome.service import Service as ChromeService
import chromedriver_autoinstaller
from selenium import webdriver
from tkinter import *
import time
import requests
import urllib.request
import os
import zipfile
from io import BytesIO
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys


class Web_Controller:

    def __init__(self, sleeptime):
        global sleep
        sleep = sleeptime
        # self.edgedriver()
        # self.openEdge()
    
    def actualizarIntervalo(self, valor):
        global sleep
        sleep = valor

      
    
    def retornarHtml(self):
        return self.browser.page_source

    def chromedriver(self):
        chromedriver_autoinstaller.install()
    
    def edgedriver(self):
        # Obtener la última versión del controlador de Microsoft Edge WebDriver
        response = requests.get('https://msedgewebdriverstorage.blob.core.windows.net/edgewebdriver/LATEST_STABLE')
        latest_version = response.text.strip()
        print(latest_version)


        # URL de descarga del controlador
        url = f'https://msedgedriver.azureedge.net/{latest_version}/edgedriver_win64.zip'

        # Descargar y extraer el archivo zip del controlador
        response = urllib.request.urlopen(url)
        zipfile.ZipFile(BytesIO(response.read())).extractall(os.getcwd())

        # Agregar el controlador al PATH del sistema
        os.environ['PATH'] += os.pathsep + os.getcwd()
    

    
    def validate(funcion):
        def execute(self,*args, **kwargs):
            proof = True
            contador = 1
            while proof:
                try:
                    data = funcion(self,*args, **kwargs)
                    proof= False
                    time.sleep(int(sleep))
                    return data
                except:
                    if contador < 30:
                        print(f'intento numero {contador}')
                        time.sleep(1)
                        contador +=1
                    else:
                        raise('Excedio el numero de intentos')
        return execute
    
    def openChrome(self):
        service = ChromeService('chromedriver')
        options =  webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(chrome_options= options)
    
    def openEdge(self):
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("start-maximized")
        self.browser = Edge(executable_path='msedgedriver.exe', options=options)
        self.browserOriginal = self.browser
    
    def crearNavegador(self):
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("start-maximized")
        return Edge(executable_path='msedgedriver.exe', options=options)

    

    @validate
    def selectPage(self,link):
        self.browser.get(link)
    
    @validate
    def insert(self, byStr, text, by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        else: find =None
        if find is not None:
            find.send_keys(text)
    
    @validate
    def click(self, byStr, by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        else: find =None
        if find is not None:
            find.click()
    
    @validate
    def read(self, byStr, by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        if find is not None:
            return find.text
        else: return "none"

    def readNoValidate(self, byStr, by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        if find is not None:
            return find.text
        else: return "none"
    
    @validate
    def waitExist(self, byStr, by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        if find is not None:
            pass
        else: raise('')

    @validate
    def wait(self, byStr, condition ,by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        if find is not None:
            if find.text is not None:
                if condition in find.text:
                    raise('error')
    
    @validate     
    def erase(self, byStr, by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        else: find =None
        if find is not None:
            find.clear()
    
    @validate   
    def eraseLetter(self, byStr, cantidad, by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        else: find =None
        if find is not None:
            for i in range(0,cantidad):
                find.send_keys(Keys.BACKSPACE)

    @validate   
    def write(self, byStr, keys, by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        else: find =None
        if find is not None:
            find.send_keys(keys)
    
    def readonly(self, byStr, by='xpath'):
        if by == "xpath": find = self.browser.find_element_by_xpath(byStr)
        elif by == "id": find = self.browser.find_element_by_id(byStr)
        elif by == "name": find = self.browser.find_element_by_name(byStr)
        if find is not None:
            readonly_value = find.get_attribute('readonly')
            if readonly_value == 'readonly':
                return True
            else:
                return False
        else: return None

    
    def browserGet(self):
        return self.browser
    
    def cerrar(self):
        self.browser.quit()