## crear una clase "Cuadrado" que tenga como argumento el lado, 
## obtener el perimetro y el area del cuadrado
import math
from cuadrados import Cuadrado
from rectangulo import Rectangulo
from circulo import Circulo

def mostrar(figura):
    print(f"Area: {figura.area()}")
    print(f"Perimetro: {figura.perimetro()}")

continuar = True
while continuar:
    print("[1]: Cuadrado")
    print("[2]: Rectangulo")
    print("[3]: Circulo")
    a=input("Que desea calcular?" ).upper()
    if a=="1":
        lado = int(input("Ingrese el lado del cuadrado: "))
        c = Cuadrado(lado)
        mostrar(c)
    elif a=="2":
        largo = int(input("Ingrese el largo del rectangulo: "))
        ancho = int(input("Ingrese el ancho del rectangulo: "))
        c = Rectangulo(largo,ancho)
        mostrar(c)
    elif a=="3":
        radio = int(input("Ingrese el radio: "))
        c = Circulo(radio)
        mostrar(c)
    else:
        print("La opcion es incorrecta")
    continuar = input("Desea continuar (S/N)").upper() == "S"