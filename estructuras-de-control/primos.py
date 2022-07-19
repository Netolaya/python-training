numero = int(input("Escriba un numero entero: "))

contar_divisores = 0
is_primo = True
for num in range(1,numero+1):
    if numero%num == 0:
        contar_divisores += 1
    if contar_divisores > 2:
        is_primo = False
        print("No es un numero primo")
        break

if is_primo:
    print("Es un numero primo")
