import pandas as pd

class Excel_controller:

    def leer_excel(self,file,tituloColumna=None):

        self.excel = pd.read_excel(file)
        self.cantidad = None
        if tituloColumna is not None:
            self.cantidad = len(self.excel[tituloColumna])
    
    def guardar(self, posicion, columna, text, destino ='src\legalizador\legalizador.xlsx', nuevo= False):
        if nuevo:
            self.excel.loc[posicion]= {columna: text}
        else:
            self.excel[columna][posicion] = text
            self.excel.to_excel(destino, index=False)
    
    def quitarFormatoCientifico(self, tituloColumna):
        if self.cantidad is not None:
            for i in range(self.cantidad):
                self.excel[tituloColumna][i] = " "+str(self.excel[tituloColumna][i]).strip()
        
        else:
            raise('No tiene cantidad determinada en la funcion de lectura, por no agregar titulo')
    
    def export(self, result, file):
        df = pd.DataFrame(result[1:], columns=result[0])
        df.to_excel(file, index=False)