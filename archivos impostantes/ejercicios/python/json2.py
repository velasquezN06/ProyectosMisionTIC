import json

archivo="dic.json"

try:
    with open(archivo,"r") as f:
        dic=json.load(f)
except FileNotFoundError:
    d={"1": "lapiz", "2": "borrador", "3": "cuaderno"}
    with open(archivo,"w") as f:
        dic=json.dump(d,f)

else:
    print("diccionario",dic)
    print(dic["2"])

