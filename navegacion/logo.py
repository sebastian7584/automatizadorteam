import customtkinter as ctk
from PIL import Image


class Logo:

    def __init__(self, master) -> None:
        image_path = "src\\team\logoTeam.png"
        image = Image.open(image_path)
        nuevo_ancho = 800
        nuevo_alto = 600  
        imagen_redimensionada = image.resize((nuevo_ancho, nuevo_alto))
        imagen = ctk.CTkImage(light_image=imagen_redimensionada)
        widget_imagen = ctk.CTkLabel(master, image=imagen)
        widget_imagen.pack()
        # widget_imagen.place(relx=0.7, rely=0.7, relheight=0.3, relwidth=0.3)