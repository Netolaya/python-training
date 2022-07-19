frutas = {"platano":1.35,
        "manzana":0.80,
        "pera":0.85,
        "naranja":0.70
        }
fruta=input("que fruta desea: ")
kilo=float(input("cuantos kilos desea: "))
if fruta not in frutas:
    print("no tengo esa fruta casera")
else:
    precio=kilo*frutas.get(fruta)
    print(precio)
