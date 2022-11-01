n=int(input())
valorfinal=0
totaliva=0

# entrada

for i in range(n):
    codigo=int(input())
    nombre=input()
    cantidad=float(input())
    valorunitario=float(input())
    tipoiva=int(input())
    valorproducto=cantidad*valorunitario
    if tipoiva ==1:
     iva=0
    elif tipoiva==2:
        iva=valorproducto*0.05
    else:
        tipoiva==3
        iva=valorproducto*0.19

    # proceso
    valoriva=iva
    valorfinal=valorproducto+valoriva
    valortotalcompra=valorfinal+totaliva
    totaliva+=iva

    

    # salida
    print(codigo)
    print(nombre)
    print(valorunitario)
    print(valorfinal)

    
print(valortotalcompra)
print(totaliva)
   