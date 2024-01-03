from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True

# Configurar el modo IE
options.add_argument("--ie-mode-test")

# Puedes agregar más opciones según sea necesario

browser = webdriver.Edge(executable_path='msedgedriver.exe', options=options)

pass