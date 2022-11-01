from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("tabla")
ventana.geometry("400x300")

table_frame=Frame(ventana)
table_frame.pack()
table_frame.place(x=60,y=100,height=100)


tabla =ttk.Treeview(table_frame)
tabla['columns'] = ('tripulante ID','tripulante nombre','tripulante nota')
tabla.column('#0',width=0,stretch=NO)
tabla.column('tripulante ID', anchor=CENTER, width=80)
tabla.column('tripulante nombre', anchor=CENTER, width=80)
tabla.column('tripulante nota', anchor=CENTER, width=80)

tabla.heading("#0",text="" , anchor=CENTER)
tabla.heading("tripulante ID",text="id", anchor=CENTER)
tabla.heading("tripulante nombre",text="nombre", anchor=CENTER)
tabla.heading("tripulante nota",text="nota", anchor=CENTER)

tabla.insert(parent='',index="end",iid=1,text="",values=("1","carlos","4.4"))
tabla.insert(parent='',index="end",iid=2,text="",values=("2","julieth","3.4"))
tabla.pack()

etiqueta_nombre=ttk.Label("nombre")
etiqueta_nombre.place(x=70,y=60)
caja_nombre=ttk.Entry()
caja_nombre.place(x=120,y=60,width=60)

etiqueta_nota=ttk.Label("nota")
etiqueta_nota.place(x=220,y=60,width=30)
etiqueta_nota=ttk.Entry()
etiqueta_nota.place(x=240,y=60,width=30)

ventana.mainloop()