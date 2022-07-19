numeros=input("ingrese varios numeros separador por ',': ")
list_numeros=numeros.split(",")
print(list_numeros)
def media(numeros):
    suma=0
    cant=0
    for n in numeros:
        suma+=int(n)
        cant+=1
    promedio=suma/cant

    return promedio
print(media(list_numeros))

