
divisas = {
    "Euro": "€",
    "Dollar": "$",
    "Yen": "¥"
}

print("Divisas")
print("=======")
print("Euro")
print("Dollar")
print("Yen")
divisa = input("Escoger una divisa: ")
if divisa not in divisas:
    print("No existe la divisa")
else:
    simbolo = divisas.get(divisa)
    print(simbolo)
