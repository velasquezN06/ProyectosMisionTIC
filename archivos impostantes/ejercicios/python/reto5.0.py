articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}
totaliva=0
valortotalcompra=0
dic={}

n =int(input())

for i in range(n):
    codigo=int(input())
    cantidad=int(input())
    tipoiva=int(input())
    nombre=articulos[codigo]
    precio=precios[codigo]

    valorproducto=(precio*cantidad)

    if tipoiva==1:
        iva=0
    elif tipoiva==2:
        iva=valorproducto*0.05 
    else:
        tipoiva
        iva=valorproducto*0.19


    precio_totalIva=valorproducto+iva
    lista=[codigo,nombre,cantidad,tipoiva,precio,valorproducto,iva,precio_totalIva]
    
    dic={}
    dic.setdefault(codigo,lista)
    

    totaliva=totaliva+iva
    valortotalcompra=valortotalcompra+precio_totalIva



 for d in dic:
      print(dic[d][0],"-",dic[d][1])

ordenado={}

for i in range (len(dic)):
    menor=100
    for d in dic:
        if dic[d][0]<menor:
            menor=dic[d][0]
    ordenado.setdefault(menor,dic[menor])
    dic.pop(menor)

# print(ordenado)
print(lista[1],"-",lista[4],"-",lista[7])
print("Total : $",valortotalcompra)
print("TotalIva : $",totaliva)