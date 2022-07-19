
numero = int(input("Ingrese un numero: "))

lista_impares = []
for num in range(1, numero):
    impar = num * 2 - 1
    lista_impares.append(str(impar))
    new_lista = [*lista_impares]
    new_lista.reverse()
    print(" ".join(new_lista))
    