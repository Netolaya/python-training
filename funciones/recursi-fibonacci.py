numero = int(input("Ingrese la posicion de fibo que desea consultar:"))

def fibonacci(posicion):
    if posicion == 1:
        return 0
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion-1)+fibonacci(posicion-2)

print(fibonacci(numero))


