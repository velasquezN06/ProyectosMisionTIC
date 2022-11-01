N=int(input())
codigos=[]
nombres=[]
cantidades=[]
valoresunitarios=[]
tiposiva=[]
total_ventas=0
total_iva=0

for i in range(N):
    codigo=int(input())
    codigos.append(codigo)
    nombre=input()
    nombres.append(nombre)
    cantidad=float(input())
    cantidades.append(cantidad)
    valor_unitario=float(input())
    valoresunitarios.append(valor_unitario)
    tipo=int(input())
    tiposiva.append(tipo)

print(len(codigos))
print(len(nombres))
print(len(cantidades))
print(len(valoresunitarios))
print(len(tiposiva))

for i in range(N):
    valor_producto=cantidades[i] * valoresunitarios[i]
    if tiposiva[i]==1:
        iva=0
    elif tiposiva[i]==2:
        iva=valor_producto*0.05 
    else:
        iva=valor_producto*0.19
    
    valor_final=valor_producto+iva
    total_iva+=iva
    total_ventas+=valor_final
    

    
    print(codigos[i])
    print(nombres[i])
    print(valor_producto)
    print(valor_final)

print(total_ventas)
print(total_iva)
   


   


 

    








