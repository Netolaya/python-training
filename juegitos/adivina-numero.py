import random
nombre = input("Hola, ¿Como te llamas?: ")
print(f"Bueno {nombre}, estoy pensando un numero entre 1 y 20")

aleatorio = random.randint(1,20)
continuar = True
intentos = 0
while continuar:
    numero=int(input("Intenta adivinar: "))
    if numero > aleatorio:
        intentos = intentos + 1
        print("tu estimacion es muy alta ")
    elif numero < aleatorio:
        intentos = intentos + 1
        print("tu estimacion es muy baja ")
    else:
        intentos = intentos + 1
        continuar = False

if intentos == 1:
    print("Que crack eres :v adivinaste al primer intento")
elif intentos <= 5:
    print(f"Adivinaste el numero en {intentos} intentos")
else:
    print(f"No seas malo ps adivinaste en {intentos} intentos")
