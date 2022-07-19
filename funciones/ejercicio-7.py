numeros = input("Ingrese los numeros separados por coma: ")
lista_numeros = numeros.split(",")

def cuadrados(lista_numeros):
    lista_cuadrados = []
    for numero in lista_numeros:
        lista_cuadrados.append(int(numero)**2)
    return lista_cuadrados

def cuadrados_v2(lista_numeros):
    return [int(numero)**2 for numero in lista_numeros] ## lista comphresion

print(cuadrados_v2(lista_numeros))