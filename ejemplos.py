# def create_pdf(n_clicks, data_informe, empresa):
#     if (empresa is None) or (n_clicks == 0) or not data_informe:
#         raise PreventUpdate
#     # Configuración inicial
#     pdf = io.BytesIO()  # Almacena el pdf generado
#     doc = canvas.Canvas(pdf, pagesize=letter)  # lienzo

#     # Carga de datos
#     figs = data_informe['figs']
#     dates = data_informe['dates']
#     store = data_informe['store']
#     city = data_informe['city']
#     product = data_informe['product']
#     business = data_informe['business']

#     # Portada
#     doc.drawImage('static/images/FullColor.png', x=360, y=680, width=170, height=66)
#     doc.setFont('Helvetica', 35)
#     doc.drawString(text=f'Informe Magnet - {empresa}', x=110, y=450)
#     doc.setFont('Helvetica', 16)
#     doc.drawString(text=dates['text'] + ': ' + dates['data'], x=40, y=380)
#     doc.drawString(text=city['text'] + ': ' + city['data'], x=40, y=350)
#     doc.drawString(text=store['text'] + ': ' + store['data'], x=40, y=320)
#     doc.drawString(text=product['text'] + ': ' + product['data'], x=40, y=290)
#     doc.drawString(text=business['text'] + ': ' + business['data'], x=40, y=260)
#     doc.showPage()  # Cambio de pagina

#     # Primera hoja
#     # -Clientes
#     doc.setFont('Helvetica', 20)
#     data = figs['clientes']
#     doc.drawCentredString(letter[0] / 2, y=650, text=data['titulo'])
#     graph = Image.open(io.BytesIO(go.Figure(data['graphs'][0]).to_image(format="png")))
#     doc.drawInlineImage(graph, x=20, y=480, width=300, height=150)
#     graph = Image.open(io.BytesIO(go.Figure(data['graphs'][1]).to_image(format="png")))
#     doc.drawInlineImage(graph, x=300, y=480, width=300, height=150)
#     # -Cluster
#     doc.setFont('Helvetica', 20)
#     data = figs['clusters']
#     doc.drawCentredString(letter[0] / 2, y=400, text=data['titulo'])
#     graph = Image.open(io.BytesIO(go.Figure(data['graphs'][0]).to_image(format="png")))
#     doc.drawInlineImage(graph, x=20, y=180, width=310, height=190)
#     graph = Image.open(io.BytesIO(go.Figure(data['graphs'][1]).to_image(format="png")))
#     doc.drawInlineImage(graph, x=320, y=180, width=310, height=190)
#     doc.showPage()  # Hace la pagina

#     # Segunda hoja
#     # -Tabla
#     doc.setFont('Helvetica', 20)
#     data = figs['tabla']
#     doc.drawCentredString(letter[0] / 2, y=650, text=data['titulo'])
#     graph = Image.open(io.BytesIO(go.Figure(data['graphs'][0]).to_image(format="png", width=800, height=900, scale=2)))
#     doc.drawInlineImage(graph, x=16, y=140, width=580, height=480)
#     doc.showPage()  # Hace la pagina

#     # Tercera hoja
#     # -Margen
#     data = figs['margen']
#     if data['estado']:
#         doc.setFont('Helvetica', 20)
#         doc.drawCentredString(letter[0] / 2, y=650, text=data['titulo'])
#         graph = Image.open(io.BytesIO(go.Figure(data['graphs'][0]).to_image(format="png")))
#         doc.drawInlineImage(graph, x=20, y=320, width=580, height=300)
#         doc.showPage()

#     # Se guarda doc
#     doc.save()

#     # se cambia bytesIo a Bytes
#     pdf = pdf.getvalue()
#     data = dcc.send_bytes(pdf, 'informe.pdf')

#     return data



# def funcion(figs):
#     doc =''
#     Image=''
#     letter=''
#     io=''
#     go=''


#     doc.setFont('Helvetica', 20)
#     data = figs['clientes']
#     doc.drawCentredString(letter[0] / 2, y=650, text=data['titulo'])
#     graph = Image.open(io.BytesIO(go.Figure(data['graphs'][0]).to_image(format="png")))
#     doc.drawInlineImage(graph, x=20, y=480, width=300, height=150)
#     graph = Image.open(io.BytesIO(go.Figure(data['graphs'][1]).to_image(format="png")))
#     doc.drawInlineImage(graph, x=300, y=480, width=300, height=150)



# def pagina(titulo, cuerpo, numeroPagina, encabezado=True):
#     if encabezado:
#         print('encabezado')
#     print(titulo)
#     print(cuerpo)
#     print(f'numero de pagina {numeroPagina}')
#     print('---------------')
    


# lista = [
#     {'titulo': '1', 'cuerpo': 'primero', 'encabezado': False},
#     {'titulo': '2', 'cuerpo': 'segundo', 'encabezado': True},
#     {'titulo': '3', 'cuerpo': 'tercero', 'encabezado': False},
#     {'titulo': '4', 'cuerpo': 'cuarto', 'encabezado': True},
# ]

# numeroPagina = 1
# for item in lista:
#     if item['encabezado']:
#         print('encabezado')
#     print(item['titulo'])
#     print(item['cuerpo'])
#     print(f'numero de pagina {numeroPagina}')
#     print('---------------')
#     # pagina(item['titulo'], item['cuerpo'], numeroPagina, item['encabezado'])
#     numeroPagina += 1


# def dibujar(doc, figs, font='Helvetica', size=20):

#     letter = ''
#     Image = ''
#     io = ''
#     go = ''

#     doc.setFont(font, size)
#     data = figs['clientes']
#     doc.drawCentredString(letter[0] / 2, y=650, text=data['titulo'])
#     graph = Image.open(io.BytesIO(go.Figure(data['graphs'][0]).to_image(format="png")))
#     doc.drawInlineImage(graph, x=20, y=480, width=300, height=150)
#     graph = Image.open(io.BytesIO(go.Figure(data['graphs'][1]).to_image(format="png")))
#     doc.drawInlineImage(graph, x=300, y=480, width=300, height=150)



figs = {
    'clientes': {
        'graphs':'1',
        'titulo' : '1 titulo',
    },
    'cluster' : {
        'graphs':'2',
        'titulo' : '2 titulo',
    }
}


for key, value in figs.items():
    print(key)
    print(value)
    print('--------------------')

# dibujar()