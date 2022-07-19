#palabra=input("Ingrese una palabra: ")
#a = list(palabra)
#a.reverse()
#print(a)

#abigail -> frase
#a -> letra
# recorrer todas las letras de la frase
# se debe verificar por cada iteracion si letra es igual al valor recorrido
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = 0
for l in frase:
    if letra == l:
        contador = contador + 1
print("La letra "+ letra+ " se repite "+ str(contador) + " veces")
