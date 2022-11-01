
articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}

# metodo de ordenamiento de burbuja.
def intercambiar(lista,i,j):
    auxiliar=lista[i]
    lista[i]=lista[j]
    lista[j]=auxiliar
def ordenar (codigos,cantidades,tipos):
    conteo=len(codigos)
    for i in range(conteo-1):
        for j in range(i+1,conteo):
            if articulos[codigos[j]]>articulos[codigos[i]]:
                intercambiar(codigos,i,j)
                intercambiar(cantidades,i,j)
                intercambiar(tipos,i,j)



N=int(input())


codigos=[]
cantidades=[]
tipos=[]
valor_productos=[]
valores_iva=[]
valores_finales=[]
total_ventas=0
total_iva=0

for i in range(N):
    codigo=int(input())
    cantidad=float(input())
    tipo=int(input())
    codigos.append(codigo)
    cantidades.append(cantidad)
    tipos.append(tipo)
ordenar(codigos,cantidades,tipos)
for i in range(N):
    valorproducto=cantidades[i]* precios[codigos[i]]
    if tipos[i]==1:
        iva=0
    elif tipos[i]==2:
        iva=valorproducto*0.05 
    else:
        tipos[i]
        iva=valorproducto*0.19
  
    valorfinal=valorproducto+iva
    total_iva+=iva
    total_ventas+=valorfinal
    if valorproducto==int(valorproducto):
        valorproducto=int(valorproducto)
    if valorfinal==int(valorfinal):
        valorfinal=int(valorfinal)
    
    # ingresando a listas
    valor_productos.append(valorproducto)
    valores_iva.append(total_iva)
    valores_finales.append(valorfinal)
    
    # print(codigos[i])
    print(articulos[codigos[i]],"-",valorproducto,"-",valorfinal)
    # print(valorproducto)
    # print(valorfinal)


print("Total : $",total_ventas)
print("TotalIva: $",total_iva)



    