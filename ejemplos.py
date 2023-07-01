from tkinter import *
import pyautogui

# Función para capturar la posición y dimensiones del área seleccionada
def capture_area(event):
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    print(x,y)
    contador +=1
    if contador > 1:
        root.quit()
    # Aquí puedes guardar las coordenadas (x, y) para usarlas posteriormente

# Crear la ventana principal
root = Tk()
root.attributes("-transparentcolor", "white")
root.attributes("-alpha", 0.3)
root.overrideredirect(True)
screen_width, screen_height = pyautogui.size()
print(screen_width, screen_height)
root.geometry(f'{screen_width}x{screen_height}')
contador = 1

# Cargar la imagen del puntero en forma de cruz
crosshair_image = PhotoImage(file="src\portas\crosshair.png")

# Crear un Label que muestra la imagen del puntero
crosshair_label = Label(root, image=crosshair_image)
crosshair_label.pack()

# Capturar el evento de clic del ratón para obtener el área seleccionada
root.bind("<Button-1>", capture_area)


# Mostrar la ventana
root.mainloop()