## crear una clase "Cuadrado" que tenga como argumento el lado, 
## obtener el perimetro y el area del cuadrado
import math

def mostrar(figura):
    print(f"Area: {figura.area()}")
    print(f"Perimetro: {figura.perimetro()}")

class Cuadrado():
    ## inicializar el cuadrado
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado * 4      

class Rectangulo():
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
    
    def area(self):
        return self.largo*self.ancho 
    
    def perimetro(self):
        return self.largo*2 + self.ancho*2

class Circulo():
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return self.radio * self.radio * math.pi
    
    def perimetro(self):
        return 2 * math.pi * self.radio


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