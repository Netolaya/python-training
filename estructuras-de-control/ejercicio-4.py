

def validar_numero(input_numero):
    try:
        numero=int(input_numero)
        if numero<=0:
            numero_valido = False
        else:
            numero_valido = True
    except:
        numero_valido = False
    return numero_valido

## validar numero
numero = input("ingrese un numero entero positivo: ")
numero_valido = validar_numero(numero)
while numero_valido == False:
    numero=input("ingrese un numero entero positivo: ")
    numero_valido = validar_numero(numero)

numero = int(numero)
lista_retro=[str(numero)]
while numero>0:
    numero=numero-1
    lista_retro.append(str(numero))
print(" , ".join(lista_retro))

