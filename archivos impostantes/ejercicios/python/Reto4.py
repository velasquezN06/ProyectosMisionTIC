
N=int(input())


diccionario={}

total_ventas=0
total_iva=0

for i in range(N):
    codigo=int(input())
    
    nombre=input()
    
    cantidad=float(input())
    
    valor_unitario=float(input())
    
    tipo=int(input())
    
    producto=[nombre,cantidad,valor_unitario,tipo]

    # agregando clave, valor a diccionario.
    diccionario.setdefault(codigo,producto)


for codigo in diccionario:
    
    valorproducto=diccionario[codigo][1] * diccionario[codigo][2]
    if diccionario[codigo][3]==1:
        iva=0
    elif diccionario[codigo][3]==2:
        iva=valorproducto*0.05 
    else:
        diccionario[codigo][3]
        iva=valorproducto*0.19
    
    valorfinal=valorproducto+iva
    total_iva+=iva
    total_ventas+=valorfinal

# guardando valores en las listas

    

    print(diccionario[codigo][0],"-" ,valorfinal)
    

def mostrar(total_ventas):
    return total_ventas
print("Total : $",total_ventas)


def mostar1(total_iva):
    return total_iva
print("Totaliva  :$",total_iva)












 


    









