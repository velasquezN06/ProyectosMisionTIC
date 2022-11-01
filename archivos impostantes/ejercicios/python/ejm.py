from cgitb import text
import tkinter as tk
from tkinter import ttk


ventana=tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")

boton7=ttk.Button(text="7")
boton7.place(x=50,y=80)

boton6=ttk.Button(text=6)
boton6.place(x=140,y=80)


ventana.mainloop()