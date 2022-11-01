tripulantes=[]
documentos=[]
notas=[]
n=2
acumulador=0
for i in range(n):
    print("nombre")
    tripulante=input()
    error=True
    while error:
        if tripulante.isalpha():
            error=False
        else:
            error=True
            print("el nombre debe ser solo letras....")
            tripulante=input()
   


    tripulantes.append(tripulante)
    print("documento")
    documento=int(input())
    documentos.append(documento)


    print("nota")
    nota=float(input())
    error=True
    while error:
        if nota > 0.0 and nota <=5.0:
            error=False
        else:
            error=True
            nota=float(input())
    notas.append(nota)
    acumulador=acumulador+nota
promedio=acumulador/n

if promedio>= 3:
    print("continuar semana 4")
else:
    print("a practicar")

print(tripulantes,documentos,notas,promedio)




