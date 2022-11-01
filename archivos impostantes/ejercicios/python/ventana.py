import tkinter as tk
from tkinter import messagebox,ttk
from turtle import title

def show_selection():
    selecion=combo.get
    messagebox.show_info(message=f"opcion seleccionada{selecion}", title="seleccion")

ventana=tk.Tk()
ventana.config(width=300,height=200)

ventana.title("combobox")

combo = ttk.Combobox(state="readonly" ,values=["python","c","java","c++"])
combo.place(x=50,y=50)

boton =ttk.Button(text="mostrar seleccion", command=show_selection)
boton.place(x=50,y=100)


ventana.mainloop()


