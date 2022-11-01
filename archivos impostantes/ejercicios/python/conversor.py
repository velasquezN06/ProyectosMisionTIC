
import tkinter as tk
from tkinter import ttk

def convertir_temp():
    temp_celsius=float(caja_temp_celsius.get())
    temp_kelvin = temp_celsius + 273.15
    etiqueta_temp_kelvin.config(text=f"temperatura en ºK: {temp_kelvin}")

    temp_farenheit = temp_celsius * 1.8 + 32
    etiqueta_temp_farenheit.config(text=f"temperatura en ºF {temp_farenheit}")


ventana = tk.Tk()
ventana.title("conversor")
ventana.config(width=400,height=300)

etiqueta_temp_celsius = ttk.Label(text="temperatura en ºC:")
etiqueta_temp_celsius.place(x=20,y=20)

caja_temp_celsius = ttk.Entry()
caja_temp_celsius.place(x=140,y=20,width=60)

boton =ttk.Button(text="convertir" , command=convertir_temp)
boton.place(x=20,y=60)

etiqueta_temp_kelvin = ttk.Label(text="temperatura  en k n/a")
etiqueta_temp_kelvin.place(x=20,y=120)

etiqueta_temp_farenheit =ttk.Label(text="temperatura en f n/a")
etiqueta_temp_farenheit.place(x=20,y=160)

ventana.mainloop()




